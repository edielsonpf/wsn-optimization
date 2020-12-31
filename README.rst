.. -*- mode: rst -*-

|Travis|_ |PyPi|_ |DOI|_ |PythonVersion|_

.. |Travis| image:: https://travis-ci.org/edielsonpf/wsn-toolkit.svg?branch=main
.. _Travis: https://travis-ci.org/edielsonpf/wsn-toolkit

.. |PyPi| image:: https://badge.fury.io/py/wsn-toolkit.svg
.. _PyPi: https://badge.fury.io/py/wsn-toolkit

.. |DOI| image:: https://zenodo.org/badge/319434165.svg
.. _DOI: https://zenodo.org/badge/latestdoi/319434165

.. |PythonVersion| image:: https://img.shields.io/pypi/pyversions/wsn-toolkit.svg
.. _PythonVersion: https://pypi.python.org/pypi/wsn-toolkit
   

.. |PythonMinVersion| replace:: 3.6
.. |NumPyMinVersion| replace:: 1.13.3
.. |MatplotlibMinVersion| replace:: 2.1.1
.. |PytestMinVersion| replace:: 5.0.1

**wsn-toolkit** is a Python module for simulation of Wireless Sensor Networks

Installation
------------

Dependencies
~~~~~~~~~~~~

wsn-toolkit requires:

- Python (>= |PythonMinVersion|)
- NumPy (>= |NumPyMinVersion|)

=======

Some examples require Matplotlib >= |MatplotlibMinVersion|.


User installation
~~~~~~~~~~~~~~~~~

using ``pip``::

    pip install -U wsn-toolkit

or ``conda``::

    conda install -c conda-forge wsn-toolkit


Source code
~~~~~~~~~~~

You can check the latest sources with the command::

    git clone https://github.com/edielsonpf/wsn-toolkit.git


Testing
~~~~~~~

After installation, the test suite can be exeuted from outside the source
directory (you will need to have ``pytest`` >= |PyTestMinVersion| installed)::

    pytest wsntk

