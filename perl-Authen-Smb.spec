%define		pdir	Authen
%define		module	Authen-Smb
Summary:	Perl extension to authenticate against an SMB server
Name:		perl-%module
Version:	0.91
Release:	%mkrel 10
License:	GPL
Url:		http://search.cpan.org/dist/%module/
Group:		Development/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{module}-%{version}.tar.gz
Patch0:		Authen-Smb-0.91-64bit-fixes.patch
BuildRequires:	perl-devel >= 5.6
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Authen::Smb is a Perl module to authenticate against an SMB server.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1 -b .64bit-fixes

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/%pdir/*
%{perl_vendorarch}/auto/%pdir/*
%{_mandir}/man3/*


