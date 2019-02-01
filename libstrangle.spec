
Name:           libstrangle
Version:        0.0.4
Release:        1
Summary:        Frame rate limiter for Linux via OpenGL
License:        GPL3
Group:          Games
URL:            https://gitlab.com/torkel104/libstrangle
Source0:        https://gitlab.com/torkel104/libstrangle/-/archive/0.0.4/libstrangle-0.0.4.tar.bz2
Patch0:         defer-ldconfig.patch

BuildRequires:  glibc-devel
BuildRequires:  clang-devel
#BuildRequires:  gcc

%description
Libstrangle is a frame rate limiter for Linux.

%prep
%setup -q
%autopatch -p1

%build
%make_build

%install
%make_install

%files
%{_bindir}/*