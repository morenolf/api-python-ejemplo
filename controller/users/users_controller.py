from fastapi import FastAPI, HTTPException
from service.users.i_users_service import IUsersService

users_router = APIRouter("/users")

def init_users_controller(self, service: IUsersService) -> None:
    self.service = service
    
@users_router.users_router.get("/")
def get_by_id(self, user_id: int):
        user = self.service.get_by_id(user_id)
        if user == None:
            raise HTTPException(status_code=404, detail="User not found") 
        return user