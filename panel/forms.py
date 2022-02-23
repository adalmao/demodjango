from django import forms
from panel.models import Person

class PersonForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ('first_name','last_name','email')
	def __init__(self,*args,**kwargs):
		super(PersonForm,self).__init__(*args,**kwargs)
		_instance = kwargs.pop('instance',None)