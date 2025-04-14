from . import Repository, ABC, abstractmethod, async_session_maker, UserRepository, TaskRepository

class AbstractUnitOfWork(ABC):
    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, *args):
        raise NotImplementedError

    @abstractmethod 
    async def commit(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError

class UnitOfWork(AbstractUnitOfWork):
    repos: Repository

    def __init__(self):
        self.session_factory = async_session_maker

    @abstractmethod
    async def __aenter__(self):
        self.session = self.session_factory()

        self.repos = Repository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()

class UserUnitOfWork(UnitOfWork):
    repos: UserRepository

    async def __aenter__(self):
        self.session = self.session_factory()

        self.repos = UserRepository(self.session)

class TaskUnitOfWork(UnitOfWork):
    repos: TaskRepository

    async def __aenter__(self):
        self.session = self.session_factory()
        
        self.repos = TaskRepository(self.session)