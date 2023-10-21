from django.shortcuts import render

def home_view(request):
    return render(request, "recipes/pages/home.html", status=200, context={
        'name': 'Cleber Goulart Nandi'
    })
