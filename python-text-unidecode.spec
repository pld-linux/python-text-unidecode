#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	The most basic Text::Unidecode port
Summary(pl.UTF-8):	Bardzo podstawowy port Text::Unidecode
Name:		python-text-unidecode
Version:	1.3
Release:	3
License:	GPL v1+ or Artistic
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/text-unidecode/
Source0:	https://files.pythonhosted.org/packages/source/t/text-unidecode/text-unidecode-%{version}.tar.gz
# Source0-md5:	53a0a6c5aef8f5eb5834e78e0fdf0499
URL:		https://pypi.org/project/text-unidecode/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
text-unidecode is the most basic port of the Text::Unidecode Perl
library.

%description -l pl.UTF-8
text-unidecode to bardzo podstawowy port biblioteki Perla
Text::Unidecode.

%package -n python3-text-unidecode
Summary:	The most basic Text::Unidecode port
Summary(pl.UTF-8):	Bardzo podstawowy port Text::Unidecode
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-text-unidecode
text-unidecode is the most basic port of the Text::Unidecode Perl
library.

%description -n python3-text-unidecode -l pl.UTF-8
text-unidecode to bardzo podstawowy port biblioteki Perla
Text::Unidecode.

%prep
%setup -q -n text-unidecode-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/src \
%{__python} -m pytest test_unidecode.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest test_unidecode.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/text_unidecode
%{py_sitescriptdir}/text_unidecode-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-text-unidecode
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/text_unidecode
%{py3_sitescriptdir}/text_unidecode-%{version}-py*.egg-info
%endif
