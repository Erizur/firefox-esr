# firefox-esr

[![⚡️ Powered By: Copr](https://img.shields.io/badge/⚡️_Powered_by-COPR-blue?style=flat-square)](https://copr.fedorainfracloud.org/)
![📦 Architecture: x86_64](https://img.shields.io/badge/📦_Architecture-x86__64-blue?style=flat-square)
[![Latest Version](https://img.shields.io/badge/dynamic/json?color=blue&label=Version&query=builds.latest.source_package.version&url=https%3A%2F%2Fcopr.fedorainfracloud.org%2Fapi_3%2Fpackage%3Fownername%3Dthe4runner%26projectname%3Dfirefox-dev%26packagename%3Dfirefox-dev%26with_latest_build%3DTrue&style=flat-square&logo=firefoxbrowser&logoColor=blue)](https://copr.fedorainfracloud.org/coprs/the4runner/firefox-dev/package/firefox-dev/)
[![Copr build status](https://copr.fedorainfracloud.org/coprs/erizur/firefox-esr/package/firefox-esr/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/erizur/firefox-esr/package/firefox-esr/)

An unofficial RPM package of [Firefox ESR](https://www.mozilla.org/en-US/firefox/enterprise) designed for [Fedora](https://getfedora.org).
This repo was based on the original RPM packaging system created by [the4runner](https://github.com/the4runner/firefox-dev/) for the [Firefox Developer Edition](https://www.mozilla.org/en-US/firefox/developer).

## ⚠️ Special Note
This is just an RPM packaging for the said software and does not include any licenses of its own. The only additional file included is the `.desktop` file written based on the original executable from the Firefox Release Channel (default).

## About the Application
Firefox ESR releases are maintained for more than a year, with point releases that coincide with regular Firefox releases. 
These point releases contain security upgrades.

The ESR version will also have a three cycle (at least 12 weeks) overlap between the time of a new release and the end-of-life of the previous release to permit testing and certification before you deploy the new version to your organization.

We rely on Firefox ESR users to provide feedback for each new ESR release. 
During the first two cycles, please report any bugs such as web compatibility regressions and stability issues.

Maintenance of each ESR through point releases is limited to high-risk/high-impact security vulnerabilities, and in rare cases may also include off-schedule releases that address live security vulnerabilities. Backports of any functional enhancements and/or stability fixes are not in scope. 

Bugs related to Firefox Developer Edition should be reported directly to Mozilla: [https://bugzilla.mozilla.org](https://bugzilla.mozilla.org)

Bugs related to this package should be reported at this GitHub project:
[https://github.com/Erizur/firefox-esr/issues](https://github.com/Erizur/firefox-esr/issues)

## Installation Instructions
1. Enable `erizur/firefox-esr` [Copr](https://copr.fedorainfracloud.org/) repository according to your package manager.

```Shell
# If you are using dnf... (you need to have 'dnf-plugins-core' installed)
sudo dnf copr enable erizur/firefox-esr

# If you are using yum... (you need to have 'yum-plugins-copr' installed)
sudo yum copr enable erizur/firefox-esr
```

2. (Optional) Update your package list.

```Shell
sudo dnf check-update
```

3. Execute the following command to install the package.

```Shell
sudo dnf install firefox-esr
```

4. Launch the application from the Application Menu or execute following command in terminal.

```Shell
firefox-esr
```
