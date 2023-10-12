import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from plyer import gps
import ephem

class SkyApp(App):
    def build(self):
        self.box = BoxLayout()
        gps.configure(on_location=self.update_location)
        gps.start()
        return self.box

    def update_location(self, **kwargs):
        lat = kwargs['lat']
        lon = kwargs['lon']
        self.box.add_widget(Image(source=generate_sky_image(lat, lon)))

def generate_sky_image(lat, lon):
    obs = ephem.Observer()
    obs.lat = str(lat)
    obs.lon = str(lon)
    obs.date = ephem.now()
    star_map = ephem.Constellation().draw(obs)
    # генерируем изображение звездного неба из star_map
    return star_map

if __name__ == "main.py":
   SkyApp().run()