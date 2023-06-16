from ast import main
from csv import unix_dialect

import kivy
from kivy.app import App
from kivy.uix import layout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
import kivy.core.window.window_info as f
from kivy.uix.widget import Widget
import threading
from socket import *
import sys

host_name = "192.168.4.1"
port = 1234
address = (host_name, port)
udp_socket = socket(AF_INET, SOCK_DGRAM)
Window.clearcolor = (1, 1, 1, 1)
Window.title = "Навигация"
data = "0000"


class MyApp(App):
    def __init__(self):
        super().__init__()
        self.left = Button(text="",
                           size_hint=(.3, .3),
                           background_normal='left.png',
                           color=(0, 1, 1, 1),
                           )
        self.on = Button(text="on",
                         size_hint=(.3, .1),
                         color=(0, 1, 1, 1),
                         )
        self.off = Button(text="off",
                          size_hint=(.3, .1),
                          color=(0, 1, 1, 1),
                          )
        self.fcSp = Button(text="1",
                         size_hint=(.3, .1),
                         color=(0, 1, 1, 1),
                         )
        self.scSp = Button(text="2",
                          size_hint=(.3, .1),
                          color=(0, 1, 1, 1),
                          )
        self.thSp = Button(text="3",
                         size_hint=(.3, .1),
                         color=(0, 1, 1, 1),
                         )

        self.left.bind(state=self.turn_left)

        self.stop = Button(text="stop",
                           size_hint=(.3, .3),
                           color=(0, 1, 1, 1),
                           )
        self.stop.bind(state=self.stoped)
        self.right = Button(text="",
                            size_hint=(.3, .3),
                            background_normal='right.png',
                            font_size="20sp",
                            color=(0, 1, 1, 1),
                            )
        self.right.bind(state=self.turn_right)
        self.forward = Button(text="",
                              size_hint=(.3, .3),
                              background_normal='forward.png',
                              font_size="20sp",
                              color=(0, 1, 1, 1),
                              )
        self.forward.bind(state=self.forwardd)
        self.back = Button(text="",
                           size_hint=(.3, .3),
                           background_normal='back.png',
                           font_size="20sp",
                           color=(0, 1, 1, 1),
                           )
        self.back.bind(state=self.turn_back)

    def build(self):
        main_l = FloatLayout()
        main_right_l = FloatLayout(size_hint=(0.5, 0.9))
        on_l = AnchorLayout(anchor_x='center', anchor_y='top')
        off_l = AnchorLayout(anchor_x='right', anchor_y='top')
        frSp_l = AnchorLayout(anchor_x='center', anchor_y='center')
        scSp_l = AnchorLayout(anchor_x='right', anchor_y='center')
        thSp_l = AnchorLayout(anchor_x='right', anchor_y='bottom')
        stop_l = AnchorLayout(anchor_x='center', anchor_y='center')
        back_l = AnchorLayout(anchor_x='center', anchor_y='bottom')
        forward_l = AnchorLayout(anchor_x='center', anchor_y='top')
        left_l = AnchorLayout(anchor_x='left', anchor_y='center')
        right_l = AnchorLayout(anchor_x='right', anchor_y='center')
        frSp_l.add_widget(self.fcSp)
        scSp_l.add_widget(self.scSp)
        thSp_l.add_widget(self.thSp)
        on_l.add_widget(self.on)
        off_l.add_widget(self.off)
        stop_l.add_widget(self.stop)
        back_l.add_widget(self.back)
        forward_l.add_widget(self.forward)
        left_l.add_widget(self.left)
        right_l.add_widget(self.right)
        main_right_l.add_widget(stop_l)
        main_right_l.add_widget(back_l)
        main_right_l.add_widget(forward_l)
        main_right_l.add_widget(left_l)
        main_right_l.add_widget(right_l)
        # main_left_l.add_widget(on_l)
        main_l.add_widget(main_right_l)
        main_l.add_widget(on_l)
        main_l.add_widget(off_l)
        main_l.add_widget(frSp_l)
        main_l.add_widget(scSp_l)
        main_l.add_widget(thSp_l)
        # main_l.add_widget(main_left_l)

        '''main_layout = GridLayout(cols=1, rows=3, row_force_default=True, row_default_height=Window.width/4)
        layout = GridLayout(cols=3, rows=3, row_force_default=True, row_default_height=Window.width / 6)
        layout.add_widget(Button(background_color=(1, 1, 1, 0)))
        layout.add_widget(self.forward)
        layout.add_widget(Button(background_color=(1, 1, 1, 0)))
        layout.add_widget(self.left)
        layout.add_widget(self.stop)
        layout.add_widget(self.right)
        layout.add_widget(Button(background_color=(1, 1, 1, 0)))
        layout.add_widget(self.back)
        main_layout.add_widget(layout)
        main_layout.add_widget(self.on)
        main_layout.add_widget(self.off)'''
        return main_l

    def turn_right(self, state, value):
        global data
        data = 'right' if value == 'down' else 'stop'
        tmp = str.encode(data)
        udp_socket.sendto(tmp, address)

    def on(self, state, value):
        global data
        data = 'on'
        tmp = str.encode(data)
        udp_socket.sendto(tmp, address)

    def off(self, state, value):
        global data
        data = 'off'
        tmp = str.encode(data)
        udp_socket.sendto(tmp, address)

    def fr_speed(self, state, value):
        global data
        data = 'frSp'
        tmp = str.encode(data)
        udp_socket.sendto(tmp, address)

    def sc_speed(self, state, value):
        global data
        data = 'scSp'
        tmp = str.encode(data)
        udp_socket.sendto(tmp, address)

    def th_speed(self, state, value):
        global data
        data = 'thSp'
        tmp = str.encode(data)
        udp_socket.sendto(tmp, address)

    def turn_left(self, state, value):
        global data
        data = 'left' if value == 'down' else 'stop'
        tmp = str.encode(data)
        udp_socket.sendto(tmp, address)

    def stoped(self, state, value):
        global data
        data = 'stop'
        tmp = str.encode(data)
        udp_socket.sendto(tmp, address)

    def forwardd(self, state, value):
        global data
        data = 'forward' if value == 'down' else 'stop'
        tmp = str.encode(data)
        udp_socket.sendto(tmp, address)

    def turn_back(self, state, value):
        global data
        data = 'back' if value == 'down' else 'stop'
        tmp = str.encode(data)
        udp_socket.sendto(tmp, address)


# Запуск проекта
if __name__ == "__main__":
    MyApp().run()
