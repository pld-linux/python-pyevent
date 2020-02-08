#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		module	pyevent

Summary:	Python extension module for libevent
Summary(pl.UTF-8):	Moduł rozszerzenia Pythona dla biblioteki libevent
Name:		python-%{module}
Version:	0.3
Release:	13
License:	MIT
Group:		Libraries/Python
Source0:	http://pyevent.googlecode.com/files/%{module}-%{version}.tar.gz
# Source0-md5:	584912c92d08bf005283fb29a47a6e4d
Patch0:		%{name}-python25.patch
Patch1:		%{name}-setup.patch
Patch2:		libevent-2.1.patch
Patch3:		test-path.patch
URL:		http://code.google.com/p/pyevent/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	libevent-devel
BuildRequires:	python-Pyrex
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python extension module for libevent.

%description -l pl.UTF-8
Moduł rozszerzenia Pythona dla biblioteki libevent.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
pyrexc event.pyx
%py_build
%{?with_tests:./test.py}

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{py_sitedir}/event.so
%{py_sitedir}/event-*.egg-info
