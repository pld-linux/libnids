Summary:	"libpwrite" Network Routine Library
Summary(pl):	Biblioteka czynno¶ci sieciowych
Name:		libnids
Version:	1.16
Release:	2
Epoch:		1
License:	BSD
Group:		Libraries
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
Libnids jest implementacj± E-komponentu Systemu Wykrywania Intruzów w
Sieci (NIDS). Emuluje ona stos IP Linuksa 2.0.x. Libnids oferuje
defragmentacjê IP, asemblacjê strumienia TCP oraz wykrywanie
skanowania portów TCP.

%package devel
Summary:	Header files and develpment documentation for libnids
Summary(pl):	Pliki nag³ówkowe i dokumetacja do libnids
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and develpment documentation for libnids.

%description devel -l pl
Pliki nag³ówkowe i dokumetacja do libnids.

%package static
Summary:	Static libnids library
Summary(pl):	Biblioteka statyczna libnids
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libnids library.

%description static -l pl
Biblioteka statyczna libnids.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
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
