Name     : clear-containers-runtime
Version  : 3.0.2
Release  : 5
URL      : https://github.com/clearcontainers/runtime/archive/3.0.2.tar.gz
Source0  : https://github.com/clearcontainers/runtime/archive/3.0.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause ISC MIT
BuildRequires : go

Patch0001: 678.patch

%description
This repository holds supplemental Go packages for low-level interactions with the operating system.

%prep
%setup -q -n runtime-3.0.2
# fix hangs in Clear Linux
%patch0001 -p1


%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export GOPATH="${PWD}/gopath/"
mkdir -p "${GOPATH}/src/github.com/clearcontainers/"
ln -sf "${PWD}" "${GOPATH}/src/github.com/clearcontainers/runtime"
cd "${GOPATH}/src/github.com/clearcontainers/runtime"
make \
	QEMUCMD=qemu-lite-system-x86_64 \
  PAUSEROOTPATH=/usr/share/lib/clear-containers/runtime/bundles/pause_bundle/ \
	PREFIX=/usr \
	SYSCONFDIR=/etc \
	LOCALSTATEDIR=/var \
	SHAREDIR=/usr/share \
	PROXYURL=unix:///var/run/clear-containers/proxy.sock

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} PREFIX=/usr SYSCONFDIR=/etc LOCALSTATEDIR=/usr/share SHAREDIR=/usr/share SCRIPTS_DIR=%{buildroot}/usr/bin/cc-collect-data.sh


%files
%defattr(-,root,root,-)
/usr/bin/cc-runtime
/usr/bin/cc-collect-data.sh
/usr/share/lib/clear-containers/runtime/bundles/pause_bundle/bin/pause
/usr/share/defaults/clear-containers/configuration.toml
%exclude /usr/share/bash-completion/completions
