Summary:	GSSAPI interface using mechanisms from other GSSAPI implementations
Summary(pl):	Interfejs GSSAPI u¿ywaj±cy mechanizmów z innych implementacji GSSAPI
Name:		libgssapi
Version:	0.1
Release:	1
License:	mixture of UM and Sun licenses
Group:		Libraries
Source0:	http://www.citi.umich.edu/projects/nfsv4/linux/libgssapi/%{name}-%{version}.tar.gz
# Source0-md5:	6e37f3d1366fee219fd714e5f30b7649
Patch0:		%{name}-configure.patch
URL:		http://www.citi.umich.edu/projects/nfsv4/linux/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	heimdal-devel
BuildRequires:	libtool
# it's checked before heimdal (which is preferred in PLD)
BuildConflicts:	krb5-devel
Requires:	heimdal-libs
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
Summary:	Header files for libgssapi library
Summary(pl):	Pliki nag³ówkowe biblioteki libgssapi
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libgssapi library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libgssapi.

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
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-krb5=/usr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_libdir}/libgssapi.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgssapi.so
%{_libdir}/libgssapi.la

%files static
%defattr(644,root,root,755)
%{_libdir}/libgssapi.a
