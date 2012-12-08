%define name crack-attack-sounds
%define version 1
%define release %mkrel 12

Summary:	Sound files for crack-attack
Name:		%{name}
Version:	%{version}
Release: 	%{release}
Url:		http://www.miguev.net/misc/
Source0:	%{name}.tar.bz2
Group:		Games/Arcade
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	crack-attack >= 1.1.10-5mdk
BuildArch:	noarch

%description
'Crack Attack!' is a free OpenGL game
based on the Super Nintendo classic Tetris Attack.

This package provides sounds to enhance the gaming experience.
%prep
%setup -q  -n data

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_gamesdatadir}/crack-attack/
cp -a sounds $RPM_BUILD_ROOT%{_gamesdatadir}/crack-attack/sounds

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_gamesdatadir}/crack-attack/sounds



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1-11mdv2011.0
+ Revision: 663423
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 1-10mdv2011.0
+ Revision: 603857
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1-9mdv2010.1
+ Revision: 522419
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1-8mdv2010.0
+ Revision: 413275
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1-7mdv2009.1
+ Revision: 350746
- rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1-6mdv2009.0
+ Revision: 220515
- rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1-5mdv2008.1
+ Revision: 149138
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Apr 25 2007 Adam Williamson <awilliamson@mandriva.org> 1-4mdv2008.0
+ Revision: 18382
- rebuild for new era


* Mon Sep 27 2004 Pascal Terjan <pterjan@mandrake.org> 1-3mdk
- rebuild

* Sun Dec 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1-2mdk
- move stuff to %%{_gamesdatadir}
- rm -rf $RPM_BUILD_ROOT at the beginning of %%install

* Wed Dec 10 2003 Pascal Terjan <CMoi@tuxfamily.org> 1.1.10-5mdk
- first package

