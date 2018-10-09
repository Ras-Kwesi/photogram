from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^home/$',views.index,name='index'),
    url('^explore/',views.explore_results,name='explore'),
    url('profile/$',views.profile,name='profile'),
    url('^update/$',views.update,name='update'),
    url('^new_post/',views.new_post,name='new_post'),
    url('^comment/(\d+)',views.comment,name='comment'),
    url('^$',views.signup, name='signup')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)