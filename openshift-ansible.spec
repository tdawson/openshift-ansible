# %commit is intended to be set by tito custom builders provided
# in the .tito/lib directory. The values in this spec file will not be kept up to date.
%{!?commit:
%global commit c64d09e528ca433832c6b6e6f5c7734a9cc8ee6f
}

Name:           openshift-ansible
Version:        3.0.2
Release:        1%{?dist}
Summary:        Openshift and Atomic Enterprise Ansible
License:        ASL 2.0
URL:            https://github.com/openshift/openshift-ansible
Source0:        https://github.com/openshift/openshift-ansible/archive/%{commit}/%{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:      ansible

%description
Openshift and Atomic Enterprise Ansible

This repo contains Ansible code and playbooks
for Openshift and Atomic Enterprise.

%prep
%setup -q

%build


%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -rp * %{buildroot}%{_datadir}/%{name}


%files
%{_datadir}/%{name}

%changelog
