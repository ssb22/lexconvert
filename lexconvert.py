#!/usr/bin/env python

program_name = "lexconvert v0.16 - convert between lexicons of different speech synthesizers\n(c) 2007-2012,2014 Silas S. Brown.  License: GPL"

# Run without arguments for usage information

#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

# Old versions of this code are being kept on SourceForge's E-GuideDog SVN at
# http://svn.code.sf.net/p/e-guidedog/code/ssb22/lexconvert
# although some early ones are missing.

def Phonemes():
   """Create phonemes by calling vowel(), consonant(),
     variant() and other().
   
     For the variants, if a particular variant does not
     exist in the destination format then we will treat it
     as equivalent to the last non-variant we created.
  
     For anything else that does not exist in the
     destination format, we will first try to break it
     down into parts (useful for having compounds like
     'opt_ol_as_in_gold' without having to put them into
     ALL of the formats), and if that still doesn't work
     then we drop a character (with warning depending on
     the format's setting of safe_to_drop_characters)."""
   a_as_in_ah = vowel()
   _, var1_a_as_in_ah = variant()
   _, var2_a_as_in_ah = variant()
   _, var3_a_as_in_ah = variant()
   _, var4_a_as_in_ah = variant()
   _, var5_a_as_in_ah = variant()
   a_as_in_apple = vowel()
   u_as_in_but = vowel() # or the first part of un as in hunt
   o_as_in_orange = vowel()
   _, var1_o_as_in_orange = variant()
   _, var2_o_as_in_orange = variant()
   o_as_in_now = vowel()
   _, var1_o_as_in_now = variant()
   a_as_in_ago = vowel()
   _, var1_a_as_in_ago = variant()
   _, var2_a_as_in_ago = variant()
   _, var3_a_as_in_ago = variant()
   _, var4_a_as_in_ago = variant()
   _, var5_a_as_in_ago = variant()
   e_as_in_herd = vowel()
   eye = vowel()
   _, var1_eye = variant()
   b = consonant()
   ch = consonant()
   d = consonant()
   th_as_in_them = consonant()
   e_as_in_them = vowel()
   _, var1_e_as_in_them = variant()
   ar_as_in_year = vowel()
   a_as_in_air = vowel()
   _, var1_a_as_in_air = variant()
   _, var2_a_as_in_air = variant()
   _, var3_a_as_in_air = variant()
   _, var4_a_as_in_air = variant()
   a_as_in_ate = vowel()
   _, var1_a_as_in_ate = variant()
   f = consonant()
   g = consonant()
   h = consonant()
   i_as_in_it = vowel()
   _, var1_i_as_in_it = variant()
   _, var2_i_as_in_it = variant()
   ear = vowel()
   _, var1_ear = variant()
   e_as_in_eat = vowel()
   _, var1_e_as_in_eat = variant()
   j_as_in_jump = consonant()
   k = consonant()
   _, opt_scottish_loch = variant()
   l = consonant()
   _, var1_l = variant()
   m = consonant()
   n = consonant()
   ng = consonant()
   o_as_in_go = vowel()
   _, var1_o_as_in_go = variant()
   _, var2_o_as_in_go = variant()
   _, var3_o_as_in_go = variant()
   opt_ol_as_in_gold = vowel()
   oy_as_in_toy = vowel()
   _, var1_oy_as_in_toy = variant()
   p = consonant()
   r = consonant()
   _, var1_r = variant()
   s = consonant()
   sh = consonant()
   t = consonant()
   _, var1_t = variant()
   th = consonant()
   oor_as_in_poor = vowel()
   _, var1_oor_as_in_poor = variant()
   _, opt_u_as_in_pull = variant()
   opt_ul_as_in_pull = vowel()
   oo_as_in_food = vowel()
   _, var1_oo_as_in_food = variant()
   _, var2_oo_as_in_food = variant()
   close_to_or = vowel()
   _, var1_close_to_or = variant()
   _, var2_close_to_or = variant()
   _, var3_close_to_or = variant()
   v = consonant()
   w = consonant()
   _, var1_w = variant()
   y = consonant()
   z = consonant()
   ge_of_blige_etc = consonant()
   glottal_stop = other()
   syllable_separator = other()
   _, primary_stress = variant()
   _, secondary_stress = variant()
   text_sharp = other()
   text_space = other()
   text_underline = other()
   text_question = other()
   text_exclamation = other()
   text_comma = other()
   return locals()

