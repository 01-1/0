This repository has miscellaneous files and projects that are too small to warrant their own repository. Here's a table of contents:

# Table of Contents
## ASCIITable.txt
This is an ASCII table in ASCII, with fancy formatting / ASCII art. It is taken from multiple sources. It is also available as [a gist.](https://gist.github.com/01-1/ba989a502bed38c3cfe48832967b358b)
## berlin.py
This python program creates a GeoJSON for https://www.scribblemaps.com/ connecting a selection of Berlins around the world, using the actual shortest straight-line path rather than a straight line path on the Mercator projection. It is adaptable to other selections of points on a globe as well.
## blindcat.bash
"Double" blind audio concatenation tool, shuffling the order of concatenation. Useful to test if you can hear the difference between two similar audio files. Look at the text file produced to check your answers. This is also available as [a gist.](https://gist.github.com/01-1/ce3e30289145d84753422cbbc7dd59b8) 

Usage: `./blindcat.bash input_file_1 input_file_2 output_file`
## m.py
Given a matrix, this predicts the value of missing entries in a particular column using preceding rows, creating another matrix out of these predictions. That is to say, there is a particular "output column" for which for every "split" row, there are a number of rows picked before it (ranging from 24 to the total number of rows before it) such that the rows picked before it are used to predict the value in the output column of the split row from the values of every other column, using linear algebra. This is intentionally obfuscated in order to withhold the purpose of the code.
