from django import forms

class MailForm(forms.Form):
    visitor_mail = forms.EmailField(label='Insira seu e-mail...', max_length=100)