def LexFormats():
  """Makes the phoneme conversion tables of each format.
     Each table has string to phoneme entries and phoneme
     to string entries.  The string to phoneme entries are
     used when converting OUT of that format, and the
     phoneme to string entries are used when converting IN
     (so you can recognise phonemes you don't support and
     convert them to something else).  By default, a tuple
     of the form (string,phoneme) will create entries in
     BOTH directions; one-directional entries are created
     via (string,phoneme,False) or (phoneme,string,False).
     The makeDic function checks the keys are unique."""
  globals().update(Phonemes())
  return { "festival" : makeDic(
    "Festival's default British voice",
    ('0',syllable_separator),
    ('1',primary_stress),
    ('2',secondary_stress),
    ('aa',a_as_in_ah),
    ('a',a_as_in_apple),
    ('uh',u_as_in_but),
    ('o',o_as_in_orange),
    ('au',o_as_in_now),
    ('@',a_as_in_ago),
    ('@@',e_as_in_herd),
    ('@1',var2_a_as_in_ago),
    ('@2',var3_a_as_in_ago),
    ('ai',eye),
    ('b',b),
    ('ch',ch),
    ('d',d),
    ('dh',th_as_in_them),
    ('e',e_as_in_them),
    (ar_as_in_year,'@@',False),
    ('e@',a_as_in_air),
    ('ei',a_as_in_ate),
    ('f',f),
    ('g',g),
    ('h',h),
    ('i',i_as_in_it),
    ('i@',ear),
    ('ii',e_as_in_eat),
    ('jh',j_as_in_jump),
    ('k',k),
    ('l',l),
    ('m',m),
    ('n',n),
    ('ng',ng),
    ('ou',o_as_in_go),
    ('oi',oy_as_in_toy),
    ('p',p),
    ('r',r),
    ('s',s),
    ('sh',sh),
    ('t',t),
    ('th',th),
    ('u@',oor_as_in_poor),
    ('u',opt_u_as_in_pull),
    ('uu',oo_as_in_food),
    ('oo',close_to_or),
    ('v',v),
    ('w',w),
    ('y',y),
    ('z',z),
    ('zh',ge_of_blige_etc),
    # lex_filename etc not set (handled as special case, taking from ~/.festivalrc, and read-only for now)
    inline_format = "%s", inline_header="",
    space_separates_words_not_phonemes=False,
    stress_comes_before_vowel=False,
    safe_to_drop_characters=True, # TODO: really? (could instead give a string of known-safe characters)
    cleanup_regexps=[],
  ),

  "espeak" : makeDic(
    "eSpeak's default British voice", # but note that eSpeak's phoneme representation is not always that simple, hence the cleanup_regexps and some special-case code later
    ('%',syllable_separator),
    ("'",primary_stress),
    (',',secondary_stress),
    # TODO: glottal_stop? (in regional pronunciations etc)
    ('A:',a_as_in_ah),
    ('A@',a_as_in_ah,False),
    ('aa',a_as_in_ah,False),
    ('A',var1_a_as_in_ah),
    ('a',a_as_in_apple),
    ('&',a_as_in_apple,False),
    ('V',u_as_in_but),
    ('0',o_as_in_orange),
    ('aU',o_as_in_now),
    ('@',a_as_in_ago),
    ('a#',a_as_in_ago,False), # (TODO: eSpeak sometimes uses a# in 'had' when in a sentence, and this doesn't always sound good on other synths; might sometimes want to convert it to a_as_in_apple; not sure what contexts would call for this though)
    ('3:',e_as_in_herd),
    ('3',var1_a_as_in_ago),
    ('a2',var2_a_as_in_ago),
    ('@2',var3_a_as_in_ago),
    ('@-',var3_a_as_in_ago,False), # (eSpeak @- sounds to me like a shorter version of @, TODO: double-check the relationship between @ and @2 in Festival)
    ('aI',eye),
    ('aI2',eye,False),
    ('aI;',eye,False),
    ('aI2;',eye,False),
    ('b',b),
    ('tS',ch),
    ('d',d),
    ('D',th_as_in_them),
    ('E',e_as_in_them),
    (ar_as_in_year,'3:',False),
    ('e@',a_as_in_air),
    ('eI',a_as_in_ate),
    ('f',f),
    ('g',g),
    ('h',h),
    ('I',i_as_in_it),
    ('I;',i_as_in_it,False),
    ('i',i_as_in_it,False),
    ('I2',var2_i_as_in_it,False),
    ('I2;',var2_i_as_in_it,False),
    ('i@',ear),
    ('i:',e_as_in_eat),
    ('i:;',e_as_in_eat,False),
    ('dZ',j_as_in_jump),
    ('k',k),
    ('x',opt_scottish_loch),
    ('l',l),
    ('L',l,False),
    ('m',m),
    ('n',n),
    ('N',ng),
    ('oU',o_as_in_go),
    ('oUl',opt_ol_as_in_gold), # (espeak says "gold" in a slightly 'posh' way though)
    ('OI',oy_as_in_toy),
    ('p',p),
    ('r',r),
    ('r-',r,False),
    ('s',s),
    ('S',sh),
    ('t',t),
    ('T',th),
    ('U@',oor_as_in_poor),
    ('U',opt_u_as_in_pull),
    ('@5',opt_u_as_in_pull,False),
    ('Ul',opt_ul_as_in_pull),
    ('u:',oo_as_in_food),
    ('O:',close_to_or),
    ('O@',var3_close_to_or),
    ('o@',var3_close_to_or,False),
    ('O',var3_close_to_or,False),
    ('v',v),
    ('w',w),
    ('j',y),
    ('z',z),
    ('Z',ge_of_blige_etc),
    lex_filename = "en_extra",
    lex_header = "",
    lex_entry_format = "%s %s\n",
    lex_word_case = any,
    lex_footer = "",
    inline_format = "[[%s]]", inline_header="",
    space_separates_words_not_phonemes=True,
    stress_comes_before_vowel=True,
    safe_to_drop_characters="_: !",
    cleanup_regexps=[
      ("k'a2n","k'@n"),
      ("ka2n","k@n"),
      ("gg","g"),
      ("@U","oU"), # (eSpeak uses oU to represent @U; difference is given by its accent parameters)
      ("([iU]|([AO]:))@r$","\1@"),
      ("([^e])@r",r"\1_remove_3"),("_remove_",""),
      # (r"([^iU]@)l",r"\1L") # only in older versions of espeak (not valid in more recent versions)
      ("rr$","r"),
      ("3:r$","3:"),
      # TODO: 'declared' & 'declare' the 'r' after the 'E' sounds a bit 'regional' (but pretty).  but sounds incomplete w/out 'r', and there doesn't seem to be an E2 or E@
      # TODO: consider adding 'g' to words ending in 'N' (if want the 'g' pronounced in '-ng' words) (however, careful of words like 'yankee' where the 'g' would be followed by a 'k'; this may also be a problem going into the next word)
    ],
  ),

  "sapi" : makeDic(
    "Microsoft Speech API (American English)",
    ('-',syllable_separator),
    ('1',primary_stress),
    ('2',secondary_stress),
    ('aa',a_as_in_ah),
    ('ae',a_as_in_apple),
    ('ah',u_as_in_but),
    ('ao',o_as_in_orange),
    ('aw',o_as_in_now),
    ('ax',a_as_in_ago),
    ('er',e_as_in_herd),
    ('@',var4_a_as_in_ago),
    ('ay',eye),
    ('b',b),
    ('ch',ch),
    ('d',d),
    ('dh',th_as_in_them),
    ('eh',e_as_in_them),
    ('ey',var1_e_as_in_them),
    (ar_as_in_year,'er',False),
    ('eh r',a_as_in_air),
    (a_as_in_ate,'ey',False),
    ('f',f),
    ('g',g),
    ('h',h), # Jan suggested 'hh', but I can't get this to work on Windows XP (TODO: try newer versions of Windows)
    ('ih',i_as_in_it),
    ('iy ah',ear),
    ('iy',e_as_in_eat),
    ('jh',j_as_in_jump),
    ('k',k),
    ('l',l),
    ('m',m),
    ('n',n),
    ('ng',ng),
    ('ow',o_as_in_go),
    ('oy',oy_as_in_toy),
    ('p',p),
    ('r',r),
    ('s',s),
    ('sh',sh),
    ('t',t),
    ('th',th),
    ('uh',oor_as_in_poor),
    ('uw',oo_as_in_food),
    ('AO',close_to_or),
    ('v',v),
    ('w',w),
    # ('x',var1_w), # suggested by Jan, but I can't get this to work on Windows XP (TODO: try newer versions of Windows)
    ('y',y),
    ('z',z),
    ('zh',ge_of_blige_etc),
    lex_filename="run-ptts.bat", # write-only for now
    lex_header = "rem  You have to run this file\nrem  with ptts.exe in the same directory\nrem  to add these words to the SAPI lexicon\n\n",
    lex_entry_format='ptts -la %s "%s"\n',
    lex_word_case = any,
    lex_footer = "",
    inline_format = '<pron sym="%s"/>', inline_header="",
    space_separates_words_not_phonemes=False,
    stress_comes_before_vowel=False,
    safe_to_drop_characters=True, # TODO: really?
    cleanup_regexps=[],
  ),

  "cepstral" : makeDic(
    "Cepstral's British English SSML phoneset",
    ('0',syllable_separator),
    ('1',primary_stress),
    ('a',a_as_in_ah),
    ('ae',a_as_in_apple),
    ('ah',u_as_in_but),
    ('oa',o_as_in_orange),
    ('aw',o_as_in_now),
    (a_as_in_ago,'ah',False),
    ('er',e_as_in_herd),
    ('@',var5_a_as_in_ago),
    ('ay',eye),
    ('b',b),
    ('ch',ch),
    ('d',d),
    ('dh',th_as_in_them),
    ('eh',e_as_in_them),
    (ar_as_in_year,'er',False),
    ('e@',a_as_in_air),
    ('ey',a_as_in_ate),
    ('f',f),
    ('g',g),
    ('h',h),
    ('ih',i_as_in_it),
    ('i ah',ear),
    ('i',e_as_in_eat),
    ('jh',j_as_in_jump),
    ('k',k),
    ('l',l),
    ('m',m),
    ('n',n),
    ('ng',ng),
    ('ow',o_as_in_go),
    ('oy',oy_as_in_toy),
    ('p',p),
    ('r',r),
    ('s',s),
    ('sh',sh),
    ('t',t),
    ('th',th),
    ('uh',oor_as_in_poor),
    ('uw',oo_as_in_food),
    ('ao',close_to_or),
    ('v',v),
    ('w',w),
    ('j',y),
    ('z',z),
    ('zh',ge_of_blige_etc),
    lex_filename="lexicon.txt",
    lex_header = "",
    lex_entry_format = "%s 0 %s\n",
    lex_word_case = "lower",
    lex_footer = "",
    inline_format = "<phoneme ph='%s'>p</phoneme>",
    inline_header = "",
    space_separates_words_not_phonemes=False,
    stress_comes_before_vowel=False,
    safe_to_drop_characters=True, # TODO: really?
    cleanup_regexps=[(" 1","1"),(" 0","0")],
  ),

  "mac" : makeDic(
    "approximation in American English using the [[inpt PHON]] notation of Apple's US voices",
    ('=',syllable_separator),
    ('1',primary_stress),
    ('2',secondary_stress),
    ('AA',a_as_in_ah),
    ('aa',var5_a_as_in_ah),
    ('AE',a_as_in_apple),
    ('UX',u_as_in_but),
    (o_as_in_orange,'AA',False),
    ('AW',o_as_in_now),
    ('AX',a_as_in_ago),
    ('AY',eye),
    ('b',b),
    ('C',ch),
    ('d',d),
    ('D',th_as_in_them),
    ('EH',e_as_in_them),
    (ar_as_in_year,'AX',False),
    ('EH r',a_as_in_air),
    ('EY',a_as_in_ate),
    ('f',f),
    ('g',g),
    ('h',h),
    ('IH',i_as_in_it),
    ('IX',var2_i_as_in_it),
    ('IY UX',ear),
    ('IY',e_as_in_eat),
    ('J',j_as_in_jump),
    ('k',k),
    ('l',l),
    ('m',m),
    ('n',n),
    ('N',ng),
    ('OW',o_as_in_go),
    ('OY',oy_as_in_toy),
    ('p',p),
    ('r',r),
    ('s',s),
    ('S',sh),
    ('t',t),
    ('T',th),
    ('UH',oor_as_in_poor),
    ('UW',oo_as_in_food),
    ('AO',close_to_or),
    ('v',v),
    ('w',w),
    ('y',y),
    ('z',z),
    ('Z',ge_of_blige_etc),
    lex_filename="substitute.sh", # write-only for now
    lex_header = "# I don't yet know how to add to the Apple US lexicon,\n# so here is a 'sed' command you can run on your text\n# to put the pronunciation inline:\n\nsed",
    lex_entry_format=' -e "s/%s/[[inpt PHON]]%s[[inpt TEXT]]/g"',
    lex_word_case = any,
    lex_footer = "\n",
    inline_format = "[[inpt PHON]]%s[[inpt TEXT]]",
    inline_header = "",
    space_separates_words_not_phonemes=True,
    stress_comes_before_vowel=False,
    safe_to_drop_characters=True, # TODO: really?
    cleanup_regexps=[],
  ),

  "mac-uk" : makeDic(
    "Scansoft/Nuance British voices for Mac OS 10.7+ (system lexicon editing required, see --mac-uk option)",
    ('.',syllable_separator),
    ("'",primary_stress),
    ('',secondary_stress),
    ('A',a_as_in_ah),
    ('@',a_as_in_apple),
    ('$',u_as_in_but),
    ('A+',o_as_in_orange),
    ('a&U',o_as_in_now),
    ('E0',a_as_in_ago),
    (e_as_in_herd,'E0',False),
    ('a&I',eye),
    ('b',b),
    ('t&S',ch),
    ('d',d),
    ('D',th_as_in_them),
    ('E',e_as_in_them),
    ('0',ar_as_in_year),
    ('E&$',a_as_in_air),
    ('e&I',a_as_in_ate),
    ('f',f),
    ('g',g),
    ('h',h),
    ('I',i_as_in_it),
    (ear,'E0',False),
    ('i',e_as_in_eat),
    ('d&Z',j_as_in_jump),
    ('k',k),
    ('l',l),
    ('m',m),
    ('n',n),
    ('nK',ng),
    ('o&U',o_as_in_go),
    ('O&I',oy_as_in_toy),
    ('p',p),
    ('R+',r),
    ('s',s),
    ('S',sh),
    ('t',t),
    ('T',th),
    ('O',oor_as_in_poor),
    ('U',opt_u_as_in_pull),
    (oo_as_in_food,'U',False),
    (close_to_or,'O',False),
    ('v',v),
    ('w',w),
    ('j',y),
    ('z',z),
    ('Z',ge_of_blige_etc),
    # lex_filename not set (mac-uk code does not permanently save the lexicon; see --mac-uk option to read text)
    inline_format = "%s", inline_header = "mac-uk phonemes output is for information only; you'll need the --mac-uk or --trymac-uk options to use it\n",
    space_separates_words_not_phonemes=True,
    stress_comes_before_vowel=True,
    safe_to_drop_characters=True, # TODO: really?
    cleanup_regexps=[(r'o\&U\.Ol', r'o\&Ul')],
  ),

  "x-sampa" : makeDic(
    "General X-SAMPA notation (contributed by Jan Weiss)",
    ('.',syllable_separator),
    ('"',primary_stress),
    ('%',secondary_stress),
    ('A',a_as_in_ah),
    (':',var2_a_as_in_ah),
    ('A:',var3_a_as_in_ah),
    ('Ar\\',var4_a_as_in_ah),
    ('a:',var5_a_as_in_ah),
    ('{',a_as_in_apple),
    ('V',u_as_in_but),
    ('Q',o_as_in_orange),
    (var1_o_as_in_orange,'A',False),
    ('O',var2_o_as_in_orange),
    ('aU',o_as_in_now),
    ('{O',var1_o_as_in_now),
    ('@',a_as_in_ago),
    ('3:',e_as_in_herd),
    ('aI',eye),
    ('Ae',var1_eye),
    ('b',b),
    ('tS',ch),
    ('d',d),
    ('D',th_as_in_them),
    ('E',e_as_in_them),
    ('e',var1_e_as_in_them),
    (ar_as_in_year,'3:',False),
    ('E@',a_as_in_air),
    ('Er\\',var1_a_as_in_air),
    ('e:',var2_a_as_in_air),
    ('E:',var3_a_as_in_air),
    ('e@',var4_a_as_in_air),
    ('eI',a_as_in_ate),
    ('{I',var1_a_as_in_ate),
    ('f',f),
    ('g',g),
    ('h',h),
    ('I',i_as_in_it),
    ('1',var1_i_as_in_it),
    ('I@',ear),
    ('Ir\\',var1_ear),
    ('i',e_as_in_eat),
    ('i:',var1_e_as_in_eat),
    ('dZ',j_as_in_jump),
    ('k',k),
    ('x',opt_scottish_loch),
    ('l',l),
    ('m',m),
    ('n',n),
    ('N',ng),
    ('@U',o_as_in_go),
    ('oU',var2_o_as_in_go),
    ('@}',var3_o_as_in_go),
    ('OI',oy_as_in_toy),
    ('oI',var1_oy_as_in_toy),
    ('p',p),
    ('r\\',r),
    (var1_r,'r',False),
    ('s',s),
    ('S',sh),
    ('t',t),
    ('T',th),
    ('U@',oor_as_in_poor),
    ('Ur\\',var1_oor_as_in_poor),
    ('U',opt_u_as_in_pull),
    ('}:',oo_as_in_food),
    ('u:',var1_oo_as_in_food),
    (var2_oo_as_in_food,'u:',False),
    ('O:',close_to_or),
    (var1_close_to_or,'O',False),
    ('o:',var2_close_to_or),
    ('v',v),
    ('w',w),
    ('W',var1_w),
    ('j',y),
    ('z',z),
    ('Z',ge_of_blige_etc),
    lex_filename="acapela.txt",
    lex_header = "",
    lex_entry_format = "%s"+chr(9)+"#%s"+chr(9)+"UNKNOWN\n", # TODO: may be able to convert part-of-speech (NOUN etc) to/from some other formats e.g. Festival
    lex_word_case = any,
    lex_footer = "",
    inline_format = "%s", # TODO: ?
    inline_header = "",
    space_separates_words_not_phonemes=True,
    stress_comes_before_vowel=False,
    safe_to_drop_characters=True, # TODO: really?
    cleanup_regexps=[],
  ),

  "acapela-uk" : makeDic(
    'Acapela-optimised X-SAMPA for UK English voices (e.g. "Peter"), contributed by Jan Weiss',
    ('A:',a_as_in_ah),
    ('{',a_as_in_apple),
    ('V',u_as_in_but),
    ('Q',o_as_in_orange),
    ('A',var1_o_as_in_orange),
    ('O',var2_o_as_in_orange),
    ('aU',o_as_in_now),
    ('{O',var1_o_as_in_now),
    ('@',a_as_in_ago),
    ('3:',e_as_in_herd),
    ('aI',eye),
    ('A e',var1_eye),
    ('b',b),
    ('t S',ch),
    ('d',d),
    ('D',th_as_in_them),
    ('e',e_as_in_them),
    (ar_as_in_year,'3:',False),
    ('e @',a_as_in_air),
    ('e r',var1_a_as_in_air),
    ('e :',var2_a_as_in_air),
    (var3_a_as_in_air,'e :',False),
    ('eI',a_as_in_ate),
    ('{I',var1_a_as_in_ate),
    ('f',f),
    ('g',g),
    ('h',h),
    ('I',i_as_in_it),
    ('1',var1_i_as_in_it),
    ('I@',ear),
    ('I r',var1_ear),
    ('i',e_as_in_eat),
    ('i:',var1_e_as_in_eat),
    ('dZ',j_as_in_jump),
    ('k',k),
    ('x',opt_scottish_loch),
    ('l',l),
    ('m',m),
    ('n',n),
    ('N',ng),
    ('@U',o_as_in_go),
    ('o U',var2_o_as_in_go),
    ('@ }',var3_o_as_in_go),
    ('OI',oy_as_in_toy),
    ('o I',var1_oy_as_in_toy),
    ('p',p),
    ('r',r),
    ('s',s),
    ('S',sh),
    ('t',t),
    ('T',th),
    ('U@',oor_as_in_poor),
    ('U r',var1_oor_as_in_poor),
    ('U',opt_u_as_in_pull),
    ('u:',oo_as_in_food),
    ('O:',close_to_or),
    (var1_close_to_or,'O',False),
    ('v',v),
    ('w',w),
    ('j',y),
    ('z',z),
    ('Z',ge_of_blige_etc),
    lex_filename="acapela.txt",
    lex_header = "",
    lex_entry_format = "%s"+chr(9)+"#%s"+chr(9)+"UNKNOWN\n", # TODO: part-of-speech (as above)
    lex_word_case = any,
    lex_footer = "",
    inline_format = "\\Prn=%s\\", inline_header = "",
    space_separates_words_not_phonemes=False,
    stress_comes_before_vowel=False,
    safe_to_drop_characters=True, # TODO: really?
    cleanup_regexps=[],
  ),

  "cmu" : makeDic(
    'format of the US-English Carnegie Mellon University Pronouncing Dictionary (contributed by Jan Weiss)', # (http://www.speech.cs.cmu.edu/cgi-bin/cmudict)
    ('0',syllable_separator),
    ('1',primary_stress),
    ('2',secondary_stress),
    ('AA',a_as_in_ah),
    (var1_a_as_in_ah,'2',False),
    (var2_a_as_in_ah,'1',False),
    ('AE',a_as_in_apple),
    ('AH',u_as_in_but),
    (o_as_in_orange,'AA',False),
    ('AW',o_as_in_now),
    (a_as_in_ago,'AH',False),
    ('ER',e_as_in_herd), # TODO: check this one
    ('@',var4_a_as_in_ago),
    (var5_a_as_in_ago,'@',False),
    ('AY',eye),
    ('B ',b),
    ('CH',ch),
    ('D ',d),
    ('DH',th_as_in_them),
    ('EH',e_as_in_them),
    (ar_as_in_year,'ER',False),
    (a_as_in_air,'ER',False),
    ('EY',a_as_in_ate),
    ('F ',f),
    ('G ',g),
    ('HH',h),
    ('IH',i_as_in_it),
    ('EY AH',ear),
    ('IY',e_as_in_eat),
    ('JH',j_as_in_jump),
    ('K ',k),
    ('L ',l),
    ('M ',m),
    ('N ',n),
    ('NG',ng),
    ('OW',o_as_in_go),
    ('OY',oy_as_in_toy),
    ('P ',p),
    ('R ',r),
    ('S ',s),
    ('SH',sh),
    ('T ',t),
    ('TH',th),
    ('UH',oor_as_in_poor),
    ('UW',oo_as_in_food),
    ('AO',close_to_or),
    ('V ',v),
    ('W ',w),
    ('Y ',y),
    ('Z ',z),
    ('ZH',ge_of_blige_etc),
    # lex_filename not set (does CMU have a lex file?)
    inline_format = "%s", inline_header="",
    space_separates_words_not_phonemes=False,
    stress_comes_before_vowel=False,
    safe_to_drop_characters=True, # TODO: really?
    cleanup_regexps=[],
  ),

  "bbcmicro" : makeDic(
    "BBC Micro Speech program from 1985 (see comments in lexconvert.py for more details)",
    # Speech was written by David J. Hoskins and published by Superior Software.  It took 7.5k of RAM including 3.1k of samples (49 phonemes + 1 for fricatives at 64 bytes each, 4-bit ~5.5kHz), 2.2k of lexicon, and 2.2k of machine code; sounds "retro" by modern standards but quite impressive for the BBC Micro in 1985.  Samples are played by amplitude-modulating the BBC's tone generator.
    # If you use an emulator like BeebEm, you'll need diskimg/Speech.ssd.  This can be made from your original Speech disc, or you might be able to find one but beware of copyright!  Same goes with the Model B ROM images included in BeebEm (you might want to delete the other models).  There has been considerable discussion over whether UK copyright law does or should allow "format-shifting" your own legally-purchased media, and I don't fully understand all the discussion so I don't want to give advice on it here.  The issue is "format-shifting" your legally-purchased BBC Micro ROM code and Speech disc to emulator images; IF this is all right then I suspect downloading someone else's copy is arguably allowed as long as you bought it legally "back in the day", but I'm not a solicitor so I don't know.
    # lexconvert's --phones bbcmicro option creates *SPEAK commands which you can type into the BBC Micro or paste into an emulator, either at the BASIC prompt, or in a listing with line numbers provided by AUTO.  You have to load the Speech program first of course.
    # To script this on BeebEm, first turn off the Speech disc's boot option (by turning off File / Disc options / Write protect and entering "*OPT 4,0"; use "*OPT 4,3" if you want it back later), and then you can do (e.g. on a Mac) open /usr/local/BeebEm3/diskimg/Speech.ssd && sleep 1 && (echo '*SPEECH';python lexconvert.py --phones bbcmicro "Greetings from 19 85") | pbcopy && osascript -e 'tell application "System Events" to keystroke "v" using command down'
    # or if you know it's already loaded: echo "Here is some text" | python lexconvert.py --phones bbcmicro | pbcopy && osascript -e 'tell application "BeebEm3" to activate' && osascript -e 'tell application "System Events" to keystroke "v" using command down'
    # (unfortunately there doesn't seem to be a way of doing it without giving the emulator window focus)
    ('4',primary_stress),
    ('5',secondary_stress), # (these are pitch numbers on the BBC; normal pitch is 6, and lower numbers are higher pitches, so try 5=secondary and 4=primary; 3 sounds less calm)
    ('AA',a_as_in_ah),
    ('AE',a_as_in_apple),
    ('AH',u_as_in_but),
    ('O',o_as_in_orange),
    ('AW',o_as_in_now),
    (a_as_in_ago,'AH',False),
    ('ER',e_as_in_herd),
    ('IY',eye),
    ('B',b),
    ('CH',ch),
    ('D',d),
    ('DH',th_as_in_them),
    ('EH',e_as_in_them),
    (ar_as_in_year,'ER',False),
    ('AI',a_as_in_air),
    ('AY',a_as_in_ate),
    ('F',f),
    ('G',g),
    ('/H',h),
    ('IH',i_as_in_it),
    ('IX',var2_i_as_in_it), # (IX sounds to me like a slightly shorter version of IH)
    ('IXAH',ear),
    ('EE',e_as_in_eat),
    ('J',j_as_in_jump),
    ('K',k),
    ('C',k,False), # for CT as in "fact", read out as K+T
    ('L',l),
    ('M',m),
    ('N',n),
    ('NX',ng),
    ('OW',o_as_in_go),
    ('OL',opt_ol_as_in_gold),
    ('OY',oy_as_in_toy),
    ('P',p),
    ('R',r),
    ('S',s),
    ('SH',sh),
    ('T',t),
    ('TH',th),
    ('AOR',oor_as_in_poor),
    ('UH',oor_as_in_poor,False), # TODO: really? (espeak 'U' goes to opt_u_as_in_pull, and eSpeak also used U for the o in good, which sounds best with Speech's default UH4, hence the line below, but where did we get UH->oor_as_in_poor from?  Low-priority though because how often do you convert OUT of bbcmicro format)
    (opt_u_as_in_pull,'UH',False),
    ('/U',opt_u_as_in_pull,False),
    ('/UL',opt_ul_as_in_pull),
    ('UW',oo_as_in_food),
    ('UX',oo_as_in_food,False),
    ('AO',close_to_or),
    ('V',v),
    ('W',w),
    ('Y',y),
    ('Z',z),
    ('ZH',ge_of_blige_etc),
    lex_filename="BBCLEX",
    lex_header = "",
    lex_entry_format="> %s_"+chr(128)+"%s", # (specifying 'whole word' for now; remove the space before or the _ after if you want)
    lex_word_case = "upper",
    lex_footer = ">**",
    # inline_format not set - handled by special-case code
    inline_header = "",
    space_separates_words_not_phonemes=True,
    stress_comes_before_vowel=False,
    safe_to_drop_characters=True, # TODO: really?
    cleanup_regexps=[
      ('KT','CT'), # Speech instructions: "CT as in fact"
      ('DYUW','DUX'), # "DUX as in duke" (TODO: converting that back out? will currently read as D+UX)
    ],
  ),

  "unicode-ipa" : makeDic(
    "Unicode IPA (as used in an increasing number of dictionary programs, websites etc)",
    ('.',syllable_separator,False),
    (u'\u02c8',primary_stress),
    (u'\u02cc',secondary_stress),
    ('#',text_sharp),
    (' ',text_space),
    ('_',text_underline),
    ('?',text_question),
    ('!',text_exclamation),
    (',',text_comma),
    (u'\u0251',a_as_in_ah),
    (u'\u02d0',var2_a_as_in_ah),
    (u'\u0251\u02d0',var3_a_as_in_ah),
    (u'\u0251\u0279',var4_a_as_in_ah),
    ('a\\u02d0',var5_a_as_in_ah),
    (u'\xe6',a_as_in_apple),
    ('a',a_as_in_apple,False),
    (u'\u028c',u_as_in_but),
    (u'\u0252',o_as_in_orange),
    (var1_o_as_in_orange,u'\u0251',False),
    (u'\u0254',var2_o_as_in_orange),
    (u'a\u028a',o_as_in_now),
    (u'\xe6\u0254',var1_o_as_in_now),
    (u'\u0259',a_as_in_ago),
    (u'\u0259\u02d0',e_as_in_herd),
    (u'\u025a',var1_a_as_in_ago),
    (u'a\u026a',eye),
    (u'\u0251e',var1_eye),
    ('b',b),
    (u't\u0283',ch),
    (u'\u02a7',ch,False),
    ('d',d),
    (u'\xf0',th_as_in_them),
    (u'\u025b',e_as_in_them),
    ('e',var1_e_as_in_them),
    (u'\u025d',ar_as_in_year),
    (u'\u025c\u02d0',ar_as_in_year,False),
    (u'\u025b\u0259',a_as_in_air),
    (u'\u025b\u0279',var1_a_as_in_air),
    (u'e\u02d0',var2_a_as_in_air),
    (u'\u025b\u02d0',var3_a_as_in_air),
    (u'e\u0259',var4_a_as_in_air),
    (u'e\u026a',a_as_in_ate),
    (u'\xe6\u026a',var1_a_as_in_ate),
    ('f',f),
    (u'\u0261',g),
    ('h',h),
    (u'\u026a',i_as_in_it),
    (u'\u0268',var1_i_as_in_it),
    (u'\u026a\u0259',ear),
    (u'\u026a\u0279',var1_ear),
    ('i',e_as_in_eat),
    (u'i\u02d0',var1_e_as_in_eat),
    (u'd\u0292',j_as_in_jump),
    (u'\u02a4',j_as_in_jump,False),
    ('k',k),
    ('x',opt_scottish_loch),
    ('l',l),
    (u'd\u026b',var1_l),
    ('m',m),
    ('n',n),
    (u'\u014b',ng),
    (u'\u0259\u028a',o_as_in_go),
    ('o',var1_o_as_in_go),
    (u'o\u028a',var2_o_as_in_go),
    (u'\u0259\u0289',var3_o_as_in_go),
    (u'\u0254\u026a',oy_as_in_toy),
    (u'o\u026a',var1_oy_as_in_toy),
    ('p',p),
    (u'\u0279',r),
    (var1_r,'r',False),
    ('s',s),
    (u'\u0283',sh),
    ('t',t),
    (u'\u027e',var1_t),
    (u'\u03b8',th),
    (u'\u028a\u0259',oor_as_in_poor),
    (u'\u028a\u0279',var1_oor_as_in_poor),
    (u'\u028a',opt_u_as_in_pull),
    (u'\u0289\u02d0',oo_as_in_food),
    (u'u\u02d0',var1_oo_as_in_food),
    ('u',var2_oo_as_in_food),
    (u'\u0254\u02d0',close_to_or),
    (var1_close_to_or,u'\u0254',False),
    (u'o\u02d0',var2_close_to_or),
    ('v',v),
    ('w',w),
    (u'\u028d',var1_w),
    ('j',y),
    ('z',z),
    (u'\u0292',ge_of_blige_etc),
    (u'\u0294',glottal_stop),
    lex_filename="words-ipa.html", # write-only for now
    lex_header = '<html><head><meta name="mobileoptimized" content="0"><meta name="viewport" content="width=device-width"><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></head><body><table>',
    lex_entry_format="<tr><td>%s</td><td>%s</td></tr>\n",
    lex_word_case = any,
    lex_footer = "</table></body></html>\n",
    inline_format = "%s", inline_header="",
    space_separates_words_not_phonemes=True,
    stress_comes_before_vowel=True,
    safe_to_drop_characters=True, # TODO: really? (at least '-' should be safe to drop)
    cleanup_regexps=[],
  ),

  "latex-ipa" : makeDic(
    "LaTeX IPA package (in case you need to typeset your custom pronunciations in an academic paper or something)",
    ('.',syllable_separator,False),
    ('"',primary_stress),
    ('\\textsecstress{}',secondary_stress),
    ('\\#',text_sharp),
    (' ',text_space),
    ('\\_',text_underline),
    ('?',text_question),
    ('!',text_exclamation),
    (',',text_comma),
    ('A',a_as_in_ah),
    (':',var2_a_as_in_ah),
    ('A:',var3_a_as_in_ah),
    ('A\\textturnr{}',var4_a_as_in_ah),
    ('a:',var5_a_as_in_ah),
    ('\\ae{}',a_as_in_apple),
    ('2',u_as_in_but),
    ('6',o_as_in_orange),
    (var1_o_as_in_orange,'A',False),
    ('O',var2_o_as_in_orange),
    ('aU',o_as_in_now),
    ('\\ae{}O',var1_o_as_in_now),
    ('@',a_as_in_ago),
    ('@:',e_as_in_herd),
    ('\\textrhookschwa{}',var1_a_as_in_ago),
    ('aI',eye),
    ('Ae',var1_eye),
    ('b',b),
    ('tS',ch),
    ('d',d),
    ('D',th_as_in_them),
    ('E',e_as_in_them),
    ('e',var1_e_as_in_them),
    ('3:',ar_as_in_year),
    ('E@',a_as_in_air),
    ('E\\textturnr{}',var1_a_as_in_air),
    ('e:',var2_a_as_in_air),
    ('E:',var3_a_as_in_air),
    ('e@',var4_a_as_in_air),
    ('eI',a_as_in_ate),
    ('\\ae{}I',var1_a_as_in_ate),
    ('f',f),
    ('g',g),
    ('h',h),
    ('I',i_as_in_it),
    ('1',var1_i_as_in_it),
    ('I@',ear),
    ('I\\textturnr{}',var1_ear),
    ('i',e_as_in_eat),
    ('i:',var1_e_as_in_eat),
    ('dZ',j_as_in_jump),
    ('k',k),
    ('x',opt_scottish_loch),
    ('l',l),
    ('d\\textltilde{}',var1_l),
    ('m',m),
    ('n',n),
    ('N',ng),
    ('@U',o_as_in_go),
    ('o',var1_o_as_in_go),
    ('oU',var2_o_as_in_go),
    ('@0',var3_o_as_in_go),
    ('OI',oy_as_in_toy),
    ('oI',var1_oy_as_in_toy),
    ('p',p),
    ('\\textturnr{}',r),
    (var1_r,'r',False),
    ('s',s),
    ('S',sh),
    ('t',t),
    ('R',var1_t),
    ('T',th),
    ('U@',oor_as_in_poor),
    ('U\\textturnr{}',var1_oor_as_in_poor),
    ('U',opt_u_as_in_pull),
    ('0:',oo_as_in_food),
    ('u:',var1_oo_as_in_food),
    ('u',var2_oo_as_in_food),
    ('O:',close_to_or),
    (var1_close_to_or,'O',False),
    ('o:',var2_close_to_or),
    ('v',v),
    ('w',w),
    ('\\textturnw{}',var1_w),
    ('j',y),
    ('z',z),
    ('Z',ge_of_blige_etc),
    ('P',glottal_stop),
    lex_filename="words-ipa.tex", # write-only for now
    lex_header = r'\documentclass[12pt,a4paper]{article} \usepackage[safe]{tipa} \usepackage{longtable} \begin{document} \begin{longtable}{ll}',
    lex_entry_format=r"%s & \textipa{%s}\\"+"\n",
    lex_word_case = any,
    lex_footer = r"\end{longtable}\end{document}"+"\n",
    inline_format = "\\textipa{%s}",
    inline_header = r"% In preamble, put \usepackage[safe]{tipa}", # (the [safe] part is recommended if you're mixing with other TeX)
    space_separates_words_not_phonemes=True,
    stress_comes_before_vowel=True,
    safe_to_drop_characters=True, # TODO: really?
    cleanup_regexps=[],
  ),

  "pinyin-approx" : makeDic(
    "Rough approximation using roughly the spelling rules of Chinese Pinyin (for getting Chinese-only voices to speak some English words - works with some words better than others)", # write-only for now
    ('4',primary_stress),
    ('2',secondary_stress),
    ('a5',a_as_in_ah),
    ('ya5',a_as_in_apple),
    ('e5',u_as_in_but),
    ('yo5',o_as_in_orange),
    ('ao5',o_as_in_now),
    (a_as_in_ago,'e5',False),
    ('wu5',var4_a_as_in_ago),
    (var5_a_as_in_ago,'wu5',False),
    ('ai5',eye),
    ('bu0',b),
    ('che0',ch),
    ('de0',d),
    ('ze0',th_as_in_them),
    ('ye5',e_as_in_them),
    (ar_as_in_year,'e5',False),
    (a_as_in_air,'ye5',False),
    ('ei5',a_as_in_ate),
    ('fu0',f),
    ('ge0',g),
    ('he0',h),
    ('yi5',i_as_in_it),
    ('yi3re5',ear),
    (e_as_in_eat,'yi5',False),
    ('zhe0',j_as_in_jump),
    ('ke0',k),
    ('le0',l),
    ('me0',m),
    ('ne0',n),
    ('eng0',ng),
    ('ou5',o_as_in_go),
    ('ruo2yi5',oy_as_in_toy),
    ('pu0',p),
    ('re0',r),
    ('se0',s),
    ('she0',sh),
    ('te0',t),
    (th,'zhe0',False),
    (oor_as_in_poor,'wu5',False),
    ('yu5',oo_as_in_food),
    ('huo5',close_to_or),
    (v,'fu0',False),
    ('wu0',w),
    ('yu0',y),
    (z,'ze0',False),
    (ge_of_blige_etc,'zhe0',False),
    lex_filename="words-pinyin-approx.tex", # write-only for now
    lex_header = "Pinyin approxmations (very approximate!)\n----------------------------------------\n",
    lex_entry_format = "%s ~= %s\n",
    lex_word_case = any,
    lex_footer = "",
    inline_format = "%s", inline_header = "",
    space_separates_words_not_phonemes=True,
    stress_comes_before_vowel=False,
    safe_to_drop_characters=True, # TODO: really?
    cleanup_regexps=[
      ("te0ye","tie"),
      ("e0e5","e5"),("([^aeiou][uo])0e(5)",r"\1\2"),
      ("yu0y","y"),
      ("wu0yo5","wo5"),
      ("([bdfghklmnpwz])[euo]0ei",r"\1ei"),
      ("([bdghklmnpstwz])[euo]0ai",r"\1ai"),
      ("([ghklmnpstyz])[euo]0ya",r"\1a"),("([ghklmnpstz])a([0-5]*)ne0",r"\1an\2"),
      ("([bdfghklmnpstwyz])[euo]0a([1-5])",r"\1a\2"),
      ("([bdjlmnpt])[euo]0yi",r"\1i"),("([bjlmnp])i([1-5]*)ne0",r"\1in\2"),
      ("([zs])he0ei",r"\1hei"),
      ("([dfghklmnprstyz])[euo]0ou",r"\1ou"),
      ("([dghklnrst])[euo]0huo",r"\1uo"),
      ("([bfpm])[euo]0huo",r"\1o"),
      ("([bdghklmnprstyz])[euo]0ao",r"\1ao"),
      ("([zcs])h[eu]0ao",r"\1hao"),
      ("re0r","r"),
      ("zhe0ne0","zhun5"),
      ("54","4"),
      ("52","2"),
      ("([bdjlmnpty])i([1-9])eng0",r"\1ing\2"),
      ("ya([1-9])eng0",r"yang\1"),
      ("ya([1-9])ne0",r"an\1"),
      ("ye([1-9])ne0",r"yan\1"),("([wr])[eu]0yan",r"\1en"),
      ("yi([1-9])ne0",r"yin\1"),
      
      ("yu0","yu5"),("eng0","eng5"), # they won't work unvoiced anyway
      ("0","5"), # comment out if the synth supports 'tone 0 for unvoiced'
      #("[euo]0","0"), # comment in if it expects consonants only when doing that
    ],
  ),
}

