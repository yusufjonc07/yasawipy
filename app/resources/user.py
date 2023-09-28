from ..resource import Resource
from ..models.product import Product
from ..schemas.product import NewProduct

user_router = Resource(
    name='user',
    modelClass=Product,
    createForm=NewProduct,
    tags=['Hodimlar']
)