%define		upstream_name	 Authen-Smb
%define		upstream_version 0.91

Summary:	Perl extension to authenticate against an SMB server
Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	23
License:	GPLv2
Group:		Development/Perl
Url:		https://metacpan.org/dist/Authen-Smb
Source0:	https://cpan.metacpan.org/authors/id/P/PM/PMKANE/Authen-Smb-%{upstream_version}.tar.gz
Patch0:		Authen-Smb-0.91-64bit-fixes.patch
BuildRequires:	make
BuildRequires:	perl-devel >= 5.6

%description
Authen::Smb is a Perl module to authenticate against an SMB server.

%prep
%setup -qn %{upstream_name}-%{upstream_version}
%autopatch -p1

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

