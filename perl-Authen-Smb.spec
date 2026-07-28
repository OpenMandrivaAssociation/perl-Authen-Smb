%define		upstream_name	 Authen-Smb
Summary:	Perl extension to authenticate against an SMB server
Name:		perl-%{upstream_name}
Version:	0.91
Release:	25
License:	GPLv2
Group:		Development/Perl
Url:		https://metacpan.org/dist/Authen-Smb
Source0:	https://cpan.metacpan.org/authors/id/P/PM/PMKANE/Authen-Smb-%{version}.tar.gz
Patch0:		Authen-Smb-0.91-64bit-fixes.patch
BuildRequires:	make
BuildRequires:	perl-devel >= 5.6

%description
Authen::Smb is a Perl module to authenticate against an SMB server.

%prep
%setup -qn %{upstream_name}-%{version}
%autopatch -p1

%build
# old XS: clang defaults to -Werror=implicit-function-declaration
export CFLAGS="${CFLAGS:-%{optflags}} -Wno-error=implicit-function-declaration -Wno-implicit-function-declaration"
export CXXFLAGS="${CXXFLAGS:-%{optflags}} -Wno-error=implicit-function-declaration -Wno-implicit-function-declaration"
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

