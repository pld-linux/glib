Summary:	Useful routines for 'C' programming
Summary(pl):	Biblioteka zawieraj�ca wiele u�ytecznych funkcji C
Name:		glib
Version:	1.2.3
Release:	2
Copyright:	LGPL
Group:		Libraries
Group(pl):	Biblioteki
Source:		ftp://ftp.gimp.org/pub/gtk/v1.1/%{name}-%{version}.tar.gz
Patch0:		glib-info.patch
URL:		http://www.gtk.org/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
GLib, is a library which includes support routines for C such as lists,
trees, hashes, memory allocation, and many other things. GLIB includes
also generally useful data structures used by GIMP and many other.

%description -l pl
Glib jest zestawem bibliotek zawieraj�cych funkcje do obs�ugi list, drzewek,
funkcji mieszaj�cych, funkcji do alokacji pami�ci i wielu innych
podstawowych funkcji i r�nych struktur danych u�ywanych przez program GIMP i
wiele innch.

%package	devel
Summary:	Glib heades files, documentation
Summary(pl):	Pliki nag��wkowe i dokumentacja do glib
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	autoconf >= 2.13
Requires:	automake >= 1.4
Requires:	libtool	 >= 1.3.2 

%description devel
Header files for the support library for the GIMP's X libraries, which are
available as public libraries. GLIB includes generally useful data
structures.

%description -l pl devel
Pliki nag��wkowe i dokumentacja do glib przydatna przy pisaniu program�w
wykorzystuj�cych t� bibliotek�.

%package	static
Summary:	Static glib libraries
Summary(pl):	Biblioteki statyczne do glib
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static glib libraries.

%description -l pl static
Biblioteki statyczne do glib.

%prep
%setup -q
%patch -p1

%build
aclocal && autoconf
%configure \
	--prefix=%{_prefix} \
	--enable-threads
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/glib* \
	$RPM_BUILD_ROOT%{_mandir}/man1/* \
	AUTHORS ChangeLog NEWS README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
/sbin/install-info %{_infodir}/glib.info.gz /etc/info-dir

%preun devel
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/glib.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root,755)
%{_libdir}/libg*.so.*

%files devel
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz

%attr(755,root,root) %{_libdir}/lib*.so

%{_libdir}/glib
%{_includedir}/*
%{_datadir}/aclocal/*

%{_infodir}/glib.info*

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/glib-config.1.*

%files static
%defattr(644,root,root,755) 

%{_libdir}/lib*.a

%changelog
* Mon May 10 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2.2-2]
-�spec based on version included in tar ball,
- spec rewrited in PLD coding style,
- added pl translation.
