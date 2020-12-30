.. LimberDuck documentation master file, created by
   sphinx-quickstart on Mon Dec 28 10:20:42 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

:hide-toc:

about
=====

|stars_from_users|

.. image:: _static/img/LimberDuck-logo.png
   :alt: LimberDuck logo
   :width: 100px
   :align: left
   :target: .

**LimberDuck** (pronounced ˈlɪm.bɚ dʌk) is a project initiated on November 26, 2018. The main 
goal of this project is to create an array of free and Open Source [1]_ tools dedicated 
for Security Engineers who wants to automate their work, decrease their workload and 
focus on data analysis.

Projects
--------

nessus-file-analyzer
++++++++++++++++++++

.. image:: _static/img/LimberDuck-nessus-file-analyzer-logo.png
   :alt: LimberDuck nessus-file-analyzer logo
   :width: 80px
   :align: left
   :target: nessus-file-analyzer

This is a |GUI| tool that allows you to analyze nessus files containing the 
results of scans performed by using *Nessus* or *Tenable.sc* by © Tenable, Inc.
used for |VA| [2]_ process. 

:doc:`read more <nessus-file-analyzer/index>`

----

nessus-file-reader
++++++++++++++++++

.. image:: _static/img/LimberDuck-nessus-file-reader-logo.png
   :alt: LimberDuck nessus-file-reader logo
   :width: 80px
   :align: left
   :target: nessus-file-reader

This is a python module that allows you to quickly parse nessus files 
containing the results of scans performed by using *Nessus* or *Tenable.sc* by © Tenable, Inc.
used for |VA| [2]_ process.

:doc:`read more <nessus-file-reader/index>`

----

converter-csv
++++++++++++++++++++

.. image:: _static/img/LimberDuck-converter-csv-logo.png
   :alt: LimberDuck converter-csv logo
   :width: 80px
   :align: left
   :target: converter-csv

This is a |GUI| tool that allows you to convert multiple large |csv| files to |xlsx| files 
keeping your operational memory usage at a low level.

:doc:`read more <converter-csv/index>`

----

.. |stars_from_users| image:: https://img.shields.io/github/stars/LimberDuck?label=Stars%20from%20users&style=social
    :target: https://github.com/LimberDuck
    :alt: Stars from users 


.. toctree::
   :caption: Projects
   :maxdepth: 1
   :glob:
   :hidden:

   nessus-file-analyzer/index
   nessus-file-reader/index
   converter-csv/index

.. toctree::
   :caption: Other
   :maxdepth: 1
   :glob:
   :hidden:

   glossary/index
   contact/index
   GitHub <https://github.com/limberduck>

.. rubric:: Footnotes

.. [1] read more about :term:`Open Source` in glossary
.. [2] read more about :term:`Vulnerability Assessment` in glossary