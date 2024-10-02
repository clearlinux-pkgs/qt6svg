#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v20
# autospec commit: f35655a
#
Name     : qt6svg
Version  : 6.7.3
Release  : 51
URL      : https://download.qt.io/official_releases/qt/6.7/6.7.3/submodules/qtsvg-everywhere-src-6.7.3.zip
Source0  : https://download.qt.io/official_releases/qt/6.7/6.7.3/submodules/qtsvg-everywhere-src-6.7.3.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qt6svg-lib = %{version}-%{release}
Requires: qt6svg-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : libxkbcommon-dev
BuildRequires : libxkbfile-dev
BuildRequires : llvm-staticdev
BuildRequires : qt6base-dev
BuildRequires : qtbase-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package dev
Summary: dev components for the qt6svg package.
Group: Development
Requires: qt6svg-lib = %{version}-%{release}
Provides: qt6svg-devel = %{version}-%{release}
Requires: qt6svg = %{version}-%{release}

%description dev
dev components for the qt6svg package.


%package lib
Summary: lib components for the qt6svg package.
Group: Libraries
Requires: qt6svg-license = %{version}-%{release}

%description lib
lib components for the qt6svg package.


%package license
Summary: license components for the qt6svg package.
Group: Default

%description license
license components for the qt6svg package.


