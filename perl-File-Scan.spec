%define	upstream_name	 File-Scan
%define	upstream_version 1.43

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl extension for Scanning files for Viruses
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
The File::Scan module is designed to allow users to scan files for known
viruses. Its purpose is to provide a perl module to make platform
independent virus scanners.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make
make test

%install
%makeinstall_std

%files
%doc docs/write_sign_bin.txt
%doc examples/*
%doc FAQ README Changes TODO
%dir %{perl_vendorlib}/File
%{perl_vendorlib}/File/*
%{_mandir}/*/*


%changelog
* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 1.430.0-1mdv2010.0
+ Revision: 409037
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.43-4mdv2009.0
+ Revision: 257008
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.43-2mdv2008.1
+ Revision: 171025
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 1.43-1mdv2008.0
+ Revision: 67614
- use %%mkrel


* Thu Jun 30 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.43-1mdk
- 1.43

* Tue Mar 08 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.42-1mdk
- 1.42

* Wed Jan 05 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.39-1mdk
- 1.39

* Wed Nov 24 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.38-1mdk
- 1.38

* Mon Oct 11 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.32-1mdk
- 1.32

* Mon Aug 23 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.27-1mdk
- 1.27

* Wed Jul 28 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.26-1mdk
- 1.26

* Thu Jul 22 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.25-1mdk
- 1.25

* Mon Jul 12 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.22-1mdk
- 1.22

* Tue Jul 06 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.21-1mdk
- 1.21
- bundle doc and examples in the rpm

* Tue Jun 29 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.19-1mdk
- 1.19

* Sat Jun 19 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.17-1mdk
- 1.17
- drop redundant perl requires

* Wed Jun 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.15-1mdk
- 1.15

* Mon Aug 25 2003 Tibor Pittich <Tibor.Pittich@phuture.sk> 0.63-1mdk
- initial contrib import. this module is needed for amavis-ng.

