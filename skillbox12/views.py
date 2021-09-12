from django.shortcuts import render
from .forms import ExForm



def reg(request):
    form=ExForm()

    return render(request, 'skillbox12/reg.html', locals())
# Create your views here.