%prep
%setup -q -n qtsvg-everywhere-src-6.7.3
cd %{_builddir}/qtsvg-everywhere-src-6.7.3
pushd ..
cp -a qtsvg-everywhere-src-6.7.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1727842314
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1727842314
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6svg
cp %{_builddir}/qtsvg-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6svg/79453f55fa8ee32d7b95581473edcbfd043e088f || :
cp %{_builddir}/qtsvg-everywhere-src-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/qt6svg/dc8f2e570bf431427dbc3bab9d4d551b53a60208 || :
cp %{_builddir}/qtsvg-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6svg/7713a1753ce88f2c7e6b054ecc8e4c786df76300 || :
cp %{_builddir}/qtsvg-everywhere-src-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6svg/c70af14df11e3908dfc10397b1ba4b1f346661f3 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/QtSvg/6.7.3/QtSvg/private/qsvgfilter_p.h
/usr/include/QtSvg/6.7.3/QtSvg/private/qsvgfont_p.h
/usr/include/QtSvg/6.7.3/QtSvg/private/qsvggraphics_p.h
/usr/include/QtSvg/6.7.3/QtSvg/private/qsvghandler_p.h
/usr/include/QtSvg/6.7.3/QtSvg/private/qsvghelper_p.h
/usr/include/QtSvg/6.7.3/QtSvg/private/qsvgnode_p.h
/usr/include/QtSvg/6.7.3/QtSvg/private/qsvgstructure_p.h
/usr/include/QtSvg/6.7.3/QtSvg/private/qsvgstyle_p.h
/usr/include/QtSvg/6.7.3/QtSvg/private/qsvgtinydocument_p.h
/usr/include/QtSvg/6.7.3/QtSvg/private/qsvgvisitor_p.h
/usr/include/QtSvg/6.7.3/QtSvg/private/qtsvgexports_p.h
/usr/include/QtSvg/6.7.3/QtSvg/private/qtsvgglobal_p.h
/usr/include/QtSvg/QSvgGenerator
/usr/include/QtSvg/QSvgRenderer
/usr/include/QtSvg/QtSvg
/usr/include/QtSvg/QtSvgDepends
/usr/include/QtSvg/QtSvgVersion
/usr/include/QtSvg/qsvggenerator.h
/usr/include/QtSvg/qsvgrenderer.h
/usr/include/QtSvg/qtsvgexports.h
/usr/include/QtSvg/qtsvgglobal.h
/usr/include/QtSvg/qtsvgversion.h
/usr/include/QtSvgWidgets/QGraphicsSvgItem
/usr/include/QtSvgWidgets/QSvgWidget
/usr/include/QtSvgWidgets/QtSvgWidgets
/usr/include/QtSvgWidgets/QtSvgWidgetsDepends
/usr/include/QtSvgWidgets/QtSvgWidgetsVersion
/usr/include/QtSvgWidgets/qgraphicssvgitem.h
/usr/include/QtSvgWidgets/qsvgwidget.h
/usr/include/QtSvgWidgets/qtsvgwidgetsexports.h
/usr/include/QtSvgWidgets/qtsvgwidgetsglobal.h
/usr/include/QtSvgWidgets/qtsvgwidgetsversion.h
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/QtSvgTestsConfig.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QSvgIconPluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QSvgIconPluginConfig.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QSvgIconPluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QSvgIconPluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QSvgIconPluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QSvgIconPluginTargets.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QSvgPluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QSvgPluginConfig.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QSvgPluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QSvgPluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QSvgPluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QSvgPluginTargets.cmake
/usr/lib64/cmake/Qt6Svg/Qt6SvgAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Svg/Qt6SvgConfig.cmake
/usr/lib64/cmake/Qt6Svg/Qt6SvgConfigVersion.cmake
/usr/lib64/cmake/Qt6Svg/Qt6SvgConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Svg/Qt6SvgDependencies.cmake
/usr/lib64/cmake/Qt6Svg/Qt6SvgTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Svg/Qt6SvgTargets.cmake
/usr/lib64/cmake/Qt6Svg/Qt6SvgVersionlessTargets.cmake
/usr/lib64/cmake/Qt6SvgWidgets/Qt6SvgWidgetsAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6SvgWidgets/Qt6SvgWidgetsConfig.cmake
/usr/lib64/cmake/Qt6SvgWidgets/Qt6SvgWidgetsConfigVersion.cmake
/usr/lib64/cmake/Qt6SvgWidgets/Qt6SvgWidgetsConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6SvgWidgets/Qt6SvgWidgetsDependencies.cmake
/usr/lib64/cmake/Qt6SvgWidgets/Qt6SvgWidgetsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6SvgWidgets/Qt6SvgWidgetsTargets.cmake
/usr/lib64/cmake/Qt6SvgWidgets/Qt6SvgWidgetsVersionlessTargets.cmake
/usr/lib64/libQt6Svg.prl
/usr/lib64/libQt6Svg.so
/usr/lib64/libQt6SvgWidgets.prl
/usr/lib64/libQt6SvgWidgets.so
/usr/lib64/pkgconfig/Qt6Svg.pc
/usr/lib64/pkgconfig/Qt6SvgWidgets.pc
/usr/lib64/qt6/mkspecs/modules/qt_lib_svg.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_svg_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_svgwidgets.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_svgwidgets_private.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libQt6Svg.so.6.7.3
/V3/usr/lib64/libQt6SvgWidgets.so.6.7.3
/V3/usr/lib64/qt6/plugins/iconengines/libqsvgicon.so
/V3/usr/lib64/qt6/plugins/imageformats/libqsvg.so
/usr/lib64/libQt6Svg.so.6
/usr/lib64/libQt6Svg.so.6.7.3
/usr/lib64/libQt6SvgWidgets.so.6
/usr/lib64/libQt6SvgWidgets.so.6.7.3
/usr/lib64/qt6/metatypes/qt6svg_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6svgwidgets_relwithdebinfo_metatypes.json
/usr/lib64/qt6/modules/Svg.json
/usr/lib64/qt6/modules/SvgWidgets.json
/usr/lib64/qt6/plugins/iconengines/libqsvgicon.so
/usr/lib64/qt6/plugins/imageformats/libqsvg.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6svg/7713a1753ce88f2c7e6b054ecc8e4c786df76300
/usr/share/package-licenses/qt6svg/79453f55fa8ee32d7b95581473edcbfd043e088f
/usr/share/package-licenses/qt6svg/c70af14df11e3908dfc10397b1ba4b1f346661f3
/usr/share/package-licenses/qt6svg/dc8f2e570bf431427dbc3bab9d4d551b53a60208
