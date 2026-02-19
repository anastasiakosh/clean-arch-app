from fastapi.responses import JSONResponse
from app.core.exceptions import DomainException


def register_exeption_handler(app):


    @app.exception_handler(DomainException)
    def handle_domain_exception(_, exc):
       return JSONResponse(
           status_code=400,
           contet={"error": str(exc)}
       )
