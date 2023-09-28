from ..resource import Resource
from ..models.product import Product
from ..schemas.product import NewProduct

fruit_router = Resource(
    name='fruit',
    modelClass=Product,
    createForm=NewProduct,
    tags=['Meva']
)