
import gi
gi.require_version('Gtk', '3.0')
import os
from gi.repository import Gtk, GdkPixbuf, Gio

class Widget(Gtk.VBox):
    def __init__(self, picture):
        Gtk.VBox.__init__(self, spacing=1, halign=Gtk.Align.START)
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
        filename=picture, 
        width=100, 
        height=100, 
        preserve_aspect_ratio=True)
        image = Gtk.Image.new_from_pixbuf(pixbuf)
        image.set_size_request(5, 5)
        self.add(image)
        print(picture)
        
        g = Gtk.Label("wallpaper")
        self.add(g)
        
class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='GMouse 600')
        self.set_border_width(10)
        self.set_default_size(800, 550)
        self.deneme = []
        self.backgrounds = "/usr/share/backgrounds"

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "HeaderBar example"
        self.set_titlebar(hb)
             
        button=Gtk.Button(label="info")
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


    def info(self, widged, data=None):
        return 0
        

window = MainWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()




#https://stackoverflow.com/questions/28551977/python-gtk3-limit-label-width


