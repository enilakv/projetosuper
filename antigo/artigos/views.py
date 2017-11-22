from django.shortcuts import render

# Create your views here.
from .models import Artigo

def artigos_list(request):
    artigos = Artigo.objects.all()

    context ={
        'artigos_list': artigos,
    }

    return render(request,'artigo/artigo_list.html',context)
