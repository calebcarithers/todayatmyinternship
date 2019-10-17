from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

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
            return redirect("/")

    if request.user.is_authenticated:
        logged_in = True
    else:
        logged_in = False

    form = {
        "object_list" : userSubForm,
        "logged_in": logged_in
    }

    return render(request, "tamiAPP/submit.html", form)

def home_page(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            object_pk = request.POST.get('item_pk')
            object_vote = request.POST.get('item_vote')
            review = userSub.objects.get(pk=object_pk)
            if object_vote == "up":
                review.votes.up(request.user.id)
            elif object_vote == "down":
                review.votes.down(request.user.id)
            print(review.votes.count())
        else:
            print("send back to front end, user is not logged in, and alert them")
            return JsonResponse({'logged_in': 'false'})

    if request.user.is_authenticated:
        logged_in = True
    else:
        logged_in = False

    queryset = userSub.objects.all().order_by('-vote_score')

    context = {
        "object_list": queryset,
        "logged_in": logged_in,
        "sort": "top"
    }
    print(logged_in)

    return render(request, "tamiAPP/home.html", context)

def home_new_page(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            # print("user is logged in as: ")
            # print(request.user)
            object_pk = request.POST.get('item_pk')
            object_vote = request.POST.get('item_vote')
            # print("object id: " + str(object_pk))
            # print("object vote: " + str(object_vote))
            review = userSub.objects.get(pk=object_pk)
            if object_vote == "up":
                review.votes.up(request.user.id)
            elif object_vote == "down":
                review.votes.down(request.user.id)
            print(review.votes.count())
        else:
            print("send back to front end, user is not logged in, and alert them")
    queryset = userSub.objects.all().order_by('-created_at')

    if request.user.is_authenticated:
        logged_in = True
    else:
        logged_in = False

    context = {
        "object_list":queryset,
        "logged_in": logged_in,
        "sort": "new"
    }

    return render(request, "tamiAPP/home.html", context)

def detail_page(request, company=""):
    if request.method == "POST":
        print("got post")
        if request.user.is_authenticated:
            # print("user is logged in as: ")
            # print(request.user)
            object_pk = request.POST.get('item_pk')
            object_vote = request.POST.get('item_vote')
            # print("object id: " + str(object_pk))
            # print("object vote: " + str(object_vote))
            review = userSub.objects.get(pk=object_pk)
            if object_vote == "up":
                review.votes.up(request.user.id)
            elif object_vote == "down":
                review.votes.down(request.user.id)
            print(review.votes.count())
        else:
            print("send back to front end, user is not logged in, and alert them")
    queryset = userSub.objects.filter(where__exact=company).order_by('-vote_score')

    if request.user.is_authenticated:
        logged_in = True
    else:
        logged_in = False

    context = {
        "object_list": queryset,
        "company":company,
        "logged_in": logged_in
    }
    return render(request, "tamiAPP/detail.html", context)

def detail_new_page(request, company=""):
    if request.method == "POST":
        if request.user.is_authenticated:
            # print("user is logged in as: ")
            # print(request.user)
            object_pk = request.POST.get('item_pk')
            object_vote = request.POST.get('item_vote')
            # print("object id: " + str(object_pk))
            # print("object vote: " + str(object_vote))
            review = userSub.objects.get(pk=object_pk)
            if object_vote == "up":
                review.votes.up(request.user.id)
            elif object_vote == "down":
                review.votes.down(request.user.id)
            print(review.votes.count())
        else:
            print("send back to front end, user is not logged in, and alert them")
    queryset = userSub.objects.filter(where__exact=company).order_by('-created_at')

    if request.user.is_authenticated:
        logged_in = True
    else:
        logged_in = False

    context = {
        "object_list": queryset,
        "company": company,
        "logged_in": logged_in
    }
    return render(request, "tamiAPP/detail.html", context)

def login_page(request):
    if request.method == "POST":
        print("got a post")
    return render(request, "tamiAPP/login.html")




