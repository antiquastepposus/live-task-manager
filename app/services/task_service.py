from . import TaskUnitOfWork, TaskCreate, TaskFromDB, TaskNotFoundError

class TaskService:
    def __init__(self, uow: TaskUnitOfWork): 
        self.uow = uow

    async def find_all(self) -> list[TaskFromDB]:
        async with self.uow:
            tasks: list = await self.uow.repos.find_all()
            return [TaskFromDB.model_validate(task) for task in tasks]

    async def find_one(self, id: int) -> TaskFromDB:
        async with self.uow:
            task: TaskFromDB = await self.uow.repos.find_one(id)
            if task:
                return task
            raise TaskNotFoundError()

    async def add(self, task: TaskCreate) -> TaskFromDB:
        task_dict: dict = task.model_dump()

        async with self.uow:
            task_from_db = await self.uow.repos.add(task_dict)
            task_to_return = TaskFromDB.model_validate(task_from_db)

            await self.uow.commit()

            return task_to_return            
        
    async def update(self, id: int, task: TaskCreate) -> TaskFromDB:
        task_dict: dict = task.model_dump()

        async with self.uow:
            task_from_db = await self.uow.repos.update(id, task)

            if task_from_db:
                task_to_return = TaskFromDB.model_validate(task_from_db)

                await self.uow.commit()
                return task_to_return
            
            raise TaskNotFoundError()

    async def delete(self, id: int) -> bool:
        async with self.uow:
            result = await self.uow.repos.delete(id)
            
            if result:
                return result
            raise TaskNotFoundError()
        