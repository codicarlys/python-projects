from fastapi import FastAPI
from pydantic.main import BaseModel

app = FastAPI()

@app.get('/')
def home():
    return {"data": "seja bem-vindo"}

# Criar model
class Usuario(BaseModel):
    id: int
    nome: str 

# Criar base de dados
base_de_dados = {
    "id": 1,
    "nome": "fernando"
    }

# Rota Get All
@app.get('/usuarios')
def get_usuario():
    return  

# Rota Get Id
@app.get('/')