from panther import status
from panther.app import API
from panther.request import Request
from panther.response import Response
from panther.websocket import send_message_to_websocket

from app.serializers import SendMessageSerializer


@API(methods=['POST'], input_model=SendMessageSerializer)
async def send_message_api(connection_id: str, request: Request):
    payload: SendMessageSerializer = request.validated_data
    await send_message_to_websocket(connection_id=connection_id, data=payload.message)
    return Response(data={'detail': 'Message Sent Successfully'}, status_code=status.HTTP_200_OK)