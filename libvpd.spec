%define name libvpd
%define version 2.2.1

Name:		%{name}
Version:	%{version}
Release:	3%{?dist}
Summary:	VPD Database access library for lsvpd

Group:		System Environment/Libraries
License:	LGPLv2+
URL:		http://linux-diag.sf.net/Lsvpd.html
Source:		http://downloads.sourceforge.net/linux-diag/%{name}-%{version}.tar.gz

Patch1: libvpd-2.1.3-gcc47.patch
Patch2: libvpd-2.2.1-auto-vpdupdate.patch

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	sqlite-devel zlib-devel libstdc++-devel libtool

ExclusiveArch: ppc ppc64

%description
The libvpd package contains the classes that are used to access a vpd database
created by vpdupdate in the lsvpd package.

%package devel
Summary:	Header files for libvpd
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release} sqlite-devel pkgconfig
%description devel
Contains header files for building with libvpd.

%prep
%setup -q

%patch1 -p1 -b .gcc47
%patch2 -p1 -b .avpd

%build
./bootstrap.sh
%configure --disable-static
%{__make} %{?_smp_mflags}

%clean 
%{__rm} -rf $RPM_BUILD_ROOT

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%defattr(-,root,root,-)
%doc COPYING NEWS README TODO AUTHORS
%exclude %{_libdir}/*.la
%{_libdir}/libvpd_cxx-2.2.so.*
%{_libdir}/libvpd-2.2.so.*
%{_sysconfdir}/udev/rules.d/90-vpdupdate.rules
%{_sharedstatedir}/lsvpd/run.vpdupdate

%files devel
%defattr(-,root,root,-)
%exclude %{_libdir}/*.la
%{_includedir}/libvpd-2
%{_libdir}/libvpd_cxx.so
%{_libdir}/libvpd.so
%{_libdir}/pkgconfig/libvpd-2.pc
%{_libdir}/pkgconfig/libvpd_cxx-2.pc

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.2.1-3
- Mass rebuild 2013-12-27

* Wed Nov 06 2013 Filip Kocina <fkocina@redhat.com> - 2.2.2
- Resolves: #1026771 - applied patch to update vpd database automatically

* Sat May 18 2013 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 2.2.1
- Update to latest upstream 2.2.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-5
- Rebuilt for c++ ABI breakage

* Wed Jan 18 2012 Jiri Skala <jskala@redhat.com> 2.1.3-4
- fix for gcc-4.7

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 23 2011 Jiri Skala <jskala@redhat.com> 2.1.3-2
- added ExclusiveArch for ppc[64]

* Wed Aug 10 2011 Jiri Skala <jskala@redhat.com> 2.1.3-1
- update to latest upstream 2.1.3

* Mon Feb 14 2011 Jiri Skala <jskala@redhat.com> 2.1.2-2
- rebuild due to tag correction

* Mon Feb 14 2011 Jiri Skala <jskala@redhat.com> 2.1.2-1
- Update to latest upstream 2.1.2
- fixes library numbering

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 02 2009 Eric Munson <ebmunson@us.ibm.com> - 2.1.1-1
- Update to latest libvpd release

* Wed Nov 18 2009 Eric Munson <ebmunson@us.ibm.com> - 2.1.0-5
- Bump dist for rebuild for broken dependencies

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 16 2009 Eric Munson <ebmunson@us.ibm.com> 2.1.0-3
- Bump dist for rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Mar 17 2008 Eric Munson <ebmunson@us.ibm.com> 2.0.1-1
- Update for libvpd-2.0.1

* Tue Feb 26 2008 Eric Munson <ebmunson@us.ibm.com> 2.0.0-2
- Updating release number for new build in FC

* Mon Feb 25 2008 Eric Munson <ebmunson@us.ibm.com> 2.0.0-1
- Updated library to use sqlite instead of berkeley db.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5.0-2
- Autorebuild for GCC 4.3

* Mon Jan 7 2008 Eric Munson <ebmunson@us.ibm.com> -1.5.0-1
- Moved pkgconfig to devel Requires
- Updated %%defattrs to -,root,root,-
- Added AUTHORS to %%doc

* Thu Jan 3 2008 Eric Munson <ebmunson@us.ibm.com> - 1.5.0-0
- Updated Requires and Provides fields per fedora community request

* Fri Dec 7 2007 Brad Peters <bpeters@us.ibm.com> - 1.4.2-0
- Added functions to helper_functions class
- Mnior changes necessary to support new device discovery method

* Fri Nov 16 2007 Eric Munson <ebmunson@us.ibm.com> - 1.4.1-1
- Removing INSTALL from docs and docs from -devel package
- Fixing Makfile.am so libraries have the .so extension
- Using %%configure, %%{__make}, and %%{__rm} calls
- Changing source URL

* Wed Oct 31 2007 Eric Munson <ebmunson@us.ibm.com> - 1.4.0-2
- Changing files lists for libdirs to match library file names

* Tue Oct 30 2007 Eric Munson <ebmunson@us.ibm.com> - 1.4.0-1
- Adding C Library to files lists.

* Sat Oct 20 2007 Ralf Corsepius <rc040203@freenet.de>	- 1.3.5-4
- Various spec-file fixes.

* Fri Oct 19 2007 Eric Munson <ebmunson@us.ibm.com> - 1.3.5-3
- Removed hard coded /usr/lib from spec file
- Install now sets all headers to 644
- Updated license
