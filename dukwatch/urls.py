from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from dukwatch.models import VideoBoard

class VideoSerializers(serializers.ModelSerializer) :
    class Meta:
        model = VideoBoard

class VideoBoardViewSet(viewsets.ModelViewSet) :
    queryset = VideoBoard.objects.all()
    serializer_class = VideoSerializers

router = routers.DefaultRouter()
router.register(r'video', VideoBoardViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]