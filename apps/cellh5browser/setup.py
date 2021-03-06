"""
    The CellH5 Project
    Copyright (c) 2012 - 2013 Christoph Sommer, Michael Held, Bernd Fischer
    Gerlich Lab, IMBA Vienna, Huber Lab, EMBL Heidelberg
    www.cellh5.org

    CellH5 is distributed under the LGPL License.
    See LICENSE.txt for details.
    See AUTHORS.txt for author contributions.
"""

#-------------------------------------------------------------------------------
# standard library imports:
#
from setuptools import setup
import os
import sys
import matplotlib

sys.path.append("C:/Python27/Lib/site-packages/PyQt4")
sys.path.append("C:/Python27/Lib/site-packages/zmq")
sys.path.append("C:/Users/sommerc/cellh5/pysrc")

#-------------------------------------------------------------------------------
# cecog imports:
#


#-------------------------------------------------------------------------------
# constants:
#
MAIN_SCRIPT = 'cellh5browser.py'

APP = [MAIN_SCRIPT]
INCLUDES = ['sip', ]
EXCLUDES = ['PyQt4.QtDesigner', 'PyQt4.QtNetwork',
            'PyQt4.QtOpenGL', 'PyQt4.QtScript',
            'PyQt4.QtSql', 'PyQt4.QtTest',
            'PyQt4.QtWebKit', 'PyQt4.QtXml',
            'PyQt4.phonon', 'zmq'
            ]

PACKAGES = ['h5py', 'vigra', 'matplotlib', 'cellh5']

DLL_EXCLUDES = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'libgdk_pixbuf-2.0-0.dll']


#-------------------------------------------------------------------------------
# functions:
#
def tempsyspath(path):
    def decorate(f):
        def handler():
            sys.path.insert(0, path)
            value = f()
            del sys.path[0]
            return value
        return handler
    return decorate

def read_pkginfo_file(setup_file):
    path = os.path.dirname(setup_file)
    @tempsyspath(path)
    def _import_pkginfo_file():
        if '__pgkinfo__' in sys.modules:
            del sys.modules['__pkginfo__']
        return __import__('__pkginfo__')
    return _import_pkginfo_file()

# -------------------------------------------------------------------------------
# main:

pkginfo = read_pkginfo_file(__file__)

if sys.platform == 'win32':
    import py2exe # pylint: disable-msg=F0401,W0611
    FILENAME_ZIP = 'data.zip'
    OPTIONS = {'windows': [{'script': MAIN_SCRIPT,
                            'icon_resources': \
                               [(1, 'cecog_analyzer_icon_128x128.ico')],
                           }],
               # FIXME: the one-file version is currently not working!
               'zipfile' : FILENAME_ZIP,
               
               }
    SYSTEM = 'py2exe'
    DATA_FILES = matplotlib.get_py2exe_datafiles()
    EXTRA_OPTIONS = {'includes': INCLUDES,
                     'excludes': EXCLUDES,
                     'packages': PACKAGES,
                     'dll_excludes' : DLL_EXCLUDES,
                     'optimize': 2,
                     'compressed': False,
                     'skip_archive': True,
                     'bundle_files': 3}

setup(
    data_files=DATA_FILES,
    options={SYSTEM: EXTRA_OPTIONS},
    includes=[],
    setup_requires=[SYSTEM],
    name=pkginfo.name,
    version=pkginfo.version,
    author=pkginfo.author,
    author_email=pkginfo.author_email,
    license=pkginfo.license,
    description=pkginfo.description,
    long_description=pkginfo.long_description,
    url=pkginfo.url,
    download_url=pkginfo.download_url,
    classifiers=pkginfo.classifiers,
    package_dir=pkginfo.package_dir,
    packages=pkginfo.packages,
    provides=pkginfo.provides,
    **OPTIONS
)
