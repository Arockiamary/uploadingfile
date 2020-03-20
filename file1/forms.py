from django import forms

class StudentForm(forms.Form):
	firstname=forms.CharField(label="Enter first name", max_length=50)
	lastname=forms.CharField(label="Enter last name", max_length=50)
	email=forms.EmailField(label="Enter Email")
	file=forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True})) #for creating file ClearableFileInput