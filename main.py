from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from socket import *

from kivy.uix.gridlayout import GridLayout

host_name = "192.168.4.1"
port = 1234
address = (host_name, port)
udp_socket = socket(AF_INET, SOCK_DGRAM)
Window.clearcolor = (1, 1, 1, 1)
Window.title = "Навигация"
data = "0000"


def send_data(data):
    '''tmp = str.encode(data)'''
    try:
       '''udp_socket.sendto(tmp, address)'''
    except Exception as e:
        print("Ошибка отправки данных:", e)


class MyApp(App):
    def __init__(self):
        super().__init__()
        self.left = Button(text="",

                           background_normal='left.png',
                           color=(0, 1, 1, 1),
                           )
        self.onCart = Button(text="on",

                             color=(0, 1, 1, 1),
                             )
        self.offCart = Button(text="off",

                              color=(0, 1, 1, 1),
                              )
        self.fcSp = Button(text="1",

                           color=(0, 1, 1, 1),
                           )
        self.scSp = Button(text="2",

                           color=(0, 1, 1, 1),
                           )
        self.thSp = Button(text="3",

                           color=(0, 1, 1, 1),
                           )

        self.left.bind(state=self.turn_left)

        self.stop = Button(text="stop",

                           color=(0, 1, 1, 1),
                           )
        self.stop.bind(state=self.stoped)
        self.right = Button(text="",

                            background_normal='right.png',
                            font_size="20sp",
                            color=(0, 1, 1, 1),
                            )
        self.right.bind(state=self.turn_right)
        self.forward = Button(text="",

                              background_normal='forward.png',
                              font_size="20sp",
                              color=(0, 1, 1, 1),
                              )
        self.forward.bind(state=self.forwardd)
        self.back = Button(text="",

                           background_normal='back.png',
                           font_size="20sp",
                           color=(0, 1, 1, 1),
                           )
        self.back.bind(state=self.turn_back)
        self.onCart.bind(state=self.on_cart)
        self.offCart.bind(state=self.off_cart)
        self.fcSp.bind(state=self.fr_speed)
        self.scSp.bind(state=self.sc_speed)
        self.thSp.bind(state=self.th_speed)

    def build(self):
        buttonList = [self.onCart, BoxLayout(), self.offCart,
                      BoxLayout(), self.forward,
                      BoxLayout(), self.left, self.stop,
                      self.right, BoxLayout(), self.back, BoxLayout(), self.fcSp,
                      self.scSp, self.thSp]
        gridLayout = GridLayout(cols=3)
        for i in range(15):
            gridLayout.add_widget(buttonList[i])
        return gridLayout

    def turn_right(self, state, value):
        global data
        data = 'right' if value == 'down' else 'stop'
        send_data(data)

    def on_cart(self, state, value):
        global data
        data = 'on'
        send_data(data)

    def off_cart(self, state, value):
        global data
        data = 'off'
        send_data(data)

    def fr_speed(self, state, value):
        global data
        data = 'frSp'
        send_data(data)

    def sc_speed(self, state, value):
        global data
        data = 'scSp'
        send_data(data)

    def th_speed(self, state, value):
        global data
        data = 'thSp'
        send_data(data)

    def turn_left(self, state, value):
        global data
        data = 'left' if value == 'down' else 'stop'
        send_data(data)

    def stoped(self, state, value):
        global data
        data = 'stop'
        send_data(data)

    def forwardd(self, state, value):
        global data
        data = 'forward' if value == 'down' else 'stop'
        send_data(data)

    def turn_back(self, state, value):
        data = 'back' if value == 'down' else 'stop'
        send_data(data)


# Запуск проекта
if __name__ == "__main__":
    MyApp().run()
