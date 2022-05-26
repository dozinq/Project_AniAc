from django import forms
from .models import Movie

# Create your forms here.
class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        exclude = ('like_users')