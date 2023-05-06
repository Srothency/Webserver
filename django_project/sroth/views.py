from django.shortcuts import render
from .models import Post, App
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MyModelSerializer
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def is_admin(user):
    return user.is_authenticated and user.is_superuser

@api_view(['POST'])
def post_view(request):
    serializer = MyModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'sroth/home.html', context)

@user_passes_test(is_admin, login_url="/")
def sroth_apps(request):
    context = {
        'apps': App.objects.all(),
        'title': 'sroth_apps'
    }
    return render(request, 'sroth/sroth_apps.html', context)

def app_detail(request, app_id):
    app = get_object_or_404(App, id=app_id)
    if app.name == "espApp":
        # Code to be executed for App1
        pass
    elif app.name == "otherAppName":
        # Code to be executed for App2
        pass
    return render(request, 'sroth/app_detail.html', {'app': app})
