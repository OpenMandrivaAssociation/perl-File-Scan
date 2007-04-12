%define	module	File-Scan
%define	name	perl-%{module}
%define	version	1.43
%define	release	1mdk

Summary:	File::Scan is perl extension for Scanning files for Viruses
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/File-Scan/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires:	perl-devel
Buildarch:	noarch

%description
The File::Scan module is designed to allow users to scan files for known
viruses. Its purpose is to provide a perl module to make platform
independent virus scanners.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc docs/write_sign_bin.txt
%doc examples/*
%doc FAQ README Changes TODO
%dir %{perl_vendorlib}/File
%{perl_vendorlib}/File/*
%{_mandir}/*/*

