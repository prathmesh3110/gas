

from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import UserLoginForm
from .forms import CustomerRegistrationForm
from .models import Customer


@login_required
def submit_request(request):
    
        if request.method == 'POST':
            form = ServiceRequestForm(request.POST, request.FILES)
            # if form.is_valid():
            #     service_request = form.save(commit=False)
            #     service_request.customer = request.user.customer 
            #     service_request.save()
            return redirect('/home')
        else:
            form = ServiceRequestForm()
        
        return render(request, 'submit_request.html', {'form': form})



def track_request(request):
    service_requests = ServiceRequest.objects.filter(customer=request.user.customer)
    return render(request, 'track_request.html', {'service_requests': service_requests})

def account_info(request):
    customer = request.user.customer
    return render(request, 'account_info.html', {'customer': customer})
def home(request):
    return render(request, 'home.html')
@login_required
def user_page(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'login.html', context)
class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = UserLoginForm
    success_url = reverse_lazy('home')  
    

def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 
    else:
        form = CustomerRegistrationForm()
    return render(request, 'register.html', {'form': form})

def some_view(request):
    
    current_user = request.user
    
  
    try:
        customer = current_user.customer
    except Customer.DoesNotExist:
       
        customer = None
    
    
    return render(request, 'some_template.html', {'customer': customer})
