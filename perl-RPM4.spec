#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	RPM4
#
Summary:	RPM4 - perl module to access and manipulate RPM files
Summary(pl.UTF-8):	Moduł języka Perl manipulacji i dostępu do plików RPM
Name:		perl-RPM4
Version:	0.23
Release:	0.2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/N/NA/NANARDON/RPM4/RPM4-%{version}.tar.gz
# Source0-md5:	29b408f63d719619ac57930428ad14bb
URL:		http://search.cpan.org/dist/RPM4/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Digest-SHA1
#BuildRequires:	perl(MDV::Packdrakeng)
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# N/A yet
%define		_noautoreq 'perl(MDV::Packdrakeng)'

%description
This module allow to use API functions from rpmlib - a RPM files
manipulation library - directly or trough perl objects.

%description -l pl.UTF-8
Moduł RPM4 pozwala na użycie funkcji API biblioteki manipulacji
plikami RPM rpmlib bezpośrednio lub poprzez obiekty perlowe.

%prep
%setup -q -n %{pdir}-%{version}

# those tests need root or expect MDV::Packdrakeng
mv t/09hdlist.t{,no}
mv t/11media.t{,no}
mv t/04spec.t{,.no}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{_bindir}/hrpmreb
%{_bindir}/rpm_produced
%{_bindir}/rpmresign
%{perl_vendorarch}/RPM4.pm
%dir %{perl_vendorarch}/RPM4
%{perl_vendorarch}/RPM4/Header.pm
%dir %{perl_vendorarch}/RPM4/Header
%{perl_vendorarch}/RPM4/Header/Changelogs.pm
%{perl_vendorarch}/RPM4/Header/Dependencies.pm
%{perl_vendorarch}/RPM4/Header/Files.pm
%{perl_vendorarch}/RPM4/Index.pm
%{perl_vendorarch}/RPM4/Media.pm
%{perl_vendorarch}/RPM4/Sign.pm
%{perl_vendorarch}/RPM4/Spec.pm
%{perl_vendorarch}/RPM4/Transaction.pm
%dir %{perl_vendorarch}/RPM4/Transaction
%{perl_vendorarch}/RPM4/Transaction/Problems.pm
%dir %{perl_vendorarch}/auto/RPM4
%attr(755,root,root) %{perl_vendorarch}/auto/RPM4/RPM4.so
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
