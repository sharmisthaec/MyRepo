
from django.conf.urls import url
from django.contrib import admin
from shortsiri.views import siriview, HomeView


urlpatterns = [
    url(r'^admin/', admin.site.urls),

url(r'^(?P<shorturl>[\w-]+)/', siriview.as_view()),
url(r'^$', HomeView.as_view()),
]
