Name:		texlive-context-fixme
Version:	20091109
Release:	1
Summary:	Make editorial marks on a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-fixme
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-fixme.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-fixme.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-fixme.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-context
Conflicts:	texlive-texmf <= 20110705-3
Requires(post):	texlive-context.bin

%description
The module will create a variety of marks, and produce
summaries by mark type.

%pre
    %_texmf_mtxrun_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mtxrun_post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_post
	%_texmf_mktexlsr_post
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
