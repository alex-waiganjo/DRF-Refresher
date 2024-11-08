from django.shortcuts import render
from .models import Todo
from . import serializers
from rest_framework import generics, status
from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Get and Post data
class TodosView(generics.GenericAPIView):
    serializer_class = serializers.TodoSerializer
    queryset = Todo.objects.all()
    permission_classes =[IsAuthenticated]

    def get(self, request: HttpRequest):
        todos = Todo.objects.all()
        serializer = self.serializer_class(instance=todos, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request: HttpRequest):
        # data = request.data
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get, Put, Patch and Delete data
class TodoView(generics.GenericAPIView):
    serializer_class = serializers.TodoSerializer
    queryset =Todo.objects.all()
    permission_classes =[IsAuthenticated]

    def get(self, request: HttpRequest, id):
        todo = Todo.objects.get(pk=id)
        serializer = self.serializer_class(instance=todo, many=False)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request: HttpRequest, id):
        todo = Todo.objects.get(pk=id)

        if todo is not None:
            serializer = self.serializer_class(
                instance=todo, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(data={"Message": "Resource Not Found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(data=serializer.erros, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request: HttpRequest, id):
        todo_update = Todo.objects.get(pk=id)
        serializer = self.serializer_class(
            instance=todo_update, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: HttpRequest, id):
        todo_delete = Todo.objects.get(pk=id)
        todo_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
