from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from tweeter import views

router = DefaultRouter()
router.register(r'tweets', views.TweetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^thanks/$', views.thanks, name='thanks'),
	url(r'^api/', include(router.urls)),
]