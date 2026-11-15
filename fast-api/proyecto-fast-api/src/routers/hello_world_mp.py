from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class CotizacionMoto(BaseModel):
    modelo: str
    cantidad: int = 1
    codigo_chasis: str


@router.get("/")
def read_root() -> dict[str, str]:
    return {
        "mensaje": "Concesionario de Motos con FastAPI + uv",
        "asesor": "Diego Calderon",
        "version": "0.1.0",
    }


@router.get("/Yamaha-MT03")
def endpoint_yamaha() -> CotizacionMoto:
    return {
        "modelo": "Yamaha MT-03 321cc",
        "codigo_chasis": "VIN-YMH-039821",
    }


@router.get("/Kawasaki-Z400", response_model=CotizacionMoto)
def endpoint_kawasaki():
    return {
        "modelo": "Kawasaki Z400 ABS",
        "cantidad": 5,
        "codigo_chasis": "VIN-KWS-400712",
    }


@router.get("/campo-extra", response_model=CotizacionMoto)
def endpoint_campo_extra():
    return {
        "modelo": "Honda CB500F",
        "cantidad": 5,
        "codigo_chasis": "VIN-HND-500994",
        "descuento_interno": "no debe salir esto",
    }