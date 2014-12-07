%define upstream_name    Class-Accessor-Grouped
%define upstream_version 0.10012

Summary:	Lets you build groups of accessors

Name:		perl-%{upstream_name}
Epoch:		1
Version:	%perl_convert_version %{upstream_version}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Algorithm::C3)
BuildRequires:	perl(Class::XSAccessor)
BuildRequires:	perl(Class::C3)
BuildRequires:	perl(Class::Inspector)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(Module::AutoInstall)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Sub::Identify)
BuildRequires:	perl(Sub::Name)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Module::Runtime)

%description
This class lets you build groups of accessors that will call different getters
and setters.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 README Changes

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/man3/*
