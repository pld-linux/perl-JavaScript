#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	JavaScript
Summary:	JavaScript - Execute JavaScript from within Perl
Summary(pl):	JavaScript - Wykonywanie JavaScriptu z Perla
Name:		perl-JavaScript
Version:	0.52
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Acme/CLAESJAC/%{pnam}-%{version}.tar.gz
# Source0-md5:	675eee19cb5269e4dbfde9f64953fab0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	js-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JavaScript.pm is an interface to the SpiderMonkey JS engine. It lets you
execute JS code, call JS functions, bind Perl classes to JS, import Perl
functions to JS, precompile and exeute scripts among many other things.
It does conversion between Perl and JS datatypes.

%description -l pl
JavaScript.pm jest interfejsem do enginu SpiderMonkey JS. Pozwala
wykonywaæ kod JS, wywo³ywaæ funkcje JS, pod³±czaæ klasy Perlowe do JS,
importowaæ funkcje Perla do JS, prekompilowaæ i wykonywaæ skrypty
podobnie jak wiele innych rzeczy. Robi tak¿e konwersjê miêdzy danymi z
Perla do JS.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	INC="%{rpmcflags} -I%{_includedir}/js"
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_vendorarch}/*.pm
%dir %{perl_vendorarch}/auto/%{pnam}
%attr(755,root,root) %{perl_vendorarch}/auto/%{pnam}/*.so
%{perl_vendorarch}/auto/%{pnam}/*.bs
%{perl_vendorarch}/auto/%{pnam}/*.ix
%{_mandir}/man3/*
