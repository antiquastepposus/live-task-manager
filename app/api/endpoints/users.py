from . import (
            APIRouter, UserCreate, UserService, Depends, get_user_service, UserNotFoundError,
            WrongCredentialsError, HTTPException, status, UsernameAlreadyExists,
            OAuth2PasswordRequestForm
    )

users_router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@users_router.post("/sign_up")
async def sign_up(user: UserCreate, user_service: UserService = Depends(get_user_service)):
    try: 
        if await user_service.add(user):
            return {"success": "User was created"} 
    
    except UsernameAlreadyExists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username is already taken")


@users_router.post("/login")
async def login(user_service: UserService = Depends(get_user_service),  form_data: OAuth2PasswordRequestForm = Depends()):
    try: 
        token = await user_service.login(form_data)
        
        return {
            "access_token": token,
            "token_type": "bearer"
        }

    except WrongCredentialsError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong credentials")

    except UserNotFoundError:    
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

