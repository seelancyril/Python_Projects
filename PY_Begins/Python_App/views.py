from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Python_App.models import Book
from django.contrib import messages

def index(request):
    return render(request, 'Python_App/index.html', context=None)
    #return HttpResponseRedirect('secondPage')

def SecondPage(request):
    return render(request, 'Python_App/SecondPage.html', {'content' : ''})

def BookDetails(request):
    name_book = request.GET.get("book")
    pub_book = request.GET.get("pub")
    author_book = request.GET.get("author")
    if (name_book !=''):
        data = Book.objects.filter(Q(Name__icontains = name_book))
    elif (author_book != ''):
        data = Book.objects.filter(Q(Author__icontains = author_book))
    elif(pub_book != ''):
        data = Book.objects.filter(Q(Publication__icontains = pub_book))
    else:
        data = Book.objects.filter(Q(Name__icontains = name_book) | Q(Publication__icontains = pub_book) | Q(Author__icontains = author_book)).order_by('Name')
    totalValue = data.count()
    return render(request, 'Python_App/Details.html', {'valueIS' : data, 'Tot' : totalValue })

def AddBook(request):
    name_book = request.GET.get("bookName")
    pub_book = request.GET.get("publication")
    author_book = request.GET.get("author")
    Max_ID = Book.objects.latest('Book_id')
    bookId = int(Max_ID.Book_id) + 1
    data = Book(Book_id = bookId, Name = name_book, Author = author_book, Publication = pub_book)
    if(name_book !='' and pub_book !='' and author_book !=''):
        data.save()
        messages.success(request, ' Book added to the library')
        status = 'SUCCESS'
    else:
        status = 'FAIL'
        messages.error(request, ' Book not added to the library')
    dataAll = Book.objects.all().order_by('Name')
    totalValue = dataAll.count()
    return render(request, 'Python_App/Details.html', {'Status' : status, 'valueIS' : dataAll, 'Tot' : totalValue})

def removeBook(request):
    name_book = request.GET.get("bookName")
    pub_book = request.GET.get("publication")
    author_book = request.GET.get("author")
    availabilityResult  = Book.objects.filter(Q(Name = name_book),Q(Publication = pub_book),Q(Author = author_book)).values()
    if availabilityResult:
        data = Book.objects.get(Name=name_book, Author=author_book, Publication=pub_book)
        data.delete()
        status = 'SUCCESS'
        messages.success(request, ' Book removed from the library')
    else:
        status = 'FAIL'
        messages.success(request, ' Book not removed, Please provide the correct book info')
    dataAll = Book.objects.all().order_by('Name')
    totalValue = dataAll.count()
    return render(request, 'Python_App/Details.html', {'Status': status, 'valueIS' : dataAll, 'Tot' : totalValue})

def updateBook(request):
    oldBook = request.GET.get("bookNameOld")
    name_book = request.GET.get("bookName")
    pub_book = request.GET.get("publication")
    author_book = request.GET.get("author")
    data = Book.objects.get(Name=oldBook)
    if (name_book != '' and pub_book != '' and author_book != ''):
        data.Name = name_book
        data.Publication = pub_book
        data.Author = author_book
        data.save()
        messages.success(request, ' Book information updated to the library')
    else:
        pass
    dataAll = Book.objects.all().order_by('Name')
    totalValue = dataAll.count()
    return render(request, 'Python_App/Details.html', {'valueIS' : dataAll, 'Tot' : totalValue})