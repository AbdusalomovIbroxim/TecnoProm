from rest_framework import viewsets
from .models import App
from .serializers import MyModelSerializer

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = MyModelSerializer
