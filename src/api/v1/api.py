"""API V1 endpoints
"""

from fastapi import APIRouter

from src.api.v1.endpoints import get_quantum_machine_learning, get_quantum_protein_folding

api_router = APIRouter()

api_router.include_router(get_quantum_machine_learning.router, tags=["v1"])
api_router.include_router(get_quantum_protein_folding.router, tags=["v1"])
