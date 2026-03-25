from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.tasks import long_running_task

router = APIRouter()

@router.post("/trigger-task")
async def trigger_task(duration: int = 5):
    task = long_running_task.delay(duration)
    return {"task_id": task.id, "status": "Triggered"}

@router.get("/task-status/{task_id}")
async def get_task_status(task_id: str):
    from app.core.celery_app import celery_app
    task_result = celery_app.AsyncResult(task_id)
    return {
        "task_id": task_id,
        "status": task_result.status,
        "result": task_result.result if task_result.ready() else None
    }
