from i_users_repository import IUsersRepository
from sqlmodel import SQLModel, create_engine, Session, Field, select


class UsersRepository(IUsersRepository):
    def __init__(self, db_string):
        self.engine = create_engine(db_string)
        SQLModel.metadata.create_all(self.engine)
        self.session = Session(self.engine)
        
    def get_by_id(self, userId: int):
        return {"user_id": userId, "name": "Rick", "last_name": "Morty"}