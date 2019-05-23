from django.conf.urls import url 
 
from . import views 
app_name = "polls"

urlpatterns = [ 
    #url(r'^$', views.index, name='index'),
	# url(r'^login/', views.search, name='search'),
    url('^widelake/', views.formView, name='formView'),
    url('^widelake', views.search, name='search'),
    url('^suggest/title', views.suggest_title, name='suggestTitle'),
    url('^advance/', views.formAdvanceView, name='formAdvanceView'),
    url('^advance', views.search_advance, name='searchAdvance'),
    # url(r'^logout/', views.logoutView, name='logoutView'),
	# url(r'^ratedMovieList/', views.ratedView, name='ratedView'),
]
