Apparate Map Creator
====================

Apparate Map Creator will convert an image file a map file for the pathfinding
tool Apparate.

Usage
-----

    $ java ApparateMapCreator [inputfile] [outputfile]

inputfile - the image to be converted
outputfile - map file to be created or replaced

Input images use the following palette:

* White (0xFFFFFF) - Ground
* Green (0x0000FF) - Tree
* Black (0x000000) - Swamp
* Red   (0xFF0000) - Out of bounds

Extras
------

    extras/Apparate-Map-Creator.gpl

Color palette to assist image editing in the GIMP.

Credits
-------

Created by Rhys van der Waerden (rhys.vdw@gmail.com).
