


from channels.consumer import SyncConsumer, AsyncConsumer
from channels.consumer import StopConsumer


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('Websocket Connected.....',event)

    def websocket_receive(self,event):
        print('Message Received from Client.....',event)

    def websocket_disconnect(self,event):
        print('Websocket Disconnected.....',event)