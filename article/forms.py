from django import forms

from .models import Comment

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field, Submit

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Field(
                'author', css_class="bg-light"
            ),
            Field(
                'content', css_class="bg-light"
            )
        )
        self.helper.form_class = 'bg-light'
        self.helper.add_input(Submit('submit', 'Gönder', css_class='btn btn-primary float-right'))

