%?mingw_package_header

%global qt_module qtscript
#%%global pre rc1

#%%global snapshot_date 20121111
#%%global snapshot_rev d1427402

%if 0%{?snapshot_date}
%global source_folder qt-%{qt_module}
%else
%global source_folder %{qt_module}-opensource-src-%{version}%{?pre:-%{pre}}
%endif

# first two digits of version
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-qt5-%{qt_module}
Version:        5.6.0
Release:        2%{?pre:.%{pre}}%{?snapshot_date:.git%{snapshot_date}.%{snapshot_rev}}%{?dist}
Summary:        Qt5 for Windows - QtScript component

License:        GPLv3 with exceptions or LGPLv2 with exceptions
Group:          Development/Libraries
URL:            http://qt-project.org/

%if 0%{?snapshot_date}
# To regenerate:
# wget http://qt.gitorious.org/qt/%{qt_module}/archive-tarball/%{snapshot_rev} -O qt5-%{qt_module}-%{snapshot_rev}.tar.gz
Source0:        qt5-%{qt_module}-%{snapshot_rev}.tar.gz
%else
%if "%{?pre}" != ""
Source0:        http://download.qt-project.org/development_releases/qt/%{release_version}/%{version}-%{pre}/submodules/%{qt_module}-opensource-src-%{version}-%{pre}.tar.xz
%else
Source0:        http://download.qt-project.org/official_releases/qt/%{release_version}/%{version}/submodules/%{qt_module}-opensource-src-%{version}.tar.xz
%endif
%endif

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-qt5-qtbase >= 5.6.0

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-qt5-qtbase >= 5.6.0


%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win32
%package -n mingw32-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtScript component

%description -n mingw32-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win64
%package -n mingw64-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtScript component

%description -n mingw64-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


%?mingw_debug_package


%prep
%setup -q -n %{source_folder}


%build
%mingw_qmake_qt5 ../qtscript.pro
%mingw_make %{?_smp_mflags}


%install
%mingw_make install INSTALL_ROOT=$RPM_BUILD_ROOT

# .prl files aren't interesting for us
find $RPM_BUILD_ROOT -name "*.prl" -delete


# Win32
%files -n mingw32-qt5-%{qt_module}
%{mingw32_bindir}/Qt5Script.dll
%{mingw32_bindir}/Qt5ScriptTools.dll
%{mingw32_includedir}/qt5/QtScript/
%{mingw32_includedir}/qt5/QtScriptTools/
%{mingw32_libdir}/libQt5Script.dll.a
%{mingw32_libdir}/libQt5ScriptTools.dll.a
%{mingw32_libdir}/cmake/Qt5Script/
%{mingw32_libdir}/cmake/Qt5ScriptTools/
%{mingw32_libdir}/pkgconfig/Qt5Script.pc
%{mingw32_libdir}/pkgconfig/Qt5ScriptTools.pc
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_script.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_script_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_scripttools.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_scripttools_private.pri

# Win64
%files -n mingw64-qt5-%{qt_module}
%{mingw64_bindir}/Qt5Script.dll
%{mingw64_bindir}/Qt5ScriptTools.dll
%{mingw64_includedir}/qt5/QtScript/
%{mingw64_includedir}/qt5/QtScriptTools/
%{mingw64_libdir}/libQt5Script.dll.a
%{mingw64_libdir}/libQt5ScriptTools.dll.a
%{mingw64_libdir}/cmake/Qt5Script/
%{mingw64_libdir}/cmake/Qt5ScriptTools/
%{mingw64_libdir}/pkgconfig/Qt5Script.pc
%{mingw64_libdir}/pkgconfig/Qt5ScriptTools.pc
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_script.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_script_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_scripttools.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_scripttools_private.pri


%changelog
* Fri Feb 03 2017 Jajauma's Packages <jajauma@yandex.ru> - 5.6.0-2
- Rebuild with GCC 5.4.0

* Thu Apr  7 2016 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.6.0-1
- Update to 5.6.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 30 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.5.1-1
- Update to 5.5.1

* Fri Aug  7 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.5.0-1
- Update to 5.5.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 22 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4.1-1
- Update to 5.4.1

* Thu Jan  1 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4.0-1
- Update to 5.4.0

* Sat Sep 20 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.3.2-1
- Update to 5.3.2
- Remove unneeded BR: mingw{32,64}-gcc-c++

* Tue Jul  8 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.3.1-1
- Update to 5.3.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.3.0-1
- Update to 5.3.0

* Sun Mar 30 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.1-2
- Make sure we're built against mingw-qt5-qtbase >= 5.2.1 (RHBZ 1077213)

* Sat Feb  8 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.1-1
- Update to 5.2.1

* Sat Jan 11 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-2
- Dropped manual rename of import libraries

* Sun Jan  5 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-1
- Update to 5.2.0

* Fri Nov 29 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-0.1.rc1
- Update to 5.2.0 RC1

* Sat Sep  7 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.1.1-1
- Update to 5.1.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 14 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.1.0-1
- Update to 5.1.0

* Fri May  3 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.2-1
- Update to 5.0.2

* Sat Feb  9 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1

* Thu Jan  3 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-1
- Update to Qt 5.0.0 Final

* Sun Nov 11 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-0.2.beta1.git20121111.d1427402
- Update to 20121111 snapshot (rev d1427402)
- Rebuild against latest mingw-qt5-qtbase
- Dropped pkg-config rename hack as it's unneeded now
- Dropped upstream patch

* Mon Sep 10 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-0.1.beta1
- Initial release

