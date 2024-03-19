from django.shortcuts import render
def homePage(request):
    return render(request ,'home.html')

def logInPage(request):
    return render(request ,'logIn.html')

def signUpPage(request):
    return render(request ,'signUp.html')
# Create your views here.
