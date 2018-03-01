from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from Python_App.models import Book, User
from django.contrib import messages
import datetime
import requests

def index(request):
    first_name = 'John'
    timeNow = datetime.datetime.now()
    print(request.user)
    print(request.user)
    if request.user.is_authenticated() == True:
        allow = True
        current_user = request.user
        return render(request, 'Python_App/home.html', {'allow':allow ,'current_user':current_user})
    else:
        allow = False
        return render(request, 'Python_App/login.html', {'allow':allow})
    #return HttpResponseRedirect('secondPage')

def loginPage(request):
    return render(request, 'Python_App/login.html')

def registerUser(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    uId = request.POST.get('uname')
    password = request.POST.get('passwd')
    role = 'RO'
    user = authenticate(request, username=uId, password=password)
    loggedIn = datetime.datetime.now()
    availabilityResult = User.objects.filter(Q(UID = uId))
    if availabilityResult:
        messages.success(request,' This user may registered already or the user name already exists!!')
        status = 'Fail'
    else:
        data = User(UID = uId, Email = email, User_Name = name, logged_In = loggedIn, Password = password, Role = role)
        data.save()
        messages.success(request, 'User registered to the system successfully!')
        status = 'Pass'
    return render(request, 'Python_App/login.html', { 'status': status })

# def initiate_login(request, login):
#     def check_login(*args, **kwargs):
#         return render(request, 'Python_App/login.html')
#     return check_login

def loginUser(request):
    uId = request.POST.get('uname')
    password = request.POST.get('passwd')
    user = authenticate(request, username=uId, password=password)
    if user is not None:
        login(request, user)
        print("user logged in: ", request.user.is_authenticated())
        user_ID = request.user
        print("Logged user:", user_ID)
        allow = True
        return render(request, 'Python_App/SecondPage.html', {'current_user': user_ID, 'allow':allow}, )
    else:
        result = 'Invalid Credential'
        return render(request, 'Python_App/login.html', {'result': result})
    # user = User.objects.filter(Q(UID=uId), Q(Password=password))
    # if user:
    #     for a in user:
    #         userName = a.User_Name
    #     return render(request, 'Python_App/SecondPage.html', {'userDetails' : user}, userName)
    # else:
    #     result = 'Invalid Credential'
    #     return render(request, 'Python_App/login.html', {'result': result})
    return render(request, 'Python_App/SecondPage.html', {'content' : ''})

def SecondPage(request):
    return render(request, 'Python_App/SecondPage.html', {'content' : ''})

def BookDetails(request):
    name_book = request.POST.get("book")
    pub_book = request.POST.get("pub")
    author_book = request.POST.get("author")
    loggedUser = request.POST.get("LoggedUser")
    Role = request.POST.get("Role")
    if(Role == 'admin'):
        showButtons  = True
    else:
        showButtons = False
    if (name_book !=''):
        data = Book.objects.filter(Q(Name__icontains = name_book))
    elif (author_book != ''):
        data = Book.objects.filter(Q(Author__icontains = author_book))
    elif(pub_book != ''):
        data = Book.objects.filter(Q(Publication__icontains = pub_book))
    else:
        data = Book.objects.filter(Q(Name__icontains = name_book) | Q(Publication__icontains = pub_book) | Q(Author__icontains = author_book)).order_by('Name')
    totalValue = data.count()
    return render(request, 'Python_App/Details.html', {'valueIS' : data, 'Tot' : totalValue, 'Access':showButtons, 'loggedInuser':loggedUser})

def AddBook(request):
    name_book = request.POST.get("bookName")
    pub_book = request.POST.get("publication")
    author_book = request.POST.get("author")
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
    name_book = request.POST.get("bookName")
    pub_book = request.POST.get("publication")
    author_book = request.POST.get("author")
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
    oldBook = request.POST.get("bookNameOld")
    name_book = request.POST.get("bookName")
    pub_book = request.POST.get("publication")
    author_book = request.POST.get("author")
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

def weatherForecast(request):
    default_location = "Sholinganallur"
    location = request.GET.get('city')
    if location is None:
        location = default_location
    weather_data = {}
    base_API_url = "http://api.openweathermap.org/data/2.5/weather?appid=122db1be332cfd2a8320b53ba1c0e5b8&q="
    full_url = base_API_url + location
    API_data = requests.get(full_url).json()
    if API_data['cod'] != 200:
        print("No Match found")
    else:
        weather_data['Main'] = API_data['weather'][0]['main']
        weather_data['Description'] = API_data['weather'][0]['description']
        weather_data['Temperature'] = API_data['main']['temp']
        weather_data['Pressure'] = API_data['main']['pressure']
        weather_data['Humidity'] = API_data['main']['humidity']
        weather_data['Wind'] = API_data['wind']['speed']
        weather_data['Name'] = API_data['name']
        return render(request, 'Python_App/weather.html', {'fromAPI': weather_data})
    return render(request, 'Python_App/weather.html', {'fromAPI': weather_data})

def logoutUser(request):
    logout(request)
    return render(request, 'Python_App/login.html')