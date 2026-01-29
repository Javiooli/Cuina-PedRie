from django.shortcuts import render

# Create your views here.
def recipes(request):
    return render(request, "recipes/recipes.html", {
        "pagina": "recipes",
    })

def error(request):
    return render(request, "home/home.html", {
        "pagina": "error"
    })
