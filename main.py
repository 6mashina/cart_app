import kivy
from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
import kivy.core.window.window_info as f
from kivy.uix.widget import Widget
import threading
from socket import *
import sys

HEIGHT = 900
WEIGHT = 600

host_name = "192.168.4.1"
port = 1234
address = (host_name, port)

#Window.size = (HEIGHT, WEIGHT)
Window.clearcolor = (1, 1, 1, 1)
Window.title = "Навигация"
address = (host_name, port)
udp_socket = socket(AF_INET, SOCK_DGRAM)
data = "0000"


def send_data(data):
    tmp = str.encode(data)
    try:
        udp_socket.sendto(tmp, address)
    except Exception as e:
        print("Ошибка отправки данных:", e)



class MyApp(App):

    def __init__(self):
        super().__init__()
        self.left = Button(text="",
                           background_normal='left.png',
                           font_size="20sp",
                           color=(0, 1, 1, 1),
                           )

        self.left.bind(state=self.turn_left)

        self.stop = Button(text="stop",
                           font_size="20sp",
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

    def build(self):
        layout = GridLayout(cols=3, rows=3, row_force_default=True, row_default_height=Window.width / 3)
        layout.add_widget(Button(background_color=(1, 1, 1, 0)))
        layout.add_widget(self.forward)
        layout.add_widget(Button(background_color=(1, 1, 1, 0)))
        layout.add_widget(self.left)
        layout.add_widget(self.stop)
        layout.add_widget(self.right)
        layout.add_widget(Button(background_color=(1, 1, 1, 0)))
        layout.add_widget(self.back)
        return layout

    def turn_right(self, state, value):
        global data
        data = '1000' if value == 'down' else '0000'
        send_data(data)

    def turn_left(self, state, value):
        global data
        data = '0100' if value == 'down' else '0000'
        send_data(data)

    def stoped(self, state, value):
        global data
        data = '0000'
        send_data(data)

    def forwardd(self, state, value):
        global data
        data = '0010' if value == 'down' else '0000'
        send_data(data)

    def turn_back(self, state, value):
        global data
        data = '0001' if value == 'down' else '0000'
        send_data(data)


# Запуск проекта
if __name__ == "__main__":
    MyApp().run()