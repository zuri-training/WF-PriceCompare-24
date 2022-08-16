from django.contrib.auth.forms import UserCreationForm # UserChangeForm
from django.contrib.auth.models import User
from django import forms

class EmailForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)



# class CreateProfile(UserCreationForm):
    
#     email = forms.EmailField(label="", widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Email Address'}), )
#     first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'First Name'}))
#     last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Last Name'}))


# class Meta:
#     model = User
#     fields = ('username', 'first_name', 'last_name',
#               'email', 'password1', 'password2',)


# def __init__(self, *args, **kwargs):
#     super(CreateProfile, self).__init__(*args, **kwargs)

#     self.fields['username'].widget.attrs['class'] = 'form-control'
#     self.fields['username'].widget.attrs['placeholder'] = 'User Name'
#     self.fields['username'].label = ''
#     self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

#     self.fields['password1'].widget.attrs['class'] = 'form-control'
#     self.fields['password1'].widget.attrs['placeholder'] = 'Password'
#     self.fields['password1'].label = ''
#     self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

#     self.fields['password2'].widget.attrs['class'] = 'form-control'
#     self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
#     self.fields['password2'].label = ''
#     self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, help_text='first name / username')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')
    phone_number = forms.IntegerField(help_text='Phone Number')


    class Meta:
        model = User
        fields = ('username', 'last_name', 'email', 'phone_number', 'password1', 'password2')