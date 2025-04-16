from app.api.schemas.task import TaskCreate, TaskFromDB
from app.exceptions.exceptions import AccessDeniedError, TaskNotFoundError
from app.utils.unitofwork import UnitOfWork


class TaskService:
    def __init__(self, uow: UnitOfWork): 
        self.uow = uow

    async def find_all(self, user: dict) -> list[TaskFromDB]:
        async with self.uow:
            tasks: list = await self.uow.tasks.find_all(user)
            return [TaskFromDB.model_validate(task) for task in tasks]

    async def find_one(self, id: int, user: dict) -> TaskFromDB:
        async with self.uow:
            task: TaskFromDB = await self.uow.tasks.find_one(id)

            if task:
                if task.created_by == user.id:
                    return TaskFromDB.model_validate(task)
                
                raise AccessDeniedError()
            
            raise TaskNotFoundError()

    async def add(self, task: TaskCreate, user: dict) -> TaskFromDB:
        task_dict: dict = task.model_dump()
        task_dict["created_by"] = user.id

        async with self.uow:
            task_from_db = await self.uow.tasks.add(task_dict)

            task_to_return = TaskFromDB.model_validate(task_from_db)

            await self.uow.commit()

            return task_to_return            
        
    async def update(self, id: int, task: TaskCreate, user: dict) -> TaskFromDB:
        task_dict: dict = task.model_dump()

        async with self.uow:
            task = await self.uow.tasks.find_one(id)
            if task:
                if task.created_by == user.id:
                    
                    task_from_db = await self.uow.tasks.update(id, task_dict)

                    task_to_return = TaskFromDB.model_validate(task_from_db)

                    await self.uow.commit()
                    return task_to_return
                    
                raise AccessDeniedError()
                
            raise TaskNotFoundError()
            

    async def delete(self, id: int, user: dict) -> bool:
        async with self.uow:
            task: TaskFromDB = await self.uow.tasks.find_one(id)

            if task:
                if task.created_by == user.id:

                    result = await self.uow.tasks.delete(id)
                    await self.uow.commit()
                    
                    return result
                    
                raise AccessDeniedError()
            
            raise TaskNotFoundError()
