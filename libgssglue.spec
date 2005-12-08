Summary:	GSSAPI interface using mechanisms from other GSSAPI implementations
Summary(pl):	Interfejs GSSAPI u¿ywaj±cy mechanizmów z innych implementacji GSSAPI
Name:		libgssapi
Version:	0.6
Release:	1
License:	mixture of UM and Sun licenses
Group:		Libraries
Source0:	http://www.citi.umich.edu/projects/nfsv4/linux/libgssapi/%{name}-%{version}.tar.gz
# Source0-md5:	e11eb9bc5d3e8e5011918cd2ba6eb8a4
URL:		http://www.citi.umich.edu/projects/nfsv4/linux/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library exports a GSSAPI interface, but doesn't implement any
GSSAPI mechanisms itself; instead it calls GSSAPI routines in other
libraries, depending on the mechanism.

%description -l pl
Ta biblioteka eksportuje interfejs GSSAPI, ale sama nie implementuje
¿adnego mechanizmu GSSAPI - zamiast tego wywo³uje funkcje GSSAPI z
innych bibliotek, w zale¿no¶ci od mechanizmu.

%package devel
Summary:	Development files for libgssapi library
Summary(pl):	Pliki programistyczne biblioteki libgssapi
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for libgssapi library.

%description devel -l pl
Pliki programistyczne biblioteki libgssapi.

%package static
Summary:	Static libgssapi library
Summary(pl):	Statyczna biblioteka libgssapi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgssapi library.

%description static -l pl
Statyczna biblioteka libgssapi.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D doc/gssapi_mech.conf $RPM_BUILD_ROOT%{_sysconfdir}/mech.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libgssapi.so.*.*.*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mech.conf

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgssapi.so
%{_libdir}/libgssapi.la
%{_includedir}/gssglue
%{_pkgconfigdir}/libgssapi.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgssapi.a
