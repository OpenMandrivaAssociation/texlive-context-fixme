# revision 29341
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-fixme
# catalog-date 2013-03-04 16:31:08 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-context-fixme
Version:	20130304
Release:	8
Summary:	Make editorial marks on a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-fixme
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-fixme.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
The module will create a variety of marks, and produce
summaries by mark type.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/fixme/t-fixme.mkii
%{_texmfdistdir}/tex/context/third/fixme/t-fixme.mkiv

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
