Name: workrave
Version: 1.8.4
Release: 4%{?dist}
Summary: Program that assists in the recovery and prevention of RSI
# Based on older packages by Dag Wieers <dag@wieers.com> and Steve Ratcliffe
License: GPLv2+
Group: Applications/Productivity
URL: http://workrave.sourceforge.net/
# For some reason the upstream tarball contains the -2 added to the version.
Source0: http://prdownloads.sourceforge.net/workrave/%{name}-%{version}-2.tar.gz
Source1: workrave.desktop
Patch1: workrave-1.8.4-applet-crash.patch
Patch2: workrave-1.8.4-applet-fix.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  gettext
BuildRequires:  gnet2-devel
BuildRequires: 	libgnomeuimm26-devel
BuildRequires:  gnome-panel-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libXmu-devel
BuildRequires:  libXt-devel

%description
Workrave is a program that assists in the recovery and prevention of
Repetitive Strain Injury (RSI). The program frequently alerts you to
take micro-pauses, rest breaks and restricts you to your daily limit.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p2 -b .crash
%patch2 -p2 -b .appletfix

%build
if [ ! -x configure ]; then
  ### Needed for snapshot releases.
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh --prefix=%{_prefix} --localstatedir=%{_localstatedir} --sysconfdir=%{_sysconfdir}
else
  %configure
fi
%{__make}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall
%find_lang %{name}

desktop-file-install --vendor fedora                    \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications       \
  --add-category X-Fedora                               \
  %{SOURCE1}


%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/*
%{_datadir}/workrave/
%{_datadir}/sounds/workrave
%{_sysconfdir}/sound/events/workrave.soundlist
%{_libdir}/bonobo/servers/Workrave-Applet.server
%{_libdir}/bonobo/servers/Workrave-Control.server
%{_libexecdir}/workrave-applet
%{_datadir}/gnome-2.0/ui/GNOME_WorkraveApplet.xml
%dir %{_datadir}/pixmaps/workrave
%{_datadir}/pixmaps/workrave/workrave-icon-huge.png
%{_datadir}/applications/fedora-workrave.desktop

%changelog
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
