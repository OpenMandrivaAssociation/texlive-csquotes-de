Name:		texlive-csquotes-de
Version:	23371
Release:	2
Summary:	German translation of csquotes documentation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/translations/csquotes/de
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csquotes-de.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csquotes-de.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
