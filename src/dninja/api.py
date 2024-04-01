from typing import List

from ninja import NinjaAPI

from src.dninja.schema import CategorySchema, ProductSchema
from src.inventory.models import Category, Product

api = NinjaAPI()


@api.post("/inventory/category/")
def post_category(request, data:CategorySchema):
    qs = Category.objects.create(**data.dict())
    return {"id": qs.name}


@api.post("/inventory/product/")
def post_product(request, data: ProductSchema):
    qs = Product.objects.create(**data.dict())
    return {"id": qs.name}


@api.get("/inventory/category/all/", response=List[CategorySchema])
def category_all(request):
    qs = Category.objects.all()
    return qs


@api.get("inventory/product/category/{category_slug}", response=List[ProductSchema])
def get_product_by_category(request, category_slug: str):
    qs = Product.objects.filter(category_slug=category_slug)
    return qs


























