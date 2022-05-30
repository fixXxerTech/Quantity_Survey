from django import forms
from .models import UserProfile
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm, 
    AuthenticationForm,
)

Authenticated_user = get_user_model()

class RegisterationForm(UserCreationForm):

    username = forms.CharField(
        label='User Name',
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'id': 'username',
                'name': 'username',
                'placeholder': '',
                'required': 'required',
                'autofocus': 'autofocus',
                'class': 'form-control form-control-lg',
            }
        )
    )

    email = forms.CharField(
        label='Email Address',
        widget=forms.EmailInput(
            attrs={

                'type': 'email',
                'id': 'email',
                'name': 'email',
                'placeholder': '',
                'class': 'form-control form-control-lg',

            }
        )
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={

                'type': 'password',
                'name': 'password1',
                'id': 'password1',
                'class': 'form-control form-control-lg',

            }
        )
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={

                'type': 'password',
                'name': 'password2',
                'id':'password2',
                'class': 'form-control form-control-lg',

            }
        )
    )

    class Meta:
    	model = Authenticated_user
    	fields = (
    		"username",
    		"email",
    		"password1",
    		"password2",
    	)

    	exclude = (
    		"first_name", 
    		"last_name",
    	)

    def clean_email(self):
        useremail = self.cleaned_data['email'].lower()
        Auth_user = Authenticated_user.objects.filter(email=useremail)
        if Auth_user.exists():
            raise ValidationError(
                f'This user email: "{useremail}" is already in use !!')
        return useremail

    def save(self, commit=True):
        Auth_user = super(RegisterationForm, self).save(commit=False)
        Auth_user.username = self.cleaned_data['username']
        Auth_user.email = self.cleaned_data['email']

        if commit:
            Auth_user.save()

        return Auth_user


class UserProfileForm(forms.ModelForm):
    ''' NOTE!!!: Do not touch this class for an reason. The text input tyoes are there because
    postgres db has a problem with normal integer field which take long digits eg phonenumbers, I don't know why. '''

    userphonenumber = forms.CharField(
        label='Phone Number',
        widget=forms.TextInput(
            attrs={

                'type': 'text',
                'id': 'userphone',
                'maxlength': '20',
                'name': 'userphonenumber',
                'placeholder': 'Phone Number',
                'class': 'form-control form-control-lg',

            }
        )
    )

    class Meta:
        model = UserProfile
        fields = (
            'userphonenumber',
        )

    # You must use the exact name of the field in the form here or the function wont't run.
    def clean_userphonenumber(self):
        phonenumber = self.cleaned_data['userphonenumber']
        Auth_user = UserProfile.objects.filter(
            userphonenumber=phonenumber
        )
        try:
            if int(phonenumber) and not str(phonenumber):
                min_length = 10
                max_length = 13
                ph_length = str(phonenumber)
                if len(ph_length) < min_length or len(ph_length) > max_length:
                    raise ValidationError('Phone number length not valid')

            if Auth_user.exists():
                raise ValidationError(
                    f'This user phone number: "{phonenumber}" is already in use !!')

        except (ValueError, TypeError):
            raise ValidationError('Please enter a valid phone number')

        return phonenumber

    def save(self, commit=True):
        UserProfile = super(UserProfileForm, self).save(commit=False)
        try:
            UserProfile.userphonenumber = self.cleaned_data['userphonenumber']
        except Exception as Error:
            raise (Error)

        if commit:
            try:
                UserProfile.save()
            except Exception as Error:
                raise (Error)

        return UserProfile



class LoginForm(AuthenticationForm):
    # uncomment email and comment username

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={

                'id': 'name3',
                'type': 'text',
                'name': 'username',
                'class': 'input--dark input--squared',
                'placeholder': '',
            }
        )
    )

    # email = forms.CharField(
    #     label='Email Address',
    #     widget=forms.EmailInput(
    #         attrs={

    #             'type': 'email',
    #             'id': 'email',
    #             'name': 'email',
    #             'placeholder': '',
    #             'class': 'input--dark input--squared',

    #         }
    #     )
    # )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={

                'id': 'password3',
                'type': 'password',
                'name': 'password',
                'placeholder': '',
                'class': 'input--dark input--squared',
            }
        )
    )

    remember_me = forms.BooleanField(
        required=False,
        label='Remember Me',
        widget=forms.CheckboxInput(
            attrs={

                'type': 'checkbox',
                'id': 'remember_me',
                'checked': 'checked',
                'name': 'remember_me',
                'class': 'custom-control-input',
            }
        )
    )

    class Meta:
        model = Authenticated_user

        fields = (
            # 'email',
            'username',
            'password',
        )

        exclude = (
            'first_name',
            'last_name',
            # 'username',
        )
