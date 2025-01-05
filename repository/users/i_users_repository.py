from abc import ABC, abstractmethod

class IUsersRepository(ABC):
    @abstractmethod
    def get_by_id(self, userId: int):
        pass