%{?python_enable_dependency_generator}
%global pypi_name sushy-tools
%global common_desc  A set of tools to support the development and test of the Sushy library

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif

Name:           python-%{pypi_name}
Version:        0.7.0
Release:        1%{?dist}
Summary:        %{common_desc}
License:        ASL 2.0
URL:            https://github.com/openstack/%{pypi_name}
Source0:        https://pypi.io/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if %{with python2}
%package -n python2-%{pypi_name}
Summary:        %{common_desc}
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:    python2-setuptools
BuildRequires:    python2-setuptools_scm
BuildRequires:    python2-devel
BuildRequires:    python2-pytest
BuildRequires:    python2-oslotest
BuildRequires:    python2-libvirt
BuildRequires:    python2-munch
BuildRequires:    python2-pbr >= 2.0.0
BuildRequires:    python2-flask >= 1.0.2
BuildRequires:    python2-requests >= 2.14.2
BuildRequires:    python2-six >= 1.1.0
%if %{undefined __pythondist_requires}
Requires:         python2-pbr >= 2.0.0
Requires:         python2-flask >= 1.0.2
Requires:         python2-requests >= 2.14.2
Requires:         python2-six >= 1.1.0
%endif


%description -n python2-%{pypi_name}
%{common_desc}
%endif

%if %{with python3}
%package -n python3-%{pypi_name}

Summary:          %{common_desc}
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:    python3-setuptools
BuildRequires:    python3-setuptools_scm
BuildRequires:    python3-devel
BuildRequires:    python3-pytest
BuildRequires:    python3-oslotest
BuildRequires:    python3-libvirt
BuildRequires:    python3-munch
BuildRequires:    python3-pbr >= 2.0.0
BuildRequires:    python3-flask >= 1.0.2
BuildRequires:    python3-requests >= 2.14.2
BuildRequires:    python3-six >= 1.1.0
%if %{undefined __pythondist_requires}
Requires:         python3-pbr >= 2.0.0
Requires:         python3-flask >= 1.0.2
Requires:         python3-requests >= 2.14.2
Requires:         python3-six >= 1.9.0
%endif


%description -n python3-%{pypi_name}
This is a set of simple simulation tools aiming at supporting the development
and testing of the Redfish protocol implementations and, in particular, Sushy
library (https://docs.openstack.org/sushy/).

%endif

%description
This is a set of simple simulation tools aiming at supporting the development
and testing of the Redfish protocol implementations and, in particular, Sushy
library (https://docs.openstack.org/sushy/).

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

%install
%if %{with python2}
%py2_install
%endif
%if %{with python3}
%py3_install
%endif

%check
%if %{with python3}
# XXX: fails under python3
pytest-%{python3_version}
%endif
%if %{with python2}
pytest-%{python2_version}
%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/*
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/*
%endif


%changelog
* Tue Nov 5 2019 Christopher Brown <chris.brown@redhat.com> - 0.7.0-1
- initial package release
