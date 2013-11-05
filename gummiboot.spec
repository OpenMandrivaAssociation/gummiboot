Name:           gummiboot
Version:        38
Release:        %mkrel 2
Summary:        Simple EFI Boot Manager
Group:          System/Boot and Init
ExclusiveArch:  x86_64
License:        LGPLv2+
URL:            http://freedesktop.org/wiki/Software/gummiboot
# git clone git://anongit.freedesktop.org/gummiboot
# cd gummiboot/
# ./autogen
# ./configure
# make distcheck
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  gnu-efi-devel
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



%changelog
* Tue Oct 22 2013 umeabot <umeabot> 38-2.mga4
+ Revision: 541673
- Mageia 4 Mass Rebuild

* Sun Oct 13 2013 tmb <tmb> 38-1.mga4
+ Revision: 496328
- update to v38

* Sun Mar 31 2013 colin <colin> 29-1.mga3
+ Revision: 406860
- New version: 29
- New version: 28

* Sat Feb 23 2013 tmb <tmb> 23-1.mga3
+ Revision: 400161
- BR xsltproc
- add group

  + colin <colin>
    - Import Fedora Package


* Wed Feb 20 2013 Kay Sievers <kay@redhat.com> - 23-1
- version 23

* Tue Feb 19 2013 Kay Sievers <kay@redhat.com> - 22-1
- version 22

* Mon Feb 18 2013 Kay Sievers <kay@redhat.com> - 21-1
- version 21

* Mon Feb 18 2013 Kay Sievers <kay@redhat.com> - 20-1
- version 20

* Mon Feb 11 2013 Kay Sievers <kay@redhat.com> - 19-1
- version 19

* Fri Feb 08 2013 Kay Sievers <kay@redhat.com> - 18-1
- version 18

* Sun Feb 03 2013 Kay Sievers <kay@redhat.com> - 17-1
- version 17

* Thu Jan 24 2013 Kay Sievers <kay@redhat.com> - 16-1
- version 16

* Wed Jan 23 2013 Kay Sievers <kay@redhat.com> - 15-1
- version 15

* Tue Jan 22 2013 Kay Sievers <kay@redhat.com> - 14-1
- version 14

* Mon Jan 21 2013 Kay Sievers <kay@redhat.com> - 13-1
- version 13

* Mon Jan 21 2013 Kay Sievers <kay@redhat.com> - 12-1
- version 12

* Sat Jan 19 2013 Kay Sievers <kay@redhat.com> - 11-1
- version 11

* Thu Jan 17 2013 Kay Sievers <kay@redhat.com> - 10-1
- initial packaging
