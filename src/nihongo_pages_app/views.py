from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

def home(request):
    return render(request, 'pages/index.html')