#!/usr/bin/env python2.7
"""Gnome Applet to stop Audio Gain Control from WebRTC"""

import signal
import subprocess
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3

class AOCStopper():
    """Class for AOC Stopper Indicator"""
    def __init__(self):
        self.child = 0
        self.running = 0
        self.app = 'AOCindicator'
        self.indicator = AppIndicator3.Indicator.new(
            self.app,
            'whatever',
            AppIndicator3.IndicatorCategory.OTHER)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.create_menu())

    def create_menu(self):
        """Function to add menu items to menu"""
        menu = Gtk.Menu()

        #menu item 1
        self.item_run = Gtk.MenuItem('Disable Audio Gain Control')
        self.item_run.connect('activate', self.menu_run)
        menu.append(self.item_run)

        #menu item 2
        self.item_stop = Gtk.MenuItem('Enable Audio Gain Control')
        self.item_stop.connect('activate', self.menu_stop)
        self.item_stop.set_sensitive(False)
        menu.append(self.item_stop)

        #menu item 3
        item_quit = Gtk.MenuItem('Quit')
        item_quit.connect('activate', self.menu_quit)
        menu.append(item_quit)

        menu.show_all()
        return menu

    def menu_run(self, _):
        """Function to stop AGC"""
        self.child = subprocess.Popen(['bash', './audio-fix.sh'])
        self.running = 1
        self.item_run.set_sensitive(False)
        self.item_stop.set_sensitive(True)

    def menu_stop(self, _):
        """Function to stop script"""
        self.child.kill()
        self.running = 0
        self.item_run.set_sensitive(True)
        self.item_stop.set_sensitive(False)

    def menu_quit(self, _):
        """Function to quit menu and stop script if running"""
        if self.running == 1:
            self.child.kill()
        Gtk.main_quit()

AOCStopper()
signal.signal(signal.SIGINT, signal.SIG_DFL)
Gtk.main()
