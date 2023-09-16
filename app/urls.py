from app.apis import send_message_api
from app.websockets import EchoWebsocket

urls = {
    'send/<user_id>/': send_message_api,
    'ws/': EchoWebsocket,
}
