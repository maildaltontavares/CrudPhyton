from django.shortcuts import render,redirect

from django.shortcuts import HttpResponse
# Create your views here.

from . models import News,DataRegistro
from . forms import RegistroForm,LoginForm
from django.contrib import messages
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def home(request):
    context = {
        "text":"daltontavares",
        "nomes":["elemento 01","elemento 02","elemento 03"]

    }
#    return HttpResponse("<h1>BEM VINDO AO PROJETO DJANGO</h1>")
    return render(request,"home.html",context)

def contato(request):
#    return HttpResponse("<h1>BEM VINDO A PAGINA CONTATO</h1>")
    context = {
        "text":"daltontavares"
    }
    return render(request,"contato.html",context)

def usuario(request):

    username = request.GET.get('nome',None)
    email = request.GET.get('email',None)

    if username or email:
        list = DataRegistro.objects.filter(username=username) | DataRegistro.objects.filter(email=email).order_by('username')

    else:
        list = DataRegistro.objects.all().order_by('username')

    paginator = Paginator(list, 6)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # Se o page request (9999) está fora da lista, mostre a última página.
    try:
        list_users = paginator.page(page)
    except (EmptyPage, InvalidPage):
        list_users = paginator.page(paginator.num_pages)


    context = {
        "arquivo_list": list_users,
        "pesqUsername":username,
        "pesqEmail":email,


    }


    return render(request,"usuario.html",context)

def novidade_anual(request,year):
#    return HttpResponse("<h1>BEM VINDO A PAGINA CONTATO</h1>")
    list = News.objects.filter(pub_date__year=year)
    context = {
        "year":year,
        "arquivo_list": list
    }
    return render(request,"novidade_anual.html",context)

def registro(request):
#    return HttpResponse("<h1>BEM VINDO A PAGINA CONTATO</h1>")
    form = RegistroForm(request.POST or None)
     ## Verifica se recebeu algum submit. Caso nao tenha recebido, form.is_valid() não é valido

    if form.is_valid():
        registro = DataRegistro(
                                username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'],
                                email=form.cleaned_data['email'],
                                tel=form.cleaned_data['tel']
                                )
        registro.save()
        return redirect("usuario")

    context = {
        "form":form
    }
    return render(request,"registro.html",context)


def addUser(request):
    form = RegistroForm(request.POST or None)
    ## Verifica se recebeu algum submit. Caso nao tenha recebido, form.is_valid() não é valido
    if form.is_valid():
        registro = DataRegistro(
                                username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'],
                                email=form.cleaned_data['email'],
                                tel=form.cleaned_data['tel']
                                )
        registro.save()
        messages.add_message(request,messages.SUCCESS,"Registro cadastrado com sucesso!")
        # return redirect('add')
        return redirect('usuario')

def altUser(request,id):
    registroF = DataRegistro.objects.get(id=id)
    form = RegistroForm(request.POST or None ,instance= registroF ) ##
    context = {
        "form":form,
        "registroA":registroF
    }
    if form.is_valid():
        registroF.save()
        return redirect("usuario")

    return render(request,"registro.html",context)

def excUser(request,id):

    registroF = DataRegistro.objects.get(id=id)

    if request.method == 'POST':
        registroF.delete()
        return redirect("usuario")

    context = {
        "registroA":registroF}

    return render(request,"confdel.html",context)

def pesqUser(request,pUsername):
    ##list = DataRegistro.objects.filter(pub_date__username=pUsername)
    list = DataRegistro.objects.get(username=pUsername)
    context = {
        "arquivo_list": list
    }
    return render(request, "usuario.html", context)

def index(request):
    context = {

    }
    return render(request,"index.html",context)

def login(request):
    #    return HttpResponse("<h1>BEM VINDO A PAGINA CONTATO</h1>")
    form = LoginForm(request.POST or None)
    ## Verifica se recebeu algum submit. Caso nao tenha recebido, form.is_valid() não é valido

    if form.is_valid():
        pUsername = form.cleaned_data['username']
        pPassword = form.cleaned_data['password']

        registroLogin = DataRegistro.objects.filter(username=pUsername,password=pPassword)

        if registroLogin:
            return redirect("index")
        else:
            messages.add_message(request, messages.SUCCESS,"Username ou Password Invalido!")
            return redirect("login")

    context = {
        "form": form
    }
    return render(request,"login.html",context)