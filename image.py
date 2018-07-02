
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='GMouse 600')
        self.set_default_size(300, 250)

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "HeaderBar example"
        self.set_titlebar(hb)
             
        button=Gtk.Button(label="click me to set the image")
        button.connect('clicked', self.update_image)
        hb.pack_end(button)
        
        self.scrolled = Gtk.ScrolledWindow()
        self.scrolled.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.scrolled.set_hexpand(True)
        self.scrolled.set_vexpand(True)
        self.add(self.scrolled)
        
        self.image_area = Gtk.Box()
        self.image_area.set_valign(Gtk.Align.START)

        self.add(self.image_area)
        self.scrolled.add(self.image_area)

    def update_image(self, widged, data=None):
        print("j")
        self.image = Gtk.Image()
        self.image.set_from_file('./test.png')
        self.image_area.add(self.image)
        self.image_area.show_all()  
        

window = MainWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()






