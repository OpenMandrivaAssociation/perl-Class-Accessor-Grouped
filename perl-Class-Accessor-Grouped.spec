%define upstream_name    Class-Accessor-Grouped
%define upstream_version 0.09000

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Lets you build groups of accessors
License:    GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

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
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}

%description
This class lets you build groups of accessors that will call different getters
and setters.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
