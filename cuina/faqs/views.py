from django.shortcuts import render

# Create your views here.
def faqs(request):
    return render(request, "faqs/faqs.html", {
        "pagina": "faqs",
    })

def error(request):
    return render(request, "home/home.html", {
        "pagina": "error"
    })
