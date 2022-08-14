#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nethogs
Version  : 0.8.6
Release  : 6
URL      : https://github.com/raboof/nethogs/archive/v0.8.6/nethogs-0.8.6.tar.gz
Source0  : https://github.com/raboof/nethogs/archive/v0.8.6/nethogs-0.8.6.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: nethogs-bin = %{version}-%{release}
Requires: nethogs-license = %{version}-%{release}
Requires: nethogs-man = %{version}-%{release}
BuildRequires : libpcap-dev
BuildRequires : pkgconfig(ncursesw)

%description
Nethogs
=======
[![Build Status](https://travis-ci.org/raboof/nethogs.svg?branch=master)](https://travis-ci.org/raboof/nethogs)

%package bin
Summary: bin components for the nethogs package.
Group: Binaries
Requires: nethogs-license = %{version}-%{release}

%description bin
bin components for the nethogs package.


%package license
Summary: license components for the nethogs package.
Group: Default

%description license
license components for the nethogs package.


%package man
Summary: man components for the nethogs package.
Group: Default

%description man
man components for the nethogs package.


%prep
%setup -q -n nethogs-0.8.6
cd %{_builddir}/nethogs-0.8.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1644258371
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1644258371
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nethogs
cp %{_builddir}/nethogs-0.8.6/COPYING %{buildroot}/usr/share/package-licenses/nethogs/4cc77b90af91e615a64ae04893fdffa7939db84c
%make_install PREFIX=/usr

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nethogs

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nethogs/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/nethogs.8
