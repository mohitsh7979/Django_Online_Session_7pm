from django import forms 

class StudentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    mobile_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    date = forms.DateField(widget=forms.DateTimeInput(attrs={'class':'form-control'}))
    