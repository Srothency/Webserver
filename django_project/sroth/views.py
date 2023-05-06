from django.shortcuts import render
from .models import Post
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MyModelSerializer
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

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
    return render(request, 'sroth/sroth_apps.html', {'title': 'sroth_apps'})