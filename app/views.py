from django.shortcuts import render
from app.forms import RegisterForm, LoginForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test

def index(request):
    return render(request, 'app/index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'app/register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if not user:
                # Invalid login
                return render(request, 'app/login.html', {'form': form, 'error_message': 'Invalid credentials.'})
            
            # After user authentication success, log in and redirect the user to their dashboard
            login(request, user)
            if user.is_superuser:
                return redirect('super_dashboard')
            elif user.is_staff:
                return redirect('staff_dashboard')
            else:
                return redirect('dashboard')
                
    else:
        form = LoginForm()
    return render(request, 'app/login.html', {'form': form})


@login_required
def dashboard(request):
    """
    Regular User Dashboard
    """
    return render(request, 'app/dashboard.html')

@user_passes_test(lambda u: u.is_superuser)
@login_required
def super_dashboard(request):
    """
    Super User Dashboard
    """
    return render(request, 'app/super_dashboard.html')

@user_passes_test(lambda u: u.is_staff)
@login_required
def staff_dashboard(request):
    """
    Staff User Dashboard
    """
    return render(request, 'app/staff_dashboard.html')