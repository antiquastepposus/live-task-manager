from base_repository import Repository
from . import User

class UserRepository(Repository):
    model = User

    async def find_by_username(self, username: str):
        return self.session.query(self.model).filter(self.model.username == username).first()
    