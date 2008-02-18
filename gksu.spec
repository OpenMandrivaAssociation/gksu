%define name 	gksu
%define version 2.0.0
%define release %mkrel 4

Summary: 	GTK+ frontend to the su and sudo programs
Name:	 	%name
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 	 	Graphical desktop/GNOME
Url:		http://www.nongnu.org/gksu/
Source:  	http://people.debian.org/~kov/gksu/gksu/%name-%version.tar.bz2
BuildRoot: 	%{_tmppath}/%name-root
BuildRequires: 	gettext pkgconfig libgtk+2.0-devel bison autoconf2.5
#BuildRequires:	libgksuui-devel
BuildRequires:	libgksu2-devel 
BuildRequires:	libGConf2-devel gnome-vfs-devel
BuildRequires:	gtk-doc
BuildRequires:  perl-XML-Parser
BuildRequires:  gnome-keyring-devel
BuildRequires:  nautilus-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  desktop-file-utils

%description
gksu is a Gtk+ frontend to /bin/su. It supports login shells and preserving
environment when acting as a su frontend. It is useful to menu items or
other graphical programs that need to ask a user's password to run another
program as another user.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Settings" \
  --add-category="X-MandrivaLinux-System-Configuration-Other" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

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
%{_libdir}/nautilus/extensions-1.0/*
%{_mandir}/man1/*.1.*


