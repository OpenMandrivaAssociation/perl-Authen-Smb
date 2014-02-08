%define		upstream_name	 Authen-Smb
%define		upstream_version 0.91

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    10

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.910.0-7mdv2012.0
+ Revision: 765070
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.910.0-6
+ Revision: 763486
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.910.0-5
+ Revision: 667034
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.910.0-4mdv2011.0
+ Revision: 564359
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.910.0-3mdv2011.0
+ Revision: 555668
- rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.910.0-2mdv2011.0
+ Revision: 555664
- rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.910.0-1mdv2010.1
+ Revision: 406845
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.91-11mdv2009.1
+ Revision: 351677
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.91-10mdv2009.0
+ Revision: 223567
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.91-9mdv2008.1
+ Revision: 151474
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Feb 09 2007 Michael Scherer <misc@mandriva.org> 0.91-8mdv2007.0
+ Revision: 118346
- bunzip patch
- rebuilt to get ride of mdk extension

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Authen-Smb

* Tue May 02 2006 Stefan van der Eijk <stefan@eijk.nu> 0.91-7mdk
-_rebuild_for_sparc

* Sat Jun 11 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.91-6mdk
- Rebuild, spec cleanup

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.91-5mdk
- Rebuild for new perl

* Wed Apr 14 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.91-4mdk
- Rebuild for new perl

