pkgname = "bmake"
version = "20210420"
revision = 0
wrksrc = "bmake"
short_desc = "Portable version of NetBSD make"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
homepage = "http://www.crufty.net/help/sjg/bmake.html"
distfiles = [f"http://www.crufty.net/ftp/pub/sjg/bmake-{version}.tar.gz"]
checksum = ["47e551293843d504fe4197413aa6d7ee003090669ac200932ff40e9ccb4658aa"]

options = ["bootstrap"]

def do_build(self):
    import os
    os.makedirs(self.cwd / "build", exist_ok = True)
    eargs = []
    if self.cross_build:
        eargs = ["--host=" + self.build_profile.short_triplet]
    self.do(
        self.chroot_cwd / "boot-strap",
        eargs + ["--prefix=/usr", "op=build"],
        wrksrc = "build"
    )

def do_install(self):
    import shutil
    eargs = []
    if self.cross_build:
        eargs = ["BMAKE=make"]
    self.do(
        self.chroot_cwd / "boot-strap", [
            "--prefix=/usr", "--install-destdir=" + str(self.chroot_destdir),
            "op=install"
        ] + eargs,
        wrksrc = "build"
    )
    shutil.rmtree(self.destdir / "usr/share/man")
    self.install_man("bmake.1")
    self.install_man("make.1")
    self.install_license("LICENSE")
    self.install_link("bmake", "usr/bin/make")