from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BlogPost
from .serializers import BlogPostSerializer


# Create your views here.
class BlogPostView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self,request,*args, **kwargs):
        BlogPost.objects.all().delete()
        return Responce(status=status.HTTP_204_NO_CONTENT)


class BlogPostRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field =  "pk" 


class BlogPostList(APIView):
    def get(self,request,format=None):
        # get the title from the query parameters (if none,default to empty string)
        title = request.query_params.get("title","")

        if title:
            # filter the query set based on title
            blog_posts = BlogPost.objects.filter(title_icontains=title)

        else:
            # If no title is provided return all blog posts
            blog_posts = BlogPost.objects.all()

        serializer = BlogPostSerializer(blog_posts,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)