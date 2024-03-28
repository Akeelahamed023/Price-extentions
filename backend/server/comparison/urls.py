from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name='index'),
    # path('api/', views.apiOverview, name='api-overview'),
    path('api/all/', views.model_view.as_view(), name='comparison-create'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])