class Counter(object):
    c=sc=0
def other():
    Counter.c += 1 ; Counter.sc=0 ; return Counter.c
consonants = []
def consonant():
    r = other() ; consonants.append(r) ; return r
def vowel(): return other()
def variant():
    Counter.sc += 1
    while str(Counter.sc).endswith('0'): Counter.sc += 1
    return 0, float('%d.%d' % (Counter.c,Counter.sc))
    # the 0 is so we can say _, name = variant()
    # so as to get some extra indentation

def makeDic(doc,*args,**kwargs):
    d = {("settings","doc"):doc}
    for a in args:
        assert type(a)==tuple and (len(a)==2 or len(a)==3)
        k=a[0]
        assert not k in d, "Duplicate key "+repr(k) # Python does not do this in {...} notation, just lets you overwrite!
        v=a[1] ; d[k] = v
        if len(a)==3: bidir=a[2]
        else: bidir=True
        if bidir:
            # (k,v,True) = both (k,v) and (v,k)
            assert not v in d, "Duplicate key "+repr(v)+" (did you forget a ,False to suppress bidirectional mapping?)"
            d[v] = k
    for k,v in kwargs.items(): d[('settings',k)] = v
    return d
def getSetting(formatName,settingName):
  return lexFormats[formatName][('settings',settingName)]
