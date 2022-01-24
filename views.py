from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from .filters import Filter

def main(request):
    return render(request, 'teammate_finder_app/main.html')


def register(request):
    if request.method == "POST":     
        form= UserRegisterForm(request.POST) 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your  account was creaated succesfully')
            return redirect('login')
    else:
        form = UserRegisterForm()
        
    return render(request, 'teammate_finder_app/register.html', {'form':form})

def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your  account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form,
        
    }

    return render(request, 'teammate_finder_app/profile.html',context)

def find_your_teammate(request):
    profile_list = Profile.objects.all()
    myFilter = Filter(request.GET, queryset=profile_list)

    return render(request, 'teammate_finder_app/find_your_teammate.html',{'myFilter' : myFilter})

