__author__ = 'koke07'
from django import forms
from models import Photo

# lista tacos http://goo.gl/G2nCu7

BADWORDS = ('aparcabicis','bocachancla','abollao','limpiatubos','mascachapas')

class LoginForm(forms.Form):

    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['name','url','description','license','visibility']

    def clean(self):
        cleaned_data = super(PhotoForm, self).clean()

        description = cleaned_data.get("description")

        for badword in BADWORDS:
            if badword in description:
                raise forms.ValidationError(badword + u'no esta permitido')
        else:
            return cleaned_data # todo fue ok