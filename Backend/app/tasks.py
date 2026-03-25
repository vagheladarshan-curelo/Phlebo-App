import time
from app.core.celery_app import celery_app

@celery_app.task(name="app.tasks.long_running_task")
def long_running_task(duration: int = 5):
    time.sleep(duration)
    return f"Completed task after {duration} seconds"
