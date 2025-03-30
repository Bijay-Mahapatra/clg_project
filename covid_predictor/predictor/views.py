from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
def dash(request):
    return render(request, 'dashboard.html')
def acc(request):
    return render(request, 'account.html')
def medical(request):
    return render(request, 'medical-history.html')
def log(request):
    return render(request, 'logout.html')