lexFormats = LexFormats()

import commands,sys,re,os

cached_sourceName,cached_destName,cached_dict = None,None,None
def make_dictionary(sourceName,destName):
    global cached_sourceName,cached_destName,cached_dict
    if (sourceName,destName) == (cached_sourceName,cached_destName): return cached_dict
    source = lexFormats[sourceName]
    dest = lexFormats[destName]
    d = {}
    global dest_consonants ; dest_consonants = []
    global dest_syllable_sep ; dest_syllable_sep = dest.get(syllable_separator,"")
    global implicit_vowel_before_NL
    implicit_vowel_before_NL = None
    for k,v in source.items():
      if type(k)==tuple: continue # settings
      if type(v) in [str,unicode]: continue # (num->string entries are for converting IN to source; we want the string->num entries for converting out)
      if not v in dest: v = int(v) # (try the main version of a variant)
      if not v in dest: continue # (haven't got it - will have to ignore or break into parts)
      d[k] = dest[v]
      if v in consonants: dest_consonants.append(d[k])
      if int(v)==e_as_in_herd and (not implicit_vowel_before_NL or v==int(v)): # TODO: or u_as_in_but ?  used by festival and some other synths before words ending 'n' or 'l' (see usage of implicit_vowel_before_NL later)
        implicit_vowel_before_NL = d[k]
    cached_sourceName,cached_destName,cached_dict=sourceName,destName,d
    return d

