from django import forms 


# class RegisterForm(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     age = forms.IntegerField()
#     address = forms.CharField()
#     mobile = forms.CharField()
#     date = forms.DateField()

class RegisterForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    age = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    date = forms.DateField(widget=forms.TextInput(attrs={'class':'form-control'}))
    