from django.http import HttpResponse


def index(request):
    first_name = "Seelan"
    last_name = "Cyrilraj"
    return HttpResponse("Hello "+first_name+" "+last_name+", You're in your book library app.")

def SecondPage(request):
    first_name = "Seelan"
    last_name = "Cyrilraj"
    return HttpResponse("Hello "+first_name+" "+last_name+", You're in the second page of your Python app.")