def convert(pronunc,source,dest):
    if source==dest: return pronunc # essential for --try experimentation with codes not yet supported by lexconvert
    if source=="unicode-ipa":
        # try to decode it
        if "\\u" in pronunc and not '"' in pronunc: # maybe \uNNNN copied from Gecko on X11, can just evaluate it to get the unicode
            # (NB make sure to quote the \'s if pasing in on the command line)
            try: pronunc=eval('u"'+pronunc+'"')
            except: pass
        else: # see if it makes sense as utf-8
            try: pronunc = pronunc.decode('utf-8')
            except: pass
    ret = [] ; toAddAfter = None
    dictionary = make_dictionary(source,dest)
    maxLen=max(len(l) for l in dictionary.keys())
    debugInfo=""
    safe_to_drop = getSetting(source,"safe_to_drop_characters")
    while pronunc:
        for lettersToTry in range(maxLen,-1,-1):
            if not lettersToTry:
              if safe_to_drop==True: pass
              elif (not safe_to_drop) or not pronunc[0] in safe_to_drop: sys.stderr.write("Warning: ignoring unknown "+source+" character "+repr(pronunc[0])+debugInfo+"\n")
              pronunc=pronunc[1:] # ignore
            elif dictionary.has_key(pronunc[:lettersToTry]):
                debugInfo=" after "+pronunc[:lettersToTry]
                toAdd=dictionary[pronunc[:lettersToTry]]
                isStressMark=(toAdd and toAdd in [lexFormats[dest].get(primary_stress,''),lexFormats[dest].get(secondary_stress,''),lexFormats[dest].get(syllable_separator,'')])
                if isStressMark and not getSetting(dest,"stress_comes_before_vowel"):
                    if getSetting(source,"stress_comes_before_vowel"): toAdd, toAddAfter = "",toAdd # move stress marks from before vowel to after
                    else:
                        # With Cepstral synth, stress mark should be placed EXACTLY after the vowel and not any later.  Might as well do this for others also.
                        # (not dest in ["espeak","latex-ipa"] because they use 0 as a phoneme; dealt with separately below)
                        r=len(ret)-1
                        while ret[r] in dest_consonants or ret[r].endswith("*added"): r -= 1 # (if that raises IndexError then the input had a stress mark before any vowel) ("*added" condition is there so that implicit vowels don't get the stress)
                        ret.insert(r+1,toAdd) ; toAdd=""
                elif isStressMark and not getSetting(source,"stress_comes_before_vowel"): # it's a stress mark that should be moved from after the vowel to before it
                    i=len(ret)
                    while i and (ret[i-1] in dest_consonants or ret[i-1].endswith("*added")): i -= 1
                    if i: i-=1
                    ret.insert(i,toAdd)
                    if dest_syllable_sep: ret.append(dest_syllable_sep) # (TODO: this assumes stress marks are at end of syllable rather than immediately after vowel; correct for Festival; check others; probably a harmless assumption though; mac-uk is better with syllable separators although espeak basically ignores them)
                    toAdd = ""
                # attempt to sort out the festival dictionary's (and other's) implicit_vowel_before_NL
                elif implicit_vowel_before_NL and ret and ret[-1] and toAdd in ['n','l'] and ret[-1] in dest_consonants: ret.append(implicit_vowel_before_NL+'*added')
                elif len(ret)>2 and ret[-2].endswith('*added') and toAdd and not toAdd in dest_consonants and not toAdd==dest_syllable_sep: del ret[-2]
                # OK, add it:
                if toAdd:
                    toAdd=toAdd.split()
                    ret.append(toAdd[0])
                    if toAddAfter and not toAdd[0] in dest_consonants:
                        ret.append(toAddAfter)
                        toAddAfter=None
                    ret += toAdd[1:]
                    # TODO: the above few lines make sure that toAddAfter goes after the FIRST phoneme if toAdd is multiple phonemes, but works only when converting from eSpeak to non-eSpeak; it ought to work when converting from non-eSpeak to non-eSpeak also (doesn't matter when converting TO eSpeak)
                if source=="espeak" and pronunc[:lettersToTry]=="e@" and len(pronunc)>lettersToTry and pronunc[lettersToTry]=="r" and (len(pronunc)==lettersToTry+1 or pronunc[lettersToTry+1] in "bdDfghklmnNprsStTvwjzZ"): lettersToTry += 1 # hack because the 'r' is implicit in other synths (but DO have it if there's another vowel to follow)
                pronunc=pronunc[lettersToTry:]
                break
    if toAddAfter: ret.append(toAddAfter)
    if ret and ret[-1]==dest_syllable_sep: del ret[-1] # spurious syllable separator at end
    if getSetting(dest,'space_separates_words_not_phonemes'): separator = ''
    else: separator = ' '
    ret=separator.join(ret).replace('*added','')
    for s,r in getSetting(dest,'cleanup_regexps'):
      ret=re.sub(s,r,ret)
    return ret

def espeak_probably_right_already(existing_pronunc,new_pronunc):
    # Compares our "new" pronunciation with eSpeak's existing pronunciation.  As our transcription into eSpeak notation is only approximate, it could be that our new pronunciation is not identical to the existing one but the existing one is actually correct.
    if existing_pronunc==new_pronunc: return True
    def simplify(pronunc): return \
        pronunc.replace(";","").replace("%","") \
        .replace("a2","@") \
        .replace("3","@") \
        .replace("L","l") \
        .replace("I2","i:") \
        .replace("I","i:").replace("i@","i:@") \
        .replace(",","") \
        .replace("s","z") \
        .replace("aa","A:") \
        .replace("A@","A:") \
        .replace("O@","O:") \
        .replace("o@","O:") \
        .replace("r-","r")
    # TODO: rewrite @ to 3 whenever not followed by a vowel?
    if simplify(existing_pronunc)==simplify(new_pronunc): return True # almost the same, and festival @/a2 etc seems to be a bit ambiguous so leave it alone

def parse_festival_dict(festival_location):
    ret = []
    for line in open(festival_location).xreadlines():
        line=line.strip()
        if "((pos" in line: line=line[:line.index("((pos")]
        if line.startswith('( "'): line=line[3:]
        line=line.replace('"','').replace('(','').replace(')','')
        try:
            word, pos, pronunc = line.split(None,2)
        except ValueError: continue # malformed line
        if pos not in ['n','v','a','cc','dt','in','j','k','nil','prp','uh']: continue # two or more words
        yield (word.lower(), pos, pronunc)

def convert_system_festival_dictionary_to_espeak(festival_location,check_existing_pronunciation,add_user_dictionary_also):
    os.system("mv en_extra en_extra~") # start with blank 'extra' dictionary
    if check_existing_pronunciation: os.system("espeak --compile=en") # so that the pronunciation we're checking against is not influenced by a previous version of en_extra
    outFile=open("en_extra","w")
    print "Reading dictionary lists"
    wordDic = {} ; ambiguous = {}
    for line in filter(lambda x:x.split() and not re.match(r'^[a-z]* *\$',x),open("en_list").read().split('\n')): ambiguous[line.split()[0]]=ambiguous[line.split()[0]+'s']=True # this stops the code below from overriding anything already in espeak's en_list.  If taking out then you need to think carefully about words like "a", "the" etc.
    for word,pos,pronunc in parse_festival_dict(festival_location):
        pronunc=pronunc.replace("i@ 0 @ 0","ii ou 2 ").replace("i@ 0 u 0","ii ou ") # (hack for OALD's "radio"/"video"/"stereo"/"embryo" etc)
        pronunc=pronunc.replace("0","") # 0's not necessary, and OALD sometimes puts them in wrong places, confusing the converter
        if wordDic.has_key(word):
            ambiguous[word] = True
            del wordDic[word] # better not go there
        if not ambiguous.has_key(word):
            wordDic[word] = (pronunc, pos)
    toDel = []
    if check_existing_pronunciation:
        print "Checking existing pronunciation"
        proc=os.popen("espeak -q -x -v en-rp > /tmp/.pronunc 2>&1","w")
        wList = []
    progressCount=0 ; oldPercent=-1
    for word,(pronunc,pos) in wordDic.items():
        if check_existing_pronunciation:
            percent = int(progressCount*100/len(wordDic))
            if not percent==oldPercent: sys.stdout.write(str(percent)+"%\r") ; sys.stdout.flush()
            oldPercent=percent
            progressCount += 1
        if not re.match("^[A-Za-z]*$",word): # (some versions of eSpeak also OK with "-", but not all)
            # contains special characters - better not go there
            toDel.append(word)
        elif word.startswith("plaque") or word in "friday saturday sunday tuesday thursday yesterday".split():
            # hack to accept eSpeak's pl'ak instead of pl'A:k - order was reversed in the March 2009 draft
            toDel.append(word)
        elif word[-1]=="s" and wordDic.has_key(word[:-1]):
            # unnecessary plural (espeak will pick up on them anyway)
            toDel.append(word)
        elif word.startswith("year") or "quarter" in word: toDel.append(word) # don't like festival's pronunciation of those (TODO: also 'memorial' why start with [m'I])
        elif check_existing_pronunciation:
            proc.write(word+"\n")
            proc.flush() # so the progress indicator works
            wList.append(word)
    if check_existing_pronunciation:
        proc.close() ; print
        oldPronDic = {}
        for k,v in zip(wList,open("/tmp/.pronunc").read().split("\n")): oldPronDic[k]=v.strip().replace(" ","")
    for w in toDel: del wordDic[w]
    print "Doing the conversion"
    lines_output = 0
    total_lines = 0
    not_output_because_ok = []
    items = wordDic.items() ; items.sort() # necessary because of the hacks below which check for the presence of truncated versions of the word (want to have decided whether or not to output those truncated versions before reaching the hacks)
    for word,(pronunc,pos) in items:
        total_lines += 1
        new_e_pronunc = convert(pronunc,"festival","espeak")
        if new_e_pronunc.count("'")==2 and not '-' in word: new_e_pronunc=new_e_pronunc.replace("'",",",1) # if 2 primary accents then make the first one a secondary (except on hyphenated words)
        # TODO if not en-rp? - if (word.endswith("y") or word.endswith("ie")) and new_e_pronunc.endswith("i:"): new_e_pronunc=new_e_pronunc[:-2]+"I"
        unrelated_word = None
        if check_existing_pronunciation: espeakPronunc = oldPronDic.get(word,"")
        else: espeakPronunc = ""
        if word[-1]=='e' and wordDic.has_key(word[:-1]): unrelated_word, espeakPronunc = word[:-1],"" # hack: if word ends with 'e' and dropping the 'e' leaves a valid word that's also in the dictionary, we DON'T want to drop this word on the grounds that espeak already gets it right, because if we do then adding 's' to this word may cause espeak to add 's' to the OTHER word ('-es' rule).
        if espeak_probably_right_already(espeakPronunc,new_e_pronunc):
            not_output_because_ok.append(word)
            continue
        if not unrelated_word: lines_output += 1
        outFile.write(word+" "+new_e_pronunc+" // from Festival's ("+pronunc+")")
        if espeakPronunc: outFile.write(", not [["+espeakPronunc+"]]")
        elif unrelated_word: outFile.write(" (here to stop espeak's affix rules getting confused by Festival's \""+unrelated_word+"\")")
        outFile.write("\n")
    print "Corrected(?) %d entries out of %d" % (lines_output,total_lines)
    if add_user_dictionary_also: convert_user_lexicon("festival","espeak",outFile)
    outFile.close()
    os.system("espeak --compile=en")
    if not_output_because_ok:
      print "Checking for unwanted side-effects of those corrections" # e.g. terrible as Terr + ible, inducing as in+Duce+ing
      proc=os.popen("espeak -q -x -v en-rp > /tmp/.pronunc 2>&1","w")
      progressCount = 0
      for w in not_output_because_ok:
          proc.write(w+"\n") ; proc.flush()
          percent = int(progressCount*100/len(not_output_because_ok))
          if not percent==oldPercent: sys.stdout.write(str(percent)+"%\r") ; sys.stdout.flush()
          oldPercent = percent
          progressCount += 1
      proc.close()
      outFile=open("en_extra","a") # append to it
      for word,pronunc in zip(not_output_because_ok,open("/tmp/.pronunc").read().split("\n")):
        pronunc = pronunc.strip().replace(" ","")
        if not pronunc==oldPronDic[word] and not espeak_probably_right_already(oldPronDic[word],pronunc):
          outFile.write(word+" "+oldPronDic[word]+" // (undo affix-side-effect from previous words that gave \""+pronunc+"\")\n")
      outFile.close()
      os.system("espeak --compile=en")
    return not_output_because_ok

