# recipe/views.py

import form
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Recipe, Ingredient, Category
from .forms import RecipeForm, IngredientForm
from django.shortcuts import  redirect, render
from django.contrib.auth import authenticate, login


class HomePage(ListView):
    model = Recipe
    template_name = 'home.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        queryset = Recipe.objects.all()
        selected_category_id = self.request.GET.get('category')
        if selected_category_id:
            queryset = queryset.filter(categories__id=selected_category_id)
        return queryset

    def get_context_data(self, **kwargs):
        # Получаем категории и добавляем их в контекст
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['selected_category_id'] = self.request.GET.get('category')
        context['recipe_count'] = Recipe.objects.count()
        return context


class RecipeDetail(DetailView):
    model = Recipe
    template_name = 'recipe-details.html'


class AddRecipe(CreateView):
    form_class = RecipeForm
    template_name = 'add-recipe.html'
    success_url = reverse_lazy('recipe:home')


class EditRecipe(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'edit-recipe.html'
    context_object_name = 'object'
    success_url = reverse_lazy('recipe:home')

    def form_valid(self, form):
        # Если нужно делать что-то перед сохранением, можно переопределить form_valid
        return super().form_valid(form)


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'


class DeleteRecipe(DeleteView):
    model = Recipe
    template_name = 'delete-recipe.html'
    success_url = reverse_lazy('recipe:home')


def add_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = IngredientForm()
    return render(request, 'add-ingredient.html', {'form': form})

    # Регистрация пользователя


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Сохраняем нового пользователя
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('recipe:home')
            else:
                # Если аутентификация не прошла (неполный логин)
                return redirect('recipe:register')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

    # Авторизация пользователя


def login_view(request):
    if request.method == 'POST':
        # Получаем данные из формы
        username = request.POST.get('login')
        password = request.POST.get('password')

        if username and password:
            # Пытаемся аутентифицировать пользователя
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('recipe:home')
            else:
                # Если аутентификация не прошла
                return render(request, 'login.html', {'error': 'Неверный логин или пароль'})
        else:
            # Если поля пустые
            return render(request, 'login.html', {'error': 'Заполните все поля'})

    return render(request, 'login.html')
    # Выход пользователя


@login_required
def logout_view(request):
    logout(request)
    return redirect('recipe:home')




# Create your views here.
