%define Product Archetypes
%define product archetypes
%define name    zope-%{Product}
%define version 1.5.4
%define release %mkrel 4

%define zope_minver     2.7
%define zope_home       %{_prefix}/lib/zope
%define software_home   %{zope_home}/lib/python

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Developers framework for deploying content types with Zope and Plone
License:    GPL
Group:      System/Servers
URL:        https://plone.org/products/%{product}
Source:     http://plone.org/products/%{product}/releases/1.5/%{version}/%{Product}-%{version}.tar.bz2
Requires:   zope >= %{zope_minver}
Requires:   zope-CMF
Requires:   python2.4-imaging
Requires:   lynx
Requires:   pdftohtml
Requires:   rtf-converter
Provides:   zope-validation = %{version}-%{release}
Provides:   zope-PortalTransforms = %{version}-%{release}
Provides:   zope-MimetypesRegistry = %{version}-%{release}
Provides:   zope-Marshall = %{version}-%{release}
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
A developers framework for rapidly developing and deploying rich, full 
featured content types within the context of Zope/CMF and Plone

%prep
%setup -c -q

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*

