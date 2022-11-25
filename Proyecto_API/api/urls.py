from django.urls import path
from .views import PersonaView

urlpatterns=[
    path('persona/',PersonaView.as_view(),name='lista_personas'),
    path('persona/<int:id>',PersonaView.as_view(),name='proceso_persona')
]