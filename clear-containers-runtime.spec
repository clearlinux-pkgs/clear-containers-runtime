#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clear-containers-runtime
Version  : 3.0.23
Release  : 29
URL      : https://github.com/clearcontainers/runtime/archive/3.0.23.tar.gz
Source0  : https://github.com/clearcontainers/runtime/archive/3.0.23.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause ISC MIT WTFPL
Requires: clear-containers-runtime-bin
Requires: clear-containers-runtime-data
BuildRequires : go
Patch1: 0001-add-fake-autogen.patch

%description
[![Build Status](http://cc-jenkins-ci.westus2.cloudapp.azure.com/job/clear-containers-runtime-azure-ubuntu-16-04-master/badge/icon)](http://cc-jenkins-ci.westus2.cloudapp.azure.com/job/clear-containers-runtime-azure-ubuntu-16-04-master/)
[![Build Status](http://cc-jenkins-ci.westus2.cloudapp.azure.com/job/clear-containers-runtime-azure-ubuntu-17-04-master/badge/icon)](http://cc-jenkins-ci.westus2.cloudapp.azure.com/job/clear-containers-runtime-azure-ubuntu-17-04-master/)
[![Build Status](http://cc-jenkins-ci.westus2.cloudapp.azure.com/job/clear-containers-runtime-fedora-26-master/badge/icon)](http://cc-jenkins-ci.westus2.cloudapp.azure.com/job/clear-containers-runtime-fedora-26-master/)
[![Go Report Card](https://goreportcard.com/badge/github.com/clearcontainers/runtime)](https://goreportcard.com/report/github.com/clearcontainers/runtime)
[![Coverage Status](https://coveralls.io/repos/github/clearcontainers/runtime/badge.svg?branch=master)](https://coveralls.io/github/clearcontainers/runtime?branch=master)

%package bin
Summary: bin components for the clear-containers-runtime package.
Group: Binaries
Requires: clear-containers-runtime-data

%description bin
bin components for the clear-containers-runtime package.


%package data
Summary: data components for the clear-containers-runtime package.
Group: Data

%description data
data components for the clear-containers-runtime package.


%prep
%setup -q -n runtime-3.0.23
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522762794
%autogen --disable-static ;export GOPATH="${PWD}/gopath/" \
;mkdir -p "${GOPATH}/src/github.com/clearcontainers/" \
;ln -sf "${PWD}" "${GOPATH}/src/github.com/clearcontainers/runtime" \
;cd "${GOPATH}/src/github.com/clearcontainers/runtime"
make  %{?_smp_mflags} QEMUCMD=qemu-lite-system-x86_64 PAUSEROOTPATH=/usr/share/lib/clear-containers/runtime/bundles/pause_bundle/ PREFIX=/usr SYSCONFDIR=/etc LOCALSTATEDIR=/var SHAREDIR=/usr/share PROXYURL=unix:///var/run/clear-containers/proxy.sock

%install
export SOURCE_DATE_EPOCH=1522762794
rm -rf %{buildroot}
%make_install QEMUCMD=qemu-lite-system-x86_64 PAUSEROOTPATH=/usr/share/lib/clear-containers/runtime/bundles/pause_bundle/ PREFIX=/usr SYSCONFDIR=/etc LOCALSTATEDIR=/var SHAREDIR=/usr/share PROXYURL=unix:///var/run/clear-containers/proxy.sock BASH_COMPLETIONSDIR=%{buildroot}/usr/share/bash-completion/completions/cc-runtime

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cc-collect-data.sh
/usr/bin/cc-runtime

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/cc-runtime
/usr/share/defaults/clear-containers/configuration.toml
