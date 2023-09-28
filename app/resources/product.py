from ..resource import Resource
from ..models.product import Product
from ..schemas.product import NewProduct

product_router = Resource(
    name='product',
    modelClass=Product,
    createForm=NewProduct
)