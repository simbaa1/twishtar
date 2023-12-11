from django.shortcuts import render



def index(request):
    welcome = 'Welcome'
    context = {
        'welcome': welcome
    }

    return render(request, 'home.html', context)
