%global tl_name lstaddons
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Add-on packages for listings: autogobble and line background
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lstaddons
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lstaddons.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lstaddons.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lstaddons.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle contains a small collection of add-on packages for the
listings package. Current packages are: lstlinebgrd: colour the
background of some or all lines of a listing; and lstautogobble: set the
standard "gobble" option to the indent of the first line of the code.

