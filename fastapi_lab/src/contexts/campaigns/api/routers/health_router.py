from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def healt_check():
    return {
        'message': "Retrieving data from back-end"
    }
