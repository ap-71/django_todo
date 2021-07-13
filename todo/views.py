from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets, permissions, mixins, request, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from todo.models import ToDoAction
from todo.serializers import ToDoActionSerialize, ToDoActionAddSerialize, ToDoActionDelSerialize


@login_required
def task(request):
    todo_list = ToDoAction.objects.all()
    return render(request, 'todo.html')


class TaskAPI(viewsets.ReadOnlyModelViewSet):
    serializer_class = ToDoActionSerialize
    permission_classes = [permissions.IsAuthenticated]

    # TODO = Доступ только туда, куда разрешено пользователю в его пользовательской группе

    def get_queryset(self):
        self.queryset = ToDoAction.objects.filter(user=self.request.user)
        return super(TaskAPI, self).get_queryset()


class TaskAddAPI(mixins.CreateModelMixin, GenericViewSet):
    queryset = ToDoAction.objects.all()
    serializer_class = ToDoActionAddSerialize
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.user.id)
        return serializer.save(user=user)


class TaskDelAPI(GenericViewSet, mixins.DestroyModelMixin):
    queryset = ToDoAction.objects.all()
    serializer_class = ToDoActionDelSerialize
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, request):
        todo_task = get_object_or_404(ToDoAction, id=request.id)
        todo_task.delete()

# class TaskUpdAPI(viewsets.ModelViewSet):
#     queryset = ToDoAction.objects.all()
#     serializer_class = ToDoActionModifySerialize
#     permission_classes = [permissions.IsAuthenticated]
