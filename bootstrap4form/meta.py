from packaging.version import Version, parse
from platform import python_version
if Version(python_version()) >= Version('3.10'):
    VERSION = Version('4.0.2')
else:
    from distutils.version import StrictVersion
    VERSION = StrictVersion('4.0.2')
