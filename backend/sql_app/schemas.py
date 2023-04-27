from pydantic import BaseModel
from typing import List

# --------------------------- MODELOS Pydantic ---------------------------
'''
Antes de criar um item, não sabemos qual será o ID atribuído a ele. ---> ItemCreate
Ao ler esse item (ao retorná-lo da API) já saberemos seu ID.        ---> Item
Ao ler um usuário, agora podemos declarar que os itens conterão os itens que pertencem a esse usuário.  --> User
'''

class ItemBase(BaseModel):
    title: str
    description: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item]

    class Config:
        orm_mode = True    # Seta um valor de configuração , por isso o "="


# Para os modelos de leitura : Item e User , adicionamos a classe interna Config 

# O orm_mode do Pydantic dirá ao modelo Pydantic para ler os dados, mesmo que não seja um dict, mas um modelo ORM.
# id = dados["id"] ou id = data.id
# E com isso, o modelo Pydantic é compatível com ORMs, e você pode apenas declará-lo no argumento response_model em suas operações de caminho.
# Você poderá retornar um modelo de banco de dados e ele lerá os dados dele.

# -------- SQLAlchemy --------

# -  "carregamento lento" : não buscam os dados para relacionamentos do banco de dados, a menos que você tente acessar o atributo que conteria esses dados.

# - current_user.items    -- > faria o SQLAlchemy ir até a tabela de itens e obter os itens para este usuário, mas não antes.

# Sem orm_mode, se você retornasse um modelo SQLAlchemy de sua operação de caminho, ele não incluiria os dados de relacionamento.

# Mesmo que você tenha declarado essas relações em seus modelos pydantic.

# Mas com o modo ORM, como o próprio Pydantic tentará acessar os dados que 
# Precisa dos atributos (em vez de assumir um dict), você pode declarar os dados específicos que deseja retornar e ele poderá ir buscá-los, 
# mesmo de ORMs .