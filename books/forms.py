from django import forms

class SearchForm(forms.Form):
    attrsList = {
        'class':"form-control",
        'placeholder':"textbook ('gente vol 2') or class ('SPAN2001')",
        'aria-label':"search input",
        'aria-describedby':"button-addon4",
    }
    user_query = forms.CharField(label='asdf', max_length=100, widget=forms.TextInput(attrs=attrsList), required=False)