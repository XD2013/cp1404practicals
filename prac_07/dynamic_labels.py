from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabels(App):

    def __init__(self):
        super().__init__()
        self.name1 = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.name1:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

DynamicLabels().run()