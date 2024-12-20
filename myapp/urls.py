from django.urls import path
from . import views


urlpatterns = [
    path('blogpost/',views.BlogPostView.as_view(),name="blogpost-create-view")
]