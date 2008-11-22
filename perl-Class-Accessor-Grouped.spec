%define module  Class-Accessor-Grouped
%define name    perl-%{module}
%define version 0.08002
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Lets you build groups of accessors
License:        GPL or Artistic
Group:		    Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Class/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
BuildRequires:	perl(Class::Inspector)
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Module::AutoInstall)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Class::C3)
BuildRequires:	perl(Algorithm::C3)
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
This class lets you build groups of accessors that will call different getters
and setters.

%prep
%setup -q -n %{module}-%{version} 
chmod 644 README Changes

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/*/*


