
import gi
gi.require_version('Gtk', '3.0')
import os
from gi.repository import Gtk, GdkPixbuf, Gio

from config import load

class Widget(Gtk.VBox):
    def __init__(beta, pictures):
        Gtk.VBox.__init__(beta, spacing=10, border_width=5, halign = Gtk.Align.CENTER)
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
        filename = pictures, 
        width=120, 
        height=100, 
        preserve_aspect_ratio = True)
        image = Gtk.Image.new_from_pixbuf(pixbuf)
        image.set_size_request(5, 5)
        beta.add(image)
        print(pictures)
        
        
class TitledEntry(Gtk.VBox):
    def __init__(self, title=None, text=""):
        Gtk.VBox.__init__(self, spacing=2)

        title = Gtk.Label(label=title, halign=Gtk.Align.START)
        self.add(title)

        entry = Gtk.Entry(text=text)
        self.add(entry)

        self.title_label = title
        self.entry = entry

        self.show_all()
        
class MainWindow(Gtk.Window):
    def __init__(self):
		
        Gtk.Window.__init__(self, title='Hello')
        
        self.set_border_width(10)
        
        self.set_default_size(930, 600)
        
        self.walk_dir = []
        self.backgrounds = "/usr/share/backgrounds"
        self.wallpaper_select_index = 0
        
        self.data = load()
        
        HeaderBar = Gtk.HeaderBar()
        HeaderBar.set_show_close_button(True)
        HeaderBar.props.title = "Wallpaper"
        self.set_titlebar(HeaderBar)
 
        self.currency_combo = Gtk.ComboBoxText()
        self.currency_combo.connect("changed", self.on_currency_combo_changed)
        for select in ["None", "Centered", "Zoom", "Spanned", "Wallpaper", "Scaled", "Stretched"]:
            self.currency_combo.append_text(select)
        self.currency_combo.set_entry_text_column(0)
        HeaderBar.pack_end(self.currency_combo)
        if self.data.get("index") == "None":  self.currency_combo.set_active(int(index))
        else:
            self.currency_combo.set_active(int(self.data.get("index")))
             
        button=Gtk.Button(label="Cancel")
        button.connect('clicked', self.info)
        HeaderBar.pack_start(button)

        scrollbox = Gtk.ScrolledWindow(visible=True)
        self.add(scrollbox)
       

        self.flowbox = Gtk.FlowBox()
        self.flowbox.connect("child-activated", self.select_picture)
        self.flowbox.set_valign(Gtk.Align.START)
        scrollbox.add(self.flowbox)
        
        
        for j in os.walk(self.backgrounds):
            for test in j[2]:
                if test.endswith(".jpg") is True:
                    w = Widget( "{}/{}".format(j[0], test) )
                    self.walk_dir.append( "{}/{}".format(j[0], test) )
                    self.flowbox.add(w)

    def on_currency_combo_changed(self, combo):
        text = combo.get_active_text()
        if text is not None:
            self.data.set("duzen", text.lower())
            self.data.set("index", int(combo.get_active()))
        command = Gio.Settings.new("org.gnome.desktop.background")
        command.set_string("picture-options", text.lower())
        command.apply()
        print ("walpaper select index", text)
          
    def select_picture(self, beta, picture):        
        wallpaper_select_text = self.walk_dir[picture.get_index()]
        self.wallpaper_select_index = picture.get_index()
        command = Gio.Settings.new("org.gnome.desktop.background")
        command.set_string("picture-uri", wallpaper_select_text)
        command.apply()
        print ("wallpaper_select_index", self.wallpaper_select_index)

    def info(self, widged, data=None):
        return 0
        

window = MainWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()

#https://help.gnome.org/admin//system-admin-guide/3.12/background.html.en

