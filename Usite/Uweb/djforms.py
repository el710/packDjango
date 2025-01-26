'''
    Using Django input html-template forms 
'''
from django import forms

class RegForm(forms.Form):
    '''
        get from html forms data by "name":

        Example: 
        if there is in some ***.html
        ...
            <input type="text" name="NAME" maxlength="30" > 
        ...
        
        so we should create
        NAME = forms.CharField(...)
    '''

    name = forms.CharField(label="Name:", max_length=100)
    email = forms.EmailField(label="E-mail:")
    message = forms.CharField(label="Message:", widget=forms.Textarea)
    box = forms.BooleanField(label="Premium", required=False)

    '''
        this template Django will try to find in ***.html
    '''
