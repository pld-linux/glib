Summary:     Handy library of utility functions
Name:        glib
Version:     1.1.4
Release:     1
Copyright:   LGPL
Group:       Libraries
Source:      ftp://ftp.gimp.org/pub/gtk/v1.0/%{name}-%{version}.tar.gz
URL:         http://www.gtk.org/
BuildRoot:   /tmp/%{name}-%{version}-root

%description
Handy library of utility functions.  Development libs and headers
are in glib-devel.

%package devel
Summary:     glib heades files, documentation
Group:       X11/Libraries
Requires:    %{name} = %{version}

%description devel
Header files for the support library for the GIMP's X libraries, which are
available as public libraries. GLIB includes generally useful data
structures.

%package static
Summary:     Static glib libraries
Group:       X11/Libraries
Requires:    %{name}-devel = %{version}

%description static
Static glib libraries.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=/usr/X11R6 \
	--datadir=/usr/share

make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%attr(755, root, root) /usr/X11R6/lib/libg*.so.*.*

%files devel
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog NEWS README
/usr/X11R6/lib/lib*.so
/usr/X11R6/lib/glib
/usr/X11R6/include/*
/usr/share/aclocal/*
%attr(755, root, root) /usr/X11R6/bin/*

%files static
%attr(644, root, root) /usr/X11R6/lib/lib*.a

%changelog
* Fri Sep 18 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.2-2]
- changed prefix to /usr/X11R6.

* Mon Aug  10 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.2-1]
- added -q %setup parameter,
- added using %%{name} and %%{version} macros in Source,
- Buildroot changed to /tmp/%%{name}-%%{version}-root,
- added static subpackage,
- added striping shared libs.

* Mon Apr 13 1998 Marc Ewing <marc@redhat.com>
- Split out glib package
