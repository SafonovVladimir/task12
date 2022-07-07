from django.http import Http404
from django.shortcuts import render
from instagramm.models import User, Profile


def main(request):
    return render(request, 'instagramm/main.html')


def index(request):
    return render(request, 'instagramm/index.html')


def user(request, user_name):
    user_id = User.objects.get(name=user_name).id
    try:
        user = Profile.objects.get(id=user_id)
    except:
        Http404('Unknown user')
    return render(request, 'instagramm/user.html', {'user': user})

def user_edit(request, user_name):
    try:
        user_id = User.objects.get(name=user_name).id
        user = Profile.objects.get(id=user_id)
    except:
        Http404('Unknown user')
    return render(request, 'instagramm/user_edit.html', {'user': user})
