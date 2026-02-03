from django.shortcuts import render

# Create your views here.
def admin_requests(request):
    return render(request, "admin_requests/admin_requests.html", {
        "pagina": "home",
    })

def error(request):
    return render(request, "home/home.html", {
        "pagina": "error"
    })
