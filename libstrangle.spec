
Name:           libstrangle
Version:        0.0.4
Release:        1
Summary:        Frame rate limiter for Linux via OpenGL
License:        GPL3
Group:          Games
URL:            https://gitlab.com/torkel104/libstrangle
Source0:        https://gitlab.com/torkel104/libstrangle/-/archive/0.0.4/libstrangle-0.0.4.tar.bz2
%ifarch %{x86_64} %{znver} %{armx} 
Patch0:         libstrangle-0.0.4-openmandriva-fix-prefix-and-defer-ldconfig.patch
%endif
%ifarch %{ix86}
Patch1:         libstrangle-32bit.patch
%endif

BuildRequires:  glibc-devel
BuildRequires:  clang-devel
#BuildRequires:  gcc

%description
Libstrangle is a frame rate limiter for Linux.

%prep
%setup -q
%autopatch -p0

%build
%make_build

%install
%make_install

%files
%{_datadir}/doc/libstrangle/LICENSE
%{_bindir}/strangle
/usr/lib64/libstrangle/libstrangle.so
/usr/lib/libstrangle/libstrangle.so
/etc/ld.so.conf.d/libstrangle.conf

