from django.shortcuts import render, redirect
from .forms import PersonForm
from django.views.generic import DeleteView, DetailView, UpdateView
from .models import Person


def detail(request):
    person =Person.objects.all()
    return render(request, 'cdu/choose.html', {'data':person})


def create (request):
    error=""
    if request.method=='POST':
        form=PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detail')
        else:
            error="FORM неверная"

    form=PersonForm()
    data={
        'form':form,
        'error':error
    }

    return render(request, 'cdu/create.html', data)


class PersonDetailView (DetailView):
    model = Person
    template_name = "cdu/choose.html"
    context_object_name = "person"


class PersonDeleteView (DeleteView):
    model = Person
    success_url = '/cdu/'
    template_name = 'cdu/delete.html'


class PersonUpdateView (UpdateView):
    model = Person
    template_name = 'cdu/create.html'
    form_class = PersonForm

