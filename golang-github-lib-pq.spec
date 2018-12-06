# http://github.com/lib/pq

%global goipath         github.com/lib/pq
%global commit          0dad96c0b94f8dee039aa40467f767467392a0af


%gometa -i

Name:           %{goname}
Version:        0
Release:        0.11%{?dist}
Summary:        Pure Go Postgres driver for database/sql
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: glibc-devel

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
# Needs db running
#%%gochecks -d .

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE.md
%doc README.md CONTRIBUTING.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.git0dad96c
- Upload glide files

* Thu Mar 01 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.9.20150723git0dad96c
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git0dad96c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git0dad96c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git0dad96c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git0dad96c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git0dad96c
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.git0dad96c
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git0dad96c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git0dad96c
- First package for Fedora
  resolves: #1270051
