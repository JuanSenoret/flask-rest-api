"""Main API definition based on FastAPI.
"""
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from src.api.v1.api import api_router as api_router_v1

app = FastAPI(
    title="Service Gateway",
    description="Service Gateway to submit jobs and retrieve results.",
)

app.include_router(api_router_v1)


@app.get("/", include_in_schema=False)
async def docs_redirect() -> RedirectResponse:
    """Redirects to the swagger endpoint.

    Returns:
        RedirectResponse: Response of <base-url>/docs
    """
    return RedirectResponse(url="/docs")
