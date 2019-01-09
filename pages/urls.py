from django.urls import path
from .views import (Bloglistview,
                    Blogdetailview,
                    Blogcreateview,
                    Blogupdateview,
                    Blogdeleteview,
                    Aboutpageview,
                    Servicespageview,
                    Categorypageview,
                    Contactpageview,)

urlpatterns = [
    path('Contact_us/', Contactpageview.as_view(), name='Contact_us'),
    path ('Category/', Categorypageview.as_view(), name='Category'),
    path('Services/', Servicespageview.as_view(), name='Services'),
    path('about/', Aboutpageview.as_view(), name='about'),
    path('post/<int:pk>/delete/', Blogdeleteview.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', Blogupdateview.as_view(), name='post_edit'),
    path('post/new/', Blogcreateview.as_view(), name='post_new'),
    path('post/<int:pk>/', Blogdetailview.as_view(), name= 'post_detail'),
    path('', Bloglistview.as_view(), name='home'),
]