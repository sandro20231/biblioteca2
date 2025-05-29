from django.test import TestCase, Client
from .models import Autor, Livro
# Create your tests here.


class Testes(TestCase):

    def setUp(self):
        a1 = Autor.objects.create(nome="xx", idade=10)
        a2 = Autor.objects.create(nome="YY", idade=20)

        l1 = Livro.objects.create(titulo="aa", autor=a1, resumo="aaaaaaaaaaa")
        l2 = Livro.objects.create(titulo="bb", autor=a2, resumo="bbbbbbbbbbbb")

    # testes de inserção em telas

    def test_inserirautor(self):
        """Entrar na tela de url index"""
        c = Client()
        c1 = c.get('/inserirautor/')
        self.assertEqual(c1.status_code, 200)

    def test_isnerirlivro(self):
        """Entrar na tela inserir livro"""
        c = Client()
        c1 = c.get('/inserirlivro/')
        self.assertEqual(c1.status_code, 200)

    def test_index(self):
        """Entrar em index"""
        c = Client()
        c1 = c.get('')
        self.assertEqual(c1.status_code, 200)

    def test_listarautor(self):
        """Entrar em listar autor"""
        c = Client()
        c1 = c.get('/listarautores/')
        self.assertEqual(c1.status_code, 200)

    def test_listarlivros(self):
        """Entrar em listar livros"""
        c = Client()
        c1 = c.get('/listarlivros/')
        self.assertEqual(c1.status_code, 200)

    def test_login(self):
        """Entrar em login"""
        c = Client()
        c1 = c.get('/login/')
        self.assertEqual(c1.status_code, 200)

    # teste de registro de autores

    def test_contar_autor(self):
        """A quantidade de autores é 2"""
        a1 = Autor.objects.all()
        self.assertEqual(a1.count(), 2)

    # test de registro de livros

    def test_count_livro(self):
        """a quantidade de livros é 2"""
        l1 = Livro.objects.all()
        self.assertEqual(l1.count(), 2)

    # testes abrindo livros e autores individuais

    def test_mostrarautor(self):
        """a páigna de mostrar autor abre"""
        a1 = Autor.objects.get(nome="xx")
        c = Client()
        autor = c.get(f"/listarautores/{a1.id}/")
        self.assertEqual(autor.status_code, 200)

    def test_mostrarlivro(self):
        """a página mostrar livro abre"""
        l1 = Livro.objects.get(titulo="aa")
        c = Client()
        livro = c.get(f"/listarlivros/{l1.id}/")
        self.assertEqual(livro.status_code, 200)
