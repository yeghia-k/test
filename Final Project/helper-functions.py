from fastapi import HTTPException
from pathlib import Path
import json
from typing import List


class TaskFileRepository:
    def __init__(self, filename: str = "tasks.txt"):
        self.base_directory = Path(__file__).resolve().parent
        self.storage_path = self.base_directory / filename
        self._ensure_file_exists()

    def _ensure_file_exists(self) -> None:
        """Create the storage file if it does not already exist."""
        if not self.storage_path.exists():
            self.storage_path.touch()

    def _read_lines(self) -> List[str]:
        try:
            with self.storage_path.open("r", encoding="utf-8") as file:
                return [line.strip() for line in file if line.strip()]
        except Exception:
            raise HTTPException(status_code=500, detail="Unable to read task storage.")

    def _write_lines(self, lines: List[str]) -> None:
        try:
            with self.storage_path.open("w", encoding="utf-8") as file:
                for line in lines:
                    file.write(line + "\n")
        except Exception:
            raise HTTPException(status_code=500, detail="Unable to write to task storage.")

    # ---------------------------------
    # Public Interface Methods
    # ---------------------------------

    def fetch_all(self) -> List[str]:
        """Return all stored task entries (JSON strings)."""
        return self._read_lines()

    def append(self, task_object) -> None:
        """Add a new task entry to storage."""
        existing = self._read_lines()
        serialized = json.dumps(task_object.dict() if hasattr(task_object, "dict") else task_object)
        existing.append(serialized)
        self._write_lines(existing)

    def overwrite(self, serialized_tasks: List[str]) -> None:
        """Replace the entire storage content."""
        self._write_lines(serialized_tasks)
