from django import forms
from .models import Client

class CommentForm(forms.ModelForm):
	class Meta:
		model=Client
		fields=['ids', 'password']