from fastapi import FastAPI
import classes

import model
from database import engine

model.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def read_root():
 return {"Hello": "lalalalalalalalala"}

@app.post("/criar")
def criar_valores(nova_mensagem: classes.Mensagem):
    print(nova_mensagem)
    return {
        "Mensagem": f"Título: {nova_mensagem.titulo} "
                    f"Conteúdo: {nova_mensagem.conteudo} "
                    f"Publicada: {nova_mensagem.publicada}"
    }

@app.get("/quadrado/{num}")
def square(num: int):
    return num ** 2
