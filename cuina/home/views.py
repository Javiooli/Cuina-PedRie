from django.shortcuts import render

# Create your views here.
def preview_base(request):
    return render(request, "home/preview.html")