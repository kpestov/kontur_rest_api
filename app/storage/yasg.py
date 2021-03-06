from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Тестовый API",
        default_version='v1.0',
        description=
        """REST API позволяет сохранять, получать и модифицировать объекты.
           Также имется возможность спроскировать api-метод (url: api/proxy) с кэшированием устаревающим
           по времени и по количеству запросов.""",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    url='http://0.0.0.0:8080/api'
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
