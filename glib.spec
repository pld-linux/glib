Summary:	Useful routines for 'C' programming
Summary(pl):	Biblioteka zawieraj帷a wiele u篡tecznych funkcji C
Name:		glib
Version:	1.1.13
Release:	1d
Copyright:	LGPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source:		ftp://ftp.gimp.org/pub/gtk/v1.1/%{name}-%{version}.tar.gz
Patch0:		glib-info.patch
URL:		http://www.gtk.org/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
GLib, is a library which includes support routines for C such as lists,
trees, hashes, memory allocation, and many other things. GLIB includes
also generally useful data structures used by GIMP and many other.

%description -l pl
Glib jest zestawem bibliotek zawieraj帷ych funkcje do obs逝gi list, drzewek,
funkcji mieszaj帷ych, dunkcji do alokacji pami璚i i wielu innych
podstawowych funkcji i r騜nch strukt鏎 danych u篡wanych przez program GIMP i
wiele innch.

%package devel
Summary:	Glib heades files, documentation
Summary(pl):	Pliki nag堯wkowe i dokumentacja do glib
Group:		X11/Libraries/Development
Group(pl):	X11/Biblioteki/Programowanie
Prereq:		/sbin/install-info
Requires:	%{name} = %{version}
Requires:	autoconf >= 2.13, automake >= 1.4, libtool >= 1.2d

%description devel
Header files for the support library for the GIMP's X libraries, which are
available as public libraries. GLIB includes generally useful data
structures.

%description -l pl devel
Pliki nag這wkowe i dokumentacja do glib przydatna przy pisaniu program闚
wykorzystuj帷ych biblioteki glib.

%package static
Summary:	Static glib libraries
Summary(pl):	Biblioteki statyczne do glib
Group:		X11/Libraries/Development
Group(pl):	X11/Biblioteki/Programowanie
Requires:	%{name}-devel = %{version}

%description static
Static glib libraries.

%description -l pl static
Biblioteki statyczne do glib.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr/X11R6 \
	--datadir=/usr/share \
	--infodir=/usr/info \
	--enable-threads
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT/usr/{info/glib*,X11R6/man/man1/*}

bzip2 -9 AUTHORS ChangeLog NEWS README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%post devel
/sbin/install-info /usr/info/glib.info.gz /etc/info-dir

%preun devel
if [ $1 = 0 ]; then
	/sbin/install-info --delete /usr/info/glib.info.gz /etc/info-dir
fi

%files
%attr(755,root,root) /usr/X11R6/lib/libg*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.bz2
/usr/X11R6/lib/lib*.so

/usr/X11R6/lib/glib
/usr/X11R6/include/*
/usr/share/aclocal/*

/usr/info/glib.info*

%attr(755,root,root) /usr/X11R6/bin/*
%attr(644,root,root) /usr/X11R6/man/man1/glib-config.1.gz

%files static
%attr(644,root,root) /usr/X11R6/lib/lib*.a

%changelog
* Mon Jan 18 1999 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.13-1d]
- added Group(pl) and changed all Group fields,
- added "Requires: autoconf >= 2.13, automake >= 1.4, libtool >= 1.2d"
  for devel subpackage.

* Sat Jan 01 1999 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.11-1]
- standarized {un}registering info pages (added glib-info.patch).

* Sat Dec 19 1998 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.9-1]
- added gzipping man pages,
- /sbin/install-info moved to Prereq in devel,
- standarized {un}registering info pages,
- added --enable-threads ./confogure parameter.
- added using LDFLAGS="-s" to ./configure enviroment.

* Tue Nov 24 1998 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.5-1]
- added pl translation,
- added /usr/X11R6/man/man1/glib-config.1 and glib info to devel,
- changes in Summary and %description.

* Fri Sep 18 1998 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.2-2]
- changed prefix to /usr/X11R6.

* Mon Aug  10 1998 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.2-1]
- added -q %setup parameter,
- added using %%{name} and %%{version} macros in Source,
- Buildroot changed to /tmp/%%{name}-%%{version}-root,
- added static subpackage,
- added stripping shared libs.

* Mon Apr 13 1998 Marc Ewing <marc@redhat.com>
- Split out glib package
