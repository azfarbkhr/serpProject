from django import forms
from django.core import validators

from .models import Invoice, Consultation, Service, Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class sample_form(forms.Form):
    text_field = forms.CharField(required=False, help_text='Enter some text', label='Text', initial='text', widget=forms.TextInput, min_length=0, max_length=100, strip=True, error_messages={'required': 'This field is required.', 'invalid_alphanumeric': 'abc'}, validators=[validators.RegexValidator(regex='^[a-zA-Z0-9]*$', message='Only alphanumeric characters are allowed.', code='invalid_alphanumeric')])
    text_area = forms.CharField(widget=forms.Textarea, max_length=65000, required=False, help_text='Enter some text', label='Text Area', initial='text area')
    date_field = forms.DateField(widget=forms.SelectDateWidget, required=False)
    time_field = forms.TimeField(widget=forms.TimeInput, required=False, initial='00:00')
    datetime_field = forms.DateTimeField(widget=forms.DateTimeInput, required=False, initial='2019-01-01 00:00:00', help_text='YYYY-MM-DD HH:MM:SS', input_formats=['%Y-%m-%d %H:%M:%S'], label='Date and Time')
    email_field = forms.EmailField(required=False, help_text='Enter a valid email address', label='Email Address', widget=forms.TextInput(attrs={'placeholder': 'Enter some email address', 'autocomplete':'off'}), error_messages={'required': 'This field is required.', 'invalid': 'Enter a valid email value'})
    url_field = forms.URLField(widget=forms.URLInput, required=False, help_text='Enter a valid URL', label='URL')
    number_field = forms.IntegerField( widget=forms.NumberInput, required=False, help_text='Enter a valid number', label='Number', initial=0, min_value=0, max_value=100)
    decimal_field = forms.DecimalField(widget=forms.NumberInput, required=False, help_text='Enter a valid decimal number', label='Decimal', initial=0, min_value=0, max_value=100, max_digits=10, decimal_places=2)
    boolean_field = forms.BooleanField(required=False, help_text='Check this box if you want to proceed', label='Boolean', initial=False, widget=forms.CheckboxInput)
    choice_field = forms.ChoiceField(choices=[('1', 'Choice 1'), ('2', 'Choice 2')], required=False, help_text='Select a choice', label='Choice', initial='1', widget=forms.Select)
    multiple_choice_field = forms.MultipleChoiceField(choices=[('1', 'Choice 1'), ('2', 'Choice 2')])
    file_field = forms.FileField( widget=forms.FileInput, required=False, help_text='Upload a file', label='File')
    image_field = forms.ImageField( widget=forms.FileInput, required=False, help_text='Upload an image', label='Image')
    hidden_field = forms.CharField(widget=forms.HiddenInput, required=False, initial='hidden')
    password_field = forms.CharField(widget=forms.PasswordInput, required=False, help_text='Enter a password', label='Password')


    class Meta:
        fields = '__all__'
        

    


class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = '__all__'
    

    
