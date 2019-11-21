#!/bin/bash

# I don't yet know how to add to the Apple US lexicon,
# so here is a 'sed' command you can run on your text
# to put the pronunciation inline:

sed -E -e :S \
 -e 's/(^|[^A-Za-z])Shadrach($|[^A-Za-z[12=])/\1[[inpt PHON]]SEY1drAEk[[inpt TEXT]]\2/g' \
 -e 's/(^|[^A-Za-z])Meshach($|[^A-Za-z[12=])/\1[[inpt PHON]]mIY1SAEk[[inpt TEXT]]\2/g' \
 -e 's/(^|[^A-Za-z])Abednego($|[^A-Za-z[12=])/\1[[inpt PHON]]AXbEH1dnIYgOW[[inpt TEXT]]\2/g' \
 -e tS
