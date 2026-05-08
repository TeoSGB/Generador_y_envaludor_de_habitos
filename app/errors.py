from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.exceptions import SimulatedInternalError


def register_error_handlers(app: FastAPI) -> None:
    """Register clear API error responses in one place."""

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError,
    ) -> JSONResponse:
        errors = [
            {
                "field": ".".join(str(location) for location in error["loc"] if location != "body"),
                "message": error["msg"],
            }
            for error in exc.errors()
        ]
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "error": "Validation error",
                "message": "Please review the request data and try again.",
                "details": errors,
            },
        )

    @app.exception_handler(SimulatedInternalError)
    async def simulated_internal_error_handler(
        request: Request,
        exc: SimulatedInternalError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "error": "Internal error",
                "message": exc.message,
            },
        )

