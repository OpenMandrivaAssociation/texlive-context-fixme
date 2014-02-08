# revision 23167
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-fixme
# catalog-date 2009-11-09 14:23:31 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-context-fixme
Version:	20091109
Release:	3
Summary:	Make editorial marks on a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-fixme
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-fixme.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-fixme.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-fixme.source.tar.xz
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
%{_texmfdistdir}/tex/context/third/fixme/t-fixme.tex
%doc %{_texmfdistdir}/doc/context/third/fixme/fixme.pdf
#- source
%doc %{_texmfdistdir}/source/context/third/fixme/doc/fixme.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20091109-2
+ Revision: 750494
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20091109-1
+ Revision: 718129
- texlive-context-fixme
- texlive-context-fixme
- texlive-context-fixme
- texlive-context-fixme

