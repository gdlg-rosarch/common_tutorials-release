# Script generated with Bloom
pkgdesc="ROS - turtle_actionlib demonstrates how to write an action server and client with the turtlesim. The shape_server provides and action interface for drawing regular polygons with the turtlesim."
url='http://ros.org/wiki/turtle_actionlib'

pkgname='ros-melodic-turtle-actionlib'
pkgver='0.1.11_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-melodic-actionlib'
'ros-melodic-actionlib-msgs'
'ros-melodic-angles'
'ros-melodic-catkin'
'ros-melodic-geometry-msgs'
'ros-melodic-message-generation'
'ros-melodic-rosconsole'
'ros-melodic-roscpp'
'ros-melodic-std-msgs'
'ros-melodic-turtlesim'
)

depends=('ros-melodic-actionlib'
'ros-melodic-actionlib-msgs'
'ros-melodic-angles'
'ros-melodic-geometry-msgs'
'ros-melodic-message-runtime'
'ros-melodic-rosconsole'
'ros-melodic-roscpp'
'ros-melodic-std-msgs'
'ros-melodic-turtlesim'
)

conflicts=()
replaces=()

_dir=turtle_actionlib
source=()
md5sums=()

prepare() {
    cp -R $startdir/turtle_actionlib $srcdir/turtle_actionlib
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/melodic/setup.bash ] && source /opt/ros/melodic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/melodic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

