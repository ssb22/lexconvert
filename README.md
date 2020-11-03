# lexconvert
Convert phoneme codes and lexicon formats for English speech synths, from http://ssb22.user.srcf.net/gradint/lexconvert.html
(also mirrored at http://ssb22.gitlab.io/gradint/lexconvert.html just in case)

As a person with limited vision, I often use speech synthesis software to read things. Some uncommon words (such as names and places in literature) are pronounced wrongly by speech synthesizers, but if the synthesizer has a user-controlled pronunciation dictionary (lexicon) then this can be used to correct its pronunciation where necessary. However, if you move to a different speech synthesizer, you may find the lexicon format is different.

This is a Python program that converts between different codes for English phonemes and between lexicon files. It supports quite a few, and there is information in the Python file about how to add your own. It works in both Python 2 and Python 3.

See the web page or run without arguments to see the formats and usage information.
