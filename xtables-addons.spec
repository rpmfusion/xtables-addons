Name:		xtables-addons
Summary:	Extensions targets and matches for iptables
Version:	1.42
Release:	2%{?dist}
# The entire source code is GPLv2 except ACCOUNT/libxt_ACCOUNT_cl.* which is LGPLv2
License:	GPLv2 and LGPLv2
Group:		System Environment/Base
URL:		http://xtables-addons.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source1:	ipset.init
Source2:	ipset-config
BuildRequires:	iptables-devel >= 1.4.5
BuildRequires:	autoconf automake libtool
Provides:	%{name}-kmod-common = %{version}
Requires:	%{name}-kmod >= %{version}
Requires(post): chkconfig
Requires(preun): chkconfig
# This is for /sbin/service
Requires(preun): initscripts
Requires(postun): initscripts
Obsoletes:	%{name}-devel < 1.27-1

%description
Xtables-addons provides extra modules for iptables not present in the kernel,
and is the successor of patch-o-matic. Extensions includes new targets like 
TEE, TARPIT, CHAOS, or modules like geoip, ipset, and account.

This package provides the userspace libraries for iptables to use extensions 
in the %{name}-kmod package. You must also install the 
%{name}-kmod package.

%prep
%setup -q
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

# install init scripts and configuration files
install -D -pm 0755 %{SOURCE1} %{buildroot}%{_initddir}/ipset
install -D -pm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/ipset-config

%post 
/sbin/ldconfig
/sbin/chkconfig --add ipset

%preun
if [ $1 = 0 ] ; then
    /sbin/service ipset stop >/dev/null 2>&1
    /sbin/chkconfig --del ipset
fi

%postun
/sbin/ldconfig
if [ "$1" -ge "1" ] ; then
    /sbin/service ipset condrestart >/dev/null 2>&1 || :
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE README doc/* geoip
%attr(0755,root,root) %{_initddir}/*
%config(noreplace) %{_sysconfdir}/sysconfig/*
%{_libdir}/xtables/*.so
%{_libdir}/*.so.*
%{_sbindir}/iptaccount
%{_mandir}/man?/*

%changelog
* Tue Jun 05 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.42-2
- Fix for UsrMove - rfbz#2360

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
