Summary:	"libpwrite" Network Routine Library
Summary(pl):	Biblioteka czynno∂ci sieciowych
Name:		libnids
Version:	1.16
Release:	1
Epoch:		1
License:	BSD
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	http://www.packetfactory.net/Projects/Libnids/dist/%{name}-%{version}.tar.gz
Patch0:		%{name}-conf.patch
URL:		http://www.packetfactory.net/Projects/Libnids/
BuildRequires:	autoconf
BuildRequires:	libpcap-devel
BuildRequires:	libnet-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libnids is an implementation of an E-component of Network Intrusion
Detection System. It emulates the IP stack of Linux 2.0.x. Libnids
offers IP defragmentation, TCP stream assembly and TCP port scan
detection.

%description -l pl
Libnids jest implementacj± E-komponentu Systemu Wykrywania IntruzÛw w
Sieci (NIDS). Emuluje ona stos IP Linuksa 2.0.x. Libnids oferuje
defragmentacjÍ IP, asemblacjÍ strumienia TCP oraz wykrywanie
skanowania portÛw TCP.

%package devel
Summary:	Header files and develpment documentation for libnids
Summary(pl):	Pliki nag≥Ûwkowe i dokumetacja do libnids
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Header files and develpment documentation for libnids.

%description -l pl devel
Pliki nag≥Ûwkowe i dokumetacja do libnids.

%package static
Summary:	Static libnids library
Summary(pl):	Biblioteka statyczna libnids
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Static libnids library.

%description -l pl static
Biblioteka statyczna libnids.

%prep
%setup -q
%patch0 -p1

%build
autoconf
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	install_prefix=$RPM_BUILD_ROOT

gzip -9nf CHANGES README CREDITS MISC doc/*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
