from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.http import HttpResponseForbidden 

from django.shortcuts import render

@login_required
def homepage(request):
    return render(request, 'service_requests/homepage.html')


@login_required
def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid(): 
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('service_requests:list_service_requests')

    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/create.html', {'form': form})

@login_required
def list_service_requests(request):
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'service_requests/list.html', {'requests': requests})

@login_required
def track_requests(request):
    """List all service requests for the logged-in user."""
    requests = ServiceRequest.objects.filter(customer=request.user).order_by('-created_at')
    return render(request, 'service_requests/track_requests.html', {'requests': requests})

@login_required
def request_details(request, pk):
    """Show details of a specific service request."""
    service_request = get_object_or_404(ServiceRequest, pk=pk, customer=request.user)
    return render(request, 'service_requests/request_details.html', {'service_request': service_request})

@login_required
def update_request_status(request, pk):
    if not request.user.is_staff:  # Only allow staff members
        return HttpResponseForbidden("You do not have permission to update requests.")
    
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(ServiceRequest.STATUS_CHOICES):  # Validate the status
            service_request.status = new_status
            service_request.save()
            return redirect('service_requests:track_requests')  # Redirect to track requests page
    
    return render(request, 'service_requests/update_status.html', {
        'service_request': service_request,
        'status_choices': ServiceRequest.STATUS_CHOICES,  # Fetch choices from the model
    })

@login_required
def account_info(request):
    """Display account details for the logged-in user."""
    return render(request, 'service_requests/account_info.html', {
        'user': request.user,
    })

@login_required
def representative_dashboard(request):
    if not request.user.is_staff:  # Ensure only staff can access
        return HttpResponseForbidden("You do not have permission to access this page.")
    
    service_requests = ServiceRequest.objects.all().order_by('-created_at')  # View all requests
    return render(request, 'service_requests/dashboard.html', {
        'service_requests': service_requests,
    })


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after registration
            return redirect('/')  # Redirect to homepage
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
