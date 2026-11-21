from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

motos_router = APIRouter()


class MotoCreate(BaseModel):
    modelo: str = Field(min_length=3, max_length=100)
    descripcion: str | None = None
    precio: float = Field(gt=0)
    categoria: str = "urbana"
    caracteristicas: list[str] = Field(default_factory=list)


class MotoRead(BaseModel):
    id: int
    modelo: str
    descripcion: str | None
    precio: float
    categoria: str
    caracteristicas: list[str]
    esta_vendida: bool


class MotoUpdate(BaseModel):
    modelo: str | None = Field(default=None, min_length=3, max_length=100)
    descripcion: str | None = None
    precio: float | None = Field(default=None, gt=0)
    categoria: str | None = None
    caracteristicas: list[str] | None = None
    esta_vendida: bool | None = None


MOTOS: list[dict] = [
    {
        "id": 1,
        "modelo": "Yamaha MT-03",
        "descripcion": "Naked deportiva ideal para ciudad y carretera",
        "precio": 6500.0,
        "categoria": "naked",
        "caracteristicas": ["ABS", "321cc", "Inyección electrónica"],
        "esta_vendida": False,
    },
    {
        "id": 2,
        "modelo": "Honda CB190R",
        "descripcion": None,
        "precio": 3400.0,
        "categoria": "urbana",
        "caracteristicas": ["Tablero digital", "Iluminación LED"],
        "esta_vendida": False,
    },
]
NEXT_ID = 3


@motos_router.post("/motos", response_model=MotoRead, status_code=201)
def create_moto(moto: MotoCreate) -> dict:
    global NEXT_ID
    new_moto = {
        "id": NEXT_ID,
        "esta_vendida": False,
        "notas_internas": "ingresada al inventario desde la API",
        **moto.model_dump(),
    }
    MOTOS.append(new_moto)
    NEXT_ID += 1
    return new_moto


@motos_router.get("/motos", response_model=list[MotoRead])
def list_motos() -> list[dict]:
    return MOTOS


@motos_router.patch("/motos/{moto_id}", response_model=MotoRead)
def update_moto(moto_id: int, update: MotoUpdate) -> dict:
    for moto in MOTOS:
        if moto["id"] == moto_id:
            changes = update.model_dump(exclude_unset=True)
            moto.update(changes)
            return moto
    raise HTTPException(status_code=404, detail="Moto no encontrada")


@motos_router.post("/motos/from-model")
def create_from_model(moto: MotoCreate) -> dict:
    data = moto.model_dump()
    new_moto = {"id": len(MOTOS) + 1, "esta_vendida": False, **data}
    MOTOS.append(new_moto)
    validated = MotoRead.model_validate(new_moto)
    return validated.model_dump()


@motos_router.get("/motos/{moto_id}/raw-vs-validated")
def compare_raw_validated(moto_id: int) -> dict:
    raw = next((m for m in MOTOS if m["id"] == moto_id), None)
    if raw is None:
        return {"error": "moto no encontrada"}
    validated = MotoRead.model_validate(raw)

    return {
        "raw_dict": raw,
        "validated_model_dump": validated.model_dump(),
        "validated_model_dump_json": validated.model_dump_json(),
    }


@motos_router.delete("/motos/{moto_id}", status_code=204)
def delete_moto(moto_id: int) -> None:
    for index, moto in enumerate(MOTOS):
        if moto["id"] == moto_id:
            MOTOS.pop(index)
            return
    raise HTTPException(status_code=404, detail="Moto no encontrada")


@motos_router.get("/motos/{moto_id}", response_model=MotoRead)
def get_moto(moto_id: int) -> dict:
    for moto in MOTOS:
        if moto["id"] == moto_id:
            return moto
    raise HTTPException(status_code=404, detail="Moto no encontrada")