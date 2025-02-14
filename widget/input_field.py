from django import forms

class InputFieldForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your hint text here', 'rows': 3}), required=True)
