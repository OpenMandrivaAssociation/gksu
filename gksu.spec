%define Werror_cflags %nil

%define name	gksu
%define version 2.0.2
%define release %mkrel 5

Summary:	GTK+ frontend to the su and sudo programs
Name:		%name
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://www.nongnu.org/gksu/
Source:		http://people.debian.org/~kov/gksu/gksu/%name-%version.tar.bz2
Patch0:		gksu-2.0.2-use-xvt-for-terminal.patch
Patch1:		gksu-2.0.2-fix-nautilus-link.patch
BuildRoot:	%{_tmppath}/%name-root
BuildRequires:	libgksu-devel
BuildRequires:	nautilus-devel
BuildRequires:	intltool

%description
gksu is a Gtk+ frontend to /bin/su. It supports login shells and preserving
environment when acting as a su frontend. It is useful to menu items or
other graphical programs that need to ask a user's password to run another
program as another user.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %name

%clean
rm -fr %buildroot

%post
if [ -e /etc/gksu.conf ]; then
   sh /usr/share/gksu/gksu-migrate-conf.sh
fi

%files -f %name.lang
%defattr (-,root,root)
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*.png
%{_datadir}/%name
%{_libdir}/nautilus/extensions-2.0/*
%{_mandir}/man1/*.1.*
