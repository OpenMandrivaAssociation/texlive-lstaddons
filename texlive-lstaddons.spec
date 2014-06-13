# revision 26196
# category Package
# catalog-ctan /macros/latex/contrib/lstaddons
# catalog-date 2012-05-03 17:01:13 +0200
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-lstaddons
Version:	0.1
Release:	7
Summary:	Add-on packagvess for listings: autogobble and line background
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lstaddons
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lstaddons.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lstaddons.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lstaddons.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle contains a small collection of add-on packages for
the listings package. Current packages are: [?] lstlinebgrd:
colour the background of some or all lines of a listing; and
[?] lstautogobble: set the standard "gobble" option to the
indent of the first line of the code.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lstaddons/lstautogobble.sty
%{_texmfdistdir}/tex/latex/lstaddons/lstlinebgrd.sty
%doc %{_texmfdistdir}/doc/latex/lstaddons/README
%doc %{_texmfdistdir}/doc/latex/lstaddons/lstautogobble.pdf
%doc %{_texmfdistdir}/doc/latex/lstaddons/lstlinebgrd.pdf
#- source
%doc %{_texmfdistdir}/source/latex/lstaddons/lstaddons.ins
%doc %{_texmfdistdir}/source/latex/lstaddons/lstautogobble.dtx
%doc %{_texmfdistdir}/source/latex/lstaddons/lstlinebgrd.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 813616
- Update to latest release.
- Import texlive-lstaddons
- Import texlive-lstaddons

