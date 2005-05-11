Summary:	SCED - Scene Designer
Summary(pl):	SCED - projektowanie scen
Name:		sced
Version:	1.03
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.cs.wisc.edu/~schenney/sced/src/%{name}-%{version}.tar.gz
# Source0-md5:	17a468d5b499314b85aee5d8930263e7
Source1:	http://www.cs.wisc.edu/~schenney/sced/src/%{name}-1.0-guide.ps.gz
# Source1-md5:	486ec85d2f617cac047304c115b6d900
URL:		http://www.cs.wisc.edu/~schenney/sced/
BuildRequires:	XFree86-devel
Requires:	povray
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scene designer.

%description -l pl
Program s³u¿±cy do projektowania scen.

%prep
%setup -q
install %{SOURCE1} .

%build
./configure \
	--prefix=%{_prefix} \
	--with-x <<'EOF'
y
/usr/bin/povray

n
n
n
n
y
EOF
%{__make} \
	OTHER_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

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
