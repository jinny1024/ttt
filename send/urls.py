from django.urls import path
from send.views import SendView

urlpatterns=[
    path('parameter/', SendView.post)
    path('parameter/', SendView.get)
]
