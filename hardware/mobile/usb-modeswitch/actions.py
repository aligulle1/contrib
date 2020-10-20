#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

SNAPSHOT="20191128"

def build():
	autotools.make("CC='%s' CFLAGS='%s'" % (get.CC(), get.CFLAGS()))

def install():
	autotools.rawInstall("DESTDIR='%s'" % get.installDIR())
	autotools.rawInstall("-C ../usb-modeswitch-data-%s DESTDIR='%s'" % (SNAPSHOT, get.installDIR()))

	pisitools.removeDir("/etc/usb_modeswitch.d")

	pisitools.dodoc("ChangeLog", "COPYING", "README")

