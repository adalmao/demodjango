from django.shortcuts import render
from django.http import JsonResponse
from panel.forms import PersonForm
from panel.models import Person
# Create your views here.

def home(request):
	#here deploy the request POST
	if request.POST:
		form = PersonForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			message = "Revisa tu informacion"
			errors=form.errors
	return render(request,'panel/home.html',locals())
def list(request):
	persons = Person.objects.all()
	return render(request,'panel/list.html',locals())
def edit(request,code):
	person = Person.objects.get(pk=code)
	if request.POST:
		form = PersonForm(request.POST,instance=person)
		if form.is_valid():
			form.save()
		else:
			message = "revisa la info"
			errors = form.errors
	return render(request,'panel/home.html',locals())
def delete(request,code):
	person = Person.objects.get(pk=code)
	person.delete()
	return JsonResponse({'message':'se borro correctamente'},status=200)
