#!/bin/bash

# hints from Curtis:

# 1- all programs start with a standard input stream already open.

# 2- a wrapper program for the editor would listen for keyboard input AND for audio inputs.

# 3- the wrapper program would launch the actual editor program, but first it would replace 
## the editor program's input stream with one that the wrapper program can write to.  
## (look at fork(), pipe(), and exec() system calls).  This is basically what the shell does 
## when you pipe the output of one program to input for another program.

# 4- the wrapper program would pass actual keyboard input directly on to the editor program.

# 5- the wrapper program would process audio, and based on triggers, send keyboard-like input 
## to the editor program.



# run my wrapper program
# configure stuffs?

# exec code .