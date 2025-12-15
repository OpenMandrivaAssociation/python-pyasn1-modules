Name:		python-pyasn1-modules
Version:	0.4.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pyasn1_modules/pyasn1_modules-%{version}.tar.gz
Summary:	A collection of ASN.1-based protocols modules
URL:		https://pypi.org/project/pyasn1-modules/
License:	BSD
Group:		Development/Python
BuildRequires:	python%{pyver}dist(setuptools)
BuildSystem:	python
BuildArch:	noarch

%description
A collection of ASN.1-based protocols modules

%files
%{py_sitedir}/pyasn1_modules
%{py_sitedir}/pyasn1_modules-*.*-info