def read_user_lexicon(fromFormat):
    if fromFormat=="festival": return eval('['+commands.getoutput("grep '^(lex.add.entry' ~/.festivalrc | sed -e 's/;.*//' -e 's/[^\"]*\"/[\"/' -e 's/\" . /\",(\"/' -e 's/$/\"],/' -e 's/[()]/ /g' -e 's/  */ /g'")+']')
    lexfile = open(getSetting(fromFormat,"lex_filename"))
    if fromFormat=="espeak": return filter(lambda x:len(x)==2,[l.split()[:2] for l in lexfile.readlines()])
    elif fromFormat=="bbcmicro": return [(w[0].lstrip().rstrip('_').lower(),w[1]) for w in filter(lambda x:len(x)==2,[w.split(chr(128)) for w in lexfile.read().split('>')])] # TODO: this reads back the entries we generate, but is unlikely to work well with the wildcards in the default lexicon that would have been added if SPEECH_DISK was set
    elif fromFormat in ["acapela-uk","x-sampa"]:
        lex = []
        for l in lexfile.readlines():
            word, pronunc, ignore = l.split(None,2)
            if pronunc.startswith("#"): pronunc=pronunc[1:]
            lex.append((word,pronunc))
        return lex
    elif fromFormat=="cepstral":
        lex = []
        for l in lexfile.readlines():
            word, ignore, pronunc = l.split(None,2)
            lex.append((word,pronunc))
        return lex
    else: raise Exception("Reading from '%s' lexicon file not yet implemented" % (fromFormat,))

def convert_user_lexicon(fromFormat,toFormat,outFile):
    lex = read_user_lexicon(fromFormat)
    if not toFormat=="mac-uk":
      outFile.write(getSetting(toFormat,"lex_header"))
      entryFormat=getSetting(toFormat,"lex_entry_format")
      wordCase=getSetting(toFormat,"lex_word_case")
    for word, pronunc in lex:
        pronunc = convert(pronunc,fromFormat,toFormat)
        if type(pronunc)==unicode: pronunc=pronunc.encode('utf-8')
        if toFormat=="mac-uk": outFile.append((word,pronunc)) # (it's not really a file)
        else:
          if wordCase=="upper": word=word.upper()
          elif wordCase=="lower": word=word.lower()
          outFile.write(entryFormat % (word,pronunc))
    if toFormat=="bbcmicro": bbc_appendDefaultLex(outFile)
    if not toFormat=="mac-uk": outFile.write(getSetting(toFormat,"lex_footer"))

def write_inlineWord_header(format):
    h = getSetting(format,"inline_header")
    if h: print h
bbc_charsSoFar=0 # hack for bbcmicro
def markup_inline_word(format,pronunc):
    if type(pronunc)==unicode: pronunc=pronunc.encode('utf-8') # UTF-8 output - ok for pasting into Firefox etc *IF* the terminal/X11 understands utf-8 (otherwise redirect to a file, point the browser at it, and set encoding to utf-8, or try --convert'ing which will o/p HTML)
    if format=="bbcmicro":
      global bbc_charsSoFar
      if not bbc_charsSoFar or bbc_charsSoFar+len(pronunc) > 165: # 238 is max len of the immediate BASIC prompt, but get a "Line too long" message from Speech if go over 165 including the '*SPEAK ' (158 excluding it).
        if bbc_charsSoFar: r="\n"
        else: r=""
        bbc_charsSoFar = 7+len(pronunc)+1 # +1 for the space after this word.
        return r+"*SPEAK "+pronunc
      else:
        bbc_charsSoFar += len(pronunc)+1
        return pronunc
    return getSetting(format,"inline_format") % pronunc

def sylcount(festival):
  # we treat @ as counting the same as the previous syllable (e.g. "fire",
  # "power") but this can vary in different songs
  count = inVowel = maybeCount = hadAt = 0
  festival = festival.split()
  for phone,i in zip(festival,range(len(festival))):
    if phone[0] in "aeiou": inVowel=0 # unconditionally start new syllable
    if phone[0] in "aeiou@12":
      if not inVowel: count += 1
      elif phone[0]=="@" and not hadAt: maybeCount = 1 # (e.g. "loyal", but NOT '1', e.g. "world")
      if "@" in phone: hadAt = 1 # for words like "cheerful" ("i@ 1 @" counts as one)
      inVowel = 1
      if phone[0]=="@" and i>=3 and festival[i-2:i]==["ai","1"] and festival[i-3] in ["s","h"]: # special rule for higher, Messiah, etc - like "fire" but usually 2 syllables
        maybeCount = 0 ; count += 1
    else:
      if not phone[0] in "drz": count += maybeCount # not 'r/z' e.g. "ours", "fired" usually 1 syllable in songs, "desirable" usually 4 not 5
      # TODO steward?  y u@ 1 d but usally 2 syllables
      inVowel = maybeCount = hadAt = 0
  return count
def hyphenate(word,numSyls):
  orig = word
  try: word,isu8 = word.decode('utf-8'),True
  except: isu8 = False
  pre=[] ; post=[]
  while word and not 'a'<=word[0].lower()<='z':
    pre.append(word[0]) ; word=word[1:]
  while word and not 'a'<=word[-1].lower()<='z':
    post.insert(0,word[-1]) ; word=word[:-1]
  if numSyls>len(word): return orig # probably numbers or something
  l = int((len(word)+numSyls/2)/numSyls) ; syls = []
  for i in range(numSyls):
    if i==numSyls-1: syls.append(word[i*l:])
    else: syls.append(word[i*l:(i+1)*l])
    if len(syls)>1:
      if len(syls[-1])>2 and syls[-1][0]==syls[-1][1] and not syls[-1][0].lower() in "aeiou":
        # repeated consonant at start - put one on previous
        syls[-2] += syls[-1][0]
        syls[-1] = syls[-1][1:]
      elif ((len(syls[-2])>2 and syls[-2][-1]==syls[-2][-2] and not syls[-2][-1].lower() in "aeiou") \
            or (syls[-1][0].lower() in "aeiouy" and len(syls[-2])>2)) \
            and filter(lambda x:x.lower() in "aeiou",list(syls[-2][:-1])):
        # repeated consonant at end - put one on next
        # or vowel on right: move a letter over (sometimes the right thing to do...)
        # (unless doing so leaves no vowels)
        syls[-1] = syls[-2][-1]+syls[-1]
        syls[-2] = syls[-2][:-1]
  word = ''.join(pre)+"- ".join(syls)+''.join(post)
  if isu8: word=word.encode('utf-8')
  return word

def macSayCommand():
  s = os.environ.get("SAY_COMMAND","")
  if s: return s
  else: return "say"
# e.g. SAY_COMMAND="say -o file.aiff" (TODO: document this in the help text?)
# In Gradint you can set (e.g. if you have a ~/.festivalrc) extra_speech=[("en","python lexconvert.py --mac-uk festival")] ; extra_speech_tofile=[("en",'echo %s | SAY_COMMAND="say -o /tmp/said.aiff" python lexconvert.py --mac-uk festival && sox /tmp/said.aiff /tmp/said.wav',"/tmp/said.wav")]

def getInputText(i,prompt):
  txt = ' '.join(sys.argv[i:])
  if not txt:
    if (not hasattr(sys.stdin,"isatty")) or sys.stdin.isatty(): sys.stderr.write("Enter "+prompt+": ")
    txt = sys.stdin.read()
  return txt

def write_bbcmicro_phones(ph):
  # special case because it needs to track the commas to avoid "Line too long"
  # (and actually we might as well just put each clause on a separate *SPEAK command, using the natural brief delay between commands; this should minimise the occurrence of additional delays in arbitrary places)
  # also issue warnings if things get too big
  totalKeystrokes = 0 ; lines = 0
  for line in filter(lambda x:x,ph.split("\n")):
    global bbc_charsSoFar ; bbc_charsSoFar=0
    l=" ".join([markup_inline_word("bbcmicro",convert(word,"espeak","bbcmicro")) for word in line.split()])
    print l.replace(" \n","\n")
    totalKeystrokes += len(l)+1 ; lines += 1
  # and warn if it looks too big:
  limits_exceeded = [] ; severe=0
  if totalKeystrokes >= 32768:
    severe=1 ; limits_exceeded.append("BeebEm 32K keystroke limit") # At least in version 3, the clipboard is defined in beebwin.h as a char of size 32768 and its bounds are not checked.  Additionally, if you script a second paste before the first has finished (or if you try to use BeebEm's Copy command) then the first paste will be interrupted.  So if you really want to make BeebEm read a long text then I suggest setting a printer destination file, putting a VDU 2,10,3 after each batch of commands, and waiting for that \n to appear in that printer file before sending the next batch, or perhaps write a set of programs to a disk image and have them CHAIN each other or whatever.
  page=0x1900 # BBC Model B with DFS
  himem=0x7c00 # BBC Model B in Mode 7 (which is 40x25 characters = 1000 bytes, by default starting at 7c00 with 24 bytes spare at the top, but the scrolling system uses the full 1024 bytes and can tell the video controller to start rendering at any one of them; if you get Jeremy Ruston's book and program the VIDC yourself then you could fix it at 7c18 if you really want, or just set HIMEM=&8000 and don't touch the screen, but that doesn't give you very much more room)
  speech_loc=0x5500 # unless you've loaded it into Sideways RAM or run RELOCAT to put it somewhere else
  top=page+totalKeystrokes+lines*3+2 # (4 bytes for each program line, but totalKeystrokes includes 1 extra byte for each line anyway, hence lines*3)
  if top > speech_loc: limits_exceeded.append("TOP=&5500 limit (Speech program will be overwritten unless relocated)") # and the *SP8000 Sideways RAM version doesn't seem to work on emulators like BeebEm.  The Speech program does nothing to stop your program (or its variables etc) from growing large enough to overwrite &5500, nor does it stop the stack pointer (coming down from HIMEM) from overwriting &72FF. For more safety on a Model B you could use RELOCAT to put Speech at &5E00 and be sure to set HIMEM=&5E00 before loading, but then you must avoid commands that change HIMEM, such as MODE (but selecting any mode other than 7 will overwrite Speech anyway, although if you set the mode before loading Speech then it'll overwrite screen memory and still work as long as the affected part of the screen is undisturbed).  You can't do tricks like ditching the lexicon because RELOCAT won't let you go above 5E00 (unless you fix it, but I haven't looked in detail; if you can fix RELOCAT to go above 5E00 then you can create a lexicon-free Speech by taking the 1st 0x1560 bytes of SPEECH and append two * bytes, relocate to &6600 and set HIMEM, but don't expect *SAY to work, unless you put a really small lexicon into the spare 144 bytes that are left - RELOCAT needs an xx00 address so you can't have those bytes at the bottom).  You could even relocate to &6A00 and overwrite screen memory if you don't mind the screen being filled with gibberish that you'd better not erase! (well if you program the VIDC as mentioned above and you didn't re-add a small lexicon then you could get yourself 3.6 lines of usable Mode 7 display from the spare bytes but it's probably not worth the effort)
  if top > himem: limits_exceeded.append("Model B Mode 7 HIMEM limit") # unless you overwrite the screen (see above). Not sure what's supposed to happen in BAS128 for the B+(?)/Master, but BeebEm 3 won't run Speech at all unless you set Model B; it reportedly worked on a real Master but who knows about BAS128 compatibility
  if lines > 32768: limits_exceeded.append("BASIC II line number limit") # and you wouldn't get this far on a 32k computer without filling the memory first
  elif 10*lines > 32767: limits_exceeded.append("AUTO line number limit (try AUTO 0,1)") # the highest possible line number in BBC BASIC II (for the Model B) is 32767, and the default AUTO increments in steps of 10.  You can use AUTO 0,1 to start at 0 and increment in steps of 1.
  if severe: warning,after="WARNING: ",""
  else: warning,after="Note: ","It should still work if pasted into BeebEm as immediate commands. "
  after = ". "+after+"See comments in lexconvert for more details.\n"
  if len(limits_exceeded)>1: sys.stderr.write(warning+"this text may be too big for the BBC Micro. The following limits were exceeded: "+", ".join(limits_exceeded)+after)
  elif limits_exceeded: sys.stderr.write(warning+"this text may be too big for the BBC Micro because it exceeds the "+limits_exceeded[0]+after)
