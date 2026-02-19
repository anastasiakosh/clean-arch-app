from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api.routes import router
from app.core.exceptions import DomainException

setup_logging()

app = FastAPI()
app.include_router(router)


@app.exception_handler(DomainException)
def handle_domain_exception(_, exc: DomainException):
    return JSONResponse(
        status_code=400,
        content={"error": str(exc)}
)
