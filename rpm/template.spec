Name:           ros-jade-common-tutorials
Version:        0.1.8
Release:        0%{?dist}
Summary:        ROS common_tutorials package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/common_tutorials
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-actionlib-tutorials
Requires:       ros-jade-nodelet-tutorial-math
Requires:       ros-jade-pluginlib-tutorials
Requires:       ros-jade-turtle-actionlib
BuildRequires:  ros-jade-catkin

%description
Metapackage that contains common tutorials

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Wed Dec 31 2014 Daniel Stonier <d.stonier@gmail.com> - 0.1.8-0
- Autogenerated by Bloom

