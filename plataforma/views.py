from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required # importando o decorador
from .models import Link, Comentario
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from braces.views import GroupRequiredMixin

@login_required  #A pagina só poderá ser acessada se o usuario estiver logado, por causa do login_required
def home(request):
    search = request.GET.get('search')

    if search:
        links = Link.objects.filter(titulo__icontains=search).order_by('-data_criacao')[:5]
    else:
        links = Link.objects.all().order_by('-data_criacao')[:5]

    return render(request, 'home.html',  {'links': links})


############ Linkagem para respostas ################
def Link_Views(request, id):
    links = get_object_or_404(Link, pk=id)
    return render(request, 'views.html', {'links': links})

def Detalhe_comentario(request, id):
    comentarios = get_object_or_404(Comentario, pk=id)

    return render(request, 'viewsduvidas.html', {'comentarios': comentarios})


############  Create ################
class Link_Create(GroupRequiredMixin,CreateView): #GroupRequiredMixin é uma biblioteca imortada do django-braces, utilizada para controlar acesso.
    model = Link
    group_required = u"Adiministrador" #group_ required é usado para controlar o acesso de pessoas a certlo local.
    fields = ['titulo','descricao','arquivo']
    template_name = 'create.html'
    success_url = reverse_lazy('Link_List')


class Views_Form(CreateView):
    model = Comentario
    fields = ['name','explicacao','arquivo']
    template_name = 'createduvidas.html'
    success_url = reverse_lazy('home')

############# Update ################

class Link_Update(GroupRequiredMixin,UpdateView):
    model = Link
    group_required = u"Adiministrador"
    fields = ['titulo','descricao']
    template_name = 'create.html'
    success_url = reverse_lazy('Link_List')

############# Delete ################

class Link_Delete(GroupRequiredMixin,DeleteView):
    model = Link
    group_required = u"Adiministrador"
    template_name = 'delete.html'
    success_url = reverse_lazy('Link_List')

class Comentario_Delete(GroupRequiredMixin,DeleteView):
    model = Comentario
    group_required = u"Adiministrador"
    template_name = 'deleteduvidas.html'
    success_url = reverse_lazy('Coments_List')
############# ListViews ############

class Link_List(GroupRequiredMixin, ListView ):
    model = Link
    group_required = u"Adiministrador"
    template_name = 'list.html'
    paginate_by = 5

    def get_queryset(self):

        caminho_link = self.request.GET.get('titulo')

        if caminho_link:

            Links = Link.objects.filter(titulo__icontains=caminho_link)

        else:
            Links = Link.objects.all()

        return Links

class Coments_List(ListView):
    model = Comentario
    template_name = 'listduvidas.html'
    paginate_by = 5

    def get_queryset(self):
        caminho = self.request.GET.get('Busca_Comentario')

        if caminho:

            comentarios = Comentario.objects.filter(explicacao__icontains=caminho)

        else:
            comentarios = Comentario.objects.all()

        return comentarios


