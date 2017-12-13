from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Python_App.models import Book
from .forms import bookSearch

def index(request):
    first_name = "Seelan"
    last_name = "Cyrilraj"
    return render(request, 'Python_App/index.html', context=None)
    #return HttpResponseRedirect('secondPage')

def SecondPage(request):
    #first_name = "Seelan"
    #last_name = "Cyrilraj"
    #return HttpResponse("Hello "+first_name+" "+last_name+", You're in the second page of your Python app.")
    return render(request, 'Python_App/SecondPage.html', {'content' : ''})

def BookDetails(request):
    name_book = request.GET.get("book")
    pub_book = request.GET.get("pub")
    author_book = request.GET.get("author")
    if (name_book !=''):
        data = Book.objects.filter(Q(Name__contains = name_book))
    elif (author_book != ''):
        data = Book.objects.filter(Q(Author__contains = author_book))
    elif(pub_book != ''):
        data = Book.objects.filter(Q(Publication__contains = pub_book))
    else:
        data = Book.objects.filter(Q(Name__contains = name_book) | Q(Publication__contains = pub_book) | Q(Author__contains = author_book)).order_by('Name')
    totalValue = data.count()
    return render(request, 'Python_App/Details.html', {'valueIS' : data, 'Tot' : totalValue })