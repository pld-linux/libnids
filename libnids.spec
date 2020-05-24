# note: there is some fork at https://github.com/MITRECND/libnids with 1.25
Summary:	Implementation of E-component of Network Intrusion Detection System
Summary(pl.UTF-8):	Implementacja E-komponentu NIDS (sieciowego systemu wykrywania intruzów)
Name:		libnids
Version:	1.24
Release:	4
Epoch:		1
# contains modified Linux 2.0.36 sources, so v2 only
License:	GPL v2
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libnids/%{name}-%{version}.tar.gz
# Source0-md5:	72d37c79c85615ffe158aa524d649610
Patch0:		%{name}-nolibs.patch
Patch1:		gcc5.patch
URL:		http://libnids.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.2.0
BuildRequires:	libnet-devel
BuildRequires:	libpcap-devel
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libnids is an implementation of an E-component of Network Intrusion
Detection System. It emulates the IP stack of Linux 2.0.x. Libnids
offers IP defragmentation, TCP stream assembly and TCP port scan
detection.

%description -l pl.UTF-8
Libnids jest implementacją E-komponentu Systemu Wykrywania Intruzów w
Sieci (NIDS). Emuluje ona stos IP Linuksa 2.0.x. Libnids oferuje
defragmentację IP, asemblację strumienia TCP oraz wykrywanie
skanowania portów TCP.

%package devel
Summary:	Header files and development documentation for libnids
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumetacja do libnids
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libpcap-devel

%description devel
Header files and development documentation for libnids.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumetacja do libnids.

%package static
Summary:	Static libnids library
Summary(pl.UTF-8):	Biblioteka statyczna libnids
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libnids library.

%description static -l pl.UTF-8
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
%doc CHANGES README CREDITS MISC doc/{API.html,LINUX,PERFORMANCE,TESTS,bugtraq_post}
%attr(755,root,root) %{_libdir}/libnids.so.%{version}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnids.so
%{_includedir}/nids.h
%{_mandir}/man3/libnids.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libnids.a
