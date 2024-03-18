from fastapi import FastAPI
from pydantic import BaseModel
#hacer atributos opcionales
from typing import Optional

# Definir modelos de Profile
class Profile(BaseModel):
    username: str
    name: str
    email: str
    alias: str
    phone: int
    address: Optional[str]

# Establecer datos de autenticación y perfil
profile_data = {"username": "brendac123", "name": "Brenda Cuevas", "logemail": "brendac@gmail.com", "alias": "brendac", "phone": "123-456-7890",
                "address": "123 Main Street, City, State, 12345"}

# Inicializar la aplicación FastAPI
app = FastAPI()

# Definir rutas
@app.get("/profile")
def get_profile():
    return profile_data

#agregar perfiles
@app.post("/profile")
def insertar_profile(profile: Profile):
    return {"message": f"perfil {profile.name} insertado"}