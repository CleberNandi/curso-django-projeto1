from django.contrib.auth.models import User
from django.test import TestCase
from recipes.models import Category, Recipe


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def make_category(self, name="Category"):
        return Category.objects.create(name=name)

    def make_author(
            self,
            first_name="user",
            last_name="name",
            username="username",
            password="12sdfsdfs34",
            email="user@email.com"
        ):
        return  User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )
    
    def make_recipe(
            self,
            title: str="Recipe Title",
            description: str="Recipe Description",
            slug: str="recipe-slug",
            preparation_time: int=10,
            preparation_time_unit: str="Minutos",
            servings: int=5,
            servings_unit: str="Porções",
            preparation_steps: str="Recipes Preparation Steps",
            preparation_steps_is_html: bool=False,
            is_published: bool=True,
            cover:str ="recipes/cover/image.jpeg",
            category_data: Category | None=None,
            author_data: User | None=None
        ):

        if category_data is None:
            category_data = {}
        
        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,
            cover=cover,
            category=self.make_category(**category_data),
            author=self.make_author(**author_data)
        )