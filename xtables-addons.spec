Name:       xtables-addons
Summary:    Extensions targets and matches for iptables
Version:    3.28
Release:    2%{?dist}
# The entire source code is GPLv2 except ACCOUNT/libxt_ACCOUNT_cl.* which is LGPLv2
License:    GPL-2.0-only AND LGPL-2.0-only
URL:        https://inai.de/projects/xtables-addons/
Source0:    https://inai.de/files/%{name}/%{name}-%{version}.tar.xz

BuildRequires:    gcc
BuildRequires:    iptables-devel >= 1.4.5
Provides:         %{name}-kmod-common = %{version}
Requires:         %{name}-kmod >= %{version}
Requires:         ipset >= 6.11

%description
Xtables-addons provides extra modules for iptables not present in the kernel,
and is the successor of patch-o-matic. Extensions includes new targets like
TEE, TARPIT, CHAOS, or modules like geoip, ipset, and account.

This package provides the userspace libraries for iptables to use extensions
in the %{name}-kmod package. You must also install the
%{name}-kmod package.

%prep
%autosetup

%build
%configure --without-kbuild

%make_build V=1

%install
%make_install

# There is no -devel package. So no need for these files
rm -f %{buildroot}%{_libdir}/*.{la,so}


%files
%doc README.rst doc/* geoip
%license LICENSE
%{_libexecdir}/xtables-addons/
%{_libdir}/xtables/
%{_libdir}/*.so.*
%{_bindir}/xt_geoip_query
%{_sbindir}/pknlusr
%{_sbindir}/iptaccount
%{_mandir}/man?/*

%changelog
* Sun Jul 27 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri May 30 2025 Leigh Scott <leigh123linux@gmail.com> - 3.28-1
- Update to 3.28

* Wed Jan 29 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 21 2024 Leigh Scott <leigh123linux@gmail.com> - 3.27-1
- Update to 3.27

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Mar 27 2024 Leigh Scott <leigh123linux@gmail.com> - 3.26-1
- Release 3.26

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 21 2023 Leigh Scott <leigh123linux@gmail.com> - 3.25-1
- Release 3.25

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 04 2023 Leigh Scott <leigh123linux@gmail.com> - 3.24-1
- Release 3.24

* Fri Jan 13 2023 Leigh Scott <leigh123linux@gmail.com> - 3.23-1
- Release 3.23

* Sat Oct 29 2022 Leigh Scott <leigh123linux@gmail.com> - 3.22-1
- Release 3.22

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Mon Jun 27 2022 Leigh Scott <leigh123linux@gmail.com> - 3.21-1
- Release 3.21

* Sun Apr 17 2022 Leigh Scott <leigh123linux@gmail.com> - 3.20-1
- Release 3.20

* Tue Mar 22 2022 Leigh Scott <leigh123linux@gmail.com> - 3.19-1
- Release 3.19

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Mar 21 2021 Leigh Scott <leigh123linux@gmail.com> - 3.18-1
- Release 3.18

* Tue Feb 23 2021 Leigh Scott <leigh123linux@gmail.com> - 3.15-1
- Release 3.15

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 2020 Leigh Scott <leigh123linux@gmail.com> - 3.13-1
- Release 3.13

* Wed Oct 28 2020 Leigh Scott <leigh123linux@gmail.com> - 3.11-1
- Release 3.11

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Aug 08 2020 Leigh Scott <leigh123linux@gmail.com> - 3.10-1
- Release 3.10
- Fix URLs
- Drop autogen build requires

* Wed Apr 22 2020 Leigh Scott <leigh123linux@gmail.com> - 3.9-1
- Release 3.9

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Leigh Scott <leigh123linux@googlemail.com> - 3.7-1
- Release 3.7

* Sun Oct 20 2019 Leigh Scott <leigh123linux@googlemail.com> - 3.5-1
- Release 3.5

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 02 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.3-1
- Release 3.3

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.2-1
- Update to 3.2
- Remove Group tag
- Fix directoy ownership

* Sat Sep 01 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.1-1
- Update to 3.1

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.0-3
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 05 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.0-1
- Update to 3.0

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Leigh Scott <leigh123linux@googlemail.com> - 2.14-1
- Update to 2.14

* Thu Aug 24 2017 Nicolas Chauvet <kwizart@gmail.com> - 2.13-2
- Distribute xt_geoip scripts

* Mon Jul 03 2017 Nicolas Chauvet <kwizart@gmail.com> - 2.13-1
- Update to 2.13

* Tue Mar 21 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 15 2017 Leigh Scott <leigh123linux@googlemail.com> - 2.12-2
- Rebuild for iptables soname bump

* Tue Jan 17 2017 Nicolas Chauvet <kwizart@gmail.com> - 2.12-1
- Update to 2.12

* Thu Sep 08 2016 Sérgio Basto <sergio@serjux.com> - 2.11-2
- Rebuild for iptables soname bump

* Wed Jun 22 2016 Nicolas Chauvet <kwizart@gmail.com> - 2.11-1
- Update to 2.11

* Sun Jan 03 2016 Nicolas Chauvet <kwizart@gmail.com> - 2.10-1
- Update to 2.10

* Sat Oct 24 2015 Nicolas Chauvet <kwizart@gmail.com> - 2.9-1
- Update to 2.9

* Thu Jul 30 2015 Nicolas Chauvet <kwizart@gmail.com> - 2.7-1
- Update to 2.7

* Tue Nov 04 2014 Nicolas Chauvet <kwizart@gmail.com> - 2.6-1
- Update to 2.6
- Drop initscript (use ipset-services instead)
- Spec file clean-up

* Sat Apr 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 2.5-1
- Update to 2.5

* Sun Jan 12 2014 Nicolas Chauvet <kwizart@gmail.com> - 2.4-1
- Update to 2.4

* Tue Jun 18 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.3-1
- Update to 2.3

* Thu Apr 18 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.2-1
- Update to 2.2

* Mon Jan 14 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.1-1
- Update to 2.1

* Thu Oct 18 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.47.1-1
- Update to 1.47.1

* Wed Oct 03 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.46-1
- Update to 1.46

* Tue Jul 31 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.45-1
- Update to 1.45

* Thu Jun 14 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.42-3
- Fix ipset path in F-16 and later

* Tue Jun 05 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.42-2
- Fix for UsrMove - rfbz#2360
- Fix Conflict with ipset - rfbz#2201
- Add Requires ipset >= 6.11 - rfbz#2226

* Thu Apr 12 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.42-1
- Update to 1.42

* Tue Jan 24 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.41-1
- Update to 1.41

* Thu Nov 17 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.39-1
- Update to 1.39

* Wed Oct 27 2010 Chen Lei <supercyper@163.com> - 1.30-1
- update to 1.30

* Sun Jul 25 2010 Chen Lei <supercyper@163.com> - 1.28-1
- update to 1.28

* Mon Jun 28 2010 Chen Lei <supercyper@163.com> - 1.27-2
- rebuild for kernel 2.6.35

* Mon May 31 2010 Chen Lei <supercyper@163.com> - 1.27-1
- update to 1.27

* Sun May 02 2010 Chen Lei <supercyper@163.com> - 1.26-1
- update to 1.26

* Mon Apr 26 2010 Chen Lei <supercyper@163.com> - 1.25-1
- update to 1.25

* Sun Apr 25 2010 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.24-2
- rebuilt

* Thu Mar 18 2010 Chen Lei <supercyper@163.com> - 1.24-1
- initial rpm build
