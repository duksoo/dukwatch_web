from django.http.response import HttpResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response, schemas, mixins, routers, serializers, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from dukwatch.models import Post_sample

@api_view()
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def swagger_view(request):
    generator = schemas.SchemaGenerator(title='Dukwatch API')
    return response.Response(generator.get_schema(request=request))

def sample_page(request):
    return HttpResponse("Hello!")

class SampleSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Post_sample

class sample_api(GenericAPIView, mixins.ListModelMixin):
    queryset = Post_sample.objects.all()
    serializer_class = SampleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
