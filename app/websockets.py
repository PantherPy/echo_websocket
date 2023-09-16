from panther.logger import logger
from panther.websocket import GenericWebsocket


class EchoWebsocket(GenericWebsocket):
    async def connect(self):
        await self.accept()
        logger.info(f'ConnectionID: {self.connection_id}')

    async def receive(self, data: str | bytes):
        await self.send(data=data)
