from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=True)
    
class ExampleForm(forms.Form):
    # Example field(s) - adjust as needed
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
