from ninja import Schema, ModelSchema

from src.inventory.models import Product


class CategorySchema(Schema):
    name: str
    slug: str


class ProductSchema(ModelSchema):
    class Config:
        model = Product
        model_fields = ["name", "desc", "slug", "ctg"]


