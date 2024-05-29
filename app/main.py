from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from starlette.status import HTTP_204_NO_CONTENT
from .controller import product

app = FastAPI(title="TrueFan Test API")


@app.get("/")
def ping():
    return {"message": "running"}


app.include_router(product.router, prefix="/products")


@app.exception_handler(Exception)
async def handle_exception(request: Request, exc):
    return JSONResponse(status_code=400, content={"error": str(exc)})
