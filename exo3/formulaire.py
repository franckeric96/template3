from django import forms
from contact.models import Contact
from blog.models import Commentaire


class ContactForm(forms.ModelForm):
    nom = forms.CharField( label_suffix='', widget=forms.TextInput(
        attrs={
            'id': 'name',
            'class': "form-control",
            'placeholder': "Enter your name"
        }
    ))
    email = forms.CharField( label_suffix='', widget=forms.EmailInput(
        attrs={
            'id': 'email',
            'class': "form-control",
            'placeholder': "Enter email address"
        }
    ))
    sujet = forms.CharField( label_suffix='', widget=forms.TextInput(
        attrs={
            'id': 'subject',
            'class': "form-control",
            'placeholder': " Enter Subject"
        }
    ))
    message = forms.CharField( label_suffix='', widget=forms.Textarea(
        attrs={
            'id': 'message',
            'class': "form-control",
            'placeholder': "Message",
            'cols': "30",
            'rows': "9",
        }
    ))
    class Meta:
        model = Contact
        fields = ('message', 'nom', 'email', 'sujet')



class CommentForm(forms.ModelForm):
    nom = forms.CharField(label="Name", label_suffix=' *', widget=forms.TextInput(
        attrs={
            'id': 'name',
            'class': "form-control",
        }
    ))
    email = forms.CharField(label="Email", label_suffix=' *', widget=forms.EmailInput(attrs={
            'id': 'email',
            'class': "form-control",
        }
    ))
    site = forms.CharField(label="Website", label_suffix='', widget=forms.TextInput(
        attrs={
            'id': 'website',
            'class': "form-control",
        }
    ))
    contenu = forms.CharField(label="Message", label_suffix='', widget=forms.Textarea(
        attrs={
            'id': 'message',
            'class': "form-control",
            'cols': "30",
            'rows': "10",
        }
    ))
    class Meta:
        model = Commentaire
        fields = ('nom', 'email', 'site', 'contenu')
