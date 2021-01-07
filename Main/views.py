from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from Main.models import ResponseMessage, PanelMember

# Handles Message Response
from Main.pagination import GeneralPagination
from Main.serializers import PanelMemberSerializer


@api_view(['POST'])
def message_response_view(request):
    # Only Take Post Request
    if request.method == "POST":
        # Get name, email, message from request data
        name = request.data.get('name')
        email = request.data.get('email')
        message = request.data.get('message')
        # If name email and message is not none
        if name and email and message:
            # Create Response Message
            ResponseMessage.objects.create(name=name, email=email, message=message)
            return Response({
                'message': 'We have got your response, Thank You',
                'status': 200,
                'success': True
            }, status=status.HTTP_201_CREATED)
        # Else Return Error Response
        return Response({
            'message': 'Please enter name, email and your message',
            'status': 400,
            'success': False
        }, status=status.HTTP_400_BAD_REQUEST)
    # Invalid Request
    return Response({
        'message': 'Invalid Request',
        'status': 400,
        'success': False
    }, status=status.HTTP_403_FORBIDDEN)


# Shows Panel Members
class PanelMembersApiView(APIView):
    pagination_class = GeneralPagination
    serializer_class = PanelMemberSerializer

    # Gets Query Set of Panel Members
    @staticmethod
    def get_queryset():
        return PanelMember.objects.all()

    # Handles get method
    def get(self, request):
        serialized_data = self.serializer_class(self.get_queryset(), many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
