from .models import Recipe, Category, Ingredient
from django import forms


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title','categories', 'description', 'image', 'cooking_time', 'ingredients', 'steps', 'author', ]
        labels = {
            'title': 'Название рецепта',
            'categories': 'Категория',
            'description': 'Описание',
            'image': 'Картинка',
            'cooking_time': 'Время приготовления в минутах',
            'ingredients': 'Ингредиенты',
            'steps': 'шаги приготовления',
            'author': 'Автор',
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            # Добавляем класс "form-control" ко всем полям
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']
