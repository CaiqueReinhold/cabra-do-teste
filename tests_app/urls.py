from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.TestListView.as_view(), name='test_list'),
    url(r'^(?P<slug>[-\w]+)/$', views.TestDetailView.as_view(),
        name='test_detail'),
    url(r'^(?P<slug>[-\w]+)/resultado$', views.TestAnswerView.as_view(),
        name='test_answer'),
    url(r'^(?P<slug>[-\w]+)/(?P<id>[0-9]+)/$', views.TestAnswerView.as_view(),
        name='view_test_answer')
]
