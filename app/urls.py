from app.apis import send_message_api
from app.websockets import EchoWebsocket

urls = {
    'send/<connection_id>/': send_message_api,
    'ws/': EchoWebsocket,
}
