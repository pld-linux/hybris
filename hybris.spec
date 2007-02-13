Summary:	Hybris is an outline management software
Summary(pl.UTF-8):	Program do zarządzania układem dokumentów
Name:		hybris
Version:	0.5.2
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	0dfedaf5f89fa79820b1bf2fa8521af8
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Hybris is an outline management software, aiming to become a
structured document editor. It is well modularized, lightweight,
easily portable.

%description -l pl.UTF-8
Hybris to oprogramowanie umożliwiające strukturalną edycję dokumentów.
Jest lekkie, modułowe i można je łatwo przenosić na inne platformy.

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
