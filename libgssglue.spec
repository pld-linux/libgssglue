Summary:	GSSAPI interface using mechanisms from other GSSAPI implementations
Summary(pl.UTF-8):	Interfejs GSSAPI używający mechanizmów z innych implementacji GSSAPI
Name:		libgssglue
Version:	0.2
Release:	1
License:	BSD/MIT
Group:		Libraries
Source0:	http://www.citi.umich.edu/projects/nfsv4/linux/libgssglue/%{name}-%{version}.tar.gz
# Source0-md5:	89b3a589780667f666cb8bf033befeb3
Patch0:		%{name}-soname.patch
URL:		http://www.citi.umich.edu/projects/nfsv4/linux/
Obsoletes:	libgssapi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
This library exports a GSSAPI interface, but doesn't implement any
GSSAPI mechanisms itself; instead it calls GSSAPI routines in other
libraries, depending on the mechanism.

%description -l pl.UTF-8
Ta biblioteka eksportuje interfejs GSSAPI, ale sama nie implementuje
żadnego mechanizmu GSSAPI - zamiast tego wywołuje funkcje GSSAPI z
innych bibliotek, w zależności od mechanizmu.

%package devel
Summary:	Development files for libgssglue library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libgssglue
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libgssapi-devel

%description devel
Development files for libgssglue library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki libgssglue.

%package static
Summary:	Static libgssglue library
Summary(pl.UTF-8):	Statyczna biblioteka libgssglue
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libgssapi-static

%description static
Static libgssglue library.

%description static -l pl.UTF-8
Statyczna biblioteka libgssglue.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},/%{_lib}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

sed -e 's|/lib/|/%{_lib}/|g' doc/gssapi_mech.conf > $RPM_BUILD_ROOT%{_sysconfdir}/gssapi_mech.conf

mv -f $RPM_BUILD_ROOT%{_libdir}/lib*.so.* $RPM_BUILD_ROOT/%{_lib}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.so
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/lib*.so.*.*) \
	$RPM_BUILD_ROOT%{_libdir}/libgssglue.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) /%{_lib}/libgssglue.so.*.*
%attr(755,root,root) %ghost /%{_lib}/libgssglue.so.1
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gssapi_mech.conf

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgssglue.so
%{_libdir}/libgssglue.la
%{_includedir}/gssglue
%{_pkgconfigdir}/libgssglue.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgssglue.a
