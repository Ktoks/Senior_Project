# Senior project

## Voice Activated Editor Idea

Based on SABER prototype project from Code Camp.

I would like to see if it is monetizable. This, of course, would be another prototype to further test the software and see if it is feasible on a local machine. Later on, I would re-write it, with further knowledge about the problem, using more informed and advanced solutions.

### Problem

Disabled individuals cannot program without a lot of extra effort on their part, on their assistant's part, or their employer's part. As a healthy and whole programmer, I take these things for granted, but being able to type in the way I do isn't something everyone has.

### Solution

Create an editor/software that provides the tools necissary for a disabled programmer to do their job to the fullest- without being left behind.

Voice-recognition used in any editor to verbally type code __effectively__ would be a great tool for someone without the use of their hands.

### Technical Overview

This software must be fast, reliable, accurate, cost-effective, easy to use, and possibly scalable(for systems with many cores or gpus).

It must be secure- to protect the user.

It must be generally light-weight- runnable on older and portable systems.

It must be flexible- different operating systems, different languages, (spoken and written), different pitches, and different accents.

It must be a layer on top of a single existing editor, soon to work with many editors.

It must have commands mapped to each key on the keyboard that must be pre-learned such as all of the letters of the alphabet, all of the numbers, all of the special characters such as "leftcurly" maps to "{","semi-colon" maps to ";", or "newline" maps to the return key to make a new line.

In order to use shift- the user would say "shift-up" as one command, then the editor would know that the next command spoken would be the only key using shift, going back to not using shift until the shift command is used.

To turn on caps-lock, they would simply say "caps-lock-up" to all-caps or "caps-lock-down" to all-lower-case.

It must provide an easy method to navigate the modes necissary to complete tasks.

To exit any mode at any time and not cause further change to documents or to stop using any mode at any time, the user can just say "escape" to return to null mode which just listens for the master hot-word.

It could be extended with programming language specific commands. For example- "for" mapping to the following structure where the language is c++, and "|" is where the cursor would be after "for" is spoken by the user:
"for (int i = |".

It must provide flexibility when selecting a master hotword, but default to Jarvis, which will be pre-trained for the user to begin using the software upon installation.

### Milestones

1. __Master hotword and null mode:__
The user should be able to say a voice-activating master hot-word to turn the mic on to begin listening such as "Jarvis".
_This can be any word the user chooses that isn't used in regular conversation, but must be thoroughly trained._

2. __Field mode:__
The user speaks into the mic, the editor will type programming language specific text into the field in focus (by default), or it can be configured to run without programming language specific suggestions. This would basically mimic insert mode in Vi, but it could possibly also work with highlighted fields in drop-down menus or fields in browsers elsewhere(advanced-possibly implemented in step 5). Field mode would manually exitable- either when the master hotword then mode hotword are spoken or the escape key is hit- exiting to null mode, (similar to vim), then it would then leave field mode and go to null mode to listen for the master hotword again. The following is an example of how the user would get into field mode from null mode where the master hotword is Jarvis:
_User: "Jarvis field mode"_

3. __Mode hotwords:__
Once listening, the user will be able to choose which mode they want to be in. The user will be able to select from one of the following. (it will not switch modes unless a named mode is spoken followed by the word 'mode' in order for it to enter said mode; otherwise, anything said that doesn't match a mode with accuracy will be discarded).
_The above together are a two-step verification process that protects the user from being overheard in any fashion._

4. __Edit mode:__
The user speaks into the mic, the editor performs commands as if the user is clicking on a line, highlighting text, copying, cutting, pasting, replacing, using multiple columns, searching for a specific string, etc... The following is an example of a typical use of the edit mode where the master hotword is Jarvis, (the semicolons represent possible user pauses), the user moves from field mode to edit mode, then back again:
_User: "Jarvis edit mode; highlight; move down two lines; cut; move up three lines; paste; Jarvis field mode;"_

5. __Training mode:__(Advanced)
The user will enter this mode to train the algorithm to better understand certain words spoken by the user. _The user would then say the word they want to train, the algorithm would make it's best guess at how it is spelled, then ask for confirmation. The user will decide if the algorithm is correct or not. If not, it will as for the user to spell it, then confirm that the spelling on the screen is correct too._

6. __Settings mode:__(Advanced)
The user speaks into the mic, the editor will highlight file, edit, selection, view, etc... tabs on the settings bar of the program. The user can then use some commands to navigate the structure of those tabs and make changes wherever they need. _This mode would be very restricted, only a few basic commands would execute._

7. __Environment mode:__(Advanced)
The user will enter this mode to navigate the operating system to run programs, open terminals, use automated tools, shut down, restart, update, check their email, etc...
