%define Werror_cflags %nil

%define name	gksu
%define version 2.0.2
%define release 9

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
Patch2:		glib_fix.patch
BuildRoot:	%{_tmppath}/%name-root
BuildRequires:	libgksu-devel
BuildRequires:	nautilus-devel
BuildRequires:  intltool

%description
gksu is a Gtk+ frontend to /bin/su. It supports login shells and preserving
environment when acting as a su frontend. It is useful to menu items or
other graphical programs that need to ask a user's password to run another
program as another user.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoreconf -fi
%configure2_5x 
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std 

#we don't need .desktop file
rm -rf %{buildroot}%{_datadir}/applications

%find_lang %name

%post
if [ -e /etc/gksu.conf ]; then
   sh /usr/share/gksu/gksu-migrate-conf.sh
fi

%files -f %name.lang
%defattr (-,root,root)
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/*
#{_datadir}/applications/*
%{_datadir}/pixmaps/*.png
%{_datadir}/%name
%{_libdir}/nautilus/extensions-2.0/*
%{_mandir}/man1/*.1.*


%changelog
* Fri Jul 22 2011 akdengi <kazancas@mandriva.org> 2.0.2-5mdv2011.0
+ Revision: 690933
- fix missing translations problem

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

  + Sandro Cazzaniga <kharec@mandriva.org>
    - fix warnings, clean RPM_BUILD_ROOT at beginning of %%install

* Sun Oct 11 2009 Funda Wang <fwang@mandriva.org> 2.0.2-3mdv2010.0
+ Revision: 456624
- remove unneeded BR
- fix terminal command (bug#48959)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Mar 19 2009 Emmanuel Andry <eandry@mandriva.org> 2.0.2-1mdv2009.1
+ Revision: 357737
- BR intltool

  + JÃ©rÃ´me Soyer <saispo@mandriva.org>
    - Fix bug 19260

* Tue Sep 23 2008 Emmanuel Andry <eandry@mandriva.org> 2.0.0-6mdv2009.0
+ Revision: 287513
- fix license
- fix BR
- export gnome-vfs directory
- fix wrong menu entry (bug #44144)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - BuildRequires:  gnome-vfs-devel
    - rebuild
    - fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Sep 09 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.0.0-3mdv2008.0
+ Revision: 83940
- fix buildrequires
- fix postinstall script


* Tue Mar 06 2007 Emmanuel Andry <eandry@mandriva.org> 2.0.0-3mdv2007.0
+ Revision: 134099
- drop buildrequires libgksuui-devel
- add %%post for migration from previous version

* Sat Jan 27 2007 Emmanuel Andry <eandry@mandriva.org> 2.0.0-2mdv2007.1
+ Revision: 114417
- xdg menu
  fix gconf warnings

* Sat Jan 06 2007 Emmanuel Andry <eandry@mandriva.org> 2.0.0-1mdv2007.1
+ Revision: 104921
- New version 2.0.0

* Sat Nov 25 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.3.7-5mdv2007.1
+ Revision: 87229
- fix buildrequires
- Import gksu

* Fri Nov 24 2006 Götz Waschk <waschk@mandriva.org> 1.3.7-4mdv2007.1
- deinstall gconf schema in preun, not postun

* Thu Sep 14 2006 Emmanuel Andry <eandry@mandriva.org> 1.3.7-3mdv2007.0
- buildrequires gnome-keyring-devel
- use gconf macros

* Mon Sep 11 2006 Emmanuel Andry <eandry@mandriva.org> 1.3.7-2mdv2007.0
- rebuild

* Fri Apr 14 2006 Jerome Soyer <saispo@mandriva.org> 1.3.7-1mdk
- New release 1.3.7

* Sat Nov 05 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.3.6-2mdk
- Fix BuildRequires

* Fri Nov 04 2005 Austin Acton <austin@mandriva.org> 1.3.6-1mdk
- New release 1.3.6

* Sat Oct 01 2005 Lenny Cartier <lenny@mandriva.com> 1.3.5-1mdk
- 1.3.5

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.3.4-2mdk
- Fix BuildRequires

* Thu Aug 25 2005 Austin Acton <austin@mandriva.org> 1.3.4-1mdk
- 1.3.4
- source URL
- configure 2.5
- buildrequires gtk-doc
- install schemas

* Wed Oct 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2.2-1mdk
- 1.2.2

