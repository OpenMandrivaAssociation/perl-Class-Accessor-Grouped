%define upstream_name Class-Accessor-Grouped
%define upstream_version 0.10013_01

Summary:	Lets you build groups of accessors
Name:		perl-%{upstream_name}
Epoch:		1
Version:	%perl_convert_version %{upstream_version}
Release:	5
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/H/HA/HAARG/Class-Accessor-Grouped-%{upstream_version}.tar.gz
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
%autosetup -n %{upstream_name}-%{upstream_version} -p1
chmod 644 README Changes

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%doc Changes README
%{perl_vendorlib}/Class
%doc %{_mandir}/man3/*
