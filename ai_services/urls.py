from django.urls import path
from .views import DocumentQueryView

urlpatterns = [
    path('query/', DocumentQueryView.as_view(), name='document-query'),
]