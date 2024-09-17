from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def members(request):
    html=loader.get_template("presentacion.html")
    return HttpResponse(html.render())

def about(request):
    html=loader.get_template("about.html")
    valor = request.GET.get("texto")
    return HttpResponse(html.render({"name":valor}))

def login(request):
    html=loader.get_template("login.html")
    return HttpResponse(html.render())

def signup(request):
    signup=loader.get_template("signup.html")
    email = request.GET.get("email")
    name = email.split("@")
    passwd = request.GET.get("passwd")
    if (email != "" and passwd != ""):
        return HttpResponse(signup.render({"name":name[0]}))
    else:
        html=loader.get_template("login.html")
        return HttpResponse(html.render())