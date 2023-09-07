from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from item.models import Category, Item

from .forms import SignUpForm
# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items
    })

def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            print("ok till here")
            return redirect(request, '/login/', {
                'form': form
            })
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {
        'form': form
    })

@login_required
def logout_view(request):
    logout(request)
    return redirect('core/index.html')