%global             source_name firefox
%global             application_name firefox-esr
%global             full_name firefox-esr
%global             internal_name firefox-esr
%global             debug_package %{nil}

Name:               firefox-esr
Version:            140.4.0esr
Release:            1%{?dist}
Summary:            Firefox ESR Web browser

License:            MPLv1.1 or GPLv2+ or LGPLv2+
URL:                https://www.mozilla.org/en-US/firefox/enterprise/
Source0:            https://download-installer.cdn.mozilla.net/pub/firefox/releases/%{version}/linux-x86_64/en-US/firefox-%{version}.tar.xz
Source1:            %{internal_name}.desktop
Source2:            policies.json
Source3:            %{internal_name}

ExclusiveArch:      x86_64

Recommends:         (plasma-browser-integration if plasma-workspace)
Recommends:         (gnome-browser-connector if gnome-shell)

Requires(post):     gtk-update-icon-cache

%description
Firefox ESR releases are maintained for more than a year, with point releases that coincide with regular Firefox releases. 
These point releases contain security upgrades.

The ESR version will also have a three cycle (at least 12 weeks) overlap between the time of a new release and the end-of-life of the previous release to permit testing and certification before you deploy the new version to your organization.

We rely on Firefox ESR users to provide feedback for each new ESR release. 
During the first two cycles, please report any bugs such as web compatibility regressions and stability issues.

Maintenance of each ESR through point releases is limited to high-risk/high-impact security vulnerabilities, and in rare cases may also include off-schedule releases that address live security vulnerabilities. Backports of any functional enhancements and/or stability fixes are not in scope.

Bugs related to Firefox should be reported directly to Mozilla: 
<https://bugzilla.mozilla.org/>

Bugs related to this package should be reported at this GitHub project:
<https://github.com/erizur/firefox-esr/issues/>

%prep
%setup -q -n %{source_name}

%install
%__rm -rf %{buildroot}

%__install -d %{buildroot}{/opt/%{application_name},%{_bindir},%{_datadir}/applications,%{_datadir}/icons/hicolor/128x128/apps,%{_datadir}/icons/hicolor/64x64/apps,%{_datadir}/icons/hicolor/48x48/apps,%{_datadir}/icons/hicolor/32x32/apps,%{_datadir}/icons/hicolor/16x16/apps}

%__cp -r * %{buildroot}/opt/%{application_name}

%__install -D -m 0644 %{SOURCE1} -t %{buildroot}%{_datadir}/applications

%__install -D -m 0444 %{SOURCE2} -t %{buildroot}/opt/%{application_name}/distribution

%__install -D -m 0755 %{SOURCE3} -t %{buildroot}%{_bindir}

%__ln_s ../../../../../../opt/%{application_name}/browser/chrome/icons/default/default128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{full_name}.png
%__ln_s ../../../../../../opt/%{application_name}/browser/chrome/icons/default/default64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{full_name}.png
%__ln_s ../../../../../../opt/%{application_name}/browser/chrome/icons/default/default48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{full_name}.png
%__ln_s ../../../../../../opt/%{application_name}/browser/chrome/icons/default/default32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{full_name}.png
%__ln_s ../../../../../../opt/%{application_name}/browser/chrome/icons/default/default16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{full_name}.png

%post
gtk-update-icon-cache -f -t %{_datadir}/icons/hicolor

%files
%{_datadir}/applications/%{internal_name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{full_name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{full_name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{full_name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{full_name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{full_name}.png
%{_bindir}/%{internal_name}
/opt/%{application_name}

%changelog
* Sat Sep 23 2023 Namelesswonder <Namelesswonder@users.noreply.github.com> - 118.0b9-3
- firefox-developer-edition.spec: Add weak dependency for each DE browser integration

* Tue Sep 12 2023 Namelesswonder <Namelesswonder@users.noreply.github.com> - 118.0b7-2
- firefox-developer-edition.spec: Trim changelog to resolve date warnings and bump release
