Summary:	Implementation of E-component of Network Intrusion Detection System
Summary(pl):	Implementacja E-komponentu NIDS (sieciowego systemu wykrywania intruzów)
Name:		libnids
Version:	1.18
Release:	3
Epoch:		1
License:	BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/libnids/%{name}-%{version}.tar.gz
# Source0-md5:	9ee6dcdfac97bae6fe611aa27d2594a5
Patch0:		%{name}-libnet1.patch
Patch1:		%{name}-nolibs.patch
URL:		http://libnids.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	libpcap-devel
BuildRequires:	libnet1-devel
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
Requires:	%{name} = %{epoch}:%{version}

%description devel
Header files and develpment documentation for libnids.

%description devel -l pl
Pliki nag³ówkowe i dokumetacja do libnids.

%package static
Summary:	Static libnids library
Summary(pl):	Biblioteka statyczna libnids
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
Static libnids library.

%description static -l pl
Biblioteka statyczna libnids.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp -f %{_datadir}/libtool/config.sub .
%{__autoconf}
%{__autoheader}
%configure \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	install_prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES README CREDITS MISC doc/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
