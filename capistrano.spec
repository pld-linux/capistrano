#
# Conditional build:
%bcond_with	tests		# build without tests

Summary:	distributed application deployment system
Name:		capistrano
Version:	3.4.0
Release:	0.1
License:	MIT
Group:		Development
Source0:	http://rubygems.org/downloads/%{name}-%{version}.gem
# Source0-md5:	bca5e780742bb8ea95cf6fb0803edf58
URL:		http://capistranorb.com/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	ruby-mocha
BuildRequires:	ruby-rspec
%endif
Requires:	ruby-i18n
Requires:	ruby-rake >= 10.0.0
Requires:	ruby-sshkit < 2
Requires:	ruby-sshkit >= 1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Capistrano is a utility and framework for executing commands in
parallel on multiple remote machines, via SSH.

%prep
%setup -q
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -p %{name}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cap
%attr(755,root,root) %{_bindir}/capify
%{ruby_vendorlibdir}/%{name}.rb
%{ruby_vendorlibdir}/%{name}
%{ruby_vendorlibdir}/Capfile
%{ruby_specdir}/%{name}-%{version}.gemspec
