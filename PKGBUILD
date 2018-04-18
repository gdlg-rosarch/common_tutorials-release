# Script generated with Bloom
pkgdesc="ROS - Package for Nodelet tutorial."
url='http://www.ros.org/wiki/nodelet_tutorial_math'

pkgname='ros-melodic-nodelet-tutorial-math'
pkgver='0.1.11_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-melodic-catkin'
'ros-melodic-nodelet'
'ros-melodic-roscpp'
'ros-melodic-std-msgs'
)

depends=('ros-melodic-nodelet'
'ros-melodic-roscpp'
'ros-melodic-std-msgs'
)

conflicts=()
replaces=()

_dir=nodelet_tutorial_math
source=()
md5sums=()

prepare() {
    cp -R $startdir/nodelet_tutorial_math $srcdir/nodelet_tutorial_math
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

