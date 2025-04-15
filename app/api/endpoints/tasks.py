from fastapi import APIRouter, Depends, HTTPException, status

from app.api.schemas.task import TaskCreate
from app.core.security import get_current_user
from app.dependencies.dependencies import get_task_service
from app.exceptions.exceptions import AccessDeniedError, TaskNotFoundError
from app.services.task_service import TaskService


tasks_router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

@tasks_router.get("/")
async def get_tasks(task_service: TaskService = Depends(get_task_service), current_user: dict = Depends(get_current_user)):
    return await task_service.find_all(current_user)

@tasks_router.get("/{task_id}")
async def get_task(
    task_id: int,
    task_service: TaskService = Depends(get_task_service),
    current_user: dict = Depends(get_current_user)
    ):
    try:
        return await task_service.find_one(task_id, current_user)
    except TaskNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found")
    
    except AccessDeniedError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Access denied")


@tasks_router.post("/")
async def add_task(
    task: TaskCreate, 
    task_service: TaskService = Depends(get_task_service), 
    current_user: dict = Depends(get_current_user)
    ):

    try: 
        task = await task_service.add(task, current_user)
        return task
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error: {e}")
    

@tasks_router.put("/{task_id}")
async def update_task(
    task: TaskCreate,
    task_id: int, 
    task_service: TaskService = Depends(get_task_service), 
    current_user: dict = Depends(get_current_user)
    ):
    try:
        return await task_service.update(task=task, id=task_id, user=current_user)

    except TaskNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found")
    
    except AccessDeniedError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Access denied")

@tasks_router.delete("/{task_id}")
async def delete_task(
        task_id: int, 
        task_service: TaskService = Depends(get_task_service), 
        current_user: dict = Depends(get_current_user)
    ):

    try: 
        result = await task_service.delete(task_id, current_user)
        return {"success": result}

    except TaskNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found")
    
    except AccessDeniedError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Access denied")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error: {e}")
    
    
