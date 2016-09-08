Name:		xtables-addons
Summary:	Extensions targets and matches for iptables
Version:	2.11
Release:	2%{?dist}
# The entire source code is GPLv2 except ACCOUNT/libxt_ACCOUNT_cl.* which is LGPLv2
License:	GPLv2 and LGPLv2
Group:		System Environment/Base
URL:		http://xtables-addons.sourceforge.net
Source0:	http://dl.sourceforge.net/xtables-addons/Xtables-addons/%{version}/xtables-addons-%{version}.tar.xz
BuildRequires:	iptables-devel >= 1.4.5
BuildRequires:	autoconf automake libtool
Provides:	%{name}-kmod-common = %{version}
Requires:	%{name}-kmod >= %{version}
Requires:	ipset >= 6.11
Obsoletes:	%{name}-devel < 1.27-1

%description
Xtables-addons provides extra modules for iptables not present in the kernel,
and is the successor of patch-o-matic. Extensions includes new targets like 
TEE, TARPIT, CHAOS, or modules like geoip, ipset, and account.

This package provides the userspace libraries for iptables to use extensions 
in the %{name}-kmod package. You must also install the 
%{name}-kmod package.

%prep
%setup -q -n %{name}-%{version}
./autogen.sh
if [ ! -e /%{_lib}/xtables/libxt_CHECKSUM.so ]; then
	sed -i 's/build_CHECKSUM=/build_CHECKSUM=m/' mconfig
fi
if [ ! -e /%{_lib}/xtables/libxt_TEE.so ]; then
	sed -i 's/build_TEE=/build_TEE=m/' mconfig
fi
sed -i 's/build_ipset6=/build_ipset6=m/' mconfig

%build
%configure --without-kbuild

make V=1 %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

# We add xt_geoip database scripts manually
rm -rf %{buildroot}%{_libexecdir}
rm -f geoip/{Makefile*,.gitignore}
chmod 0644 geoip/*

# There is no -devel package. So no need for these files
rm -f %{buildroot}%{_libdir}/*.{la,so}


%files
%doc LICENSE README doc/* geoip
%{_libdir}/xtables/*.so
%{_libdir}/*.so.*
%{_sbindir}/iptaccount
%{_mandir}/man?/*

%changelog
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
