%define name crack-attack-sounds
%define version 1
%define release %mkrel 11

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
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_gamesdatadir}/crack-attack/
cp -a sounds %{buildroot}%{_gamesdatadir}/crack-attack/sounds

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_gamesdatadir}/crack-attack/sounds

