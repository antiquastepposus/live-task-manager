from . import UserService, UserUnitOfWork, TaskService, TaskUnitOfWork

async def get_user_service() -> UserService:
    return UserService(uow=UserUnitOfWork())

async def get_task_service() -> TaskService:
    return TaskService(uow=TaskUnitOfWork())