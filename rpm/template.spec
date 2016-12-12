Name:           ros-indigo-turtle-actionlib
Version:        0.1.10
Release:        1%{?dist}
Summary:        ROS turtle_actionlib package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/turtle_actionlib
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-angles
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-rosconsole
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-turtlesim
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-angles
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-rosconsole
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-turtlesim

%description
turtle_actionlib demonstrates how to write an action server and client with the
turtlesim. The shape_server provides and action interface for drawing regular
polygons with the turtlesim.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Dec 12 2016 Daniel Stonier <d.stonier@gmail.com> - 0.1.10-1
- Autogenerated by Bloom

* Mon Dec 12 2016 Daniel Stonier <d.stonier@gmail.com> - 0.1.10-0
- Autogenerated by Bloom

* Sun Dec 11 2016 Daniel Stonier <d.stonier@gmail.com> - 0.1.9-0
- Autogenerated by Bloom

* Wed Nov 05 2014 Daniel Stonier <d.stonier@gmail.com> - 0.1.8-0
- Autogenerated by Bloom

