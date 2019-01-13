%define Werror_cflags %nil

Summary:	GTK+ frontend to the su and sudo programs
Name:		gksu
Version:	2.0.2
Release:	20
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.nongnu.org/gksu/
Source0:	http://people.debian.org/~kov/gksu/gksu/%{name}-%{version}.tar.bz2
Patch0:		gksu-2.0.2-use-xvt-for-terminal.patch
Patch1:		gksu-2.0.2-fix-nautilus-link.patch
Patch2:		glib_fix.patch
Patch3:		gksu-2.0.2-automake-1.13.patch

BuildRequires:  intltool
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libgksu2)
BuildRequires:	pkgconfig(libnautilus-extension)

%description
gksu is a Gtk+ frontend to /bin/su. It supports login shells and preserving
environment when acting as a su frontend. It is useful to menu items or
other graphical programs that need to ask a user's password to run another
program as another user.

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*.png
%{_datadir}/%{name}
%{_libdir}/nautilus/extensions-2.0/*.so
%{_mandir}/man1/*.1*

#---------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

# locales
%find_lang %{name}

%post
if [ -e /etc/gksu.conf ]; then
	sh /usr/share/gksu/gksu-migrate-conf.sh
fi
