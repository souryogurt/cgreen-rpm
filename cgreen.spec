Name:           cgreen
Version:        1.2.0
Release:        1%{?dist}
Summary:        Modern unit test and mocking framework for C and C++
License:        ISC
URL:            https://github.com/cgreen-devs/%{name}
Source0:        https://github.com/cgreen-devs/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# https://github.com/cgreen-devs/cgreen/issues/217
Patch0:         use-variable-for-package-config-installation-path.patch
# https://github.com/cgreen-devs/cgreen/issues/218
Patch1:         add-shebang-for-cgreen-debug-script.patch
# https://github.com/cgreen-devs/cgreen/issues/219
Patch2:         add-cgreen-debug-man-file.patch


BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
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
%autosetup -p0

%build
%cmake -DCGREEN_WITH_HTML_DOCS=ON .
%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libcgreen.so.1*


%files devel
%doc doc/cgreen-guide-en-docinfo.html
%{_libdir}/libcgreen.so
%dir %{_includedir}/cgreen
%dir %{_includedir}/cgreen/internal
%{_includedir}/cgreen/assertions.h
%{_includedir}/cgreen/boxed_double.h
%{_includedir}/cgreen/breadcrumb.h
%{_includedir}/cgreen/cdash_reporter.h
%{_includedir}/cgreen/cgreen.h
%{_includedir}/cgreen/cgreen_value.h
%{_includedir}/cgreen/constraint.h
%{_includedir}/cgreen/constraint_syntax_helpers.h
%{_includedir}/cgreen/cpp_assertions.h
%{_includedir}/cgreen/cpp_constraint.h
%{_includedir}/cgreen/cute_reporter.h
%{_includedir}/cgreen/internal/assertions_internal.h
%{_includedir}/cgreen/internal/c_assertions.h
%{_includedir}/cgreen/internal/cgreen_pipe.h
%{_includedir}/cgreen/internal/cgreen_time.h
%{_includedir}/cgreen/internal/cpp_assertions.h
%{_includedir}/cgreen/internal/function_macro.h
%{_includedir}/cgreen/internal/mocks_internal.h
%{_includedir}/cgreen/internal/mock_table.h
%{_includedir}/cgreen/internal/runner_platform.h
%{_includedir}/cgreen/internal/stringify_token.h
%{_includedir}/cgreen/internal/suite_internal.h
%{_includedir}/cgreen/internal/unit_implementation.h
%{_includedir}/cgreen/legacy.h
%{_includedir}/cgreen/mocks.h
%{_includedir}/cgreen/reporter.h
%{_includedir}/cgreen/runner.h
%{_includedir}/cgreen/string_comparison.h
%{_includedir}/cgreen/suite.h
%{_includedir}/cgreen/text_reporter.h
%{_includedir}/cgreen/unit.h
%{_includedir}/cgreen/vector.h
%dir %{_libdir}/cmake/cgreen
%{_libdir}/cmake/cgreen/cgreen-config-version.cmake
%{_libdir}/cmake/cgreen/cgreen-config.cmake


%files runner
%{_bindir}/cgreen-debug
%{_bindir}/cgreen-runner
%{_mandir}/man1/cgreen-runner.1*
%{_mandir}/man1/cgreen-debug.1*
%{_mandir}/man5/cgreen.5*


%changelog
* Thu May 7 2020 Egor Artemov <egor.artemov@gmail.com> - 1.2.0-1
- Build of 1.2.0 release
