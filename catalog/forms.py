from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# This form is used for user registration. It extends the UserCreationForm provided by Django
# and adds an email field to the form.


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# This form is used to update user information. It is used to update the username and email fields
# of the User model.


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

# This form is used to update the profile image field of the Profile model


from django import forms
from .models import Ad

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'content']


from django import forms
class AdSearchForm(forms.Form):
    query = forms.CharField(label='Поиск', max_length=100)