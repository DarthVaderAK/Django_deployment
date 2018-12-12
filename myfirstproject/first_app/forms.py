from django import forms
from django.core import validators
from first_app.models import Users

#custom validation
def check_for_z(value):
    if value[0].lower()!= "z":
        raise forms.ValidationError("Name needs to start with z")

class FormPage(forms.Form):
    name=forms.CharField(validators=[check_for_z])
    email=forms.EmailField()
    verify_email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput, validators=[validators.MaxValueValidator(0)])
#to validate full form by using super()
    def clean(self):
        all_clean_data=super(FormPage,self).clean()
        email=all_clean_data['email']
        vemail=all_clean_data['verify_email']
        if email != vemail:
            raise forms.ValidationError("Email doesnt match")

#simple validation
"""def clean_botcatcher(self):
    botcatcher=self.cleaned_data['botcatcher']
    if len(botcatcher)>0:
        raise forms.ValidationError("Bot catched")
    return botcatcher"""


class NewUserForm(forms.ModelForm):
    class Meta:
        model=Users
        fields="__all__"
