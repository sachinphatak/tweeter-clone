from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponseRedirect
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view

from tweeter.models import Tweet
from tweeter.serializers import TweetSerializer, UserSerializer
from tweeter.permissions import IsCreatorOrReadOnly

class TweetViewSet(viewsets.ModelViewSet):
	queryset = Tweet.objects.all()
	serializer_class = TweetSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCreatorOrReadOnly)
	def perform_create(self, serializer):
		serializer.save(creator=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


@ensure_csrf_cookie
def index(request):
	if request.user.is_authenticated():
		context = {
			'auth_username': request.user.username,
			'auth_user_id': request.user.id,
			'auth_user_first_name': request.user.first_name,
			'auth_user_last_name' : request.user.last_name
		}
	else:
		context = {
			'auth_username': '',
			'auth_user_id': '',
			'auth_user_first_name': '',
			'auth_user_last_name' : ''
		}

	return render(request, 'tweeter/index.html', context=context)

def signup(request):
	if request.method == 'POST':
		form = NameForm(request.POST)

		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form = NameForm()

	return render(request, 'tweeter/signup.html', {'form': form})

def thanks(request):
	return render(request, 'tweeter/thanks.html', {'message': "Thanks for signing up!"})

















