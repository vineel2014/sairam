from django.conf.urls import url
from vinapp import views


urlpatterns=[
            url(r"^$",views.index,name='index'),
            url(r"^$",views.home,name='home'),
            url(r"^register/$",views.register,name='register'),
            url(r"^login/$",views.login,name='login'),
            url(r"^logout/$",views.logout,name='logout'),

]
