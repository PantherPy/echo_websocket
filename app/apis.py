from panther import status
from panther.app import API
from panther.request import Request
from panther.response import Response
from panther.websocket import send_message_to_websocket

from app.models import User
from app.serializers import SendMessageSerializer


@API(input_model=SendMessageSerializer)
async def send_message_api(user_id: int, request: Request):
    user = User.find_one(id=user_id)
    if user is None:
        return Response(data={'detail': 'User Not Found'}, status_code=status.HTTP_404_NOT_FOUND)

    payload: SendMessageSerializer = request.validated_data
    await send_message_to_websocket(connection_id=user.connection_id, data=payload.message)
    return Response(data={'detail': 'Message Sent Successfully'}, status_code=status.HTTP_200_OK)
