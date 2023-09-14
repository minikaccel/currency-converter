from convert_currency import convert

from fastapi import FastAPI


app = FastAPI()


@app.get("/rates/")
async def convert_currency(old, new, value):
    result = convert(old, new, value)
    return {"result": result}
