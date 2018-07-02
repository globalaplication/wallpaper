
import gi
gi.require_version('Gtk', '3.0')
import os
from gi.repository import Gtk, GdkPixbuf, Gio

from config import load

class Widget(Gtk.VBox):
    def __init__(self, picture):
        Gtk.VBox.__init__(self, spacing=1, halign=Gtk.Align.CENTER)
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
        filename=picture, 
        width=100, 
        height=100, 
        preserve_aspect_ratio=True)
        image = Gtk.Image.new_from_pixbuf(pixbuf)
        image.set_size_request(5, 5)
        self.add(image)
        print(picture)
        
       
class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='GMouse 600')
        self.set_border_width(10)
        self.set_default_size(800, 700)
        self.deneme = []
        self.backgrounds = "/usr/share/backgrounds"
        self.data = load()
        

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Wallpaper"
        self.set_titlebar(hb)
        
        currencies = ["Centered", "Zoom", "Spanned"]
        self.currency_combo = Gtk.ComboBoxText()
        self.currency_combo.connect("changed", self.on_currency_combo_changed)
        for currency in currencies:
            self.currency_combo.append_text(currency)
        self.currency_combo.set_entry_text_column(0)
        hb.pack_end(self.currency_combo)
        self.currency_combo.set_active(int(self.data.get("index")))
             
        button=Gtk.Button(label="")
        button.connect('clicked', self.info)
        hb.pack_end(button)

        scrollbox = Gtk.ScrolledWindow(visible=False)
        self.add(scrollbox)
        
        self.flowbox = Gtk.FlowBox()
        self.flowbox.connect("child-activated", self.test)
        self.flowbox.set_valign(Gtk.Align.START)
        scrollbox.add(self.flowbox)
        for i in os.listdir(self.backgrounds):
            w = Widget("{}/{}".format(self.backgrounds, i))
            self.deneme.append("{}/{}".format(self.backgrounds, i))
            self.flowbox.add(w)
            
    def test(self, deneme, heyo):        
        wallpaper = self.deneme[heyo.get_index()]
        settings = Gio.Settings.new("org.gnome.desktop.background")
        settings.set_string("picture-uri", wallpaper)
        settings.apply()
        
    def on_currency_combo_changed(self, combo):
        text = combo.get_active_text()
        index = combo.get_active()
        if text is not None:
            print(text.lower())
            self.data.set("duzen", text.lower())
            self.data.set("index", index)


    def info(self, widged, data=None):
        print (self.data.get("duzen"))
        

window = MainWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()



