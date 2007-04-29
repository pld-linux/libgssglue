Summary:	GSSAPI interface using mechanisms from other GSSAPI implementations
Summary(pl.UTF-8):	Interfejs GSSAPI używający mechanizmów z innych implementacji GSSAPI
Name:		libgssapi
Version:	0.11
Release:	1
License:	mixture of UM and Sun licenses
Group:		Libraries
Source0:	http://www.citi.umich.edu/projects/nfsv4/linux/libgssapi/%{name}-%{version}.tar.gz
# Source0-md5:	0e5b4c7267724f8ddf64bc35514c272e
Patch0:		%{name}-soname.patch
URL:		http://www.citi.umich.edu/projects/nfsv4/linux/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library exports a GSSAPI interface, but doesn't implement any
GSSAPI mechanisms itself; instead it calls GSSAPI routines in other
libraries, depending on the mechanism.

%description -l pl.UTF-8
Ta biblioteka eksportuje interfejs GSSAPI, ale sama nie implementuje
żadnego mechanizmu GSSAPI - zamiast tego wywołuje funkcje GSSAPI z
innych bibliotek, w zależności od mechanizmu.

%package devel
Summary:	Development files for libgssapi library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libgssapi
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for libgssapi library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki libgssapi.

%package static
Summary:	Static libgssapi library
Summary(pl.UTF-8):	Statyczna biblioteka libgssapi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgssapi library.

%description static -l pl.UTF-8
Statyczna biblioteka libgssapi.

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

sed -e 's|lib|%{_lib}|g' doc/gssapi_mech.conf > $RPM_BUILD_ROOT%{_sysconfdir}/gssapi_mech.conf

mv -f $RPM_BUILD_ROOT%{_libdir}/lib*.so.* $RPM_BUILD_ROOT/%{_lib}
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.so
ln -sf /%{_lib}/`(cd $RPM_BUILD_ROOT/%{_lib}; echo lib*.so.*.*)` \
	$RPM_BUILD_ROOT%{_libdir}/libgssapi.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) /%{_lib}/libgssapi.so.*.*
%ghost %attr(755,root,root) /%{_lib}/libgssapi.so.?
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gssapi_mech.conf

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgssapi.so
%{_libdir}/libgssapi.la
%{_includedir}/gssglue
%{_pkgconfigdir}/libgssapi.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgssapi.a
