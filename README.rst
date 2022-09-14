Patch antenna
=============


Design Patch Antenna
-------------------

A simple patch antenna design library

.. image:: https://api.travis-ci.com/bhanuchander210/patch_antenna.png


Prerequisite
------------

Python environment

- python=3.10
- Install below packages


.. code-block:: text

    pip install scipy==1.9.0
    pip install gerber_writer==0.3.4



Installation
------------

.. code-block::

    pip install patch_antenna


Design patch antenna
--------------------

To get the design results of a patch antenna use the method `design(freq, er, h)` by passing your
**resonant frequency** (Hz), **dielectric constant** and **thickness of the cavity** (m) values as arguments.


**Getting design parameters**


.. code-block::

    import patch_antenna as pa

    # resonant frequency in Hz
    freq = 2.4 * 10 ** 9

    # dielectric constant
    er = 4.4

    # thickness of the cavity in meter
    h = 1.6 * 10 ** -3

    result = pa.design_string(freq, er, h)
    print(result)


**Output:**

.. code-block::

    {'frequency': 2400000000.0, 'patch_width': 0.0380099749575278, 'patch_length': 0.0294215930843705, 'feeder_width': 0.015203989983011122, 'feeder_length': 0.015449608708025277, 'inset_gap_width': 0.007601994991505561, 'inset_length': 0.010914409094654586, 'ground_length': 0.05447120179239577, 'ground_width': 0.06281396494053892, 'input_edge_impedance': 321.50075290241097}


**Write as Gerber file for both feed types**

- Normal feed
.. code-block::

    pa.write_gerber(freq, er, h, 'patch_design_normal_2.4GHz_4.4_er_1.6_h.gbr', 'normal')


- Inset feed
.. code-block::

    pa.write_gerber(freq, er, h, 'patch_design_inset_2.4GHz_4.4_er_1.6_h.gbr', 'inset')



Customize design results
------------------------

**Using design object**

.. code-block::

    design = pa.design(freq, er, h)
    design.feeder_length *= 1.25
    design.feeder_width *= 1.10

    pa.write_gerber_design(design, 'custom_patch_normal_design.gbr', 'normal')
    pa.write_gerber_design(design, 'custom_patch_inset_design.gbr', 'inset')



Future
------

- Design and gerber generation for patch antenna arrays and including other parameters calculation.


Note
----

Patch antenna design, 3D simulation, and Gerber file facility also published as Web-Live application.

- `Patch antenna util - Web Live Application <https://bhanuchander210.github.io/patch-antenna-util/>`_
- `Patch antenna util - GitHub <https://github.com/Bhanuchander210/patch-antenna-util>`_
- `Blog post <https://bhanuchander210.github.io/Design-A-Rectangular-Patch-Antenna-Using-Python/>`_
