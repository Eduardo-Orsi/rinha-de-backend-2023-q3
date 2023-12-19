from datetime import date
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, Field, UUID4


class Pessoa(BaseModel):
    apelido: str = Field(max_length=32, min_length=1)
    nome: str = Field(max_length=100, min_length=1)
    nascimento: date
    stack: Optional[list[str]] = None


class PessoaCreate(Pessoa):
    id: UUID4 = Field(default_factory=uuid4)
