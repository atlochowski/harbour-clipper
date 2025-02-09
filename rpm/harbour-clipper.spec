# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       harbour-clipper

# >> macros
%define __provides_exclude_from ^%{_datadir}/%{name}/lib/.*\\.so\\>
%define __requires_exclude_from ^%{_datadir}/%{name}/lib/.*\\.so\\>
# << macros

Summary:    Videoworks
Version:    0.4.0
Release:    1
Group:      Qt/Qt
License:    GPLv3
URL:        https://github.com/poetater/harbour-clipper
Source0:    %{name}-%{version}.tar.bz2
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   pyotherside-qml-plugin-python3-qt5
%if "%{?vendor}" == "chum"
Requires:   ffmpeg
Requires:   ffmpeg-tools
BuildRequires:  qt5-qttools-linguist
%endif
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  desktop-file-utils

%description
Videoworks is a video editing application. In beta.

%if "%{?vendor}" == "chum"
PackageName: Videoworks
Type: desktop-application
Categories:
 - Video
 - Graphics
DeveloperName: Mark Washeim (poetaster)
Custom:
 - Repo: https://github.com/poetaster/harbour-clipper
Icon: https://github.com/poetaster/harbour-clipper/raw/main/icons/172x172/harbour-clipper.png
Screenshots:
 - https://raw.githubusercontent.com/poetaster/harbour-clipper/main/screen_1.png
 - https://raw.githubusercontent.com/poetaster/harbour-clipper/main/screen_2.png
Url:
  Donation: https://www.paypal.me/poetasterFOSS
%endif

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

# >> files
# << files
