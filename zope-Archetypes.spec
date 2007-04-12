%define product     Archetypes
%define realVersion 1.4.2-final
%define release     1

%define version %(echo  %{realVersion} | sed -e 's/-/./g')
%define sVersion %(echo %{realVersion} | cut -d- -f1)
%define zope_minver     2.7

%define zope_home       %{_prefix}/lib/zope
%define software_home   %{zope_home}/lib/python

Summary:        Developers framework for deploying content types with Zope and Plone
Name:           zope-%{product}
Version:        %{version}
Release:        %mkrel %{release}
License:        GPL
Group:          System/Servers
Source:         http://plone.org/products/archetypes/releases/%{sVersion}/Archetypes-%{realVersion}-Bundle.tar.bz2
URL:            http://plone.org/products/archetypes/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
Requires:       zope >= %{zope_minver}
Requires:       zope-CMF
Requires:       python-imaging
Requires:       zope-BTreeFolder2
Requires:       lynx
Requires:       pdftohtml
Requires:       rtf-converter

Provides:       zope-validation == %{version}
Provides:       zope-generator == %{version}
Provides:       zope-PortalTransforms == %{version}
Provides:       zope-MimetypesRegistry == %{version}
Obsoletes:      zope-validation, zope-generator, zope-PortalTransforms, zope-MimetypesRegistry

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
%defattr(0644, root, root, 0755)
%{software_home}/Products/*




