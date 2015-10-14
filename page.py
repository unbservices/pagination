#!/usr/bin/env python
"""
Pagination Algorithms
=====================



Fixed Width
-----------

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


beginPages = 1
endPages = 1

leftPages = 1
rightPages = 1

def pagify(page, pages):
  minPages = (  # 7
    (beginPages + 1) +
    (endPages + 1) +
    (leftPages + rightPages + 1)
  )

  if pages <= minPages:
    # TODO(nick): This needs to conform to whatever return value we have.
    return [range(0, page), page, range(page + 1, pages)]

  noLeftEllipses = page <= ((beginPages + 1) + leftPages)
  noRightEllipses = page >= (pages - ((endPages + 1) + rightPages + 1))

  if noLeftEllipses:
    start = []
    # It has to have right ellipses, or it would be `pages <= minPages`.
    toleft = range(0, page)

  else:
    start = range(0, beginPages) + ['...']
    if noRightEllipses:
      toleft = range(pages - (leftPages + rightPages + endPages) - 2, page)
    else:
      # no special treatment
      toleft = range(page - leftPages, page)

  if noRightEllipses:
    end = []
    toright = range(page + 1, pages)
  else:
    end = ['...'] + range(pages - endPages, pages)
    toright = range(page + 1, page + rightPages + 1)

  return [start, toleft, page, toright, end]


def page_range_to_string(page_range):
  if isinstance(page_range, int):
    return " %s " % page_range
  s = ""
  for p in page_range:
    if p == '...':
      s += p
    else:
      s += " %s " % p
  return s


if __name__ == '__main__':

  print 'Less than minimum width:'
  print 'pagify(4, 7): ', pagify(3, 7)
  print

  for i in range(0, 9):
    # pagified = pagify(i, 9)
    # strings = [page_range_to_string(r) for r in pagified]
    # print 'pagify(%s, 9): %s' % (i, ''.join(strings))
    print 'pagify(%s, 9): %s' % (i, pagify(i, 9))
