%global tl_name csquotes-de
%global tl_revision 79121

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.01
Release:	%{tl_revision}.1
Summary:	German translation of csquotes documentation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/translations/csquotes/de
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/csquotes-de.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/csquotes-de.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a translation of the documentation of csquotes version 5.1.

