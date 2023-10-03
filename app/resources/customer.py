from ..resource import Resource
from ..models.user import User
from ..schemas.user import NewUser

customer_router = Resource(
    name='customer',
    modelClass=User,
    createForm=NewUser,
    pluralLabel='Mijozlar',
    navigationGroup='Savdo bo`limi',
    label='Mijoz',
    navigationIcon='building-library',
    tags=['Mijozlar'],
    simple=True,
)