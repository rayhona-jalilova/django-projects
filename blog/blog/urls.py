from django.urls import path 
from blog.views import ( 
     BlogListView,
     BlogDetailView, 
     BlogCreateView, 
     BlogUpdateView,
     BlogDeleteView,
)   

urlpatterns = [
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('blog/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('', BlogListView.as_view(), name='home'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
]
