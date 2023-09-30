from ..resource import Resource
from ..models.user import User
from ..schemas.user import NewUser

customer_router = Resource(
    name='customer',
    modelClass=User,
    createForm=NewUser,
    pluralLabel='Mijozlar',
    navigationGroup='Boshqaruv',
    label='Mijoz',
    navigationIcon='shopping-cart',
    tags=['Mijozlar']
)