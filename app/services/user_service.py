from . import (
    UserUnitOfWork, UserCreate, UserFromDB, UserNotFoundError, get_password_hash,
    verify_password, create_access_token, timedelta, ACCESS_TOKEN_EXPIRE_MINUTES,
    WrongCredentialsError, UsernameAlreadyExists
    )

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
        
    async def find_by_username(self, username: str) -> UserFromDB:
        async with self.uow:
            user: UserFromDB = await self.uow.repos.find_by_username(username)
            if user:
                return user
            return None

    async def add(self, user: UserCreate) -> UserFromDB:
        if not await self.find_by_username(user.username):
            async with self.uow:
                user_dict = {"username": user.username, "password": get_password_hash(user.password)}

                user_from_db = await self.uow.repos.add(user_dict)
                user_to_return = UserFromDB.model_validate(user_from_db)

                await self.uow.commit()

                return True

        raise UsernameAlreadyExists()
        
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
        
    async def login(self, user_in: UserCreate):
        async with self.uow:
            user: UserFromDB = await self.uow.repos.find_by_username(user_in.username)
            if user: 

                if verify_password(user_in.password, user.password):
                    access_token = create_access_token(
                        data={"sub": user_in.username},
                        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
                    )

                    return access_token
                
                raise WrongCredentialsError()
            
            raise UserNotFoundError()
