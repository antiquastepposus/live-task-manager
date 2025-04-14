from . import (
            APIRouter, UserCreate, UserService, Depends, get_user_service, UserNotFoundError,
            WrongCredentialsError, HTTPException, status
    )

users_router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@users_router.post("/sign_up")
async def sign_up(user: UserCreate, user_service: UserService = Depends(get_user_service)):
    try: 
        return await user_service.add(user)
    
    except UserNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

@users_router.post("/login")
async def login(user: UserCreate, user_service: UserService = Depends(get_user_service)):
    try: 
        token = await user_service.login(user)
        
        return {
            "access_token": token,
            "token_type": "bearer"
        }

    except WrongCredentialsError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong credentials")

    except UserNotFoundError:    
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

