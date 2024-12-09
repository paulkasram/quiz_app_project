from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from phonenumber_field.formfields import PhoneNumberField


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email",
        error_messages={'required': 'Email is required. Please provide a valid email.'}
    )
    first_name = forms.CharField(
        required=True,
        label="First Name",
        error_messages={'required': 'First name is required.'}
    )
    last_name = forms.CharField(
        required=True,
        label="Last Name",
        error_messages={'required': 'Last name is required.'}
    )
    phone_number = PhoneNumberField(
        required=False,
        label="Phone Number",
        error_messages={'invalid': 'Enter a valid phone number with country code.'}
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken.")
        return username    

    username = forms.CharField(
        required=True,
        label="Username",
        min_length=3,
        error_messages={
            'required': 'Username is required.',
            'min_length': 'Username must be at least 3 characters long.',
            'invalid': 'Only letters, digits, and @/./+/-/_ are allowed.'
        }
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2']
