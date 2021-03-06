from typing import List, Optional

from pydantic import BaseModel


class ClienteBase(BaseModel):
	CodiClie: int
	NumeCta: int
	FaxClie: Optional[str] = None


class ClientesCreate(ClienteBase):
	pass

class Cliente(ClienteBase):
	CodiClie: int
	NumeCta: int
	FaxClie: Optional[str] = None
	
	class Config:
		orm_mode = True

