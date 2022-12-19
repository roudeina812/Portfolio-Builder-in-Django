from django import forms
from .models import Justification, Experience, Person, InfoPers


class PersonForm (forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
        widgets = {
            'Login': forms.TextInput(attrs={'class': 'form-control'}),
            'Password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'Role': forms.TextInput(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'Login': {
                'required': 'the login is required'
            },
            'Password': {
                'required': 'the password is required'
            },
            'Role': {
                'required': 'the Role is required'
            }
        }


class ExperienceForm (forms.ModelForm):
    class Meta:
        model = Experience
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 "
                         "text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                'placeholder': 'Enter the experience', 'maxlength': 255}),
            'Exp': forms.TextInput(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 "
                         "text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                'placeholder': 'Enter the experience', 'maxlength': 255}),
            'gender': forms.Select(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight "
                         "focus:outline-none focus:shadow-outline"}),
            'Date_Debut': forms.DateInput(attrs={'type': 'date',
                                                 'class': "shadow appearance-none border rounded w-full py-2 px-3 "
                                                         "text-gray-700 leading-tight "
                                                         "focus:outline-none focus:shadow-outline"}),
            'Date_Fini': forms.DateInput(attrs={'type': 'date',
                                                'class': "shadow appearance-none border rounded w-full py-2 px-3 "
                                                         "text-gray-700 leading-tight "
                                                         "focus:outline-none focus:shadow-outline"}),
            'Description': forms.TextInput(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 "
                         "leading-tight focus:outline-none focus:shadow-outline",
                'placeholder': 'Enter the description of experience', 'maxlength': 700}),

        }
        error_messages = {
            'Exp': {
                'required': 'Exp is required'
            },
            'Type': {
                'required': 'Type is required'
            },
            'Date_Debut': {
                'required': 'Date_Debut is required'
            },
            'Date_Fini': {
                'required': 'Date_Fini is required'
            },
            'Description': {
                'required': 'Description is required'
            }

        }


class JustificationForm (forms.ModelForm):
    class Meta:
        model = Justification
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 "
                         "text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                'placeholder': 'Enter the experience', 'maxlength': 255}),
            'Fichier': forms.FileInput(attrs={'class': 'form-control'})
        }




class InfoPersForm (forms.ModelForm):
    class Meta:
        model = InfoPers
        fields = "__all__"
        widgets = {
            'Nom': forms.TextInput(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 "
                         "text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                'placeholder': 'Enter the LastName',
                'maxlength': 20}),
            'Prenom': forms.TextInput(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 "
                         "text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                'placeholder': 'Enter the FirstName',
                'maxlength': 20}),
            'birthDate': forms.DateInput(attrs={'type': 'date',
                                                'class': "shadow appearance-none border rounded w-full py-2 px-3 "
                                                         "text-gray-700 leading-tight focus:outline-none "
                                                         "focus:shadow-outline"}),
            'email': forms.TextInput(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 "
                         "text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                'placeholder': 'Enter the mail',
                'maxlength': 50}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight "
                         "focus:outline-none focus:shadow-outline"}),

            'State': forms.TextInput(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 "
                         "text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                'placeholder': 'Enter the State', }),
            'DescPro': forms.TextInput(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 "
                         "text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                'placeholder': 'Enter the Description professionnelle'}),
            'Philo_Statement': forms.TextInput(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 "
                         "text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                'placeholder': 'Enter your philosophy statement',
                'maxlength': 100}),
            'Bio': forms.TextInput(attrs={
                'class': "shadow appearance-none border rounded w-full py-2 px-3 "
                         "text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                'placeholder': 'Enter your bio'}),

        }
        error_messages = {
            'Nom': {
                'required': 'LastName is required'
            },
            'Prenom': {
                'required': 'FirstName is required'
            },
            'email': {
                'required': 'email is required'
            },
            'State': {
                'required': 'State is required'
            },
            'DescPro': {
                'required': 'Description professionnelle is required'
            },
            'Philo_Statement': {
                'required': 'Philosophy Statement is required'
            },
            'Bio': {
                'required': 'Biography is required'
            }

        }
