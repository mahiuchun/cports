pkgname = "libedit"
_datever = "20210522"
_distver = 3.1
version = f"{_datever}.{_distver}"
revision = 0
build_style = "gnu_configure"
makedepends = ["ncurses-devel"]
short_desc = "Port of the NetBSD command line editing library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
homepage = "http://www.thrysoee.dk/editline"
distfiles = [f"http://thrysoee.dk/editline/{pkgname}-{_datever}-{_distver}.tar.gz"]
checksum = ["0220bc2047e927c0c1984ef5f7b4eb2a9469a5b7bf12ba573ca3b23ca02bbb6f"]

options = ["bootstrap", "!check"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libedit-devel")
def _devel(self):
    self.depends = [f"{pkgname}={version}-r{revision}"] + makedepends
    self.short_desc = short_desc + " - development files"

    return [
        "usr/include",
        "usr/lib/*.a",
        "usr/lib/*.so",
        "usr/lib/pkgconfig",
        "usr/share/man/man3",
    ]
