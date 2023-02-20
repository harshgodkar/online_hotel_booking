from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    
    return render(request, 'login.html')

def contact(request):
    return render(request, 'contact.html')

# def getUsers(request):
#     context = {}
#     form = UserForm(request.POST)
#     if form.is_valid():
#         form.save()
    
#     context['form'] = form
#     return render(request, 'create_view.html', context)

def registeruser(request):
    dic = {}
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
    dic = {'form' : form}

    return render(request, 'create_view.html', dic)

