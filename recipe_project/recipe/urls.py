# recipe/urls.py
from django.urls import path
from .views import HomePage, RecipeDetail, AddRecipe, EditRecipe, DeleteRecipe, add_ingredient
from . import views


app_name = 'recipe'
urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('<int:pk>/', RecipeDetail.as_view(), name='recipe-details'),
    path('add-recipe/', AddRecipe.as_view(), name='add-recipe'),
    path('edit-recipe/<int:pk>/', EditRecipe.as_view(), name='edit-recipe'),
    path('delete-recipe/<int:pk>/', DeleteRecipe.as_view(), name='delete-recipe'),
    path('add-ingredient/', add_ingredient, name='add-ingredient'),

    path('register/', views.register, name='register'),  # Страница регист.
    path('login/', views.login_view, name='login'),  # Страница авториз.
    path('logout/', views.logout_view, name='logout'),  # Страница выхода
]
