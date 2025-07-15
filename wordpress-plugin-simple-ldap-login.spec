%define		plugin	simple-ldap-login
Summary:	WordPress plugin to Authenticate WordPress usernames against LDAP
Name:		wordpress-plugin-%{plugin}
Version:	1.4.0.5.1
Release:	1
License:	GPL
Group:		Applications/WWW
Source0:	http://downloads.wordpress.org/plugin/simple-ldap-login.%{version}.zip
# Source0-md5:	c552fbfcd655936a0c6feccfa02643a6
Patch0:		path-adldap.patch
URL:		http://clifgriffin.com/2009/05/13/simple-ldap-login-13-for-wordpress/
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	unzip
Requires:	php-adldap >= 3.3.2
Requires:	webapps
Requires:	webserver(php)
Requires:	wordpress >= 2.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		wp_root		%{_datadir}/wordpress
%define		wp_content	%{wp_root}/wp-content
%define		pluginsdir	%{wp_content}/plugins
%define		plugindir	%{pluginsdir}/%{plugin}

%description
Integrating WordPress with LDAP shouldn't be difficult. Now it isn't.
Simple LDAP Login provides all of the features, none of the hassles.

%prep
%setup -qn %{plugin}
%undos -f php
%patch -P0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
%{__rm} $RPM_BUILD_ROOT%{plugindir}/readme.txt
%{__rm} $RPM_BUILD_ROOT%{plugindir}/adLDAP.php
rm -f $RPM_BUILD_ROOT%{plugindir}/debug*.list

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%dir %{plugindir}
%{plugindir}/Simple-LDAP-Login-Admin.php
%{plugindir}/Simple-LDAP-Login.php
%{plugindir}/screenshot-2.png
