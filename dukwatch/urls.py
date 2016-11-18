from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from dukwatch.models import Video_Board, Free_Board, Character_data

class VideoSerializers(serializers.ModelSerializer) :
    class Meta:
        model = Video_Board

class VideoBoardViewSet(viewsets.ModelViewSet) :
    queryset = Video_Board.objects.all()
    serializer_class = VideoSerializers

class PopularVideoSerializers(serializers.ModelSerializer) :
    class Meta:
        model = Video_Board

class PopularVideoBoardViewSet(viewsets.ModelViewSet) :
    queryset = Video_Board.objects.all()
    serializer_class = VideoSerializers

class FreeSerializers(serializers.ModelSerializer) :
    class Meta:
        model = Free_Board

class FreeBoardViewSet(viewsets.ModelViewSet) :
    queryset = Free_Board.objects.all()
    serializer_class = FreeSerializers

class RankingSerializers(serializers.ModelSerializer) :
    class Meta:
        model = Character_data

class RankingViewSet(viewsets.ModelViewSet) :
    queryset = Character_data.objects.all()
    serializer_class = RankingSerializers

class SearchDataSerializers(serializers.ModelSerializer) :
    class Meta:
        model = Character_data

class SearchDataViewSet(viewsets.ModelViewSet) :
    queryset = Character_data.objects.filter(UserNo=10)
    serializer_class = SearchDataSerializers



router = routers.DefaultRouter()
router.register(r'popularvideo', VideoBoardViewSet)
router.register(r'video', VideoBoardViewSet)
router.register(r'free', FreeBoardViewSet)
router.register(r'rank', RankingViewSet)
router.register(r'search', SearchDataViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]