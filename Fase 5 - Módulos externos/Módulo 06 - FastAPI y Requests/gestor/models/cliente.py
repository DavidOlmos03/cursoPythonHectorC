# pydantic me permite trabajar con modelos
from pydantic import BaseModel, constr, validator
from helpers.utils import dni_valido
import database as db

class ModeloCliente(BaseModel):
    dni: constr(min_length=3, max_length=3)
    nombre: constr(min_length=2, max_length=30)
    apellido: constr(min_length=2, max_length=30)


class ModeloCrearCliente(ModeloCliente):
    @validator('dni')
    def validar_dni(cls, dni):
        if dni_valido(dni, db.Clientes.lista):
            return dni
        raise ValueError("Cliente ya existe o DNI incorrecto")