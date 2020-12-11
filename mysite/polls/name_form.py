from django import forms # django form widgets

class NameForm(forms.Form):
    user_name = forms.CharField(label='Enter your name', max_length=64)
    subject = forms.CharField(label='Subject', max_length=120)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)