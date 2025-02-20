from django.urls import path
# from recipes.views import home     # , sobre, contato
from . import views

app_name = 'recipes'        # recipes-home | recipes-recipe

urlpatterns = [    
    # path('', home),
    # path('', views.home),
    # path('recipes/<int:id>/', views.recipe),
    path('', views.home, name="home"),      # name="recipes-home"   usando app_name para encurtar name
    path('recipes/category/<int:category_id>/',
         views.category, name="category"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),      # name="recipes-recipe"
]
