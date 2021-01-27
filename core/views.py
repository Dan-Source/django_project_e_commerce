from django.shortcuts import render
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, CreateView


from .forms import ContatcForm

User = get_user_model()

class IndexView(View):

    def get(self, request):
        return render(request, 'index.html')

index = IndexView.as_view()

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

class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('index')
    
   

register = RegisterView.as_view()

