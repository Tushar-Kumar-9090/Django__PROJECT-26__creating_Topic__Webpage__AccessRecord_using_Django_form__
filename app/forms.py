from django import forms

class TopicForm(forms.Form):
    topic_name = forms.CharField()


class WebpageForm(forms.Form):
    topic_name = forms.CharField()
    name = forms.CharField()
    url = forms.URLField()

class AccessRecordForm(forms.Form):
    name = forms.CharField()
    date = forms.DateField()
    author = forms.CharField()
