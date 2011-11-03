# revision 23371
# category Package
# catalog-ctan /info/translations/csquotes/de
# catalog-date 2011-05-30 20:16:57 +0200
# catalog-license lppl
# catalog-version 1.01
Name:		texlive-csquotes-de
Version:	1.01
Release:	1
Summary:	German translation of csquotes documentation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/csquotes/de
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csquotes-de.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csquotes-de.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is a translation of the documentation of csquotes version
5.1.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/csquotes-de/LIESMICH
%doc %{_texmfdistdir}/doc/latex/csquotes-de/csquotes-DE.pdf
%doc %{_texmfdistdir}/doc/latex/csquotes-de/csquotes-DE.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}