from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from dukwatch.models import Video_Board, Free_Board, Ranking_Board

class VideoSerializers(serializers.ModelSerializer) :
    class Meta:
        model = Video_Board

class VideoBoardViewSet(viewsets.ModelViewSet) :
    queryset = Video_Board.objects.all()
    serializer_class = VideoSerializers

class FreeSerializers(serializers.ModelSerializer) :
    class Meta:
        model = Free_Board

class FreeBoardViewSet(viewsets.ModelViewSet) :
    queryset = Free_Board.objects.all()
    serializer_class = VideoSerializers

class RankingSerializers(serializers.ModelSerializer) :
    class Meta:
        model = Ranking_Board

class RankingBoardViewSet(viewsets.ModelViewSet) :
    queryset = Ranking_Board.objects.all()
    serializer_class = VideoSerializers

router = routers.DefaultRouter()
router.register(r'video', VideoBoardViewSet)
router.register(r'free', FreeBoardViewSet)
router.register(r'rank', RankingBoardViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]