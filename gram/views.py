from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import *
from .forms import NewImageForm
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db import transaction

# Create your views here.
@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
        return redirect('index')

    else:
        form = NewImageForm()
    return render(request, 'new_post.html', {"form": form})


# @login_required(login_url='/accounts/login/')
def index(request):
    try:
        images = Image.objects.all()
        form = NewComment(instance=request.user)
        comments = Comment.objects.all()
    except DoesNotExist:
        raise Http404()
    return render(request,"index.html", {"images":images,'comment_form':form,'comm':comments})



def explore_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_query = request.GET.get("profile")
        searched_profiles = Profile.search_by_username(search_query)
        message = f"{search_term}"

        return render(request, 'explore.html',{"message":message,"articles": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'explore.html',{"message":message})



@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    print(profile)
    # profile = Profile.objects.filter(user=request.user.id)
    images = Image.objects.filter(profile = current_user)


    return render(request,'profile.html',{'profile':profile,'images':images})

@login_required(login_url='/accounts/login/')
@transaction.atomic
def update(request):
    # current_user = User.objects.get(pk=user_id)
    current_user=request.user
    if request.method == 'POST':
        user_form = EditUser(request.POST, request.FILES,instance=request.user)
        profile_form = EditProfile(request.POST, request.FILES,instance=current_user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            user_form.save()
        return redirect('profile')

    else:
        user_form = EditUser(instance=request.user)
        profile_form = EditProfile(instance=current_user.profile)
    return render(request, 'update.html', {
        "user_form": user_form,
        "profile_form": profile_form
    })

def comment(request,id):
    image = Image.objects.get(id=id)
    print(id)
    if request.method == 'POST':
        comm=NewComment(request.POST)
        if comm.is_valid():
            comment=comm.save(commit=False)
            comment.commentator = request.user
            comment.comment_image = image
            comment.save()
            return redirect('index')
    return redirect('index')

def signup(request):
    """
    signup form view function
    """
    # checking if request method is a post
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        # form validationq
        if form.is_valid():
            # saving user credentials and creating uer instance  if form is valid
            user = form.save()

            # user passed as argument to auth_login function
            auth_login(request, user)
            return redirect('edit_profile')
    else:
        form = SignUpForm()

    return render(request, 'registration/registration_form.html', {'form': form})