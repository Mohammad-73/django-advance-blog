from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework.decorators import action
from .permissions import IsOwnerOrReadOnly

# @api_view("GET","POST")
# @permission_classes([IsAuthenticatedOrReadOnly])
# def api_post_list_view(request):
#     if request.method == "GET":
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializer(posts,many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
# class PostList(APIView):
#     '''Getting a list of posts and creating posts'''
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer

#     def get(self,request):
#         '''Retrieving a list of posts'''
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializer(posts,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         '''Creating a post with provided data'''
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

class PostList(ListCreateAPIView):
    '''Getting a list of posts and creating posts'''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    # def get(self, request, *args, **kwargs):
    #     '''Retrieving a list of posts'''
    #     return self.list(request, *args, **kwargs)
    
    # def post(self, request, *args, **kwargs):
    #     '''Retrieving a list of posts'''
    #     return self.create(request, *args, **kwargs)
    

# @api_view("GET","PUT","DELETE")
# def postDetail(request,id):
#     # try:       
#     #     post = Post.objects.get(pk=id)
#     #     serializer = PostSerializer(post)
#     #     return Response(serializer.data)
#     # except Post.DoesNotExist:
#     #     return Response({"detail":"Post does not exist"},status=status.HTTP_404_NOT_FOUND)
#     # post = get_object_or_404(Post,pk=id,status=True)
#     # serializer = PostSerializer(post)
#     # return Response(serializer.data)
#     post = get_object_or_404(Post,pk=id,status=True)
#     if request.method == "GET":
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = PostSerializer(post,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == "DELETE":
#         post.delete()
#         return Response({"Detail":"Item removed successfully"},status=status.HTTP_204_NO_CONTENT)
    
# class PostDetail(APIView):
#     '''Getting detail of the post and edit plus removing it'''
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer

#     def get(self,request,id):
#         '''Retrieving the post data'''
#         post = get_object_or_404(Post,pk=id,status=True)
#         serializer = self.serializer_class(post)
#         return Response(serializer.data)
    
#     def put(self,request,id):
#         '''Editing the post data'''
#         post = get_object_or_404(Post,pk=id,status=True)
#         serializer = PostSerializer(post,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def delete(self,request,id):
#         '''Removing the post'''
#         post = get_object_or_404(Post,pk=id,status=True)
#         post.delete()
#         return Response({"Detail":"Item removed successfully"},status=status.HTTP_204_NO_CONTENT)
    
class PostDetail(RetrieveUpdateDestroyAPIView):
    '''Getting detail of the post and edit plus removing it'''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
    
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)
    
class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    @action(methods=["get"],detail=False)
    def get_ok(self,request):
        return Response({'detail':'ok'})

    # def list(self, request):
    #     serializer = self.serializer_class(self.queryset, many=True)
    #     return Response(serializer.data)
    
    # def retrieve(self, request, pk=None):
    #     post_object = get_object_or_404(self.queryset, pk=pk)
    #     serializer = self.serializer_class(post_object)
    #     return Response(serializer.data)
    
    # def create(self, request):
    #     pass

    # def update(self, request):
    #     pass
    
    # def partial_update(self, request):
    #     pass
    
    # def destroy(self, request):
    #     pass

class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()