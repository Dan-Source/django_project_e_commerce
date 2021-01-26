from django.shortcuts import render
from django.http import HttpResponse

from django.conf import settings
from django.views.generic import View

from .forms import ContatcForm

class IndexView(View):

    def get(self, request):
        return render(resquest, 'index.html')

index = IndexView.as_view()

def index(request):
    return render(request, 'index.html')

def contact(request):
    success = False
    form = ContatcForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)

