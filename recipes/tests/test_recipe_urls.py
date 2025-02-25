from django.test import TestCase    
from django.urls import reverse     


# usa reverse para testar de dentro para fora (ex.: de dentro da view para fora na url desejada)
# no terminal externo >> 'pip install pytest-watch' (deixa automático o teste a cada mudança)
# usar comando 'ptw'

class RecipeURLsTest(TestCase): # noqa
    # def test_the_pytest_is_ok(self):
    #    # variavel = '123456'
    #     print('OLÁ MUNDO')
    #     assert 1 == 1, 'Um é igual a um'

    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})    # args=tuplas / kwargs=dict
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_detail_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')
            

    # def test_the_pytest_is_ok(self):
    #     assert 1 == 2, 'Um não é igual a dois'