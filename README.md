# lexconvert
Convert phoneme codes and lexicon formats for English speech synths, from http://ssb22.user.srcf.net/gradint/lexconvert.html
(also mirrored at http://ssb22.gitlab.io/gradint/lexconvert.html just in case)

As a person with limited vision, I often use speech synthesis software to read things. Some uncommon words (such as names and places in literature) are pronounced wrongly by speech synthesizers, but if the synthesizer has a user-controlled pronunciation dictionary (lexicon) then this can be used to correct its pronunciation where necessary. However, if you move to a different speech synthesizer, you may find the lexicon format is different.

This is a Python program that converts between different codes for English phonemes and between lexicon files. It supports quite a few, and there is information in the Python file about how to add your own. It works in both Python 2 and Python 3.

Usage information
=================

lexconvert v0.41—convert phonemes between English speech synthesizers etc, © 2007-24 Silas S. Brown.  License: Apache 2

Available pronunciation formats
-------------------------------

acapela-uk
: Acapela-optimised X-SAMPA for UK English voices (e.g. "Peter"), contributed by Jan Weiss

amiga
: AmigaOS speech synthesizer (American English)

android-pico
: X-SAMPA phonemes for the default "Pico" voice in Android 1.6+ (American), wrapped in Java code

apollo
: Dolphin Apollo 2 serial-port and parallel-port hardware synthesizers (in case anybody still uses those)

audapter
: Audapter Speech System, an old hardware serial/parallel-port synthesizer (American English)

bbcmicro
: BBC Micro Speech program from 1985 (see comments in `lexconvert.py` for more details)

bbcmicro-cc
: Computer Concepts Speech ROM which provided phonemes for the BBC Micro's TMS5220 "speech chip" add-on (less widely sold than the software-only product)

braille-ipa
: IPA symbols in Braille (2008 BANA standard).  By default Braille ASCII is output; if you prefer to see the Braille dots via Unicode, set the `BRAILLE_UNICODE` environment variable.

cepstral
: Cepstral's British English SSML phoneset

cheetah
: Allophone codes for the 1983 "Cheetah Sweet Talker" SP0256-based hardware add-on for ZX Spectrum and BBC Micro home computers. The conversion from phonemes to allophones might need tweaking. Set the `CHEETAH_SYM` environment variable to see the mnemonic symbols from the instruction sheet (not actually used by the system).

cmu
: format of the US-English Carnegie Mellon University Pronouncing Dictionary, contributed by Jan Weiss

dectalk
: DECtalk hardware synthesizers (American English)

deva-approx
: Rough approximation using Devanagari (for getting Indian computer voices to speak some English words; works with some words better than others); can also be used to approximate Devanagari words in English phonemes

doubletalk
: DoubleTalk PC/LT serial-port hardware synthesizers (American English; assumes DOS driver by default, otherwise set `DTALK_COMMAND_CODE` to your current command-code binary value, e.g. `export DTALK_COMMAND_CODE=1`)

espeak
: eSpeak's default British voice

example
: A small built-in example lexicon for testing when you don't have your full custom lexicon to hand.  Use `--convert` to write it in one of the other formats and see if a synth can import it.

festival
: Festival's British voice

festival-cmu
: American CMU version of Festival

kana-approx
: Rough approximation using kana (for getting Japanese computer voices to speak some English words; works with some words better than others).  Set `KANA_TYPE` environment variable to hiragana or katakana (which can affect the sounds of some voices); default is hiragana

keynote
: Phoneme-read and lexicon-add codes for Keynote Gold hardware synthesizers (American English)

latex-ipa
: IPA symbols for typesetting in LaTeX using the "tipa" package

mac
: approximation in American English using the `[[inpt PHON]]` notation of Apple's US voices

mac-uk
: Scansoft/Nuance British voices in Mac OS 10.7+ (system lexicon editing required, see `--mac-uk` option)

names
: Lexconvert internal phoneme names (sometimes useful with the `--phones` option while developing new formats)

pinyin-approx
: Rough approximation using roughly the spelling rules of Chinese Pinyin (for getting Chinese-only voices to speak some English words; works with some words better than others)

rsynth
: rsynth text-to-speech C library (American English)

sam
: Software Automatic Mouth (1982 American English synth that ran on C64, Atari 400/800/etc and Apple II/etc)

sapi
: Microsoft Speech API (American English)

speakjet
: Allophone codes for the American English "SpeakJet" speech synthesis chip (the conversion from phonemes to allophones might need tweaking).  Set the `SPEAKJET_SYM` environment variable to use mnemonics, otherwise numbers are used (set `SPEAKJET_BINARY` for binary output).

unicode-ipa
: IPA symbols in Unicode, as used by an increasing number of dictionary programs, websites etc

unicode-ipa-syls
: Like unicode-ipa but with syllable separators preserved

unicode-rough
: A non-standard notation that's reminiscent of unicode-ipa but changed so that more of the characters show in old browsers with incomplete fonts

vocaloid
: X-SAMPA phonemes for Yamaha's Vocaloid singing synthesizer.  Contributed by Lorenzo Gatti, who tested in Vocaloid 4 using two American English voices.

x-sampa
: General X-SAMPA notation, contributed by Jan Weiss

x-sampa-strict
: A stricter version of X-SAMPA, which can distinguish between sounds not distinct in British English when converting to/from IPA, but might not work on all voices

yinghan
: As unicode-ipa but, when converting a user lexicon, generates Python code that reads Wenlin Yinghan dictionary entries and adds IPA bands to matching words

Program options
---------------

--convert `<from-format>` `<to-format>`
: Convert a user lexicon (generally from its default filename; if this cannot be found then lexconvert will tell you what it should be).  
E.g.: `python lexconvert.py` `--convert` festival cepstral

--parens `<format>` [`<words>`]
: Like `--ruby` but outputs just text with parenthesised pronunciation after each word, for pasting into instant messaging etc.  
E.g.: `python lexconvert.py` `--parens` unicode-ipa This is a test sentence.  
Beware, the considerations about eSpeak versions that apply to `--ruby` also apply here.

--phones `<format>` [`<words>`]
: Use eSpeak to convert text to phonemes, and then convert the phonemes to format `<format>`.  
E.g.: `python lexconvert.py` `--phones` unicode-ipa This is a test sentence.  
Set environment variable `PHONES_PIPE_COMMAND` to an additional command to which to write the phones as well as standard output.  (If standard input is a terminal then this will be done separately after each line.)  
(Some commercial speech synthesizers do not work well when driven entirely from phonemes, because their internal format is different and is optimised for normal text.)  
Set format to 'all' if you want to see the phonemes in *all* supported formats.

--phones2phones `<format1>` `<format2>` [`<phonemes in format1>`]
: Perform a one-off conversion of phonemes from format1 to format2 (format2 can be 'all' if you want)

--ruby `<format>` [`<words>`]
: Like `--phones` but outputs the result as HTML RUBY markup, with each word's pronunciation symbols placed above the corresponding English word.  
E.g.: `python lexconvert.py` `--ruby` unicode-ipa This is a test sentence.  
This option is made more complicated by the fact that different versions of eSpeak may space the phoneme output differently, for example when handling numbers; if your eSpeak version is not recognised then all numbers are unannotated. Anyway you are advised not to rely on this option working with the new development NG versions of eSpeak. If the version you have behaves unexpectedly, words and phonemes output might lose synchronisation. However this option is believed to be stable when used with simple text and the original eSpeak.  
You can optionally set the `RUBY_GRADINT_CGI` environment variable to the URL of an instance of Gradint Web Edition to generate audio links for each word.  If doing this in a Web Adjuster filter, see comments in the lexconvert source for setup details.

--try `<format>` [`<pronunciation>`]
: Convert input from `<format>` into eSpeak and try it out.  
(Requires the 'espeak' command.)  
E.g.: `python lexconvert.py` `--try` festival h @0 l ou1  
 or: `python lexconvert.py` `--try` unicode-ipa `'\u02c8\u0279\u026adn\u0329'` (for Unicode put `'\uNNNN'` or UTF-8)

--trymac `<format>` [`<pronunciation>`]
: Convert phonemes from `<format>` into Mac and try it using the Mac OS 'say' command

--trymac-uk `<format>` [`<pronunciation>`]
: Convert phonemes from `<format>` and try it with Mac OS British voices (see `--mac-uk` for details)

--festival-dictionary-to-espeak `<location>`
: Convert the Festival Oxford Advanced Learners Dictionary (OALD) pronunciation lexicon to eSpeak.  
You need to specify the location of the OALD file in `<location>`,  
e.g. for Debian festlex-oald package: `python lexconvert.py` `--festival-dictionary-to-espeak` /usr/share/festival/dicts/oald/all.scm  
or if you can't install the Debian package, try downloading http://ftp.debian.org/debian/pool/non-free/f/festlex-oald/festlex-oald_1.4.0.orig.tar.gz, unpack it into /tmp, and do: `python lexconvert.py` `--festival-dictionary-to-espeak` /tmp/festival/lib/dicts/oald/oald-0.4.out  
In all cases you need to cd to the eSpeak source directory before running this.  en_extra will be overwritten.  Converter will also read your `~/.festivalrc` if it exists.  (You can later incrementally update from `~/.festivalrc` using the `--convert` option; the entries from the system dictionary will not be overwritten in this case.)  Specify `--without-check` to bypass checking the existing eSpeak pronunciation for OALD entries (much faster, but makes a larger file and in some cases compromises the pronunciation quality).

--mac-uk `<from-format>` [`<text>`]
: Speak text in Mac OS 10.7+ British voices while using a lexicon converted in from `<from-format>`. As these voices do not have user-modifiable lexicons, lexconvert must binary-patch your system's master lexicon; this is at your own risk! (Superuser privileges are needed the first time. A backup of the system file is made, and all changes are restored on normal exit but if you force-quit then you might need to restore the backup manually. Text speaking needs to be under lexconvert's control because it usually has to change the input words to make them fit the available space in the binary lexicon.) By default the Daniel voice is used; Emily or Serena can be selected by setting the `MACUK_VOICE` environment variable.

--syllables [`<words>`]
: Attempt to break 'words' into syllables for music lyrics (uses espeak to determine how many syllables are needed)

Trademarks
----------
* Android is a trademark of Google LLC.
* Apache is a registered trademark of The Apache Software Foundation.
* Apple is a trademark of Apple Inc.
* Cepstral is a trademark and brand of Cepstral, LLC.
* Debian is a trademark owned by Software in the Public Interest, Inc.
* DECtalk is a trademark of Fonix Corporation.
* Java is a registered trademark of Oracle Corporation in the US and possibly other countries.
* Mac is a trademark of Apple Inc.
* Microsoft is a registered trademark of Microsoft Corp.
* Python is a trademark of the Python Software Foundation.
* ScanSoft and Nuance are trademarks of Nuance Communications, Inc.
* TeX is a trademark of the American Mathematical Society.
* Unicode is a registered trademark of Unicode, Inc. in the United States and other countries.
* Vocaloid is a trademark of Yamaha Corporation.
* Wenlin is a trademark of Wenlin Institute, Inc. SPC.
* Yamaha is a trademark of Yamaha Corporation.
* Any other trademarks I mentioned without realising are trademarks of their respective holders.
