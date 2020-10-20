#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

e = "--enable-lirc \
     --disable-pdf \
     --disable-map \
     --disable-gtk3 \
     --disable-gpu-accel \
     --disable-debug-log \
    "

def setup():
	pisitools.cflags.add("-Wno-deprecated-declarations")
	pisitools.cxxflags.add("-Wno-deprecated-declarations")
	autotools.configure(e)

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

