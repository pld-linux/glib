Summary:     Useful routines for 'C' programming
Summary(pl): Biblioteka zawierająca wiele użytecznych funkcji C
Name:        glib
Version:     1.1.5
Release:     1
Copyright:   LGPL
Group:       Libraries
Source:      ftp://ftp.gimp.org/pub/gtk/v1.0/%{name}-%{version}.tar.gz
URL:         http://www.gtk.org/
BuildRoot:   /tmp/%{name}-%{version}-root

%description
GLib, is a library which includes support routines for C such as lists,
trees, hashes, memory allocation, and many other things. GLIB includes
also generally useful data structures used by GIMP and many other.

%description -l pl
Glib jest zestawem bibliotek zawierających funkcje do obsługi list, drzewek,
funkcji mieszających, dunkcji do alokacji pamięci i wielu innych
podstawowych funkcji i różnch struktór danych używanych przez program GIMP i
wiele innch.

%package devel
Summary:     Glib heades files, documentation
Summary(pl): Pliki nagłówkowe i dokumentacja do glib
Group:       X11/Libraries
Requires:    %{name} = %{version}, /sbin/install-info

%description devel
Header files for the support library for the GIMP's X libraries, which are
available as public libraries. GLIB includes generally useful data
structures.

%description devel -l pl
Pliki nagłowkowe i dokumentacja do glib przydatna przy pisaniu programów
wykorzystujących biblioteki glib.

%package static
Summary:     Static glib libraries
Summary(pl): biblioteki statyczne do glib
Group:       X11/Libraries
Requires:    %{name}-devel = %{version}

%description static
Static glib libraries.

%description static -l pl
Biblioteki statyczne do glib.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=/usr/X11R6 \
	--datadir=/usr/share \
	--infodir=/usr/info
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT/usr/info/glib*

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/sbin/install-info /usr/info/glib.info.gz /usr/info/dir --entry \
"* GLIB: (glib).                                 Useful routines for 'C' programming"

%preun
/sbin/install-info --delete /usr/info/glib.info.gz /usr/info/dir --entry \
"* GLIB: (glib).                                 Useful routines for 'C' programming"

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
/usr/info/glib.info*
%attr(755, root, root) /usr/X11R6/bin/*
%attr(644, root, root) /usr/X11R6/man/man1/glib-config.1

%files static
%attr(644, root, root) /usr/X11R6/lib/lib*.a

%changelog
* Tue Nov 24 1998 Tomasz Kłoczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.5-1]
- added pl translation,
- added /usr/X11R6/man/man1/glib-config.1 and glib info to devel,
- changes in Summary and %description.

* Fri Sep 18 1998 Tomasz Kłoczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.2-2]
- changed prefix to /usr/X11R6.

* Mon Aug  10 1998 Tomasz Kłoczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.2-1]
- added -q %setup parameter,
- added using %%{name} and %%{version} macros in Source,
- Buildroot changed to /tmp/%%{name}-%%{version}-root,
- added static subpackage,
- added striping shared libs.

* Mon Apr 13 1998 Marc Ewing <marc@redhat.com>
- Split out glib package
