from django.urls import path

from . import views

urlpatterns=[
    path('',views.mycreate.as_view()),
    path('show/',views.myvie.as_view()),
    path('show1/',views.myempcreate.as_view()),
    path('show2/',views.myemplercreate.as_view()),
    path('show3/',views.myedresscreate.as_view()),

]