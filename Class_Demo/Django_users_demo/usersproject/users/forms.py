from django import forms
from .models import Users

# class UserForm(forms.Form):
# 	name = forms.CharField(max_length=30)
# 	email = forms.EmailField()
# 	age = forms.IntegerField()

class UserForm(forms.ModelForm):
	class Meta:
		model = Users
		fields = ['name', 'email', 'age']