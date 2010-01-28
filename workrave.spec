Name: workrave
Version: 1.9.1
Release: 2%{?dist}
Summary: Program that assists in the recovery and prevention of RSI
# Based on older packages by Dag Wieers <dag@wieers.com> and Steve Ratcliffe
License: GPLv2+
Group: Applications/Productivity
URL: http://workrave.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/workrave/%{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  gettext
BuildRequires:  gnet2-devel
BuildRequires:  libgnomeuimm26-devel
BuildRequires:  gnome-panel-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libXmu-devel
BuildRequires:  libXt-devel
BuildRequires:  libXtst-devel
BuildRequires:  dbus-devel
BuildRequires:  gstreamer-devel
BuildRequires:  intltool

Requires: dbus

%description
Workrave is a program that assists in the recovery and prevention of
Repetitive Strain Injury (RSI). The program frequently alerts you to
take micro-pauses, rest breaks and restricts you to your daily limit.

%prep
%setup -q -n %{name}-%{version}

%build
if [ ! -x configure ]; then
  ### Needed for snapshot releases.
  NOCONFIGURE=1 ./autogen.sh
fi

%configure --enable-dbus --disable-xml

%{__make}

%install
%{__rm} -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

desktop-file-install --vendor fedora                    \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications       \
  --add-category X-Fedora                               \
  --remove-category GTK                                 \
  --delete-original                                     \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop


%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%{_bindir}/*
%{_datadir}/workrave/
%{_datadir}/sounds/workrave
%{_sysconfdir}/sound/events/workrave.soundlist
%{_libdir}/bonobo/servers/Workrave-Applet.server
%{_libexecdir}/workrave-applet
%{_datadir}/gnome-2.0/ui/GNOME_WorkraveApplet.xml
%{_datadir}/pixmaps/workrave
%{_datadir}/applications/fedora-workrave.desktop
%{_datadir}/dbus-1/services/org.workrave.Workrave.service

%changelog
* Thu Jan 28 2010 Tomas Mraz <tmraz@redhat.com> - 1.9.1-2
- do not build against gdome2 - not too useful optional feature

* Tue Dec  9 2009 Tomas Mraz <tmraz@redhat.com> - 1.9.1-1
- new upstream version

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 27 2009 Tomas Mraz <tmraz@redhat.com> - 1.9.0-3
- fix build with new gcc 4.4 and glibc

* Fri Sep 26 2008 Tomas Mraz <tmraz@redhat.com> - 1.9.0-1
- new upstream version

* Fri Apr  4 2008 Tomas Mraz <tmraz@redhat.com> - 1.8.5-4
- fix locking/unlocking with gnome-screensaver (#207058)
- make it build with current libsigc++

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.8.5-3
- Autorebuild for GCC 4.3

* Tue Feb 19 2008 Tomas Mraz <tmraz@redhat.com> - 1.8.5-2
- make it build on gcc-4.3

* Mon Jan  7 2008 Tomas Mraz <tmraz@redhat.com> - 1.8.5-1
- upgrade to latest upstream version

* Wed Aug 22 2007 Tomas Mraz <tmraz@redhat.com> - 1.8.4-4
- applet counters don't start properly
- license tag fix

* Wed Apr 18 2007 Tomas Mraz <tmraz@redhat.com> - 1.8.4-3
- fixed applet crash (#236543)

* Mon Mar 26 2007 Tomas Mraz <tmraz@redhat.com> - 1.8.4-2
- new upstream version
- add datadir/pixmaps/workrave to files (#233815)

* Thu Sep  7 2006 Tomas Mraz <tmraz@redhat.com> - 1.8.3-2
- rebuilt for FC6

* Wed May 31 2006 Tomas Mraz <tmraz@redhat.com> - 1.8.3-1
- New upstream version

* Wed Feb 15 2006 Tomas Mraz <tmraz@redhat.com> - 1.8.2-2
- Rebuilt with updated gcc

* Thu Feb  2 2006 Tomas Mraz <tmraz@redhat.com> - 1.8.2-1
- Updated version, dropped obsolete patch
- Added missing buildrequires for modular X
- Fixed compilation on gcc-4.1

* Sat Oct 22 2005 Tomas Mraz <tmraz@redhat.com> - 1.8.1-4
- Added a desktop file
- Added find_lang
- Fixed wrong install extension for message translations

* Thu Oct 20 2005 Tomas Mraz <tmraz@redhat.com> - 1.8.1-3
- Removed Prefix:, added BuildRequires gnome-panel-devel
- Group: Applications/Productivity

* Thu Sep 22 2005 Tomas Mraz <tmraz@redhat.com> - 1.8.1-2
- Initial package, reused spec from package by Steve Ratcliffe
