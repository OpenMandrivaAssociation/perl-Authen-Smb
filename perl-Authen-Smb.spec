%define		upstream_name	 Authen-Smb
%define		upstream_version 0.91

Summary:	Perl extension to authenticate against an SMB server
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	18
License:	GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Authen/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		Authen-Smb-0.91-64bit-fixes.patch
BuildRequires:	perl-devel >= 5.6

%description
Authen::Smb is a Perl module to authenticate against an SMB server.

%prep
%setup -qn %{upstream_name}-%{upstream_version}
%apply_patches

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorarch}/Authen/*
%{perl_vendorarch}/auto/Authen/*
%{_mandir}/man3/*

