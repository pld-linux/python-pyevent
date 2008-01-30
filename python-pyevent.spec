
%define 	module	pyevent

Summary:	Python extension module for libevent
Name:		python-%{module}
Version:	0.3
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	http://pyevent.googlecode.com/files/%{module}-%{version}.tar.gz
# Source0-md5:	584912c92d08bf005283fb29a47a6e4d
Patch0:		%{name}-python25.patch
URL:		http://code.google.com/p/pyevent/
BuildRequires:	libevent-devel
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python extension module for libevent.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{py_sitedir}/event.so
%{py_sitedir}/event-*.egg-info
