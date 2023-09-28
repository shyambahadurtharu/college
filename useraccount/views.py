from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from useraccount.forms import SignupForm, UserForm
from useraccount.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def user_login(request):
    form = AuthenticationForm(request.POST or None)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("post:home"))
        else:
            errors = form.get_invalid_login_error()
            for error in errors:
                messages.add_message(request, messages.ERROR, error)
    context = {"form":form}
    return render(request, "login.html", context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("user:login"))
def signup(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return HttpResponseRedirect(reverse("user:login"))
    context ={"form":form}
    return render(request, "signup.html", context)

def user_profile(request):
    user_name= request.user
    
    context = {"user":user_name,}
    return render(request, "user_profile.html", context)

def add_profile(request):
    if request.user.is_authenticated:
        form = UserForm(request.POST or None, request.FILES or None, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse( "user:user_profile"))
        context = {"form":form}
        return render(request, "user_forms.html", context)
    else:
        return redirect('user:login')
def view_profile(request, username):
    user=get_object_or_404(User, username=username)
    
    context={"user":user}
    return render(request, "user_profile.html", context)