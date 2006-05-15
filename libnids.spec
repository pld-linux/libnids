Summary:	Implementation of E-component of Network Intrusion Detection System
Summary(pl):	Implementacja E-komponentu NIDS (sieciowego systemu wykrywania intruz�w)
Name:		libnids
Version:	1.21
Release:	1
Epoch:		1
License:	BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/libnids/%{name}-%{version}.tar.gz
# Source0-md5:	8c43dd7d66350eed99a29be50bc5615f
Patch0:		%{name}-libnet1.patch
Patch1:		%{name}-nolibs.patch
URL:		http://libnids.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.2.0
BuildRequires:	libnet1-devel
BuildRequires:	libpcap-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libnids is an implementation of an E-component of Network Intrusion
Detection System. It emulates the IP stack of Linux 2.0.x. Libnids
offers IP defragmentation, TCP stream assembly and TCP port scan
detection.

%description -l pl
Libnids jest implementacj� E-komponentu Systemu Wykrywania Intruz�w w
Sieci (NIDS). Emuluje ona stos IP Linuksa 2.0.x. Libnids oferuje
defragmentacj� IP, asemblacj� strumienia TCP oraz wykrywanie
skanowania port�w TCP.

%package devel
Summary:	Header files and development documentation for libnids
Summary(pl):	Pliki nag��wkowe i dokumetacja do libnids
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and development documentation for libnids.

%description devel -l pl
Pliki nag��wkowe i dokumetacja do libnids.

%package static
Summary:	Static libnids library
Summary(pl):	Biblioteka statyczna libnids
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libnids library.

%description static -l pl
Biblioteka statyczna libnids.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub .
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
