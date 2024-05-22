from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Proletary, View, Work, WorkInstance

from django.shortcuts import render, redirect
from .models import Ad
from .forms import AdForm



def index(request):
    ads = Ad.objects.all()
    form = AdForm()

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AdForm(request.POST)
            if form.is_valid():
                ad = form.save(commit=False)
                ad.user = request.user
                ad.save()
                return redirect('index')

    return render(request, 'index.html', {'ads': ads, 'form': form})

    num_works = Work.objects.all().count()
    num_instances = WorkInstance.objects.all().count()
    num_instances_available = WorkInstance.objects.filter(status__exact='a').count()
    num_proletaries = Proletary.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'index.html',
        context={'num_works': num_works, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_proletaries': num_proletaries,
                 'num_visits': num_visits},
    )



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('register')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        # Обработка форм обновления пользователя и профиля
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if hasattr(request.user, 'profile'):
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        else:
            p_form = ProfileUpdateForm(request.POST, request.FILES)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()

            if hasattr(request.user, 'profile'):
                p_form.save()
            else:
                profile = p_form.save(commit=False)
                profile.user = request.user
                profile.save()

            messages.success(request, 'Your profile has been successfully updated.')
            return redirect('profile')
    else:
        # Отображение форм обновления пользователя и профиля
        u_form = UserUpdateForm(instance=request.user)

        if hasattr(request.user, 'profile'):
            p_form = ProfileUpdateForm(instance=request.user.profile)
        else:
            p_form = ProfileUpdateForm()

    ads = Ad.objects.filter(user=request.user)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'ads': ads
    }
    return render(request, 'profile.html', context)

def home(request):
    ads = Ad.objects.all()
    form = AdForm()

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AdForm(request.POST)
            if form.is_valid():
                ad = form.save(commit=False)
                ad.user = request.user
                ad.save()
                return redirect('index')

    return render(request, 'index.html', {'ads': ads, 'form': form})


from django.shortcuts import render

def create_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            return redirect('profile')
    else:
        form = AdForm()
    return render(request, 'create_ad.html', {'form': form})

def edit_ad(request, ad_id):
    ad = Ad.objects.get(id=ad_id)
    if request.method == 'POST':
        form = AdForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = AdForm(instance=ad)
    return render(request, 'edit_ad.html', {'form': form})

def delete_ad(request, ad_id):
    ad = Ad.objects.get(id=ad_id)
    ad.delete()
    return redirect('profile')





from .forms import AdSearchForm


def ad_search(request):
    form = AdSearchForm()
    results = None

    if request.method == 'POST':
        form = AdSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Ad.objects.filter(title__icontains=query)

    return render(request, 'ad_search.html', {'form': form, 'results': results})