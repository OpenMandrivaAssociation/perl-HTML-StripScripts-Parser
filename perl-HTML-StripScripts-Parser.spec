%define upstream_name    HTML-StripScripts-Parser
%define upstream_version 1.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	XSS filter using HTML::Parser
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl(HTML::StripScripts)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This class provides an easy interface to 'HTML::StripScripts', using
'HTML::Parser' to parse the HTML.

See the HTML::Parser manpage for details of how to customise how the raw
HTML is parsed into tags, and the HTML::StripScripts manpage for details of
how to customise the way those tags are filtered.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/HTML

%changelog
* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-1mdv2010.1
+ Revision: 461288
- update to 1.03

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2010.0
+ Revision: 405858
- rebuild using %%perl_convert_version

* Sat Jul 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2009.0
+ Revision: 231922
- import perl-HTML-StripScripts-Parser


* Sat Jul 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2009.0
- initial mdv release, generated with cpan2dist
