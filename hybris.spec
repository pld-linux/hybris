Summary:	Hybris is an outline management software
Name:		hybris
Version:	0.5.2
Release:	0
License:	GPL
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Source0:	http://hybris.netpedia.net/src/%{name}-%{version}.tar.gz
URL:		http://hybris.netpedia.net/
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libxml-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfigdir	/etc/X11/GNOME

%description
Hybris is an outline management software, aiming to become a structured
document editor. It is well modularized, lightweight, easily portable.

%prep
%setup -q

%build
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	sysdir=%{_applnkdir}/Applications

gzip -9nf ChangeLog AUTHORS NEWS README TODO

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Applications/*
