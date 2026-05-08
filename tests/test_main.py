import sys
from pathlib import Path

from fastapi.testclient import TestClient

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.main import app


client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "message": "Habit Coach API running",
    }


def test_root_api_info() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["name"] == "Habit Coach API"
    assert response.json()["version"] == "1.0.0"
    assert response.json()["docs"] == "/docs"


def test_generate_plan_with_valid_data() -> None:
    response = client.post(
        "/generate-plan",
        json={
            "goal": "quiero mejorar mi condicion fisica",
            "level": "principiante",
            "available_time": "20 minutos diarios",
        },
    )

    data = response.json()
    assert response.status_code == 200
    assert len(data["habits"]) > 0
    assert "quiero mejorar mi condicion fisica" in data["prompt_used"]


def test_generate_plan_adapts_to_study_goal() -> None:
    response = client.post(
        "/generate-plan",
        json={
            "goal": "quiero aprender ingles",
            "level": "principiante",
            "available_time": "15 minutos diarios",
        },
    )

    data = response.json()
    response_text = " ".join(data["habits"]) + " " + " ".join(data["weekly_plan"]["martes"])
    assert response.status_code == 200
    assert "estudio" in response_text or "Estudiar" in response_text
    assert "15 minutos diarios" in data["habits"][0]
    assert "quiero aprender ingles" in data["prompt_used"]


def test_generate_plan_adapts_to_sleep_goal() -> None:
    response = client.post(
        "/generate-plan",
        json={
            "goal": "quiero dormir mejor",
            "level": "intermedio",
            "available_time": "30 minutos en la noche",
        },
    )

    data = response.json()
    response_text = " ".join(data["habits"]) + " " + " ".join(data["recommendations"])
    assert response.status_code == 200
    assert "descanso" in response_text or "dormir" in response_text
    assert "horas de sueno" in response_text


def test_generate_plan_changes_by_level() -> None:
    beginner_response = client.post(
        "/generate-plan",
        json={
            "goal": "quiero organizar mejor mi tiempo",
            "level": "principiante",
            "available_time": "10 minutos diarios",
        },
    )
    advanced_response = client.post(
        "/generate-plan",
        json={
            "goal": "quiero organizar mejor mi tiempo",
            "level": "avanzado",
            "available_time": "10 minutos diarios",
        },
    )

    beginner_data = beginner_response.json()
    advanced_data = advanced_response.json()
    assert beginner_response.status_code == 200
    assert advanced_response.status_code == 200
    assert beginner_data["recommendations"] != advanced_data["recommendations"]
    assert "simples" in " ".join(beginner_data["recommendations"])
    assert "retadoras" in " ".join(advanced_data["recommendations"])


def test_evaluate_progress_with_valid_data() -> None:
    response = client.post(
        "/evaluate-progress",
        json={
            "goal": "mejorar mi condicion fisica",
            "completed_habits": ["caminar 20 minutos", "tomar agua"],
            "missed_habits": ["dormir 7 horas"],
            "notes": "me costo organizar mi tiempo",
        },
    )

    data = response.json()
    assert response.status_code == 200
    assert data["score"] == 80
    assert len(data["next_recommendations"]) > 0
    assert "mejorar mi condicion fisica" in data["prompt_used"]


def test_evaluate_progress_uses_actual_habits_and_notes() -> None:
    response = client.post(
        "/evaluate-progress",
        json={
            "goal": "quiero ahorrar dinero",
            "completed_habits": ["registrar gastos", "revisar presupuesto"],
            "missed_habits": ["evitar compras impulsivas"],
            "notes": "me costo organizar mi tiempo",
        },
    )

    data = response.json()
    assert response.status_code == 200
    assert "registrar gastos" in data["strengths"][0]
    assert "evitar compras impulsivas" in data["areas_to_improve"][0]
    assert "horario fijo" in " ".join(data["areas_to_improve"])


def test_improve_prompt_with_valid_data() -> None:
    response = client.post(
        "/improve-prompt",
        json={
            "original_prompt": "Actua como coach y dame habitos",
            "objective": "obtener una respuesta mas estructurada y en formato JSON",
        },
    )

    data = response.json()
    assert response.status_code == 200
    assert "JSON" in data["improved_prompt"]
    assert len(data["improvements_applied"]) >= 5


def test_generate_plan_with_invalid_level() -> None:
    response = client.post(
        "/generate-plan",
        json={
            "goal": "quiero mejorar mi condicion fisica",
            "level": "experto",
            "available_time": "20 minutos diarios",
        },
    )

    data = response.json()
    assert response.status_code == 422
    assert data["error"] == "Validation error"
    assert data["details"][0]["field"] == "level"

