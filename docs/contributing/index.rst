Contributing
============


Development Tools
-----------------

Pagination uses
`unb-cli <https://bitbucket.org/unbsolutions/unb-cli>`_ to simplify
and standardize common development and project management tasks.

Unfortunately, `unb-cli <https://bitbucket.org/unbsolutions/unb-cli>`_ is not
(yet) available publically.


How/Where to get the project
----------------------------

Pagination is hosted at https://github.com/unbservices/pagination.

You can clone the repo with the following command.

.. code-block:: console

    git clone git@github.com:unbservices/pagination.git



How to setup a development environment
--------------------------------------

You'll need:

- git
- Python 2.7
- pip
- virtualenv
- unb-cli


How to build the project
------------------------

Build with:

.. code-block:: console

    unb pip build


How to run/use the project from the development environment
-----------------------------------------------------------

Install locally with:

.. code-block:: console

    unb pip install-local



How to run the tests
--------------------

Run the full test suite and linters with:

.. code-block:: console

    unb test


Run only the linter with:

.. code-block:: console

    unb lint


Run only the tests with:

.. code-block:: console

    unb tests


See the ``unb-cli`` documentation for more options/information.


How to submit a patch
---------------------

1) Before you begin development work, create a new branch off master.

.. code-block:: console

    git checkout master
    git checkout -b my-descriptive-branch-name


2) Make changes and commit as you normally would.

3) Push your branch upstream.

.. code-block:: console

    git push --set-upstream origin my-descriptive-branch-name


4) Submit a pull request / review

   **Review early, review often.**

   When you've reached a state where you're ready to share your code, create a
   pull request.  See the documentation at github.com for more
   information.

   Ideally you should create a pull request as soon as you have a reasonably
   coherent implementation.  Sometimes it's helpful to open a pull request when
   all you have is a psudo-code description of the problem and implementation.

   Pull requests, despite the name, shouldn't be seen as a request for a
   maintainer to merge a final, completed patch, but as the beginning of a
   conversation about a change (and possibly the concerns leading up to that
   change).

   Smaller patches are generally better, however, patches which are too small
   are just as hard to reason about as patches which are too big.  The "right
   size" of a patch is highly variable.  As a general rule-of-thumb, if your
   patch addresses one issue, it is probably the right size (regardless of the
   number of lines of code).

   Patches should, ideally, be well documented (in the project's style), and
   contain adequate tests to test any public interface changes or additions.

5) Acceptance or Rejection

   If your patch is accepted it will be merged by a project maintainer.  After
   the merge, you are free to delete your branch.

   Sometimes patches are rejected outright.  Some possible reasons: the patch
   may go against the project's goals, an alternative implementation may have
   been decided on, or the patch author may not be willing to meet the
   submission guidelines of the project.  We welcome your contributions, but
   they must *contribute to*, not *detract from*, the project's goals.

   In either case, you are now free to delete your branch.

.. code-block:: console

    git branch -D my-descriptive-branch-name


6) Release

   Although your contribution was accepted, and merged, that does not guarantee
   that it will be immediately released.  Some patches, like security patches
   and backwards-compatible critical bug fixes, may be released immediately.
   Most patches however, will be scheduled for an upcoming release.

   Depending on when your patch landed in the release cycle, your patch may be
   included in the next or a subsequent release.

   If your patch contains breaking changes, it will most likely be delayed
   until the next *major* release.  That may be a few hours or a few months,
   depending on the project.


For Maintainers
---------------


How to merge patches
~~~~~~~~~~~~~~~~~~~~

After a patch has been through review...

1) Merge master into the branch and resolve any merge conflicts.

.. code-block:: console

    git checkout branch-name-to-be-merged
    git merge master


2) Test the patch by running the test suite and using the package.

.. code-block:: console

    unb test


3) If that process has taken a long time, go to step 1.

4) Merge the patch into master with a squash merge.  Write a descriptive,
   coherent commit message that summarizes the changes.

.. code-block:: console

    git checkout master
    git merge branch-name-to-be-merged --squash
    git commit


5) Push to origin

.. code-block:: console

    git push origin master



Release Process
~~~~~~~~~~~~~~~

This is a generic release process.  If you're reading this, the maintainers
haven't updated it!  Please contact them directly to learn more (and gently
remind them to update this).

Run the entire test suite and run the project itself (whatever that means).  If
there are any quality concerns, address them before proceeding.  From this
point on, we'll assume that this is the code you intend to release (this
generic process does not include a staging step).


1) Build the distribution:

.. code-block:: console

    unb pip build


