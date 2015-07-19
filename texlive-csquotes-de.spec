# revision 23371
# category Package
# catalog-ctan /info/translations/csquotes/de
# catalog-date 2011-05-30 20:16:57 +0200
# catalog-license lppl
# catalog-version 1.01
Name:		texlive-csquotes-de
Version:	1.01
Release:	10
Summary:	German translation of csquotes documentation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/csquotes/de
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csquotes-de.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csquotes-de.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is a translation of the documentation of csquotes version
5.1.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/csquotes-de/LIESMICH
%doc %{_texmfdistdir}/doc/latex/csquotes-de/csquotes-DE.pdf
%doc %{_texmfdistdir}/doc/latex/csquotes-de/csquotes-DE.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.01-2
+ Revision: 750659
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.01-1
+ Revision: 718174
- texlive-csquotes-de
- texlive-csquotes-de
- texlive-csquotes-de
- texlive-csquotes-de

