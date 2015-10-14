Pagination
==========

A collection of pagination algorithms.


Example
=======

.. code-block:: python

   from pagination.fixed import pagify, ascii_format

   for i in range(0, 9):
     print ascii_format(pagify(i, 9))

::

   < * 0 *  1    2    3    4   ...   8   >
   <   0  * 1 *  2    3    4   ...   8   >
   <   0    1  * 2 *  3    4   ...   8   >
   <   0    1    2  * 3 *  4   ...   8   >
   <   0   ...   3  * 4 *  5   ...   8   >
   <   0   ...   4  * 5 *  6    7    8   >
   <   0   ...   4    5  * 6 *  7    8   >
   <   0   ...   4    5    6  * 7 *  8   >
   <   0   ...   4    5    6    7  * 8 * >


Documentation
=============

Documentation for Pagination can be found in the ``/docs`` directory.


Issue Reporting and Contact Information
=======================================

If you have any problems with this software, please take a moment to report
them at https://github.com/unbservices/pagination/issues/ or  by email to
nick@unb.services.

If you are a security researcher or believe you have found a security
vulnerability in this software, please contact us by email at
nick@unb.services.


Copyright and License Information
=================================

Copyright (c) 2015 Nick Zarczynski

This project is licensed under the MIT license.  Please see the LICENSE file
for more information.
