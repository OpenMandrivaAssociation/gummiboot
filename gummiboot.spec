Name:           gummiboot
Version:        45
Release:        1
Summary:        Simple EFI Boot Manager
Group:          System/Configuration/Boot and Init
ExclusiveArch:  x86_64
License:        LGPLv2+
URL:            http://freedesktop.org/wiki/Software/gummiboot
# git clone git://anongit.freedesktop.org/gummiboot
# cd gummiboot/
# ./autogen
# ./configure
# make distcheck
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  gnu-efi
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  docbook-style-xsl
BuildRequires:  xsltproc

%description
gummiboot is a simple UEFI boot manager which executes configured EFI
images. The default entry is selected by a configured pattern (glob)
or an on-screen menu.

gummiboot operates on the EFI System Partition (ESP) only. gummiboot
reads simple and entirely generic boot loader configuration files;
one file per boot loader entry to select from.

Configuration file fragments, kernels, initrds, other EFI images need
to reside on the ESP.

%prep
%setup -q

%build
export CC=gcc
%configure  --libexecdir=%{_prefix}/lib
%make

%install
%make_install

%post
/usr/bin/gummiboot update >/dev/null 2>&1 || :

%files
%doc README LICENSE
%{_bindir}/gummiboot
%{_mandir}/man8/*
%dir %{_prefix}/lib/gummiboot
%ifarch x86_64
%{_prefix}/lib/gummiboot/gummibootx64.efi
%endif
