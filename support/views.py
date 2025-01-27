from django.shortcuts import render, redirect
from .forms import SupportMessageForm

# Support Request Form

def support(request):
    if request.method == 'POST':
        form = SupportMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('support_thanks')
        else:
            print("Form is not valid")
    else:
        form = SupportMessageForm()
    return render(request, 'support.html', {'form': form})

def support_thanks(request):
    return render(request, 'thanks.html')