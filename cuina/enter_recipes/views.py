from django.shortcuts import render

# Create your views here.
def enter_recipes(request):
    return render(request, "enter_recipes/enter_recipes.html", {
        "pagina": "enter_recipes",
    })

def error(request):
    return render(request, "home/home.html", {
        "pagina": "error"
    })
