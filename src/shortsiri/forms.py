from django import forms
from .validators import *

class SubmitUrlForm(forms.Form):

	url=forms.CharField(label='Submit URL', validators=[validate_url,validate_dot_com])

	def clean(self):
		cleaned_data=super(SubmitUrlForm,self).clean()
		url=cleaned_data['url']
		print(url)

	def clean_url(self):

		url=self.cleaned_data['url']

		print(url)
		return url
