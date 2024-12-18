from django.shortcuts import render     # tem a função de ler e renderizar arquivo (ex.: template)
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'recipes/home.html')

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

def sobre(request):
    return HttpResponse('sobre')

def contato(request):
    return HttpResponse('meu contato')