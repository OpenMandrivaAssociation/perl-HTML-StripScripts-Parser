%define upstream_name    HTML-StripScripts-Parser
%define upstream_version 1.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    XSS filter using HTML::Parser
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(HTML::Parser)
BuildRequires: perl(HTML::StripScripts)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This class provides an easy interface to 'HTML::StripScripts', using
'HTML::Parser' to parse the HTML.

See the HTML::Parser manpage for details of how to customise how the raw
HTML is parsed into tags, and the HTML::StripScripts manpage for details of
how to customise the way those tags are filtered.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/HTML
