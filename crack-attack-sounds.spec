Summary:	Sound files for crack-attack
Name:		crack-attack-sounds
Version:	1
Release: 	19
Group:		Games/Arcade
License:	GPLv2
Url:		http://www.miguev.net/misc/
Source0:	%{name}.tar.bz2
BuildArch:	noarch
Requires:	crack-attack >= 1.1.10-5mdk

%description
'Crack Attack!' is a free OpenGL game
based on the Super Nintendo classic Tetris Attack.

This package provides sounds to enhance the gaming experience.
%prep
%setup -qn data

%build

%install
mkdir -p %{buildroot}%{_gamesdatadir}/crack-attack/
cp -a sounds %{buildroot}%{_gamesdatadir}/crack-attack/sounds

%files
%{_gamesdatadir}/crack-attack/sounds

