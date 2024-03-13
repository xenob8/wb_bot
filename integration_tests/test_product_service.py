import pytest

from db.models import Product
from db.product_service import ProductService
from sqlalchemy import insert, select, delete, update


#   ТЕСТ №14
@pytest.mark.asyncio
async def test_patch_start_price(connection):
    product = {'id': 5, 'number': 123, 'title': '1', 'availability': True, 'price': 100}
    product_service = ProductService(connection)
    session = product_service.session

    async with connection.connect() as conn:
        await conn.execute(insert(Product).values(id=product['id'], number=product['number'], title=product['title'],
                                                  availability=product['availability'], price=product['price']))

        await conn.commit()
        new_availability = not product['availability']
        new_price = product['price'] + 1
        await product_service.patch_product(session=session, number=product['number'], price=new_price,
                                            aval=new_availability)
        result = await conn.execute(select(Product).filter_by(id=product['id']))
        await conn.execute(delete(Product).where(Product.id == product['id']))
        await conn.commit()
        assert result.first().price == new_price
