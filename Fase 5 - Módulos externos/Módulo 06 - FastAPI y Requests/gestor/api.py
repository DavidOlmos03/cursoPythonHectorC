from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import JSONResponse
from models.cliente import ModeloCliente, ModeloCrearCliente
import database as db


# Este header no es necesario en los JSONResponse para controlar los caracteres especiales
# headers = {"content-type":"charset=utf-8"} 
app = FastAPI()

@app.get("/")
async def index():
    content = {"mensaje":"¡Hola mundo!"}
    return JSONResponse(content=content, media_type="application/json")


@app.get("/html/")
async def html():
    content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>¡Hola mundo!</title>
    </head>
    <body>
        <h1>¡Hola mundo!</h1>
    </body>
    </html>
    """
    return Response(content=content, media_type="text/html")
    
@app.get('/clientes/')
async def clientes():
    # Se debe parsear antes de enviar al JSONResponse
    content = [cliente.to_dict() for cliente in db.Clientes.lista]
    return JSONResponse(content=content)

@app.get('/clientes/buscar/{dni}')
async def clientes_buscar(dni: str):
    cliente = db.Clientes.buscar(dni=dni)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return JSONResponse(content=cliente.to_dict())

@app.post('/clientes/crear/')
async def clientes_crear(datos: ModeloCrearCliente):
    cliente = db.Clientes.crear(datos.dni, datos.nombre, datos.apellido)
    if cliente:
        return JSONResponse(content=cliente.to_dict())
    raise HTTPException(status_code=404, detail="Cliente no creado")

@app.put('/clientes/actualizar')
async def clientes_actualizar(datos: ModeloCliente):
    if db.Clientes.buscar(datos.dni):
        cliente = db.Clientes.modificar(datos.dni, datos.nombre, datos.apellido)
        if cliente:
            return JSONResponse(content=cliente.to_dict())
    raise HTTPException(status_code=404, detail = "Cliente no creado")

@app.delete('/cliente/borrar/{dni}/')
async def cliente_borrar(dni: str):
    if db.Clientes.buscar(dni):
        cliente = db.Clientes.borrar(dni=dni)
        if cliente:
            return JSONResponse(content = cliente.to_dict())
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

print("Servidor de la API...")