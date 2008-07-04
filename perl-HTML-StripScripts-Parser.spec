%define module   HTML-StripScripts-Parser
%define version    1.02
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    XSS filter using HTML::Parser
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/HTML/%{module}-%{version}.tar.gz
BuildRequires: perl(HTML::Parser)
BuildRequires: perl(HTML::StripScripts)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This class provides an easy interface to 'HTML::StripScripts', using
'HTML::Parser' to parse the HTML.

See the HTML::Parser manpage for details of how to customise how the raw
HTML is parsed into tags, and the HTML::StripScripts manpage for details of
how to customise the way those tags are filtered.

%prep
%setup -q -n %{module}-%{version} 

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

