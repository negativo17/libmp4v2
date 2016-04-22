Summary: Library for working with files using the mp4 container format
Name: libmp4v2
Version: 2.0.0
Release: 2%{?dist}
License: MPLv1.1
Group: System Environment/Libraries
URL: http://code.google.com/p/mp4v2
Source0: http://mp4v2.googlecode.com/files/mp4v2-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The libmp4v2 library provides an abstraction layer for working with files
using the mp4 container format. This library is developed by mpeg4ip project
and is an exact copy of the library distributed in the mpeg4ip package.


%package devel
Summary: Development files for the mp4v2 library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Development files and documentation needed to develop and compile programs
using the libmp4v2 library.


%prep
%setup -q -n mp4v2-%{version}


%build
%configure \
    --disable-static \
    --disable-dependency-tracking
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc README COPYING doc/Documentation.txt doc/Authors.txt doc/ReleaseNotes.txt doc/BuildSource.txt doc/ToolGuide.txt
%{_bindir}/*
%{_libdir}/libmp4v2.so.2*
%{_mandir}/man1/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/mp4v2/
%{_libdir}/libmp4v2.so


%changelog
* Sat Jan 10 2015 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-2
- track library soname, so bumps aren't a surprise
- -devel: own %%_includedir/mp4v2/

* Fri Jan 09 2015 Sérgio Basto <sergio@serjux.com> - 2.0.0-1

  Sat Mar 01 2014 Avi Alkalay <avibrazil@gmail.com>
  - included some documentation

  Mon Aug 02 2010 Honore Doktorr <hdfssk@gmail.com>
  - update to upstream 2.0.0

  Mon Aug 02 2010 François Kooman <fkooman@tuxed.net>
  - update to upstream 1.9.1
  - drop redundant patches
  - move README to main package
  - add cli-manuals to main package
  - no longer include the API documentation in devel package
  - move headers to /usr/include/mp4v2/*
  - remove *.la in install phase instead of excluding it while packaging

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Matthias Saou <http://freshrpms.net/> 1.5.0.1-9
- Rebuild to fix runtime problems of the latest builds (#507302).

* Sun Mar 01 2009 Caolán McNamara <caolanm@redhat.com> - 1.5.0.1-8
- constify rets of strchr(const char*)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5.0.1-6
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Matthias Saou <http://freshrpms.net/> 1.5.0.1-5
- Rebuild for new BuildID feature.

* Sun Aug  5 2007 Matthias Saou <http://freshrpms.net/> 1.5.0.1-4
- Update License field.

* Fri Dec 15 2006 Matthias Saou <http://freshrpms.net/> 1.5.0.1-3
- Spec file cleanup (habits, mostly) preparing to submit for Extras inclusion.

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 1.5.0.1-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Jul 18 2006 Noa Resare <noa@resare.com> 1.5.0.1-1
- new upstream release

* Sat May 13 2006 Noa Resare <noa@resare.com> 1.4.1-3
- disabled static lib
- use DESTDIR
- disable-dependency-tracking for faster builds
- removed a manpage template file apt.mpt.gz

* Mon May 08 2006 Noa Resare <noa@resare.com> 1.4.1-2
- specfile cleanups

* Fri May 05 2006 Noa Resare <noa@resare.com> 1.4.1-1.lvn5
- initial release

