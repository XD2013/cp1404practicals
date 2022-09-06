from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

FACTOR_MILES_TO_KM = 1.60934

class MilesConverter(App):

    def build(self):
        self.title = "Convert Mile KM"
        self.root = Builder.load_file('convert_miles_km.kv')
        Window.size = (700, 300)
        return self.root

    def compute_km(self):
        miles = self.get_miles()
        kilometres = miles * FACTOR_MILES_TO_KM
        self.root.ids.output_kilometres.text = str(kilometres)

    def handle_increment(self,change):
        miles = self.get_miles() + change
        self.root.ids.input_miles.text = str(miles)

    def get_miles(self):
        try:
            return float(self.root.ids.input_miles.text)
        except:
            return 0

MilesConverter().run()