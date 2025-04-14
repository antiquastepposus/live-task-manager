from . import UserUnitOfWork, UserCreate, UserFromDB, UserNotFoundError

class UserService:
    def __init__(self, uow: UserUnitOfWork): 
        self.uow = uow

    async def find_all(self) -> list[UserFromDB]:
        async with self.uow:
            users: list = await self.uow.repos.find_all()
            return [UserFromDB.model_validate(user) for user in users]

    async def find_one(self, id: int) -> UserFromDB:
        async with self.uow:
            user: UserFromDB = await self.uow.repos.find_one(id)
            if user:
                return user
            raise UserNotFoundError()

    async def add(self, user: UserCreate) -> UserFromDB:
        user_dict: dict = user.model_dump()

        async with self.uow:
            user_from_db = await self.uow.repos.add(user_dict)
            user_to_return = UserFromDB.model_validate(user_from_db)

            await self.uow.commit()

            return user_to_return            
        
    async def update(self, id: int, user: UserCreate) -> UserFromDB:
        user_dict: dict = user.model_dump()

        async with self.uow:
            user_from_db = await self.uow.repos.update(id, user)

            if user_from_db:
                user_to_return = UserFromDB.model_validate(user_from_db)

                await self.uow.commit()
                return user_to_return
            
            raise UserNotFoundError()

    async def delete(self, id: int) -> bool:
        async with self.uow:
            result = await self.uow.repos.delete(id)
            
            if result:
                return result
            raise UserNotFoundError()
        