#
# Conditional build:
#
%bcond_without	static_libs	# don't build static library
#
Summary:	Useful routines for 'C' programming
Summary(cs.UTF-8):	Šikovná knihovna s funkcemi pro pomocné programy
Summary(da.UTF-8):	Nyttige biblioteksfunktioner
Summary(de.UTF-8):	Eine nützliche Library von Dienstprogramm-Funktionen
Summary(fi.UTF-8):	Kirjasto, jossa on työkalufunktioita
Summary(fr.UTF-8):	Bibliothèque de fonctions utilitaires
Summary(pl.UTF-8):	Biblioteka zawierająca wiele użytecznych funkcji C
Summary(tr.UTF-8):	Yararlı ufak yordamlar kitaplığı
Name:		glib
Version:	1.2.10
Release:	20
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gtk.org/pub/gtk/v1.2/%{name}-%{version}.tar.gz
#Source0-md5:	6fe30dad87c77b91b632def29dd69ef9
Source1:	http://developer.gnome.org/doc/API/%{name}-docs.tar.gz
#Source1-md5:	cae06bf952176ab008100b7b954242f8
Patch0:		%{name}-info.patch
Patch1:		%{name}-ac25.patch
Patch2:		%{name}-am18.patch
Patch3:		%{name}-link.patch
Patch4:		%{name}-gcc34.patch
Patch5:		%{name}-slist_remove.patch
Patch6:		format-security.patch
Patch7:		texi-subsection.patch
Patch8:		inline.patch
URL:		http://www.gtk.org/
BuildRequires:	autoconf >= 2.13
BuildRequires:	automake >= 1.4
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	texinfo
Obsoletes:	libglib1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing

%description
GLib, is a library which includes support routines for C such as
lists, trees, hashes, memory allocation, and many other things. GLIB
includes also generally useful data structures used by GIMP and many
other.

%description -l cs.UTF-8
Šikovná knihovna s funkcemi pro pomocné programy. Vývojové knihovny a
hlavičky jsou v balíčku glib-devel.

%description -l da.UTF-8
Nyttigt bibliotek med forskellige funktioner. Udviklings- biblioteker
og headerfiler er i glib-devel pakken.

%description -l de.UTF-8
Eine nützliche Library von Dienstprogramm-Funktionen.
Entwicklungs-Libraries und Header befinden sich in glib-devel.

%description -l fi.UTF-8
Kirjasto, jossa on työkalufunktioita. Kehitysversiot ja
header-tiedostot ovat glib-devel-paketissa.

%description -l pl.UTF-8
Glib jest zestawem bibliotek zawierających funkcje do obsługi list,
drzewek, funkcji mieszających, funkcji do alokacji pamięci i wielu
innych podstawowych funkcji i różnych struktur danych używanych przez
program GIMP i wiele innych.

%description -l tr.UTF-8
Yararlı yordamlar kitaplığı. Geliştirme kitaplıkları ve başlık
dosyaları glib-devel paketinde yer almaktadır.

%package devel
Summary:	Glib heades files, documentation
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do glib
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	libglib1.2-devel

%description devel
Header files for the support library for the GIMP's X libraries, which
are available as public libraries. GLIB includes generally useful data
structures.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do glib przydatna przy pisaniu
programów wykorzystujących tę bibliotekę.

%package static
Summary:	Static glib libraries
Summary(pl.UTF-8):	Biblioteki statyczne do glib
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static glib libraries.

%description static -l pl.UTF-8
Biblioteki statyczne do glib.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
rm -f acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-debug=%{?debug:yes}%{!?debug:minimum} \
	--enable-threads \
	%{!?with_static_libs:--disable-static}

%{__make} -j1 all check

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libg*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libg*.so.0

%files devel
%defattr(644,root,root,755)
%doc glib/*.html
%attr(755,root,root) %{_bindir}/glib-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/glib
%{_includedir}/*
%{_pkgconfigdir}/*
%{_aclocaldir}/*
%{_infodir}/glib.info*
%{_mandir}/man1/glib-config.1*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
