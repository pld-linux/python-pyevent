
%define 	module	pyevent

Summary:	Python extension module for libevent
Summary(pl.UTF-8):	Moduł rozszerzenia Pythona dla biblioteki libevent
Name:		python-%{module}
Version:	0.3
Release:	8
License:	MIT
Group:		Libraries/Python
Source0:	http://pyevent.googlecode.com/files/%{module}-%{version}.tar.gz
# Source0-md5:	584912c92d08bf005283fb29a47a6e4d
Patch0:		%{name}-python25.patch
Patch1:		%{name}-setup.patch
URL:		http://code.google.com/p/pyevent/
BuildRequires:	libevent-devel
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

%build
%{__python} setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{py_sitedir}/event.so
%{py_sitedir}/event-*.egg-info
