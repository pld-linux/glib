Summary:	Useful routines for 'C' programming
Summary(cs):	©ikovná knihovna s funkcemi pro pomocné programy
Summary(da):	Nyttige biblioteksfunktioner
Summary(de):	Eine nützliche Library von Dienstprogramm-Funktionen
Summary(fi):	Kirjasto, jossa on työkalufunktioita
Summary(fr):	Bibliothèque de fonctions utilitaires
Summary(pl):	Biblioteka zawieraj±ca wiele u¿ytecznych funkcji C
Summary(tr):	Yararlý ufak yordamlar kitaplýðý
Name:		glib
Version:	1.2.8
Release:	6
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.gtk.org/pub/gtk/v1.2/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		glib-gccwarn.patch
URL:		http://www.gtk.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr

%description
GLib, is a library which includes support routines for C such as
lists, trees, hashes, memory allocation, and many other things. GLIB
includes also generally useful data structures used by GIMP and many
other.

%description -l cs
©ikovná knihovna s funkcemi pro pomocné programy. Vývojové knihovny a
hlavièky jsou v balíèku glib-devel.

%description -l da
Nyttigt bibliotek med forskellige funktioner. Udviklings- biblioteker
og headerfiler er i glib-devel pakken.

%description -l de
Eine nützliche Library von Dienstprogramm-Funktionen.
Entwicklungs-Libraries und Header befinden sich in glib-devel.

%desription -l fi
Kirjasto, jossa on työkalufunktioita. Kehitysversiot ja header-tiedostot
ovat glib-devel-paketissa.

%description -l pl
Glib jest zestawem bibliotek zawieraj±cych funkcje do obs³ugi list,
drzewek, funkcji mieszaj±cych, funkcji do alokacji pamiêci i wielu
innych podstawowych funkcji i ró¿nych struktur danych u¿ywanych przez
program GIMP i wiele innch.

%description -l tr
Yararlý yordamlar kitaplýðý. Geliþtirme kitaplýklarý ve baþlýk
dosyalarý glib-devel paketinde yer almaktadýr.

%package devel
Summary:	Glib heades files, documentation
Summary(pl):	Pliki nag³ówkowe i dokumentacja do glib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	autoconf >= 2.13
Requires:	automake >= 1.4
Requires:	libtool	 >= 1.3.2 

%description devel
Header files for the support library for the GIMP's X libraries, which
are available as public libraries. GLIB includes generally useful data
structures.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja do glib przydatna przy pisaniu
programów wykorzystuj±cych tê bibliotekê.

%package static
Summary:	Static glib libraries
Summary(pl):	Biblioteki statyczne do glib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static glib libraries.

%description -l pl static
Biblioteki statyczne do glib.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--enable-threads
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

gzip -9nf AUTHORS ChangeLog NEWS README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libg*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz

%attr(755,root,root) %{_libdir}/lib*.so

%{_libdir}/glib
%{_includedir}/*
%{_aclocaldir}/*

%{_infodir}/glib.info*

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/glib-config.1.*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
