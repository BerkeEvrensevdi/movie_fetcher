from django import forms
from film.models import Score,Post



class DetailForm(forms.ModelForm):
    score = forms.DecimalField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = Score
        fields = ('score',)


class PostForm(forms.ModelForm):
    post = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'id_long_desc',
    }
    ))

    class Meta:
        model = Post
        fields = ('post',)




