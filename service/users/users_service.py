from service.i_users_service import IUsersService
from repository.i_users_repository import IUsersRepository


class UsersService(IUsersService):
    def __init__(self, repository: IUsersRepository) -> None:
        super().__init__()
        self.repository = repository
        
    def get_by_id(self, id: int):
        user = self.repository.get_by_id(id)
        return user