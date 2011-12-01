%define		upstream_name	 Authen-Smb
%define		upstream_version 0.91

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 5

Summary:	Perl extension to authenticate against an SMB server
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Authen/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		Authen-Smb-0.91-64bit-fixes.patch

BuildRequires:	perl-devel >= 5.6
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Authen::Smb is a Perl module to authenticate against an SMB server.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1 -b .64bit-fixes

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Authen/*
%{perl_vendorarch}/auto/Authen/*
%{_mandir}/man3/*
