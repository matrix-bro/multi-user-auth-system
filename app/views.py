from django.shortcuts import render
from app.forms import RegisterForm
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'app/register.html', {'form': form})