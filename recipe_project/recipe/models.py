from django.contrib.auth.models import User
from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    steps = models.TextField()
    cooking_time = models.IntegerField(help_text="Время приготовления в минутах")
    image = models.ImageField(upload_to='recipe_img/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.TextField(blank=True)
    archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='recipe')

    def __str__(self):
        return self.title


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='recipecategory', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='recipecategory', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.recipe.title} - {self.category.name}'


# Create your models here.
