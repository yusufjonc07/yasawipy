from ..resource import Resource
from ..models.user import User
from ..schemas.user import NewUser

user_router = Resource(
    name='user',
    modelClass=User,
    createForm=NewUser,
    pluralLabel='Hodimlar',
    label='Hodim',
    navigationGroup='Boshqaruv',
    tags=['Hodimlar']
)