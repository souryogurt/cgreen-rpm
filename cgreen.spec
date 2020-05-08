%global gittag 1.2.0
Name:           cgreen
Version:        1.2.0
Release:        1%{?dist}
Summary:        Modern unit test and mocking framework for C and C++

License:        ISC
URL:            https://github.com/cgreen-devs/%{name}
Source0:        https://github.com/cgreen-devs/%{name}/archive/%{gittag}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
A modern, portable, cross-language unit testing and mocking framework for C
and C++.

%prep
%autosetup -n %{name}-%{gittag}


%build
%cmake .
%make_build


%install
# Don't put things into /usr/lib/cmake on 64-bit systems
%if "%{?_lib}" == "lib64"
    sed -i -e "s@/lib/cmake/cgreen@/lib64/cmake/cgreen@g" cmake_install.cmake
%endif
%make_install


%files
%license LICENSE
%doc README.md
%{_bindir}/cgreen-debug
%{_bindir}/cgreen-runner
%dir %{_includedir}/cgreen
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

%{_libdir}/libcgreen.so
%{_libdir}/libcgreen.so.1
%{_libdir}/libcgreen.so.1.2.0

%dir %{_libdir}/cmake/cgreen
%{_libdir}/cmake/cgreen/cgreen-config-version.cmake
%{_libdir}/cmake/cgreen/cgreen-config.cmake
%{_mandir}/man1/cgreen-runner.1*
%{_mandir}/man5/cgreen.5*


%changelog
* Thu May 7 2020 Egor Artemov <egor.artemov@gmail.com> - 1.2.0-1
- Build of 1.2.0 release
