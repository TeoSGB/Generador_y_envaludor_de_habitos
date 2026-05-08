from fastapi.testclient import TestClient

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
            "goal": "quiero mejorar mi condición física",
            "level": "principiante",
            "available_time": "20 minutos diarios",
        },
    )

    data = response.json()
    assert response.status_code == 200
    assert len(data["habits"]) > 0
    assert "quiero mejorar mi condición física" in data["prompt_used"]


def test_evaluate_progress_with_valid_data() -> None:
    response = client.post(
        "/evaluate-progress",
        json={
            "goal": "mejorar mi condición física",
            "completed_habits": ["caminar 20 minutos", "tomar agua"],
            "missed_habits": ["dormir 7 horas"],
            "notes": "me costó organizar mi tiempo",
        },
    )

    data = response.json()
    assert response.status_code == 200
    assert data["score"] == 80
    assert len(data["next_recommendations"]) > 0
    assert "mejorar mi condición física" in data["prompt_used"]


def test_improve_prompt_with_valid_data() -> None:
    response = client.post(
        "/improve-prompt",
        json={
            "original_prompt": "Actúa como coach y dame hábitos",
            "objective": "obtener una respuesta más estructurada y en formato JSON",
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
            "goal": "quiero mejorar mi condición física",
            "level": "experto",
            "available_time": "20 minutos diarios",
        },
    )

    data = response.json()
    assert response.status_code == 422
    assert data["error"] == "Validation error"
    assert data["details"][0]["field"] == "level"

