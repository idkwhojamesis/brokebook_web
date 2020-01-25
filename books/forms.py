from django import forms

class SearchForm(forms.Form):
    user_query = forms.CharField(label='your query', max_length=100, help_text='eg. ''gente volume 2''')