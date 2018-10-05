from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
import pickle

def register(request):
    if (request.method == 'POST'):
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                emails = form.cleaned_data.get('email')
                messages.success(request, f'Account created for {username}!')
                with open('/home/don/backup1/users/emailAddresses', 'ab') as handle:
                    pickle.dump(emails, handle, protocol=pickle.HIGHEST_PROTOCOL)
                handle.close()
                return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