2) Install the package locally and test that it works!

   If necessary, go back to development and patch any problems, then restart
   from step 1.

.. code-block:: console

    unb pip install-local


3) Bump the version:

.. code-block:: console

    unb version bump


4) Add an appropriate entry to ``/CHANGELOG``.

5) Commit the version bump and the changelog additions.

6) Create a tag for this release:

.. code-block:: console

    git tag -am "vX.X.X"


7) Push your version bump commit and tag.

.. code-block:: console

    git push --follow-tags


8) Upload the package to the package repository.  For PyPI, you can upload to
   the "test" repository (provided it is configured in your ~/pypirc correctly)
   with:

.. code-block:: console

    unb pip upload {version} pypitest


9) Test the distribution.

   Visit the package page on PyPI test and verify the readme looks correct.
   Install the package from PyPI test and verify that it works.  You may want
   to setup a separate test project and virtual environment for this.  If the
   package does not work, repeat from step 1.


10) Upload the package to the real PyPI repository with:

.. code-block:: console

    unb pip upload {version} pypi


11) Test the distribution.

   Visit the package page on PyPI and verify the readme looks correct.
   Install the package from PyPI and verify that it works.  You may want
   to setup a separate test project and virtual environment for this.  If the
   package does not work, repeat from step 1.

.. code-block:: console

    pip install pagination



For reference, your ``~/.pypirc`` file should look something like this:

.. code-block:: cfg

    [distutils]
    index-servers=
        pypitest
        pypi

    [pypitest]
    repository = https://testpypi.python.org/pypi
    username = myusername

    [pypi]
    repository = https://pypi.python.org/pypi
    username = myusername



Docs for the Docs
-----------------

Prose
~~~~~

Some documentation is better kept separate from the code.  For example, project
setup/build/distribution instructions, tutorials, contributing guides, etc.

For this type of documentation we have the RST files in the ``/docs``
directory.


Docstrings
~~~~~~~~~~

Code should be documented inline with docstrings.  Docstrings should follow
the formatting conventions in
`PEP 257 <https://www.python.org/dev/peps/pep-0257/>`_ and either the
`NumPy
<http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_numpy.html#example-numpy>`_
or the
`Google
<http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html>`_
styles.

Docstrings should contain examples!  Those examples should be doctested!


DocTests
~~~~~~~~

Examples in docstrings or in prose should be done in doctest form.  Doctests
ensure that example code in documentation does not break from changes to the
code.  Failing doctests should be considered as serious as failing tests.

Doctests are not a substitute for testing!  They are only meant to ensure that
example code works and will continue to work.

There are a few different styles of doctests to choose from.  Using the
``doctest`` directive is good for simple, self-contained examples that read
clearly in an interpreter prompt.

::

   .. doctest::

      >>> 2 + 2
      4


The ``testcode`` directive is better for declaritive or complex examples.

::

   .. testcode::

      def hello(name='Nick'):
        return "Hello %s." % name

   .. testcode::
      :hide:

      print hello()
      print hello('Fred')

   .. testoutput::
      :hide:

      Hello Nick.
      Hello Fred.

Both examples may be used with ``testsetup`` and ``testcleanup`` directives
(see `the docs <http://sphinx-doc.org/ext/doctest.html>`_ for more examples).

When choosing between the two, you have to think about the documentation
consumer.  When writing prose documentation (like this), it will almost
exclusively be consumed in rendered form (browser, pdf, epub, etc.), so the RST
representation of it doesn't matter as much.

However, when writing examples in docstrings it will be just as likely that the
consumer will be viewing the RST as the rendered output.  Therefore it's
important to keep the RST for docstring examples simple, clean and compact.

One particularly clean method is to combine the approaches above.  For
example, if you wanted to show the definition of the ``hello`` function, but
didn't want to show how to call it in the rendered output, you could write it
like this:

::

   .. testcode::

      def hello(name='Nick'):
        return "Hello %s." % name

   .. doctest::
      :hide:

      >>> print hello()
      Hello Nick.
      >>> print hello('Fred')
      Hello Fred.


Building
~~~~~~~~

Documentation is managed by `Sphinx <http://sphinx-doc.org/>`_.  See "How to
setup a development environment" for installation instructions.

Execute the following command from anywhere in the project directory:

.. code-block:: console

    unb build sphinx

You can then open ``/docs/.build/html/index.html`` in your browser to view the
rendered docs.


Distributing
~~~~~~~~~~~~

If documentation is hosted on `ReadTheDocs <https://readthedocs.org/>`_ it
should be built automatically when a commit is pushed to master at
https://github.com/unbservices/pagination.  (This has to be manually setup).
