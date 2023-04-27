from fastapi import FastAPI
from mode import Item

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello"}

@app.get('/{id}')
async def read(id:int):
    return {"message": "Hello123"}
@app.get('/int/{id}',response_model=int)
async def read_int(id:int):
    return id

@app.get('/bool/',response_model=bool)
async def read_bool():
    return True

@app.post('/item/',response_model=Item)
async def create_item(item:Item):
    return item

@app.put('/item/',response_model=Item)
async def update_item(item:Item):
    return item

@app.delete('/item/',response_model=Item)
async def delete_item(item:Item):
    return item