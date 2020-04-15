from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import PhonesTab

# главная страница со списком загадок
def index(request):
    message = None
    if "message" in request.GET:
        message = request.GET["message"]
    # создание HTML-страницы по шаблону index.html
    phn = PhonesTab.objects.all()
    return render(
        request,
        "index.html",
        # {
        #       "phn": PhonesTab
        #      #"message": message
        # }
        locals()
    )

