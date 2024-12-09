from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from phonenumber_field.formfields import PhoneNumberField
from .models import Question

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
 

class QuestionForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()

        option_1 = cleaned_data.get('option_1', '').strip()
        option_2 = cleaned_data.get('option_2', '').strip()
        option_3 = cleaned_data.get('option_3', '').strip() if cleaned_data.get('option_3') else ''
        option_4 = cleaned_data.get('option_4', '').strip() if cleaned_data.get('option_4') else ''
        correct_option = cleaned_data.get('correct_option')

        if option_1.lower() in ['true', 'false'] and option_2.lower() in ['true', 'false']:
            if option_1.lower() == option_2.lower():
                raise ValidationError("Option 1 and Option 2 cannot be the same for True/False questions.")
            if option_3 or option_4:
                raise ValidationError("Option 3 and Option 4 must be empty for True/False questions.")
            if correct_option not in [option_1, option_2]:
                raise ValidationError("For True/False questions, the correct option must be one of the provided options.")
        else:
            if not option_3 or not option_4:
                raise ValidationError("For multiple-choice questions, Option 3 and Option 4 are required.")
            if correct_option not in [option_1, option_2, option_3, option_4]:
                raise ValidationError("Correct option must be one of the provided options.")

        return cleaned_data

    def clean_question_text(self):
        question_text = self.cleaned_data['question_text']
        if Question.objects.filter(question_text=question_text).exists():
            raise ValidationError("This question already exists.")
        return question_text

    class Meta:
        model = Question
        fields = ['question_text', 'option_1', 'option_2', 'option_3', 'option_4', 'correct_option']
        labels = {
            'question_text': 'Question Text',
            'option_1': 'Option 1',
            'option_2': 'Option 2',
            'option_3': 'Option 3',
            'option_4': 'Option 4',
            'correct_option': 'Correct Option (Enter the text of the correct option)',
        }
        widgets = {
            'correct_option': forms.TextInput(attrs={'placeholder': 'Enter the text of the correct option (e.g., Python)'}),
        }

