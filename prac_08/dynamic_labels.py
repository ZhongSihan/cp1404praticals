from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def build(self):
        # 数据（名字列表）
        names = ["Alice", "Bob", "Charlie", "Diana", "Edward"]

        # 创建 BoxLayout
        main_layout = Builder.load_string("""
BoxLayout:
    orientation: 'vertical'
    id: main
""")

        # 遍历名字列表，动态创建 Label，并添加到 main_layout
        for name in names:
            label = Label(text=name, font_size=32, size_hint_y=None, height=40)
            main_layout.add_widget(label)

        return main_layout


DynamicLabelsApp().run()
