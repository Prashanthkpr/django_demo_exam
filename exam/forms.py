from django import forms
from exam.models import Question
from django.contrib.auth.models import User


class QuestionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
            self.fields[field].widget.attrs["placeholder"] = self.fields[field].label
        self.fields['choice'].widget.attrs["class"] = "selectpicker"
        self.fields['tags'].widget.attrs["class"] = "select2"

    class Meta:
        model = Question
        fields = ('name', 'choice', 'tags')



