from django import forms

class NewTask(forms.Form):
    title = forms.CharField(label="Task title:", max_length=200, widget=forms.TextInput(attrs={"class": 'input'}))
    description = forms.CharField(label="Task description", widget=forms.Textarea(attrs={"class": 'input'}))

class NewProject(forms.Form):
    name = forms.CharField(label="Name project:", max_length=200, widget=forms.TextInput(attrs={"class": 'input'}))