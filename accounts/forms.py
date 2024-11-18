from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError


class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'autofocus': True}))

    def clean(self):
        email = self.cleaned_data.get('username')
        print(email)
        password = self.cleaned_data.get('password')
        print(password)
        if email and password:
            self.user_cache = authenticate(self.request, username=email, password=password)
            print(self.user_cache)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
        return self.cleaned_data


User = get_user_model()


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, min_length=8, )
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput, min_length=8, )

    class Meta:
        model = User
        fields = ['email', 'username']

    def clean_password2(self):
        # Check if password1 and password2 match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")
        return password2

    def save(self, commit=True):
        # Save the user instance with a hashed password
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


# forms.py
from django import forms
from .models import UserProfile, Company


class UserProfileForm(forms.ModelForm):
    company_name = forms.CharField(max_length=100, label="Enter Company Name")

    class Meta:
        model = UserProfile
        fields = ['company_name']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        company_name = self.cleaned_data.get('company_name')

        if company_name and self.user:
            company, created = Company.objects.get_or_create(name=company_name)

            if UserProfile.objects.filter(user=self.user, company=company).exists():
                raise forms.ValidationError("A profile for this company already exists for the user.")

        return self.cleaned_data

    def save(self, commit=True):
        company_name = self.cleaned_data['company_name']
        company, created = Company.objects.get_or_create(name=company_name)

        user_profile = super(UserProfileForm, self).save(commit=False)
        user_profile.company = company

        if commit:
            user_profile.save()
        return user_profile
