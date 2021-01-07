from django.urls import path

from Main.views import message_response_view, PanelMembersApiView

urlpatterns = [
    path('message/', message_response_view, name='message-response'),
    path('panel-members/', PanelMembersApiView.as_view(), name='panel-members')
]