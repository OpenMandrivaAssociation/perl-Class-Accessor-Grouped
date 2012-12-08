%define upstream_name    Class-Accessor-Grouped
%define upstream_version 0.10003

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4
Epoch:		1

Summary:	Lets you build groups of accessors
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Algorithm::C3)
BuildRequires:	perl(Class::XSAccessor)
BuildRequires:	perl(Class::C3)
BuildRequires:	perl(Class::Inspector)
BuildRequires:	perl(Module::AutoInstall)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Sub::Identify)
BuildRequires:	perl(Sub::Name)
BuildRequires:	perl(Test::Exception)
BuildArch:		noarch

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
%{_mandir}/*/*

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1:0.100.30-3mdv2012.0
+ Revision: 765081
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Sun May 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.100.30-1
+ Revision: 672605
- update to new version 0.10003

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Thu Dec 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.100.20-1mdv2011.0
+ Revision: 624077
- update to new version 0.10002

* Tue Dec 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.100.10-1mdv2011.0
+ Revision: 621739
- update to new version 0.10001

* Sun Nov 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.100.0-1mdv2011.0
+ Revision: 602379
- update to new version 0.10000

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.90.90-1mdv2011.0
+ Revision: 601860
- update to new version 0.09009

* Sat Oct 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.90.80-1mdv2011.0
+ Revision: 586097
- new version

* Fri Sep 03 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.90.50-1mdv2011.0
+ Revision: 575588
- update to 0.09005

* Fri Aug 13 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.90.40-1mdv2011.0
+ Revision: 569459
- new version

* Mon Apr 26 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.90.30-1mdv2011.0
+ Revision: 539082
- update to 0.09003

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.90.20-1mdv2010.1
+ Revision: 461728
- update to 0.09002

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.90.0-1mdv2010.0
+ Revision: 420946
- update buildrequires:
- bumping epoch
- update to 0.09000

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.08003-1mdv2010.0
+ Revision: 370017
- update to new version 0.08003

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.08002-1mdv2009.1
+ Revision: 305703
- update to new version 0.08002

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.08001-3mdv2009.0
+ Revision: 255843
- rebuild

* Tue Jan 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.08001-1mdv2008.1
+ Revision: 152970
- update to new version 0.08001
- update to new version 0.08001

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 05 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.07000-1mdv2008.0
+ Revision: 48445
- import perl-Class-Accessor-Grouped


* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.07000-1mdv2008.0
- first mdv package 
