from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

# Para utilizar a autenticação, login e logout
from django.contrib.auth import authenticate, login, logout
# Verifica sé está logado sé não redireciona pelo LOGIN_URL = 'login' no settings.py
from django.contrib.auth.decorators import login_required

# Classes criadas para o blog
from .models import Postagem, Categoria
from .forms import ComentarioForm, CategoriaForm


# LOGIN
def login_blog(request):
	if 'username' in request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if(user != None):
			login(request,user)
			return HttpResponseRedirect('/')
	return render(request, 'login.html', {})

# LOGOUT
def logout_blog(request):
	logout(request)
	return HttpResponseRedirect('/login')



def categorias(request):
	categorias = Categoria.objects.all()
	return render(request, 'categorias.html', {'categorias': categorias})

def salvar_categoria(request):
	if request.method == 'POST':
		form = CategoriaForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			return sjdfhesgkf
	form = ComentarioForm()
	categorias = Categoria.objects.all()
	return render(request, 'categorias.html', {'categorias': categorias})

def editar_categoria(request):
	# if request.method == 'POST':
	# 	novo_nome_categoria = request.POST['nome']
	# 	antigo_nome_categoria = request.POST['antigo_nome']

	# 	if(antigo_nome_categoria):
	# 		form = CategoriaForm(request.POST)

	# categorias = Categoria.objects.all()
	return render(request, 'categorias.html', {'categorias': categorias})





@login_required()
def index(request):
	postagens = Postagem.objects.all()
	categorias = Categoria.objects.all()
	return render(request, 'index.html', {'postagens': postagens, 'categorias': categorias})

def detalhes_postagem(request, pk):
	postagem = get_object_or_404(Postagem, pk=pk)
	comentarios = postagem.comentarios.all()

	if request.method == 'POST':
		form = ComentarioForm(request.POST)
		if form.is_valid():
			comentario = form.save(commit=False)
			comentario.postagem = postagem
			comentario.save()
			form = ComentarioForm()  # Limpar o formulário após salvar o comentário
	else:
		form = ComentarioForm()

	return render(request, 'detalhes_postagem.html', {'postagem': postagem, 'comentarios': comentarios, 'form': form})

def postagens_por_categoria(request, categoria_slug):
	categoria = get_object_or_404(Categoria, nome=categoria_slug)
	postagens = Postagem.objects.filter(categorias=categoria)
	categorias = Categoria.objects.all()
	return render(request, 'postagens_por_categoria.html', {'categoria': categoria, 'postagens': postagens, 'categorias': categorias})

def search_results(request):
	query = request.GET.get('q')  # Obtém o valor digitado no campo de busca
	# Faça a lógica de pesquisa com base na consulta (query) e retorne os resultados relevantes
	# Neste exemplo, estou usando uma simples pesquisa pelo título da postagem
	postagens = Postagem.objects.filter(titulo__icontains=query)
	return render(request, 'search_results.html', {'postagens': postagens, 'query': query})
