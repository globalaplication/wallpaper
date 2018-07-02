
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
        width=120, 
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
        self.set_default_size(930, 600)
        self.deneme = []
        self.backgrounds = "/usr/share/backgrounds"
        self.wallpaper_select_index = 0
        self.data = load()
        
        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Wallpaper"
        self.set_titlebar(hb)
 
        self.currency_combo = Gtk.ComboBoxText()
        self.currency_combo.connect("changed", self.on_currency_combo_changed)
        for select in ["None", "Centered", "Zoom", "Spanned", "Wallpaper", "Scaled", "Stretched"]:
            self.currency_combo.append_text(select)
        self.currency_combo.set_entry_text_column(0)
        hb.pack_end(self.currency_combo)
        if self.data.get("index") == "None":  self.currency_combo.set_active(int(index))
        else:
            self.currency_combo.set_active(int(self.data.get("index")))
             
        button=Gtk.Button(label="Cancel")
        button.connect('clicked', self.info)
        hb.pack_start(button)

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
        self.wallpaper_select_index = heyo.get_index()
        settings = Gio.Settings.new("org.gnome.desktop.background")
        settings.set_string("picture-uri", wallpaper)
        settings.apply()
  
        
    def on_currency_combo_changed(self, combo):
        text = combo.get_active_text()
        if text is not None:
            self.data.set("duzen", text.lower())
            self.data.set("index", int(combo.get_active()))
        print ("walpaper select index", text)

        settings = Gio.Settings.new("org.gnome.desktop.background")
        settings.set_string("picture-options", text.lower())
        settings.apply()
            

        
    def info(self, widged, data=None):
        return 0
        

window = MainWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()