def bbc_appendDefaultLex(outFile):
  if not os.environ.get("SPEECH_DISK",""): return
  d=open(os.environ['SPEECH_DISK']).read()
  i=d.index('>OUS_') # if this fails, it wasn't a Speech disk
  j=d.index(">**",i)
  assert j-i==2201, "Lexicon on SPEECH_DISK is wrong size (%d). Is this really an original disk image?" % (j-i)
  outFile.write(d[i:j])
  # TODO: can we compress the BBC lexicon?  i.e. detect if a rule will happen anyway due to subsequent wildcard rules, and delete it if so (don't know how many bytes that would save)

def bbchex(n): return hex(n)[2:].upper()
def bbcshortest(n):
  if len(str(n)) < len('&'+bbchex(n)): return str(n)
  else: return '&'+bbchex(n)
def bbcPokes(data,start):
  while len(data)%4: data+=chr(0) # pad to mult of 4
  i=0 ; ret=[]
  while i<len(data):
    ret.append('!'+bbcshortest(start)+'='+bbcshortest(ord(data[i])+(ord(data[i+1])<<8)+(ord(data[i+2])<<16)+(ord(data[i+3])<<24)))
    i += 4 ; start += 4
  return '\n'.join(ret)+'\n'
def print_bbclex_instructions(fname,size):
  print "The size of this lexicon is "+str(size)+" bytes (hex "+bbchex(size)+")"
  global bbcStart ; bbcStart=None
  noSRAM_lex_offset=0x155F # (on the BBC Micro, SRAM means Sideways RAM, not Static RAM as it does elsewhere; for clarity we'd better say "Sideways RAM" in all output)
  SRAM_lex_offset=0x1683
  SRAM_max=0x4000 # 16k
  noSRAM_default_addr=0x5500
  noSRAM_min_addr=0x1900 # BBC B DFS + no program at all (RELOCAT actually supports going down to E00, but you won't be able to use the disk after this, only tapes)
  noSRAM_himem=0x7c00 # unless you do strange tricks with the screen (see comments on himem=0x7c00 above)
  def special_relocate_instructions(reloc_addr):
    pagemove_min,pagemove_max = max(0xE00,noSRAM_min_addr-0x1E00), noSRAM_min_addr+0xE00 # if relocating to within this range, must move PAGE before loading RELOCAT. RELOCAT's supported range is 0xE00 to 0x5E00, omitting (PAGE-&1E00) to (PAGE+&E00)
    if not pagemove_min<=reloc_addr<pagemove_max:
      return "" # no special instructions needed
    page = reloc_addr+0x1E00
    page_max = min(0x5E00,noSRAM_default_addr-0xE00)
    if page > page_max: return False # "Unfortunately RELOCAT can't put it at &"+bbchex(reloc_addr)+" even with PAGE changes."
    return " RELOCAT must be run with PAGE in the range of &"+bbchex(page)+" to &"+bbchex(page_max)+" for this relocation to work."
  if noSRAM_default_addr+noSRAM_lex_offset+size > noSRAM_himem:
    reloc_addr = noSRAM_himem-noSRAM_lex_offset-size
    reloc_addr -= (reloc_addr%256)
    if reloc_addr >= noSRAM_min_addr:
      instr = special_relocate_instructions(reloc_addr)
      if instr==False: print "This lexicon is too big for Speech in main RAM even with relocation, unless RELOCAT is rewritten to work from files."
      else:
        bbcStart = reloc_addr+noSRAM_lex_offset
        print "This lexicon is too big for Speech at its default address of &"+bbchex(noSRAM_default_addr)+", but you could use RELOCAT to put a version at &"+bbchex(reloc_addr)+" (then do the suggested *SAVE, reset, and run *SP; be sure to set HIMEM=&"+bbchex(reloc_addr)+") and then *LOAD "+fname+" "+bbchex(bbcStart)+" or change the relocated SP file from offset &"+bbchex(noSRAM_lex_offset)+"."+instr
    else: print "This lexicon is too big for Speech in main RAM even with relocation."
  else:
    bbcStart = noSRAM_default_addr+noSRAM_lex_offset
    print "You can load this lexicon by *LOAD "+fname+" "+bbchex(bbcStart)+" or change the SPEECH file from offset &"+bbchex(noSRAM_lex_offset)+". Suggest you also set HIMEM=&"+bbchex(noSRAM_default_addr)+" for safety."
  # Instructions for replacing lex in SRAM:
  if size > SRAM_max-SRAM_lex_offset: print "This lexicon is too big for Speech in Sideways RAM." # unless you can patch Speech to run in SRAM but read its lexicon from main RAM
  else: print "In Sideways RAM, the default lexicon starts at &"+hex(SRAM_lex_offset+0x8000)[2:]+" but you can't access this from BASIC so suggest you back up the SP8000 file and write to its offset "+hex(SRAM_lex_offset)+"."
  if not os.environ.get("SPEECH_DISK",""): print "If you want to append the default lexicon to this one, set SPEECH_DISK to the image of the original Speech disk before running lexconvert, e.g. export SPEECH_DISK=/usr/local/BeebEm3/diskimg/Speech.ssd"
  print "If you get 'Mistake in speech' when testing some words, try starting with '*SAY, ' to ensure there's a space at the start of the SAY string (bug in Speech?)" # Can't track down which words this does and doesn't apply to.
  print "It might be better to load your lexicon into eSpeak and use lexconvert's --phones option to drive the BBC with phonemes."

def main():
    if '--festival-dictionary-to-espeak' in sys.argv:
        try: festival_location=sys.argv[sys.argv.index('--festival-dictionary-to-espeak')+1]
        except IndexError:
            sys.stderr.write("Error: --festival-dictionary-to-espeak must be followed by the location of the festival OALD file (see help text)\n") ; sys.exit(1)
        try: open(festival_location)
        except:
            sys.stderr.write("Error: The specified OALD location '"+festival_location+"' could not be opened\n") ; sys.exit(1)
        try: open("en_list")
        except:
            sys.stderr.write("Error: en_list could not be opened (did you remember to cd to the eSpeak dictsource directory first?\n") ; sys.exit(1)
        convert_system_festival_dictionary_to_espeak(festival_location,not '--without-check' in sys.argv,not os.system("test -e ~/.festivalrc"))
    elif '--try' in sys.argv:
        i=sys.argv.index('--try')
        espeak = convert(getInputText(i+2,"phones in "+sys.argv[i+1]+" format"),sys.argv[i+1],'espeak')
        os.popen("espeak -x","w").write(markup_inline_word("espeak",espeak))
    elif '--trymac' in sys.argv:
        i=sys.argv.index('--trymac')
        mac = convert(getInputText(i+2,"phones in "+sys.argv[i+1]+" format"),sys.argv[i+1],'mac')
        os.popen(macSayCommand()+" -v Vicki","w").write(markup_inline_word("mac",mac)) # Need to specify a voice because the default voice might not be able to take Apple phonemes.  Vicki has been available since 10.3, as has the 'say' command (previous versions need osascript, see Gradint's code)
    elif '--trymac-uk' in sys.argv:
        i=sys.argv.index('--trymac-uk')
        macuk = convert(getInputText(i+2,"phones in "+sys.argv[i+1]+" format"),sys.argv[i+1],'mac-uk')
        m = MacBritish_System_Lexicon("",os.environ.get("MACUK_VOICE","Daniel"))
        try:
          try: m.speakPhones(macuk.split())
          finally: m.close()
        except KeyboardInterrupt:
          sys.stderr.write("Interrupted\n")
    elif '--phones' in sys.argv:
        i=sys.argv.index('--phones')
        format=sys.argv[i+1]
        txt = getInputText(i+2,"text")
        w,r=os.popen4("espeak -q -x",bufsize=max(8192,3*len(txt))) # need to make sure output buffer is big enough (TODO: or use a temp file, or progressive write/read chunks) (as things stand, if bufsize is not big enough, w.close() on the following line can hang, as espeak waits for us to read its output before it can take all of our input)
        w.write(txt) ; w.close()
        write_inlineWord_header(format)
        if format=="bbcmicro":
          write_bbcmicro_phones(r.read())
        else:
          print ", ".join([" ".join([markup_inline_word(format,convert(word,"espeak",format)) for word in line.split()]) for line in filter(lambda x:x,r.read().split("\n"))])
    elif '--syllables' in sys.argv:
        i=sys.argv.index('--syllables')
        txt=getInputText(i+1,"word(s)");words=txt.split()
        w,r=os.popen4("espeak -q -x",bufsize=max(8192,3*len(txt))) # TODO: same as above (bufsize)
        w.write('\n'.join(words).replace("!","").replace(":","")) ; w.close()
        rrr = r.read().split("\n")
        print " ".join([hyphenate(word,sylcount(convert(line,"espeak","festival"))) for word,line in zip(words,filter(lambda x:x,rrr))])
    elif '--phones2phones' in sys.argv:
        i=sys.argv.index('--phones2phones')
        format1,format2 = sys.argv[i+1],sys.argv[i+2]
        text=getInputText(i+3,"phones in "+format1+" format")
        if getSetting(format1,'space_separates_words_not_phonemes'):
          for w in text.split(): print markup_inline_word(format2, convert(w,format1,format2))
        else: print markup_inline_word(format2, convert(text,format1,format2))
    elif '--convert' in sys.argv:
        i=sys.argv.index('--convert')
        fromFormat = sys.argv[i+1]
        toFormat = sys.argv[i+2]
        assert not fromFormat==toFormat, "cannot convert a lexicon to its own format (that could result in it being truncated)"
        assert not toFormat=="mac-uk", "Cannot permanently save a Mac-UK lexicon; please use the --mac-uk option to read text"
        try: fname=getSetting(toFormat,"lex_filename")
        except KeyError: raise Exception("Write support for lexicons of format '%s' not yet implemented; try using --phones or --phones2phones options instead" % (toFormat,))
        if toFormat=="espeak":
            assert fname=="en_extra", "If you changed eSpeak's lex_filename in the table you also need to change the code below"
            try: open("en_list")
            except: raise Exception("You should cd to the espeak source directory before running this")
            os.system("mv en_extra en_extra~ ; grep \" // \" en_extra~ > en_extra") # keep the commented entries, so can incrementally update the user lexicon only
            outFile=open(fname,"a")
        else:
            l = 0
            try: l = open(fname).read()
            except: pass
            assert not l, "File "+fname+" already exists and is not empty; are you sure you want to overwrite it?  (Delete it first if so)" # (if you run with python -O then this is ignored, as are some other checks so be careful)
            outFile=open(fname,"w")
        print "Writing lexicon entries to",fname
        convert_user_lexicon(fromFormat,toFormat,outFile)
        if toFormat=="bbcmicro": print_bbclex_instructions(fname,outFile.tell())
        outFile.close()
        if toFormat=="bbcmicro" and bbcStart:
          pokes = bbcPokes(open(fname).read(),bbcStart)
          open(fname+".key","w").write(pokes)
          print "For ease of transfer to emulators etc, a self-contained keystroke file for putting "+fname+" data at &"+bbchex(bbcStart)+" has been written to "+fname+".key (but read the above first!)"
          if len(pokes) > 32767: print "(This file looks too big for BeebEm to paste though)" # see comments elsewhere
        if toFormat=="espeak": os.system("espeak --compile=en")
    elif '--mac-uk' in sys.argv:
        i=sys.argv.index('--mac-uk')
        fromFormat = sys.argv[i+1]
        accum = []
        convert_user_lexicon(fromFormat,"mac-uk",accum)
        m = MacBritish_System_Lexicon(getInputText(i+2,"text"),os.environ.get("MACUK_VOICE","Daniel"))
        try:
          try: m.read([a[0] for a in accum],[a[1] for a in accum])
          finally: m.close()
        except KeyboardInterrupt:
          sys.stderr.write("Interrupted\n")
    else:
        print program_name
        print "\nAvailable pronunciation formats:"
        keys=lexFormats.keys() ; keys.sort()
        for k in keys:
          print k+": "+getSetting(k,"doc")
        print "\nUse --convert <from-format> <to-format> to convert a user lexicon file.  Expects Festival's .festivalrc to be in the home directory, or espeak's en_extra or Cepstral's lexicon.txt to be in the current directory.\nFor InfoVox/acapela, export the lexicon to acapela.txt in the current directory.\nE.g.: python lexconvert.py --convert festival cepstral"
        print "\nUse --try <format> [<pronunciation>] to try a pronunciation with eSpeak (requires 'espeak' command),\n e.g.: python lexconvert.py --try festival h @0 l ou1\n or: python lexconvert.py --try unicode-ipa '\\u02c8\\u0279\\u026adn\\u0329' (for Unicode put '\\uNNNN' or UTF-8)\n (it converts to espeak format and then uses espeak to play it)\nUse --trymac to do the same as --try but with Mac OS 'say' instead of 'espeak'\nUse --trymac-uk to try it with Mac OS British voices (but see --mac-uk below)"
        print "\nUse --phones2phones <format1> <format2> [<phones in format1>] to perform a one-off conversion of phones from format1 to format2."
        print "\nUse --phones <format> [<words>] to convert 'words' to phones in format 'format'.  espeak will be run to do the text-to-phoneme conversion, and the output will then be converted to 'format'.\nE.g.: python lexconvert.py --phones unicode-ipa This is a test sentence.\nNote that some commercial speech synthesizers do not work well when driven entirely from phones, because their internal format is different and is optimised for normal text."
        print "\nUse --syllables [<words>] to attempt to break 'words' into syllables for music lyrics (uses espeak to determine how many syllables are needed)"
        print "\nUse --festival-dictionary-to-espeak <location> to convert the Festival Oxford Advanced Learners Dictionary (OALD) pronunciation lexicon to ESpeak.\nYou need to specify the location of the OALD file in <location>,\ne.g. for Debian festlex-oald package: python lexconvert.py --festival-dictionary-to-espeak /usr/share/festival/dicts/oald/all.scm\nor if you can't install the Debian package, try downloading http://ftp.debian.org/debian/pool/non-free/f/festlex-oald/festlex-oald_1.4.0.orig.tar.gz, unpack it into /tmp, and do: python lexconvert.py --festival-dictionary-to-espeak /tmp/festival/lib/dicts/oald/oald-0.4.out\nIn all cases you need to cd to the espeak source directory before running this.  en_extra will be overwritten.  Converter will also read your ~/.festivalrc if it exists.  (You can later incrementally update from ~/.festivalrc using the --convert option; the entries from the system dictionary will not be overwritten in this case.)  Specify --without-check to bypass checking the existing espeak pronunciation for OALD entries (much faster, but makes a larger file and in some cases compromises the pronunciation quality)."
        print "\nUse --mac-uk <from-format> [<text>] to speak text in Mac OS 10.7+ British voices while converting from a lexicon in from-format. As these voices do not have user-modifiable lexicons, lexconvert must binary-patch your system's master lexicon; this is at your own risk! (Superuser privileges are needed the first time. A backup of the system file is made, and all changes are restored on normal exit but if you force-quit then you might need to restore the backup manually.) By default the Daniel voice is used; Emily or Serena can be selected by setting the MACUK_VOICE environment variable."

