from django import forms

class pasar_dato(forms.Form):
    dato = forms.CharField(widget=forms.Textarea)