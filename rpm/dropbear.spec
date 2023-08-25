Summary: Suite providing a simplified version of SSH daemon and client
Name: dropbear
Version: 2022.83
Release: 1
License: FOSS
Source0: https://matt.ucc.asn.au/dropbear/%{name}-%{version}.tar.bz2
#Source1: rpm/udhcpd.service
#Source2: busybox-static.config
#Source3: busybox-sailfish.config
#Source4: set_ps1.sh
#Patch0:  0001-Copy-extended-attributes-if-p-flag-is-provided-to-cp.patch
#Patch1:  0002-applets-Busybox-in-usr-bin-instead-of-bin.patch
#Patch2:  0003-Align-watch-with-what-is-in-procps-ng.patch
#Patch3:  0004-ash-Load-ENV-file-also-if-SSH_CLIENT-SSH2_CLIENT-is-.patch
#Patch4:  0005-ash-job-option-to-restore-term-io-after-job-is-stopp.patch
#Patch5:  0006-ash-Write-history-on-SIGHUP.patch
URL: https://github.com/robang74/redfish-os-dropbear
BuildRequires: glibc-static
BuildRequires: libselinux-static libsepol-static
BuildRequires: pcre-static
BuildRequires: pkgconfig(systemd)
BuildRequires: sed

%define debug_package %{nil}

%description
Dropbear is providing a simplified version of SSH daemon and client

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}

%description doc
Dropbear user guide.

%package static
Summary: Statically linked version of dropbear

%description static
Dropbear is providing a simplified version of SSH daemon and client

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
# TODO: This config should be synced with the dynamic config at some point
# currently the features differ quite a bit
#cp %{SOURCE2} .config
#yes "" | make oldconfig
%make_build

# clean any leftovers from static build
make clean
make distclean

# Build dynamic version
#cp %{SOURCE3} .config

#yes "" | make oldconfig
%make_build
make all

%install
make DESTDIR=%{buildroot} install

%files
%defattr(-,root,root,-)
%license LICENSE
/bin/dropbear
%{_bindir}/dropbear

%files static
%defattr(-,root,root,-)
/bin/dropbear
%{_bindir}/dropbear

%files doc
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}-%{version}