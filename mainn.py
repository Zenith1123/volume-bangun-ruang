from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
import math

class VolumeApp(App):
    def build(self):
        self.root_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Judul
        self.root_layout.add_widget(Label(text="HITUNG VOLUME BANGUN RUANG", font_size=24, size_hint_y=None, height=40))
        
        # Layout untuk Kubus
        kubus_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height=50)
        kubus_layout.add_widget(Label(text="Sisi Kubus:"))
        self.entry_sisi = TextInput(multiline=False)
        kubus_layout.add_widget(self.entry_sisi)
        self.root_layout.add_widget(Label(text="=== KUBUS ===", font_size=18))
        self.root_layout.add_widget(kubus_layout)
        btn_kubus = Button(text="Hitung Kubus", size_hint_y=None, height=40)
        btn_kubus.bind(on_press=self.hitung_kubus)
        self.root_layout.add_widget(btn_kubus)
        
        # Layout untuk Tabung
        tabung_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height=80)
        tabung_layout.add_widget(Label(text="Jari-jari Tabung:"))
        self.entry_jari = TextInput(multiline=False)
        tabung_layout.add_widget(self.entry_jari)
        tabung_layout.add_widget(Label(text="Tinggi Tabung:"))
        self.entry_tinggi = TextInput(multiline=False)
        tabung_layout.add_widget(self.entry_tinggi)
        self.root_layout.add_widget(Label(text="=== TABUNG ===", font_size=18))
        self.root_layout.add_widget(tabung_layout)
        btn_tabung = Button(text="Hitung Tabung", size_hint_y=None, height=40)
        btn_tabung.bind(on_press=self.hitung_tabung)
        self.root_layout.add_widget(btn_tabung)
        
        # Layout untuk Bola
        bola_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height=50)
        bola_layout.add_widget(Label(text="Jari-jari Bola:"))
        self.entry_jari_bola = TextInput(multiline=False)
        bola_layout.add_widget(self.entry_jari_bola)
        self.root_layout.add_widget(Label(text="=== BOLA ===", font_size=18))
        self.root_layout.add_widget(bola_layout)
        btn_bola = Button(text="Hitung Bola", size_hint_y=None, height=40)
        btn_bola.bind(on_press=self.hitung_bola)
        self.root_layout.add_widget(btn_bola)
        
        # Label hasil
        self.label_hasil = Label(text="Hasil akan muncul di sini", font_size=18)
        self.root_layout.add_widget(self.label_hasil)
        
        return self.root_layout

    # Fungsi hitung volume
    def hitung_kubus(self, instance):
        try:
            s = float(self.entry_sisi.text)
            volume = s ** 3
            self.label_hasil.text = f"Volume Kubus = {volume:.2f}"
        except:
            self.show_error("Masukkan angka yang valid!")

    def hitung_tabung(self, instance):
        try:
            r = float(self.entry_jari.text)
            t = float(self.entry_tinggi.text)
            volume = math.pi * r**2 * t
            self.label_hasil.text = f"Volume Tabung = {volume:.2f}"
        except:
            self.show_error("Masukkan angka yang valid!")

    def hitung_bola(self, instance):
        try:
            r = float(self.entry_jari_bola.text)
            volume = (4/3) * math.pi * r**3
            self.label_hasil.text = f"Volume Bola = {volume:.2f}"
        except:
            self.show_error("Masukkan angka yang valid!")

    def show_error(self, message):
        popup = Popup(title='Error',
                      content=Label(text=message),
                      size_hint=(None, None), size=(300, 150))
        popup.open()

if __name__ == "__main__":
    VolumeApp().run()