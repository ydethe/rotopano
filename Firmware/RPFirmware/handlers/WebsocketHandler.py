from tornado.websocket import WebSocketHandler
from tornado.escape import json_encode


class WSHandler(WebSocketHandler):
    def open(self):
        for progress in range(100,10):
            data = {'progress':progress}
            self.write_message(json_encode(data))

    def on_message(self, message):
        print('message received %s' % message)

    def on_close(self):
        print('connection closed')
