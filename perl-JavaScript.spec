#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	JavaScript
Summary:	JavaScript - execute JavaScript from within Perl
Summary(pl.UTF-8):	JavaScript - wykonywanie JavaScriptu z Perla
Name:		perl-JavaScript
Version:	0.53
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pnam}/%{pnam}-%{version}.tar.gz
# Source0-md5:	02e009dcfba5645aa1e53c1d4698ffff
BuildRequires:	js-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JavaScript.pm is an interface to the SpiderMonkey JS engine. It lets
you execute JS code, call JS functions, bind Perl classes to JS,
import Perl functions to JS, precompile and exeute scripts among many
other things. It does conversion between Perl and JS datatypes.

%description -l pl.UTF-8
JavaScript.pm jest interfejsem do enginu SpiderMonkey JS. Pozwala
wykonywać kod JS, wywoływać funkcje JS, podłączać klasy perlowe do JS,
importować funkcje Perla do JS, prekompilować i wykonywać skrypty
podobnie jak wiele innych rzeczy. Robi także konwersję między danymi z
Perla do JS.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	INC="-I%{_includedir}/js"
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

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
