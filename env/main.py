from fastapi import FastAPI

app = FastAPI()

#aie ta main page tai nothing written
@app.get("/")
def index():
    return {"data":{"message":"Hiiii"}}

# aie ta holo path router link r ki
@app.get("/about")
def about():
    return {"data":{"about":"Mehzabin Haque"}}