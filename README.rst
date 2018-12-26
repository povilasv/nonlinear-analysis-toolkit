===========
Nonlinear analysis toolkit
===========


Requirements
============

Download & install Tisean 3.0.1
-------------------------

Information is provided here:

- http://www.mpipks-dresden.mpg.de/~tisean/archive_3.0.0.html
- http://www.mpipks-dresden.mpg.de/~tisean/Tisean_3.0.1/docs/install.html

Step by step (taken from links above)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    wget http://www.mpipks-dresden.mpg.de/~tisean/TISEAN_3.0.1.tar.gz
    tar -vxf TISEAN_3.0.1.tar.gz

    cd Tisean_3.0.1

    ./configure
    make
    make install

    export PATH=$PATH:/root/bin/

If errors occured (I.E. some programs didn't install) try:

if g77/f77 is not availabe you can install gfortran
and set environment variable FC to be equal to gfortran:

.. code-block:: bash

    export FC=gfortran

Installation
============

.. code-block:: python

    python setup.py install

Test
----

Run tests using:

.. code-block:: python

    python -m unitests

