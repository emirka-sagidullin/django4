from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contacts(request):
    data = {"tg": "@zzerrozz", "tel": "+7(951) 890-26-96"}
    return render(request, "contacts.html", context={"data": data})