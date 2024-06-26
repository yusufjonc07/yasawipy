from ..resource import Resource
from ..models.user import User
from ..schemas.user import NewUser

product_router = Resource(
    name='product',
    modelClass=User,
    createForm=NewUser,
    pluralLabel='Mahsulotlar',
    navigationGroup='Boshqaruv',
    label='Mahsulot',
    tags=['Mahsulotlar']
)