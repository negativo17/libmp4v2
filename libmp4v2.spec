Summary:    Library for working with files using the mp4 container format
Name:       libmp4v2
Version:    2.0.0
Release:    3%{?dist}
License:    MPLv1.1
URL:        http://code.google.com/p/mp4v2

Source0:    http://mp4v2.googlecode.com/files/mp4v2-%{version}.tar.bz2
Patch0:     %{name}-2.0.0-gcc7.patch

%description
The libmp4v2 library provides an abstraction layer for working with files using
the mp4 container format. This library is developed by mpeg4ip project and is an
exact copy of the library distributed in the mpeg4ip package.

%package devel
Summary:    Development files for the mp4v2 library
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files and documentation needed to develop and compile programs using
the libmp4v2 library.

%prep
%autosetup -p0 -n mp4v2-%{version}

%build
%configure \
    --disable-static \
    --disable-dependency-tracking
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%doc README doc/Documentation.txt doc/Authors.txt doc/ReleaseNotes.txt doc/ToolGuide.txt
%{_bindir}/*
%{_libdir}/%{name}.so.*
%{_mandir}/man1/*

%files devel
%{_includedir}/mp4v2/
%{_libdir}/%{name}.so


%changelog
* Tue Oct 24 2017 Simone Caronni <negativo17@gmail.com> - 2.0.0-3
- Clean up SPEC file.
- Fix GCC 7 build.

* Sat Jan 10 2015 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-2
- track library soname, so bumps aren't a surprise
- -devel: own %%_includedir/mp4v2/
