from django.test import TestCase    
from django.urls import reverse     # usa reverse para testar de dentro para fora (ex.: de dentro da view para fora na url desejada)

# no terminal externo >> 'pip install pytest-watch' (deixa automático o teste a cada mudança)
# usar comando 'ptw'

# Create your tests here.
class RecipeURLsTest(TestCase): # noqa
    # def test_the_pytest_is_ok(self):
    #    # variavel = '123456'
    #     print('OLÁ MUNDO')
    #     assert 1 == 1, 'Um é igual a um'

    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')
            

    # def test_the_pytest_is_ok(self):
    #     assert 1 == 2, 'Um não é igual a dois'