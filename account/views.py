from django.shortcuts import render
from .forms import AuthorInfo


# Create your views here.

def create_user(request):
    if request.method == 'POST':
        form = AuthorInfo(request.POST)
        if form.is_valid():
            form.save()
            context = {
                " successMessage": "user created successfully"
            }
            return render(request, 'success.html', context)
    else:
        form = AuthorInfo()
        context = {
            "form": form
        }
        return render(request, 'users/create_user.html', context)
