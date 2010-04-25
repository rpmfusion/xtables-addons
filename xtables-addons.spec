Name:		xtables-addons
Summary:	Extensions targets and matches for iptables
Version:	1.24
Release:	2%{?dist}
# The entire source code is GPLv2 except ACCOUNT/libxt_ACCOUNT_cl.c which is LGPLv2
License:	GPLv2 and LGPLv2
Group:		System Environment/Base
URL:		http://xtables-addons.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:	ipset.init
Source2:	ipset-config
# patch to build userspace part only
Patch0:		%{name}-userspace.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	iptables-devel
BuildRequires:	autoconf automake libtool
Provides:	%{name}-kmod-common = %{version}
Requires:	%{name}-kmod >= %{version}
Requires(post): chkconfig
Requires(preun): chkconfig
# This is for /sbin/service
Requires(preun): initscripts
Requires(postun): initscripts

%description
Xtables-addons provides extra modules for iptables not present in the kernel,
and is the successor of patch-o-matic. Extensions includes new targets like 
TEE, TARPIT, CHAOS, or modules like geoip, ipset, and account.

This package provides the userspace libraries for iptables to use extensions 
in the %{name}-kmod package. You must also install the 
%{name}-kmod package.

%package devel
Summary:		Development files for %{name}
Group:			Development/Libraries
Requires:		%{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for 
developing applications that use %{name}. 

%prep
%setup -q 
%patch0 -p1

%build
./autogen.sh
%configure -with-xtlibdir=/%{_lib}/xtables
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

# move ipset to /sbin
install -d %{buildroot}/sbin
mv %{buildroot}/%{_sbindir}/ipset %{buildroot}/sbin

# remove la file(s)
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# install header files
install -d %{buildroot}%{_includedir}
install -pm 0644 extensions/ACCOUNT/*.h %{buildroot}%{_includedir}

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
%doc LICENSE README doc/* 
%attr(0755,root,root) %{_initddir}/*
%config(noreplace) %{_sysconfdir}/sysconfig/*
/%{_lib}/xtables/*.so
%{_libdir}/*.so.*
/sbin/ipset 
%{_sbindir}/*
%{_mandir}/man8/*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_includedir}/*

%changelog
* Sun Apr 25 2010 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.24-2
- rebuilt

* Thu Mar 18 2010 Chen Lei <supercyper@163.com> - 1.24-1
- initial rpm build
