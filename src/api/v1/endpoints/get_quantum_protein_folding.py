"""Get document router.
"""
from fastapi import APIRouter, HTTPException



router = APIRouter()


@router.get(
    "/quantum_protein_folding/",
    responses={
        500: {"content": {"application/json": {"example": {"detail": "error"}}}},
    },
)
async def get_quantum_protein_folding() -> None:
    """GET to retrieve calculations from quantum machine learning showcase.

    Args:
        ToDo

    Raises:
        HTTPException: 500: if an error during the query occurs.

    """

    #query: dict = {"document_id": document_id}

    try:
        pass
    except TypeError as error:
        raise HTTPException(status_code=500, detail=str(error)) from error


