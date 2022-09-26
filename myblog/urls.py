
from django.urls import path
# from . import views
from .views import HomeView, BlogDetailView, AddBlogView, UpdateBlogView, DeleteBlogView, AddCategoryView, CategoryView, LikeView,AddCommentView

urlpatterns = [
    # path('',views.home, name = "home")
    path('', HomeView.as_view(), name = "home"),
    path('blog/<int:pk>', BlogDetailView.as_view(), name = "blog-detail"),
    # pk= primary key: id for each blogs
    path('addblog/',AddBlogView.as_view(), name = "add_blog"),
    path('addcategory/',AddCategoryView.as_view(), name = "add_category"),
    path('blog/edit/<int:pk>', UpdateBlogView.as_view(), name = "update_blog"),
    path('blog/<int:pk>/remove', DeleteBlogView.as_view(), name = "delete_blog"),
    path('category/<str:cats>', CategoryView, name = "category"),
    path('like/<int:pk>', LikeView, name = "like_blog"),
    path('blog/<int:pk>/comment/',AddCommentView.as_view(), name = "add_comment"),
]