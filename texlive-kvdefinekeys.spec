Name:		texlive-kvdefinekeys
Version:	53193
Release:	1
Summary:	Define keys for use in the kvsetkeys package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/kvdefinekeys
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kvdefinekeys.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kvdefinekeys.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kvdefinekeys.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a macro \kv@define@key (analogous to
keyval's \define@key, to define keys for use by kvsetkeys.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/kvdefinekeys
%{_texmfdistdir}/tex/generic/kvdefinekeys
%doc %{_texmfdistdir}/doc/latex/kvdefinekeys

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
