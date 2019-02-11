%define debug_package %{nil}

%global gh_user     liamg
%global gh_commit   668e0479141e390ab2bd56088fd7dabd9c14bbfd
%global gh_short    %(c=%{gh_commit}; echo ${c:0:7})

Name:           aminal
Version:        0.9.0
Release:        1%{?dist}
Summary:        Aminal is a modern terminal emulator for Mac/Linux implemented in Golang and utilising OpenGL
Group:          Applications/System
License:        GNU
URL:            https://github.com/liamg/aminal
BuildRequires:  golang libX11-devel libXcursor-devel libXrandr-devel libXinerama-devel mesa-libGL-devel libXi-devel

%description
Features
- Unicode support
- OpenGL rendering
- Customisation options
- True colour support
- Support for common ANSI escape sequences a la xterm
- Scrollback buffer
- Clipboard access
- Clickable URLs
- Multi platform support (Windows coming soon...)
- Sixel support
- Hints/overlays
- Built-in patched fonts for powerline
- Retina display support

%prep
wget https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
tar xzf v%{version}.tar.gz
mkdir -p %{_builddir}/src/github.com/%{gh_user}/
cd %{_builddir}/src/github.com/%{gh_user}/
mv %{_builddir}/%{name}-%{version} %{name}
mkdir -p %{_builddir}/%{name}-%{version}
cd %{name}

%build
export GOPATH="%{_builddir}"
export PATH=$PATH:"%{_builddir}"/bin
go get -u github.com/golang/dep/cmd/dep
go get -u github.com/gobuffalo/packr/packr
cd %{_builddir}/src/github.com/%{gh_user}/%{name}
%{_builddir}/bin/dep ensure
# test:
#go test -v ./...
go vet -v
# build:
mkdir -p bin/linux
GOOS=linux GOARCH=amd64 CGO_ENABLED=1 go build -tags release -ldflags "-X github.com/liamg/aminal/version.Version=%{version} -X main.build=%{gh_short}" -o %{_builddir}/bin/%{name}

%install
install -Dm0755 %{_builddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Wed Feb 6 2019 Jamie Curnow <jc@jc21.com> 0.9.0-1
- updated version

* Tue Jan 29 2019 Jamie Curnow <jc@jc21.com> 0.8.9-1
- updated version

* Fri Jan 25 2019 Jamie Curnow <jc@jc21.com> 0.8.8-1
- updated version

* Fri Jan 18 2019 Jamie Curnow <jc@jc21.com> 0.8.7-1
- updated version

* Tue Jan 15 2019 Jamie Curnow <jc@jc21.com> 0.8.6-1
- updated version

* Fri Jan 11 2019 Jamie Curnow <jc@jc21.com> 0.8.5-1
- updated version

* Thu Jan 10 2019 Jamie Curnow <jc@jc21.com> 0.8.4-1
- updated version

* Tue Jan 8 2019 Jamie Curnow <jc@jc21.com> 0.8.2-1
- updated version

* Mon Jan 7 2019 Jamie Curnow <jc@jc21.com> 0.7.13-1
- updated version

* Tue Dec 11 2018 Jamie Curnow <jc@jc21.com> 0.7.12-1
- updated version

* Wed Dec 5 2018 Jamie Curnow <jc@jc21.com> 0.7.9-1
- updated version

* Mon Dec 3 2018 Jamie Curnow <jc@jc21.com> 0.7.8-1
- updated version

* Fri Nov 30 2018 Jamie Curnow <jc@jc21.com> 0.7.5-1
- Initial Spec

