ztv - astronomical image viewer
===============================

ztv is an astronomical image viewer designed to be used from a python command line for display and analysis. 

ztv is useful as-is for display and simple analysis of images already loaded in to `numpy arrays <http://numpy.org>`_, as well as `FITS files <http://fits.gsfc.nasa.gov/fits_primer.html>`_.  It can display the most recently acquired image by watching a directory for new FITS files to appear or watching a single FITS file for when it changes. It can also receive new images via an `ActiveMQ message stream <http://activemq.apache.org>`_. 

ztv is intended for real-time display and analysis. ztv is not intended to produce publication quality figures. 

ztv comes with a number of built-in control panels, for:
- selecting input source (FITS file, auto-reload from FITS file, etc)
- selecting a frame to subtract (e.g. sky or dark) and a flat field frame to divide by
- setting colormap, stretch, and lower/upper limits
- doing basic slice plots, statistics, and aperture photometry.
Additional panels can be written and added, for e.g. controlling a camera.  (One example add-on panel is included that generates faked images in the FITS format.)

If proper FITS header keywords are available, ztv will display the ra/dec of the cursor point.

Examples of usage
=================

To launch:

    import ztv
    z = ztv.ZTV()

To load an image in a numpy array:

    import numpy as np
    im = np.random.normal(size=[10,256,256])  # create a 3-d image stack
    z.load(im)
    
To manipulate display parameters:

    z.set_cmap('gnuplot')
    z.set_minmax(0.3, 1)
    z.set_xy_center(30,30)
    z.set_zoom(10.)
    
To step through images in stack:
    for i in range(10):
        z.set_frame_number(1, relative=True)
    
To go back to first image:
    z.set_frame_number(0)

Download an iconic FITS image from the web and display it:
    from urllib import urlopen
    from zipfile import ZipFile
    from StringIO import StringIO
    remote_url = 'http://www.spacetelescope.org/static/projects/fits_liberator/datasets/eagle/656nmos.zip'
    local_filename = '/tmp/hst-eagle-nebula-656nmos.fits'
    zip = ZipFile(StringIO(urlopen(remote_url).read()))
    zip_filename = zip.filelist[0].filename
    open(local_filename, 'w').write(zip.open(zip_filename).read())
    z.load(local_filename)
    z.set_scaling('Log')
    z.set_cmap('spectral')
    z.set_minmax(0, 500)

Add-on Control Panel Example
----------------------------

See files in ztv_examples/fits_faker_panel/

    from ztv_examples.fits_faker_panel.launch_ztv import launch_ztv
    z = launch_ztv()

Installation and Dependencies
=============================

ztv uses several packages, including `wxPython <http://wxpython.org>`_, `astropy <http://www.astropy.org>`_.  These should be automatically installed if you install ztv with:

    pip install ztv

Background
==========

In graduate school in the late 1990's I learned to use `IDL <http://en.wikipedia.org/wiki/IDL_(programming_language)>`_ and used `Aaron Barth's ATV <http://www.physics.uci.edu/~barth/atv/>`_ extensively. I even contributed a little to a now-outdated version, adding 3-d image stack capability. ATV was and is incredibly useful for quick-looks at image data, analysis, and all the things you want when working with typical astronomical image data.

After graduate school I began migrating toward python and away from IDL. I've written about this choice elsewhere, but some of the basic reasons were to avoid IDL licensing issues and being beholden to one company.  (To be fair, I pay every year to keep my IDL license current and it's always been a reasonable price for me. It helps that my license has some obscure history to it that makes the maintenance fees moderate. But, at any time they could raise the prices on me massively. And, I wanted to be using a language that could effectively be on every machine I touch, from my main laptop to an embedded server.)

In python there are already a multitude of possible image viewers. Many of which are great and can do much of what I needed. But, inevitably as I've played with them I've found they each don't scratch my itch in some way. I wanted something that worked exactly the way I wanted, with the right (for me) mix of complexity and simplicity.  And, to be able to easily adapt it to a number of situations, including real-time use on a slit-viewing camera, quick-reduction of incoming data, etc.. So, I wrote ztv.

The name "ztv" is an obvious play off of ATV <http://www.physics.uci.edu/~barth/atv/>`_.  And, "z" is my daughter's middle initial. 

Other Image Viewers You Should Check Out
========================================

- If you're using IDL, check out `ATV <http://www.physics.uci.edu/~barth/atv/>`_ of course!
- `SAOImage DS9 <http://ds9.si.edu/site/Home.html>`_
- `Aladin Desktop Sky Atlas <http://aladin.u-strasbg.fr>`_ (not primarily an image viewer, but can open FITS files and overlay catalogs and other images nicely)

(If your favorite isn't on this list, please email hroe@hroe.me to get it added.)

Author
======
Henry Roe (hroe@hroe.me) 

License
=======
ztv is licensed under the MIT License, see ``LICENSE.txt``. Basically, feel free to use any or all of this code in any way. But, no warranties, guarantees, etc etc..