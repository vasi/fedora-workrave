Name: workrave
Version: 1.9.4
Release: 6%{?dist}
Summary: Program that assists in the recovery and prevention of RSI
# Based on older packages by Dag Wieers <dag@wieers.com> and Steve Ratcliffe
License: GPLv2+
Group: Applications/Productivity
URL: http://www.workrave.org/
Source0: http://downloads.sourceforge.net/workrave/%{name}-%{version}.tar.gz

BuildRequires:  gtkmm24-devel
BuildRequires:  GConf2-devel
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libXmu-devel
BuildRequires:  libXt-devel
BuildRequires:  libXtst-devel
BuildRequires:  dbus-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  gstreamer-devel
BuildRequires:  intltool
BuildRequires:  python-cheetah
BuildRequires:  pulseaudio-libs-devel

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



%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%{_bindir}/*
%{_datadir}/workrave/
%{_datadir}/sounds/workrave/
%{_datadir}/icons/hicolor/48x48/apps/workrave-icon-huge.png
%{_datadir}/icons/hicolor/scalable/apps/workrave-sheep.svg
%{_datadir}/applications/fedora-workrave.desktop
%{_datadir}/dbus-1/services/org.workrave.Workrave.service

%changelog
* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-5
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov  7 2011 Tomas Mraz <tmraz@redhat.com> - 1.9.4-3
- rebuilt with new libpng

* Tue Jun 28 2011 Tomas Mraz <tmraz@redhat.com> - 1.9.4-2
- no longer needs gnet2

* Wed Apr 06 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 1.9.4-1
- New upstream bug fix release. Closes rhbz#693958
- https://github.com/rcaelers/workrave/blob/b491d9b5054b5571d5b4ff0f6c9137133735129d/NEWS
- Drop buildroot definition and clean section 

* Thu Feb 10 2011 Tomas Mraz <tmraz@redhat.com> - 1.9.3-4
- due to changes in gnome applet API we have to build without
  gnome support

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb  3 2011 Tomas Mraz <tmraz@redhat.com> - 1.9.3-2
- rebuilt with new gnome-panel

* Fri Dec 17 2010 Tomas Mraz <tmraz@redhat.com> - 1.9.3-1
- new upstream release with bug fixes and usability improvements

* Wed Nov  3 2010 Tomas Mraz <tmraz@redhat.com> - 1.9.2-1
- new upstream release hopefully fixing at least some of the aborts

* Mon Apr 26 2010 Tomas Mraz <tmraz@redhat.com> - 1.9.1-4
- better guard for BadWindow errors in input monitor (#566156)

* Wed Mar 17 2010 Tomas Mraz <tmraz@redhat.com> - 1.9.1-3
- fix FTBFS (#564917)

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
