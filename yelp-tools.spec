Summary:	Create, manage, and publish documentation for Yelp
Name:		yelp-tools
Version:	3.14.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/yelp-tools/3.14/%{name}-%{version}.tar.xz
# Source0-md5:	c1e82214b07acf6e90e0cdb49e91e01f
URL:		http://projects.gnome.org/yelp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	itstool
BuildRequires:	libxml2-progs
BuildRequires:	yelp-xsl >= 3.14.0
Requires:	libxml2-progs
Requires:	libxslt-progs
Requires:	yelp-xsl >= 3.14.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
yelp-tools is a collection of scripts and build utilities to help
create, manage, and publish documentation for Yelp and the web. Most
of the heavy lifting is done by packages like yelp-xsl and itstool.
This package just wraps things up in a developer-friendly way.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/yelp-build
%attr(755,root,root) %{_bindir}/yelp-check
%attr(755,root,root) %{_bindir}/yelp-new
%{_aclocaldir}/yelp.m4
%{_datadir}/yelp-tools

