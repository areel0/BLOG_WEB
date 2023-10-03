from django.urls import path
from .views import bloglistview,detailblogview,blogcreateview,blogupdateview,blogdeleteview


urlpatterns=[
    path('post/new',blogcreateview.as_view(), name='post_new'),
    path('',bloglistview.as_view(), name='home'),
    path("post/<int:pk>/", detailblogview.as_view(), name="post_detail"),
    path('post/<int:pk>/edit/',blogupdateview.as_view(), name='post_edit'),
    path("post/<int:pk>/delete/", blogdeleteview.as_view(),name="post_delete")
]