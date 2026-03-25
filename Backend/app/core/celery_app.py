from celery import Celery
from .config import settings

celery_app = Celery(
    "worker",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

celery_app.conf.task_routes = {
    "app.tasks.sample_task": "main-queue"
}

@celery_app.task
def sample_task(name: str):
    return f"Hello {name}, task completed!"
