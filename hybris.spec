Summary:	Hybris is an outline management software
Summary(pl):	Program do zarz±dzania uk³adem dokumentów
Name:		hybris
Version:	0.5.2
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://hybris.netpedia.net/src/%{name}-%{version}.tar.gz
URL:		http://hybris.netpedia.net/
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Hybris is an outline management software, aiming to become a
structured document editor. It is well modularized, lightweight,
easily portable.

%description -l pl
Hybris to oprogramowanie umo¿liwiaj±ce strukturaln± edycjê dokumentów.
Jest lekkie, modu³owe i mo¿na je ³atwo pzrenosiæ na inne platformy.

%prep
%setup -q

%build
%{__make} OPTS="%{rpmcflags} -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	sysdir=%{_applnkdir}/Office/Misc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Office/Misc/*
