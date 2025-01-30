from django.shortcuts import render     # tem a função de ler e renderizar arquivo (ex.: template)
from utils.recipes.factory import make_recipe
from .models import Recipe
# from django.http import HttpResponse
# Create your views here.

def home(request):
    #recipes = Recipe.objects.all().order_by('-id')      # usando manage objects
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,        
    })

def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        #'recipes': [make_recipe() for _ in range(10)], status=201,
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
# def home(request):
#     return HttpResponse('HOME')

# def home(request):
#     return HttpResponse('''<!DOCTYPE>
#     <html>
#     <head><title>Olá Mundo</title></head>
                        
#     <body>
#         <h1>Olá Mundo</h1>
#     </body>
#     </html>
# ''')

# def sobre(request):
#     return HttpResponse('sobre')

# def contato(request):
#     return render(request, 'recipes/contato.html')  # namespace = recipes/contato.html

# def contato(request):
#     return render(request, 'me-apague/temp.html')