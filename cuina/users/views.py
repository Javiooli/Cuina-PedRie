
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "users/login.html", {
        "pagina": "login",
    })

def register(request):
    return render(request, "users/register.html", {
        "pagina": "register"
    })

def error(request):
    return render(request, "home/home.html", {
        "pagina": "error"
    })

