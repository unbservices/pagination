#!/usr/bin/env python
"""
Fixed Width
===========

Pagination navigation that does not grow or shrink depending on what position
the current page.

Example

::

    < *0*  1   2   3   4  ...  8  >
    <  0  *1*  2   3   4  ...  8  >
    <  0   1  *2*  3   4  ...  8  >
    <  0   1   2  *3*  4  ...  8  >
    <  0  ...  3  *4*  5  ...  8  >
    <  0  ...  4  *5*  6   7   8  >
    <  0  ...  4   5  *6*  7   8  >
    <  0  ...  4   5   6  *7*  8  >
    <  0  ...  4   5   6   7  *8* >


"""

# TODO(nick): Allow both 0 and 1 based indexing.
# TODO(nick): Allow an offset? e.g., pages 30-90.

def pagify(page, pages, left_pages=1, right_pages=1, begin_pages=1,
           end_pages=1, include_ellipses=True):
  """Return a list of page segments useful for displaying paginated navigation.

  Args
  ----

  page : int
      The current page.
  pages : int
      The total number of pages.  (Must be >= page.)
  left_pages : int
      The number of pages to show to the left of the current page.
      This is the exact number of pages shown if there are ellipses on both
      sides. However, there may be more pages shown to the left if the current
      page is near the end of the range, and less if the current page is near
      the beginning of the range.
  right_pages : int
      The number of pages to show to the right of the current page.
      This is the exact number of pages shown if there are ellipses on both
      sides.  However, there may be more pages shown to the right if the
      current page is near the beginning of the range, and less if the current
      page is near the end of the range.
  begin_pages : int
      The number of pages to include at the beginning of the pagination list
      (before the ellipses, if they are present).
  end_pages : int
      The number of pages to include at the end of the pagination list (after
      the ellipses, if they are present).

  Example
  -------

  .. testcode::

     from pagination.fixed import pagify, ascii_format

     for i in range(0, 9):
       print pagify(i, 9)

  .. testoutput::

    [[], [], 0, [1, 2, 3, 4], ['...', 8]]
    [[], [0], 1, [2, 3, 4], ['...', 8]]
    [[], [0, 1], 2, [3, 4], ['...', 8]]
    [[], [0, 1, 2], 3, [4], ['...', 8]]
    [[0, '...'], [3], 4, [5], ['...', 8]]
    [[0, '...'], [4], 5, [6, 7, 8], []]
    [[0, '...'], [4, 5], 6, [7, 8], []]
    [[0, '...'], [4, 5, 6], 7, [8], []]
    [[0, '...'], [4, 5, 6, 7], 8, [], []]

  Returns
  -------
  list
      [[start], [left], page, [right], [end]]

  """

  assert page <= pages, ("`page` (%s) cannot be greater than `pages` (%s)." %
                         (page, pages))

  # The minimum number of pages before we need to use ellipses.
  min_pages = (
    (begin_pages + 1) +  # The +1s are here to include the ellipses.
    (end_pages + 1) +
    (left_pages + right_pages + 1)  # The +1 here includes the current page.
  )

  if pages <= min_pages:
    return [[], range(0, page), page, range(page + 1, pages), []]

  no_left_ellipses = page <= ((begin_pages + 1) + left_pages)
  no_right_ellipses = page >= (pages - ((end_pages + 1) + right_pages + 1))

  if no_left_ellipses:
    # Example:  <  0   1   2  *3*  4  ...  8  >
    start = []
    toleft = range(0, page)
    maxright = (begin_pages + 1) + (left_pages + right_pages) + 1
    toright = range(page + 1, maxright)
    end = ['...'] + range(pages - end_pages, pages)

  else:
    start = range(0, begin_pages) + ['...']

    if no_right_ellipses:
      # Example:  <  0  ...  4  *5*  6   7   8  >
      toleft = range(pages - (left_pages + right_pages + end_pages) - 2, page)
      toright = range(page + 1, pages)
      end = []
    else:
      # We're in the center!  Example:  <  0  ...  3  *4*  5  ...  8  >
      toleft = range(page - left_pages, page)
      toright = range(page + 1, page + right_pages + 1)
      end = ['...'] + range(pages - end_pages, pages)

  return [start, toleft, page, toright, end]


def _fmt(i):
  return str(i).rjust(2, ' ').ljust(3, ' ')


def _page_range_to_string(page_range):
  if isinstance(page_range, int):
    return "*%s*" % _fmt(page_range)
  s = ""
  for p in page_range:
    if p == '...':
      s += ' ... '
    else:
      s += " %s " % _fmt(p)
  return s


def ascii_format(pagified):
  """Format the result of pagify as an ASCII string.

  Args
  ----
  pagified : list
      The output of the pagify function.

  Example
  -------

  .. testcode::

     from pagination.fixed import pagify, ascii_format

     for i in range(0, 9):
       print ascii_format(pagify(i, 9))

  .. testoutput::

    < * 0 *  1    2    3    4   ...   8   >
    <   0  * 1 *  2    3    4   ...   8   >
    <   0    1  * 2 *  3    4   ...   8   >
    <   0    1    2  * 3 *  4   ...   8   >
    <   0   ...   3  * 4 *  5   ...   8   >
    <   0   ...   4  * 5 *  6    7    8   >
    <   0   ...   4    5  * 6 *  7    8   >
    <   0   ...   4    5    6  * 7 *  8   >
    <   0   ...   4    5    6    7  * 8 * >

  Returns
  -------
  str
      An ASCII formatted pagination string.
  """
  s = ''.join([_page_range_to_string(s) for s in pagified])
  return '< ' + s + ' >'


if __name__ == '__main__':

  # TODO(nick): The below is primarily for doing a quick visual/manual "test"
  #   of this algorithm.  This would obviously be better if automated.

  print '\n'

  pages = 9
  left = 1
  right = 1
  start = 1
  end = 1
  include_ellipses = True

  # pretty_print = False
  pretty_print = True

  for i in range(0, pages):
    pagified = pagify(page=i,
                      pages=pages,
                      left_pages=left,
                      right_pages=right,
                      begin_pages=start,
                      end_pages=end,
                      include_ellipses=include_ellipses)
    if pretty_print:
      print 'pagify(%s, %s): ' % (_fmt(i), pages), ascii_format(pagified)
    else:
      print 'pagify(%s, %s): ' % (_fmt(i), pages), pagified

  print '\n'
