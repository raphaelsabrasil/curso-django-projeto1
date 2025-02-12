from django.shortcuts import render, get_list_or_404     # tem a função de ler e renderizar arquivo (ex.: template)
from utils.recipes.factory import make_recipe
from recipes.models import Recipe
# from django.http import Http404
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
    # recipes = Recipe.objects.filter(
    #     category__id=category_id,
    #     is_published=True,
    # ).order_by('-id')

    # if not recipes:
    #     raise Http404('Not found 😢')
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id')
    )

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category | ',
        #'recipes': [make_recipe() for _ in range(10)], status=201,
    })
    # first() << quando usa queryset // [0] << quando usar uma list

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