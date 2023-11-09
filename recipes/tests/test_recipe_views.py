from django.test import TestCase
from django.urls import resolve, reverse
from .test_recipe_base import RecipeTestBase

from recipes import views

class RecipeViewsTest(RecipeTestBase):  
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse("recipes:home"))
        self.assertIs(view.func, views.home_view)
    
    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertTemplateUsed(response, 'recipes/pages/home_view.html')
    
    def test_recipe_home_template_shows_no_recipes_found_if_no_recipe(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertIn("Sem receitas para exibir", response.content.decode("utf-8"))
    
    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse("recipes:home"))
        content = response.content.decode("utf-8")
        context = response.context['recipes']

        self.assertIn("Recipe Title", content)
        self.assertIn("5 Porções", content)
        self.assertIn("10 Minutos", content)

        self.assertEqual(len(context), 1)
 
    def test_recipe_home_template_dont_load_recipes_not_published(self):
        self.make_recipe(is_published=False)
        response = self.client.get(reverse("recipes:home"))  

        self.assertIn("Sem receitas para exibir", response.content.decode("utf-8"))

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse("recipes:category", kwargs={"category_id": 1}))
        self.assertIs(view.func, views.category_view)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        self.make_recipe(is_published=False)
        response = self.client.get(
            reverse("recipes:category", kwargs={"category_id": 1})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        title = 'This is a category test'
        self.make_recipe(title=title)
        response = self.client.get(reverse("recipes:category", args=(1,)))
        content = response.content.decode("utf-8")

        self.assertIn(title, content)
    
    def test_recipe_category_template_dont_load_recipes_not_published(self):
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(
            reverse("recipes:category", kwargs={"category_id": recipe.category.id})
        )

        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse("recipes:recipe", kwargs={"id": 1}))
        self.assertIs(view.func, views.recipe_view)
    
    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
           reverse("recipes:recipe", kwargs={"id": 1000})
        )
        self.assertEqual(response.status_code, 404)
    
    def test_recipe_detail_template_loads_the_correct_recipes(self):
        title = 'This is a detail page - It load one recipe'
        self.make_recipe(title=title)
        response = self.client.get(reverse("recipes:recipe", kwargs={"id": 1}))
        content = response.content.decode("utf-8")

        self.assertIn(title, content)

    def test_recipe_detail_template_dont_load_recipe_not_published(self):
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(
            reverse("recipes:recipe", kwargs={"id": recipe.id})
        )

        self.assertEqual(response.status_code, 404)
    