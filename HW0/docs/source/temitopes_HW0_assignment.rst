
Homework 0 Directions
=====================
 


Homework 0 will train us to use organize our code, document it, and use GitHub.

For help on documentation with Sphinx and Read the docs, see:
`this
<https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html>`_.


Step 0
^^^^^^

Install module Sphinx for documentation

.. code-block:: python

	conda install -c conda-forge sphinx

and download or clone the github repository



Step 1 
^^^^^^

Create a new python file that is similar to the following file:

.. code-block:: python

	temitopes_module.py

It should use your name and contain two functions that you've created.
Make 2 different functions and make sure they work!
Give them a descriptive name.
Push your file to Github into the folder:

.. code-block:: python

	code


Step 2
^^^^^^

Modify the Jupiter notebook:

.. code-block:: 

	notebooks/temitopes_HW0_MTH648.ipynb

that is in the folder 'notebooks' so that it
(2a) loads your module (use a line similar to 

.. code-block:: python

	from temitopes_module import *

(2b) then show that your functions work.
Push temitopes_HW0_MTH563.ipynb to Github into the folder

.. code-block:: python

	notebooks

and replace the file that was there (i.e., which you downloaded).


Step 3
^^^^^^

Create a documentation file similar to

.. code-block:: python

	temitopes_documentation.rst

But that uses your name.
Push your file to Github into the folder

.. code-block:: python

	docs

Step 4
^^^^^^

In the file 

.. code-block:: python

	docs/source/temitope_index.html

add a line that names your documentation filename under the line 15, which states

.. code-block:: python

	temitopes_documentation

Then push your file to GitHub, replacing file docs/source/temitope_index.html.



