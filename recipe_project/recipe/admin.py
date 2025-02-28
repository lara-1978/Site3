from django.contrib import admin
from .models import Recipe, Category, Ingredient
from django.http import JsonResponse


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'get_categories', 'ingredients', 'description', 'steps', 'cooking_time', 'image', 'author', 'archived')
    search_fields = ('title',)
    actions = ['export_to_json']

    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])

    get_categories.short_description = 'Categories'

    def export_to_json(self, request, queryset):
        recipes = queryset.values('title', 'ingredients')  # ну или что-нибудь другое
        response = JsonResponse(list(recipes), safe=False, json_dumps_params={'ensure_ascii': False})
        response['Content-Disposition'] = 'attachment; filename="recipe.json"'
        return response

    export_to_json.short_description = 'Export selected recipe to JSON'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Register your models here.


# Register your models here.
