from django.urls import path
from .views import AccountView, CodeView

urlpatterns = [
    path('home', AccountView.as_view()),
    path('code', CodeView.as_view())
]
