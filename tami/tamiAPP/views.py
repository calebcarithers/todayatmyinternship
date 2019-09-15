from django.shortcuts import render, get_object_or_404, redirect

from .models import userSub
from .forms import userSubForm

# Create your views here.
def submit_page(request):
    if request.method == "POST":
        form = userSubForm(request.POST)
        if form.is_valid():
            userSub.objects.create(**form.cleaned_data)
            form = {
                "object_list" : userSubForm
            }

    else:
        form = {
            "object_list" : userSubForm
        }

        print(userSubForm)
    return render(request, "tamiAPP/submit.html", form)

def home_page(request):
    queryset = userSub.objects.all()

    for this in queryset:
        print(this)

    context = {
        "object_list": queryset
    }
    return render(request, "tamiAPP/home.html", context)




