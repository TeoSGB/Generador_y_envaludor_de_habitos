import sqlite3
from pathlib import Path


DATABASE_PATH = Path(__file__).resolve().parent / "data" / "habit_coach.db"


def get_connection() -> sqlite3.Connection:
    """Create a SQLite connection for the local simulated database."""
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_database() -> None:
    """Create local database tables when the API starts."""
    with get_connection() as connection:
        connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS habit_plans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                goal TEXT NOT NULL,
                level TEXT NOT NULL,
                available_time TEXT NOT NULL,
                habits TEXT NOT NULL,
                weekly_plan TEXT NOT NULL,
                recommendations TEXT NOT NULL,
                prompt_used TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS progress_evaluations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                goal TEXT NOT NULL,
                completed_habits TEXT NOT NULL,
                missed_habits TEXT NOT NULL,
                notes TEXT NOT NULL,
                score INTEGER NOT NULL,
                feedback TEXT NOT NULL,
                strengths TEXT NOT NULL,
                areas_to_improve TEXT NOT NULL,
                next_recommendations TEXT NOT NULL,
                prompt_used TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS prompt_improvements (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_prompt TEXT NOT NULL,
                objective TEXT NOT NULL,
                improved_prompt TEXT NOT NULL,
                improvements_applied TEXT NOT NULL,
                explanation TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            """
        )