catchingSigs = inSigHandler = False
def catchSignals():
  "We had better try to catch all signals if using MacBritish_System_Lexicon so we can safely clean it up. We raise KeyboardInterrupt instead (need to catch this). Might not work with multithreaded code."
  global catchingSigs
  if catchingSigs: return
  catchingSigs = True
  import signal
  def f(sigNo,*args):
    global inSigHandler
    if inSigHandler: return
    inSigHandler = True
    os.killpg(os.getpgrp(),sigNo)
    raise KeyboardInterrupt
  for n in xrange(1,signal.NSIG):
    if not n==signal.SIGCHLD and not signal.getsignal(n)==signal.SIG_IGN:
      try: signal.signal(n,f)
      except: pass
class MacBritish_System_Lexicon(object):
    """Overwrites some of the pronunciations in the system
    lexicon (after backing up the original).  Cannot
    change the actual words in the system lexicon, so just
    alters pronunciations of words you don't intend to use
    so you can substitute these into your texts.
    Restores the lexicon on close()."""
    instances = {}
    def __init__(self,text="",voice="Daniel"):
        """text is the text you want to speak (so that any
        words used in it that are not mentioned in your
        lexicon are unchanged in the system lexicon);
        text="" means you just want to speak phonemes.
        voice can be Daniel, Emily or Serena."""
        self.voice = False
        assert not voice in MacBritish_System_Lexicon.instances, "There is already another instance of MacBritish_System_Lexicon for the "+voice+" voice"
        assert not os.system("lockfile /tmp/"+voice+".PCMWave.lock") # in case some other process has it
        self.voice = voice
        self.filename = "/System/Library/Speech/Voices/"+voice+".SpeechVoice/Contents/Resources/PCMWave"
        assert os.path.exists(self.filename),"Cannot find an installation of '"+voice+"' on this system"
        if not os.path.exists(self.filename+"0"):
            sys.stderr.write("Backing up "+self.filename+" to "+self.filename+"0...\n") # (you'll need a password if you're not running as root)
            err = os.system("sudo mv \""+self.filename+"\" \""+self.filename+"0\"; sudo cp \""+self.filename+"0\" \""+self.filename+"\"; sudo chown "+str(os.getuid())+" \""+self.filename+"\"")
            assert not err, "Error creating backup"
        lexFile = self.filename+".lexdir"
        if not os.path.exists(lexFile):
            sys.stderr.write("Creating lexdir file...\n")
            err = os.system("sudo touch \""+lexFile+"\" ; sudo chown "+str(os.getuid())+" \""+lexFile+"\"")
            assert not err, "Error creating lexdir"
        import cPickle
        if os.stat(lexFile).st_size: self.wordIndexStart,self.wordIndexEnd,self.phIndexStart,self.phIndexEnd = cPickle.Unpickler(open(lexFile)).load()
        else:
            dat = open(self.filename).read()
            def findW(word,rtnPastEnd=0):
                i = re.finditer(re.escape(word+chr(0)),dat)
                try: n = i.next()
                except StopIteration: raise Exception("word not found in voice file")
                try:
                    n2 = i.next()
                    raise Exception("word does not uniquely identify a byte position (has at least %d and %d)" % (n.start(),n2.start()))
                except StopIteration: pass
                if rtnPastEnd: return n.end()
                else: return n.start()
            self.wordIndexStart = findW("808s")
            self.phIndexStart = findW("'e&It.o&U.e&Its")
            self.wordIndexEnd = findW("zombie",1)
            self.phIndexEnd = findW("'zA+m.bI",1)
            cPickle.Pickler(open(lexFile,"w")).dump((self.wordIndexStart,self.wordIndexEnd,self.phIndexStart,self.phIndexEnd)) 
        self.dFile = open(self.filename,'r+')
        assert len(self.allWords()) == len(self.allPh())
        MacBritish_System_Lexicon.instances[voice] = self
        self.textToAvoid = text ; self.restoreDic = {}
        catchSignals()
    def allWords(self):
        self.dFile.seek(self.wordIndexStart)
        return [x for x in self.dFile.read(self.wordIndexEnd-self.wordIndexStart).split(chr(0)) if x]
    def allPh(self):
        self.dFile.seek(self.phIndexStart)
        def f(l):
            last = None ; r = [] ; pos = self.phIndexStart
            for i in l:
                if re.search(r'[ -~]',i) and not i in ["'a&I.'fo&Un","'lI.@n","'so&Un.j$"] and not (i==last and i in ["'tR+e&I.si"]): r.append((pos,i)) # (the listed pronunciations are secondary ones that for some reason are in the list)
                if re.search(r'[ -~]',i): last = i
                pos += (len(i)+1) # +1 for the \x00
            assert pos==self.phIndexEnd+1 # +1 because the last \00 will result in a "" item after; the above +1 will be incorrect for that item
            return r
        return f([x for x in self.dFile.read(self.phIndexEnd-self.phIndexStart).split(chr(0))])
    def usable_words(self,words_ok_to_redefine=[]):
        for word,(pos,phonemes) in zip(self.allWords(),self.allPh()):
            if not re.match("^[a-z0-9]*$",word): continue # it seems words not matching this regexp are NOT used by the engine
            if not (phonemes and 32<ord(phonemes[0])<127): continue # better not touch those, just in case
            if word in self.textToAvoid and not word in words_ok_to_redefine: continue
            yield word,pos,phonemes
    def check_redef(self,words,phonemes):
        aw = self.allWords() ; ap = 0
        for w,p in zip(words,phonemes):
          w = w.lower()
          if not re.match("^[a-z0-9]*$",w): continue
          if not w in aw: continue
          if not ap:
            ap = self.allPh()
            sys.stderr.write("Warning: some words were already in system lexicon\nword\told\tnew\n")
          sys.stderr.write(w+"\t"+ap[aw.index(w)][1]+"\t"+p+"\n")
    def speakPhones(self,phonesList):
        "Speaks every phonetic word in phonesList"
        words = [str(x)+"s" for x in range(len(phonesList))]
        d = self.setMultiple(words,phonesList)
        os.popen(macSayCommand()+" -v \""+self.voice+"\"",'w').write(" ".join(d.get(w,"") for w in words))
    def read(self,words,phonemes):
        "Reads the text given in the constructor after setting up the lexicon with words:phonemes"
        # self.check_redef(words,phonemes) # uncomment if you want to know about these
        tta = ' '+self.textToAvoid+' '
        words2,phonemes2 = [],[] # keep only the ones actually used in the text (no point setting whole lexicon)
        for ww,pp in zip(words,phonemes):
          if re.search(r"(?i)(?<=[^A-Za-z])"+re.escape(ww)+r"(?=[^A-Za-z])",tta):
            words2.append(ww) ; phonemes2.append(pp)
        for k,v in self.setMultiple(words2,phonemes2).iteritems():
            tta = re.sub(r"(?i)(?<=[^A-Za-z"+chr(0)+"])"+re.escape(k)+r"(?=[^A-Za-z])",chr(0)+v,tta)
        tta = tta.replace(chr(0),'')
        os.popen(macSayCommand()+" -v \""+self.voice+"\"",'w').write(tta)
    def setMultiple(self,words,phonemes):
        "Sets phonemes for words, returning dict of word to substitute word.  Flushes file buffer before return."
        avail = [] ; needed = []
        for word,pos,phon in self.usable_words(words):
            avail.append((len(phon),word,pos,phon))
        for word,phon in zip(words,phonemes):
            needed.append((len(phon),word,phon))
        avail.sort() ; needed.sort() # shortest phon first
        i = 0 ; wDic = {}
        for l,word,phon in needed:
            while avail[i][0] < l:
                i += 1
                if i==len(avail):
                    sys.stderr.write("Could not find enough lexicon slots!\n") # TODO: we passed 'words' to usable_words's words_ok_to_redefine - this might not be the case if we didn't find enough slots
                    self.dFile.flush() ; return wDic
            _,wSubst,pos,oldPhon = avail[i] ; i += 1
            if avail[i][2] in self.restoreDic: oldPhon=None # shouldn't happen if setMultiple is called only once, but might be useful for small experiments in the Python interpreter etc
            self.set(pos,phon,oldPhon)
            wDic[word] = wSubst
        self.dFile.flush() ; return wDic
    def set(self,phPos,val,old=None):
        """Sets phonemes at position phPos to new value.
        Caller should flush the file buffer when done."""
        # print "Debugger: setting %x to %s" % (phPos,val)
        if old:
            assert not phPos in self.restoreDic, "Cannot call set() twice on same phoneme while re-specifying 'old'"
            assert len(val) <= len(old), "New phoneme is too long!"
            self.restoreDic[phPos] = old
        else: assert phPos in self.restoreDic, "Must specify old values (for restore) when setting for first time"
        self.dFile.seek(phPos)
        self.dFile.write(val+chr(0))
    def __del__(self):
        "WARNING - this might not be called before exit - best to call close() manually"
        if not self.voice or not self.voice in MacBritish_System_Lexicon.instances: return # close() already called, or error in the c'tor
        self.close()
    def close(self):
        for phPos,val in self.restoreDic.items():
            self.set(phPos,val)
        self.dFile.close()
        del MacBritish_System_Lexicon.instances[self.voice]
        assert not os.system("rm -f /tmp/"+self.voice+".PCMWave.lock")
        if self.restoreDic: sys.stderr.write("... lexicon for '"+self.voice+"' restored to normal\n")

if __name__ == "__main__": main()
