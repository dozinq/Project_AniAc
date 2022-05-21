from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    rank = forms.FloatField(widget=forms.NumberInput(
            attrs={'step': 1, 'min': 0, 'max': 10}
    ))
    movie_title = forms.CharField(required=False)
    rank = forms.IntegerField(required=False)

    class Meta:
        model = Review
        fields = ['title', 'movie_title', 'rank', 'content']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['review', 'user', 'created_at']
