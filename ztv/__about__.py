from astropy_helpers.git_helpers import get_git_devstr

__all__ = [
    "__title__", "__summary__", "__uri__", "__version__", "__author__",
    "__email__", "__license__", "__copyright__",
]

__title__ = "ztv"
__summary__ = "Simple python image viewer, largely intended for astronomical applications"
__uri__ = "https://github.com/henryroe/ztv"

# VERSION should be PEP386 compatible (http://www.python.org/dev/peps/pep-0386)
__version__ = "0.1.1.dev"

VERSION = '1.1.dev'

# Indicates if this version is a release version
RELEASE = 'dev' not in VERSION

if not RELEASE:
    VERSION += get_git_devstr(False)

__author__ = "Henry Roe"
__email__ = "hroe@hroe.me"

__license__ = "MIT License"
__copyright__ = "2015 %s" % __author__
