from app.repositories.base_repository import Repository
from . import Task

class TaskRepository(Repository):
    model = Task