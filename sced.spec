Summary:	SCED - Scene Designer
Summary(pl):	SCED - projektowanie scen
Name:		sced
Version:	1.03
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.cs.wisc.edu/~schenney/%{name}/src/%{name}-%{version}.tar.gz
Source1:	http://www.cs.wisc.edu/~schenney/%{name}/src/%{name}-1.0-guide.ps.gz
URL:		http://www.cs.wisc.edu/~schenney/sced/
#Patch0:
BuildRequires:	XFree86-devel
Requires:	povray
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Scene designer.

%description -l pl
Program s�u��cy do projektowania scen.

%prep
%setup -q
install %SOURCE1 .

#%patch

%build
./configure --prefix=%{_prefix} --with-x <<'EOF'
y
/usr/bin/povray

n
n
n
n
y
EOF
%{__make} OTHER_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} mandir=$RPM_BUILD_ROOT%{_mandir} install

install -d $RPM_BUILD_ROOT/etc/skel

install scenerc $RPM_BUILD_ROOT/etc/skel/.scenerc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.ps* docs/guide.tex README*
%attr(644,root,root) /etc/skel/.scenerc
%attr(755,root,root) %{_bindir}/sced
%attr(644,root,root) %{_mandir}/man1/*
