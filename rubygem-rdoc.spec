%define rbname rdoc
%define version 3.12.2
%define release 4

Summary: RDoc produces HTML and command-line documentation for Ruby projects
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://docs.seattlerb.org/rdoc
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.7
Requires: rubygems >= 1.8.10

Requires: rubygem-json => 1.4
Requires: rubygem-json < 2
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 1.8.10
Provides: rubygem(rdoc) = %{version}
%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
RDoc produces HTML and command-line documentation for Ruby projects.  RDoc
includes the +rdoc+ and +ri+ tools for generating and displaying online
documentation.
See RDoc for a description of RDoc's markup and basic use.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0} --no-rdoc --no-ri
mkdir -p %{buildroot}/%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{gemdir}/gems/%{rbname}-%{version}/.autotest
%{gemdir}/gems/%{rbname}-%{version}/.document
%doc %{gemdir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{gemdir}/gems/%{rbname}-%{version}/Manifest.txt
%doc %{gemdir}/gems/%{rbname}-%{version}/Rakefile
%{gemdir}/gems/%{rbname}-%{version}/bin/rdoc
%{gemdir}/gems/%{rbname}-%{version}/bin/ri
%{gemdir}/gems/%{rbname}-%{version}/lib/gauntlet_rdoc.rb
%{gemdir}/gems/%{rbname}-%{version}/lib/rdoc.rb
%{gemdir}/gems/%{rbname}-%{version}/lib/rdoc
%{gemdir}/gems/%{rbname}-%{version}/test
%{gemdir}/gems/%{rbname}-%{version}/.gemtest
%{gemdir}/bin/rdoc
%{gemdir}/bin/ri
%{gemdir}/cache/%{rbname}-%{version}.gem
%{gemdir}/specifications/%{rbname}-%{version}.gemspec

%changelog
* Tue Jun 4 2013 Sergey Mihailov <sergey.mihailov@gmail.com> - 3.12.2-4
- Update to version

* Tue May 08 2012 jmontleo@redhat.com - 3.12-2
- Cleaned up spec file

