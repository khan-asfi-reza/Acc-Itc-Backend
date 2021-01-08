from django.urls import path

from Main.views import message_response_view, PanelMembersApiView, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('api/message/', message_response_view, name='message-response'),
    path('api/panel-members/', PanelMembersApiView.as_view(), name='panel-members')
]