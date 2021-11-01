Name: binder-utils

Version: 1.0.0
Release: 0
Summary: Binder utils
License: BSD
URL: https://github.com/sailfishos/binder-utils
Source: %{name}-%{version}.tar.bz2

%define libglibutil_version 1.0.52

BuildRequires: pkgconfig(libgbinder)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libglibutil) >= %{libglibutil_version}
BuildRequires: bison
BuildRequires: flex
Requires: libglibutil >= %{libglibutil_version}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Binder command line utilities.

%prep
%setup -q

%build
make -C binder-add KEEP_SYMBOLS=1 release

%install
rm -rf %{buildroot}
make -C binder-add DESTDIR=%{buildroot} install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/binder-add
