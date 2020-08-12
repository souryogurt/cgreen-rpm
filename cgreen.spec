Name:           cgreen
Version:        1.3.0
Release:        1%{?dist}
Summary:        Modern unit test and mocking framework for C and C++
License:        ISC
URL:            https://github.com/cgreen-devs/%{name}
Source0:        https://github.com/cgreen-devs/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  perl-interpreter
BuildRequires:  asciidoctor

%description
A modern, portable, cross-language unit testing and mocking framework for C
and C++.


%package devel
Summary:        Libraries and headers for developing programs with Cgreen
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Libraries and headers for developing programs with Cgreen.


%package runner
Summary:        A runner for the Cgreen unit testing and mocking framework
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description runner
A runner for the Cgreen unit testing and mocking framework.


%prep
%autosetup

%build
%cmake -DCGREEN_WITH_HTML_DOCS=ON .
%make_build

%install
%make_install

%check
# https://github.com/cgreen-devs/cgreen/issues/226
# https://github.com/cgreen-devs/cgreen/issues/227
# https://github.com/cgreen-devs/cgreen/issues/239
%ifnarch s390x ppc64le
ctest -V %{?_smp_mflags}
%endif

%files
%license LICENSE
%doc README.md
%{_libdir}/libcgreen.so.1*


%files devel
%doc doc/cgreen-guide-en-docinfo.html
%{_libdir}/libcgreen.so
%{_includedir}/cgreen
%{_libdir}/cmake/cgreen


%files runner
%{_bindir}/cgreen-debug
%{_bindir}/cgreen-runner
%{_mandir}/man1/cgreen-runner.1*
%{_mandir}/man1/cgreen-debug.1*
%{_mandir}/man5/cgreen.5*


%changelog
* Fri Jul 17 2020 Egor Artemov <egor.artemov@gmail.com> - 1.3.0-1
- Bump to 1.3.0 version

* Thu May 7 2020 Egor Artemov <egor.artemov@gmail.com> - 1.2.0-1
- Build of 1.2.0 release
