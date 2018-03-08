from django import forms
from .models import Restaurant
from datetime import date
from .validators import validate_category
#from datetime import datetime

class RestaurantCreateForm(forms.Form):
	name=forms.CharField()
	#dob = forms.date()
	location=forms.CharField(required=False)
	category=forms.CharField(required=False)
	#date= forms.DateTimeField(initial=datetime.now(), required=False)

	def clean_name(self):
		name=self.cleaned_data.get("name")
		if name=="Hello":
			raise forms.ValidationError("Not a Valid Name")
		return name


class RestaurantLocationCreateForm(forms.ModelForm):
	email=forms.EmailField()
	category=forms.CharField(required=False,validators=[validate_category])
	class Meta:
		model=Restaurant
		fields=[
			'name',
			'location',
			'category',
			'owner',
			#'dob',
			#'date',
			]

	def clean_name(self):
		name=self.cleaned_data.get("name")
		if name=="Hello":
			raise forms.ValidationError("Not a Valid Name")
		return name

	
	def clean_email(self):
		email=self.cleaned_data.get("email")
		if ".edu" in email:
			raise forms.ValidationError("We don't accept edu emails")
		return email