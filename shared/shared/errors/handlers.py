from shared.errors.http_exception import HttpException

def register_exception_handlers(app):

    @app.exception_handler(HttpException)
    async def http_exception_handler(request, exc):

        logger.exception(exc)

        return JSONResponse(
            status_code=exc.status_code,
            content={
                "detail": str(exc)
            }
        )