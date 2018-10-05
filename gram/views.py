from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import *
from .forms import NewImageForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.editor = current_user
            image.save()
        return redirect('index')

    else:
        form = NewImageForm()
    return render(request, 'new_post.html', {"form": form})


# @login_required(login_url='/accounts/login/')
def index(request,article_id):
    try:
        posts = Image.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"index.html", {"posts":posts})



def explore_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_query = request.GET.get("profile")
        searched_articles = Profile.search_by_username(search_query)
        message = f"{search_term}"

        return render(request, 'explore.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'explore.html',{"message":message})