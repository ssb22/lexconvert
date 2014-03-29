#!/usr/bin/env python

program_name = "lexconvert v0.155 - convert between lexicons of different speech synthesizers\n(c) 2007-2012,2014 Silas S. Brown.  License: GPL"
# with contributions from Jan Weiss (x-sampa, acapela-uk, cmu)

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

# Phoneme Conversion Table:
# Column 'festival': phoneme in Festival's British English notation
# Column 'espeak': approximation in eSpeak, but note that eSpeak's phoneme representation is not that simple (hence some of the code below)
# Column 'sapi': approximation in American English in MS SAPI notation
# Column 'cepstral': phoneme in Cepstral's British English SSML phoneset
# Column 'mac': approximation in American English in Apple's speech notation ([[inpt PHON]]...[[inpt TEXT]] with no spaces between the phonemes)
# Column 'mac-uk': Scansoft/Nuance British voices for Mac OS 10.7+ (system lexicon editing required, see --mac-uk option)
# Column 'x-sampa': X-SAMPA
# Column 'acapela-uk': acapela optimized X-SAMPA for UK English voices (e.g. "Peter")
# Column 'cmu': format of the US English "Carnegie Mellon University Pronouncing Dictionary" (http://www.speech.cs.cmu.edu/cgi-bin/cmudict)
# Column 'bbcmicro': BBC Micro Speech program by David J. Hoskins / Superior 1985 (for discussion of emulators like BeebEm, including copyright considerations, see comments later)
# Column 'unicode-ipa': Unicode IPA, as used on an increasing number of websites
# Column 'latex-ipa': LaTeX IPA package
# Column 'pinyin-approx' (convert TO only): Rough approximation using roughly the spelling rules of Chinese Pinyin (for getting Chinese-only voices to speak some English words - works with some words better than others)
# 0 = 'ditto' (copy the cell above)
# None = no equivalent in this column (used for groups of multiple phonemes which can be broken down into components)
table = [
   ('festival', 'espeak', 'sapi', 'cepstral', 'mac', 'mac-uk', 'x-sampa', 'acapela-uk', 'cmu', 'bbcmicro', 'unicode-ipa','latex-ipa', 'pinyin-approx'),
   # The first entry MUST be the syllable separator:
   ('0', '%', '-', '0', '=','.', '.', '', '0', '', ['','.'],['','.'],''),
   ('1', "'", '1', '1', '1',"'", '"', 0, '1', '1', u'\u02c8','"', '4'), # primary stress - ignoring this for acapela-uk
   ('2', ',', '2', '0', '2',"", '%', 0, '2', '2', u'\u02cc','\\textsecstress{}', '2'), # secondary stress - ignoring this for acapela-uk
   ('', '', '', '', '','', '', 0, '', '', '-','', ''),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, '', '#','\\#',0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, '', ' ',' ',0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, '', '_','\\_',0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, '', '?','?',0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, '', '!','!',0),
   (0, 0, 0, 0, 0, 0, 0, 0, 0, '', ',',',',0),
   ('aa', ['A:', 'A@', 'aa'], 'aa', 'a', 'AA',"A", 'A', 'A:', 'AA', 'AA', u'\u0251','A','a5'), # a as in ah
   (0, 'A', 0, 0, 0,0, 0, 0, '2', 0, 0,0,0),
   (0, 'A:', 0, 0, 0,0, ':', 0, '1', 0, u'\u02d0',':',0),
   (0, 0, 0, 0, 0,0, 'A:', 0, 'AA', 0, u'\u0251\u02d0','A:',0),
   (0, 0, 0, 0, 0,0, 'Ar\\', 0, 0, 0, u'\u0251\u0279','A\\textturnr{}',0),
   (0, 0, 0, 0, 'aa',0, 'a:', 0, 0, 0, 'a\\u02d0','a:',0),
   ('a', ['a', '&'], 'ae', 'ae', 'AE','@', '{', '{', 'AE', 'AE', [u'\xe6','a'],'\\ae{}','ya5'), # a as in apple
   ('uh', 'V', 'ah', 'ah', 'UX','$', 'V', 'V', 'AH', 'AH', u'\u028c','2','e5'), # u as in but, or the first part of un as in hunt
   ('o', '0', 'ao', 'oa', 'AA','A+', 'Q', 'Q', 'AA', 'O', u'\u0252','6','yo5'),
   (0, 0, 0, 0, 0,0, 'A', 'A', 0, 0, u'\u0251','A',0),
   (0, 0, 0, 0, 0,0, 'O', 'O', 0, 0, u'\u0254','O',0),
   ('au', 'aU', 'aw', 'aw', 'AW','a&U', 'aU', 'aU', 'AW', 'AW', u'a\u028a','aU','ao5'), # o as in now
   (0, 0, 0, 0, 0,0, '{O', '{O', 0, 0, u'\xe6\u0254','\\ae{}O',0),
   ('@', ['@','a#'], 'ax', 'ah', 'AX','E0', '@', '@', 'AH', 'AH', u'\u0259','@','e5'), # a as in ago (TODO: eSpeak sometimes uses a# in 'had' when in a sentence, and this doesn't always sound good on other synths; might sometimes want to convert it to 'a'; not sure what contexts would call for this though)
   ('@@', '3:', 'er', 'er', 0,0, '3:', '3:', 'ER', 'ER', u'\u0259\u02d0','@:','e5'), # e as in herd
   ('@', '3', 'ax', 'ah', 0,0, '@', '@', 'AH', 'AH', u'\u025a','\\textrhookschwa{}','e5'),
   ('@1', 'a2', 0, 0, 0,0, 0, 0, 0, 0, u'\u0259','@', 0),
   ('@2', ['@2','@-'], 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0), # (eSpeak @- is a shorter version of @, TODO: double-check the relationship between @ and @2 in Festival)
   ('ai', ['aI','aI2','aI;','aI2;'], 'ay', 'ay', 'AY','a&I', 'aI', 'aI', 'AY', 'IY', u'a\u026a','aI','ai5'), # eye
   (0, 0, 0, 0, 0,0, 'Ae', 'A e', 0, 0, u'\u0251e','Ae',0),
   ('b', 'b', 'b', 'b', 'b','b', 'b', 'b', 'B ', 'B', 'b','b','bu0'),
   ('ch', 'tS', 'ch', 'ch', 'C','t&S', 'tS', 't S', 'CH', 'CH', [u't\u0283', u'\u02a7'],'tS','che0'),
   ('d', 'd', 'd', 'd', 'd','d', 'd', 'd', 'D ', 'D', 'd','d','de0'),
   ('dh', 'D', 'dh', 'dh', 'D','D', 'D', 'D', 'DH', 'DH', u'\xf0','D','ze0'), # th as in them
   ('e', 'E', 'eh', 'eh', 'EH','E', 'E', 'e', 'EH', 'EH', u'\u025b','E','ye5'), # e as in them
   (0, 0, 'ey', 0, 0,0, 'e', 0, 0, 0, 'e','e',0),
   ('@@', '3:', 'er', 'er', 'AX','0', '3:', '3:', 'ER', 'ER', [u'\u025d', u'\u025c\u02d0'],'3:','e5'), # -ar of year
   ('e@', 'e@', 'eh r', 'e@', 'EH r','E&$', 'E@', 'e @', 0, 'AI', u'\u025b\u0259','E@','ye5'), # a as in air
   (0, 0, 0, 0, 0,0, 'Er\\', 'e r', 0, 0, u'\u025b\u0279','E\\textturnr{}',0),
   (0, 0, 0, 0, 0,0, 'e:', 'e :', 0, 0, u'e\u02d0','e:',0),
   (0, 0, 0, 0, 0,0, 'E:', 0, 0, 0, u'\u025b\u02d0','E:',0),
   (0, 0, 0, 0, 0,0, 'e@', 'e @', 0, 0, u'e\u0259','e@',0),
   ('ei', 'eI', 'ey', 'ey', 'EY','e&I', 'eI', 'eI', 'EY', 'AY', u'e\u026a','eI','ei5'), # a as in ate
   (0, 0, 0, 0, 0,0, '{I', '{I', 0, 0, u'\xe6\u026a','\\ae{}I',0),
   ('f', 'f', 'f', 'f', 'f','f', 'f', 'f', 'F ', 'F', 'f','f','fu0'),
   ('g', 'g', 'g', 'g', 'g','g', 'g', 'g', 'G ', 'G', [u'\u0261', 'g'],'g','ge0'),
   ('h', 'h', 'h', 'h', 'h','h', 'h', 'h', 'HH', '/H', 'h','h','he0'), # Jan suggested "hh" for SAPI, but it doesn't work on XP
   ('i', ['I','I;','i'], 'ih', 'ih', 'IH','I', 'I', 'I', 'IH', 'IH', u'\u026a','I','yi5'), # i as in it
   (0, 0, 0, 0, 0,0, '1', '1', 0, 0, u'\u0268','1',0),
   (0, ['I','I2','I2;'], 0, 0, 'IX',0, 'I', 'I', 0, 'IX', u'\u026a','I',0), # (IX sounds like a slightly shorter version of IH on the BBC)
   ('i@', 'i@', 'iy ah', 'i ah', 'IY UX','E0', 'I@', 'I@', 'EY AH', 'IXAH', u'\u026a\u0259','I@','yi3re5'), # ear
   (0, 0, 0, 0, 0,0, 'Ir\\', 'I r', 0, 0, u'\u026a\u0279','I\\textturnr{}',0),
   ('ii', ['i:','i:;'], 'iy', 'i', 'IY','i', 'i', 'i', 'IY', 'EE', 'i','i','yi5'), # e as in eat
   (0, 0, 0, 0, 0,0, 'i:', 'i:', 0, 0, u'i\u02d0','i:',0),
   ('jh', 'dZ', 'jh', 'jh', 'J','d&Z', 'dZ', 'dZ', 'JH', 'J', [u'd\u0292', u'\u02a4'],'dZ','zhe0'), # j as in jump
   ('k', 'k', 'k', 'k', 'k','k', 'k', 'k', 'K ', 'K', 'k','k','ke0'),
   (0, 'x', 0, 0, 0,0, 'x', 'x', 0, 0, 'x','x',0), # actually 'x' is like Scottish 'loch', but if the synth can't do that then try k 
   ('l', ['l', 'L'], 'l', 'l', 'l','l', 'l', 'l', 'L ', 'L', 'l','l','le0'),
   (0, 0, 0, 0, 0,0, 0, 0, 0, 0, u'd\u026b','d\\textltilde{}',0),
   ('m', 'm', 'm', 'm', 'm','m', 'm', 'm', 'M ', 'M', 'm','m','me0'),
   ('n', 'n', 'n', 'n', 'n','n', 'n', 'n', 'N ', 'N', 'n','n','ne0'),
   ('ng', 'N', 'ng', 'ng', 'N','nK', 'N', 'N', 'NG', 'NX', u'\u014b','N','eng0'),
   ('ou', 'oU', 'ow', 'ow', 'OW','o&U', '@U', '@U', 'OW', 'OW', u'\u0259\u028a','@U','ou5'), # o as in go
   (0, 0, 0, 0, 0,0, 0, 0, 0, 0, 'o', 'o', 0),
   (0, 0, 0, 0, 0,0, 'oU', 'o U', 0, 0, u'o\u028a','oU',0),
   (0, 0, 0, 0, 0,0, '@}', '@ }', 0, 0, u'\u0259\u0289','@0',0),
   (None, 'oUl', None, None, None,None, None, None, None, 'OL', None,None,None), # ol as in gold (espeak says it in a slightly 'posh' way though)
   ('oi', 'OI', 'oy', 'oy', 'OY','O&I', 'OI', 'OI', 'OY', 'OY', u'\u0254\u026a','OI','ruo2yi5'), # oy as in toy
   (0, 0, 0, 0, 0,0, 'oI', 'o I', 0, 0, u'o\u026a','oI',0),
   ('p', 'p', 'p', 'p', 'p','p', 'p', 'p', 'P ', 'P', 'p','p','pu0'),
   ('r', ['r','r-'], 'r', 'r', 'r','R+', 'r\\', 'r', 'R ', 'R', u'\u0279','\\textturnr{}','re0'),
   (0, 0, 0, 0, 0,0, 'r', 0, 0, 0, 'r','r',0),
   ('s', 's', 's', 's', 's','s', 's', 's', 'S ', 'S', 's','s','se0'),
   ('sh', 'S', 'sh', 'sh', 'S','S', 'S', 'S', 'SH', 'SH', u'\u0283','S','she0'),
   ('t', 't', 't', 't', 't','t', 't', 't', 'T ', 'T', 't','t','te0'),
   (0, 0, 0, 0, 0,0, 0, 0, 0, 0, u'\u027e','R', 0),
   ('th', 'T', 'th', 'th', 'T','T', 'T', 'T', 'TH', 'TH', u'\u03b8','T','zhe0'),
   ('u@', 'U@', 'uh', 'uh', 'UH','O', 'U@', 'U@', 'UH', ['AOR','UH'], u'\u028a\u0259','U@','wu5'), # oor as in poor
   (0, 0, 0, 0, 0,0, 'Ur\\', 'U r', 0, 0, u'\u028a\u0279','U\\textturnr{}',0),
   ('u', ['U','@5'], 0, 0, 0,'U', 'U', 'U', 0, ['UH','/U'], u'\u028a','U',0), # u as in pull (espeak also used U for the o in good; bbcmicro defaults to UH4)
   (None, 'Ul', None, None, None,None, None, None, None, '/UL', None,None,None),
   ('uu', 'u:', 'uw', 'uw', 'UW','U', '}:', 'u:', 'UW', ['UW','UX'], u'\u0289\u02d0','0:','yu5'), # oo as in food
   (0, 0, 0, 0, 0,0, 'u:', 0, 0, 0, u'u\u02d0', 'u:',0),
   (0, 0, 0, 0, 0,0, 0, 0, 0, 0, 'u', 'u', 0),
   ('oo', 'O:', 'AO', 'ao', 'AO','O', 'O:', 'O:', 'AO', 'AO', u'\u0254\u02d0','O:','huo5'), # close to 'or'
   (0, 0, 0, 0, 0,0, 'O', 'O', 0, 0, u'\u0254','O',0),
   (0, 0, 0, 0, 0,0, 'o:', 'O:', 0, 0, u'o\u02d0','o:',0),
   (0, ['O@', 'o@', 'O'], 0, 0, 0,0, 'O:', 0, 0, 0, u'\u0254\u02d0','O:',0),
   ('v', 'v', 'v', 'v', 'v','v', 'v', 'v', 'V ', 'V', 'v','v','fu0'),
   ('w', 'w', 'w', 'w', 'w','w', 'w', 'w', 'W ', 'W', 'w','w','wu0'),
   (0, 0, 0, 0, 0,0, 'W', 0, 0, 0, u'\u028d','\\textturnw{}',0), # Jan suggested "x" for SAPI here, but that doesn't work on XP
   ('y', 'j', 'y', 'j', 'y','j', 'j', 'j', 'Y ', 'Y', 'j','j','yu0'),
   ('z', 'z', 'z', 'z', 'z','z', 'z', 'z', 'Z ', 'Z', 'z','z','ze0'),
   ('zh', 'Z', 'zh', 'zh', 'Z','Z', 'Z', 'Z', 'ZH', 'ZH', u'\u0292','Z','zhe0'), # ge of blige etc
   # TODO \u0294 (glottal stop) to eSpeak? (for local dialects), latex-ipa is 'P'
   # TODO bbcmicro also has CT as in fact, DR as in dragon, DUX as in duke, TR as in track
   # Hack (must be at end) - make sure all dictionaries have an entry for '@', for the @l rule:
   ('@', '@', '@', 'ah', 'AX','E0', '@', '@', '@', 'AH', u'\u0259','@','wu5'),
   (0, 0, 'ax', '@', 0,0, 0, 0, 0, 0, 0,0,0),
   (0, 0, 0, 'ah', '@',0, 0, 0, 0, 0, 0,0,0),
   (0, 0, 0, 0, 'AX',0, 0, 0, 0, '@', '@',0,0),
]

space_separates_words_not_phonemes = ["espeak","mac","mac-uk","unicode-ipa","latex-ipa","x-sampa","bbcmicro","pinyin-approx"]
noughts_used_other_than_stress = ["espeak","latex-ipa","mac-uk"] # and might need special-case code in convert()
stress_comes_before_vowel = ["espeak","unicode-ipa","latex-ipa","mac-uk"] # otherwise after

espeak_consonants = "bdDfghklmnNprsStTvwjzZ"

import commands,sys,re,os

for row in table: assert len(row)==len(table[0]),"Wrong row length: "+repr(row) # sanity-check the table

def compare_tables(table1,table2,colsToIgnore):
  # Debug function to compare 2 versions of the table
  def checkDuplicateRows(t,which):
    d = {}
    for i in t:
      if d.has_key(i): print "Warning: duplicate row in "+which+":",i
      d[i]=1
  checkDuplicateRows(table1,"first table") ; checkDuplicateRows(table2,"second table")
  for col in table1[0]:
    if col not in table2[0]: print "Deleted column:",col
  for col in table2[0]:
    if col not in table1[0]: print "Added column:",col
  maps = [{}, {}]
  commonCols = filter(lambda x:x in table2[0],table1[0])
  for dx in [0,1]:
    table = [table1,table2][dx]
    for col1 in commonCols:
      if col1 in colsToIgnore: continue
      i1 = list(table[0]).index(col1)
      for col2 in filter(lambda x: x>col1, commonCols):
        if col2 in colsToIgnore: continue
        i2 = list(table[0]).index(col2)
        for row in table[1:]:
          if not row[i1] or not row[i2]: continue # don't bother reporting mappings involving null strings - they don't matter
          maps[dx][(col1,row[i1],col2,row[i2])] = True
  deleted_mappings = filter(lambda k:not maps[1].has_key(k), maps[0].keys())
  added_mappings = filter(lambda k:not maps[0].has_key(k), maps[1].keys())
  def simplify_mappings(mappings,which):
    byRow = {} ; byCol = {}
    for k1,v1,k2,v2 in mappings:
      if not byRow.has_key((k1,v1)): byRow[(k1,v1)]=[]
      byRow[(k1,v1)].append((k2,v2))
      if not byCol.has_key((k2,v2)): byCol[(k2,v2)]=[]
      byCol[(k2,v2)].append((k1,v1))
    byColCopy = byCol.copy()
    for r in byRow.keys():
      rowLen = len(r)
      maxColLen = max(map(lambda c:len(byCol[c]),byRow[r]))
      if rowLen > maxColLen:
        if len(byRow[r])>1: word="mappings:"
        else: word="mapping"
        print which,word,r,"to",byRow[r]
        for k in byColCopy.keys():
          if r in byColCopy[k]: byColCopy[k].remove(r)
    for c in filter(lambda x:byColCopy[x],byColCopy.keys()):
      if len(byColCopy[c])>1: word="mappings:"
      else: word="mapping"
      print which,word,c,"to",byColCopy[c]
  simplify_mappings(deleted_mappings,"Deleted")
  simplify_mappings(added_mappings,"Added")

# e.g. if someone sends in newlexconvert.py and you want to review all changes not involving sampa/acapela:
# import lexconvert,newlexconvert
# lexconvert.compare_tables(lexconvert.table,newlexconvert.table,['x-sampa', 'acapela-uk'])

def squash_table(colsToDelete):
  # For maintenance use.  Deletes colsToDelete, and introduces dittos/list-alternatives
  colsToDelete=map(lambda c:list(table[0]).index(c),colsToDelete)
  colsToDelete.sort() ; colsToDelete.reverse()
  ret = [] ; lastRow = None
  for row in table:
    row=list(row)
    for c in colsToDelete: del row[c]
    if ret:
      for i in range(len(row)):
        k=-1
        while ret[k][i]==0: k -= 1
        if row[i]==ret[k][i]: row[i]=0
      if len(filter(lambda x:not x==0,row))==1:
        # only 1 thing changed
        ret[-1]=list(ret[-1])
        for i in range(len(row)):
          if not row[i]==0:
            if not type(ret[-1][i])==type([]): ret[-1][i]=[ret[-1][i]]
            ret[-1][i].append(row[i])
        ret[-1]=tuple(ret[-1])
        continue
    ret.append(tuple(row))
  # return ret
  print "table = ["
  for r in ret: print "   "+repr(r)+","
  print "]"

# Deal with any rows that contain lists of alternatives
# or 0 (ditto) marks
# If multiple lists in a row e.g. ([ab],[cd]), give [(a,c), (b,c), (a,d)], as (b,d) would never be reached anyway.
# (Removing duplicates and redundant rows is not really necessary but may help debugging)
newTable=[] ; hadAlready = {}
prevLine = None
for line in table:
  line=list(line)
  for i in range(len(line)):
    if line[i]==0: line[i]=prevLine[i]
  line=tuple(line)
  colsWithLists = filter(lambda col: type(line[col])==type([]), range(len(line)))
  if not colsWithLists: newTable.append(line)
  for col in colsWithLists:
    def firstItemIfList(l):
      if type(l)==type([]): return l[0]
      else: return l
    for extraTuple in [tuple(map(lambda x:firstItemIfList(x),list(line[:col])+[i]+list(line[col+1:]))) for i in line[col]]:
      if hadAlready.has_key(extraTuple): continue
      hadAlready[extraTuple]=1
      newTable.append(extraTuple)
  prevLine = line
table = newTable

cached_source,cached_dest,cached_dict = None,None,None
def make_dictionary(source,dest):
    global cached_source,cached_dest,cached_dict
    if (source,dest) == (cached_source,cached_dest): return cached_dict
    types = list(table[0])
    assert source in types,"Unknown synthesizer name to convert from: "+repr(source)
    assert dest in types, "Unknown synthesizer name to convert to: "+repr(dest)
    source,dest = types.index(source), types.index(dest)
    d = {}
    global dest_consonants ; dest_consonants = []
    global dest_syllable_sep ; dest_syllable_sep = table[1][dest]
    for l in table[1:]:
        if l[source]==None or l[dest]==None: continue
        if not l[source] in d: d[l[source]]=l[dest]
        is_in_espeak_consonants=True
        for cTest in l[1]:
            if cTest not in espeak_consonants:
                is_in_espeak_consonants=False; break
        if is_in_espeak_consonants: dest_consonants.append(l[dest])
    cached_source,cached_dest,cached_dict=source,dest,d
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
    while pronunc:
        for lettersToTry in range(maxLen,-1,-1):
            if not lettersToTry:
              if source=="espeak" and not pronunc[0] in "_: !": sys.stderr.write("Warning: ignoring unknown espeak character "+repr(pronunc[0])+debugInfo+"\n")
              pronunc=pronunc[1:] # ignore
            elif dictionary.has_key(pronunc[:lettersToTry]):
                debugInfo=" after "+pronunc[:lettersToTry]
                toAdd=dictionary[pronunc[:lettersToTry]]
                if toAdd in ['0','1','2','4'] and not dest in noughts_used_other_than_stress: # it's a stress mark in a notation that places stress marks AFTER vowels (noughts_used_other_than_stress case handled below)
                    if dest=="bbcmicro": # normal pitch is 6, and lower numbers are higher pitches, so try 5=secondary stress and 4=primary stress (3 sounds less calm)
                      if toAdd=='1': toAdd='4'
                      elif toAdd=='2': toAdd='5'
                    if source in stress_comes_before_vowel: toAdd, toAddAfter = "",toAdd # move before to after
                    else:
                        # With Cepstral synth, stress mark should be placed EXACTLY after the vowel and not any later.  Might as well do this for others also.
                        # (not dest in ["espeak","latex-ipa"] because they use 0 as a phoneme; dealt with separately below)
                        r=len(ret)-1
                        while ret[r] in dest_consonants or ret[r].endswith("*added"): r -= 1 # (if that raises IndexError then the input had a stress mark before any vowel) ("*added" condition is there so that implicit vowels don't get the stress)
                        ret.insert(r+1,toAdd) ; toAdd=""
                elif ((toAdd in u"',\u02c8\u02cc" and dest in ["espeak","unicode-ipa","mac-uk"]) or (toAdd in ['"','\\textsecstress{}'] and dest=="latex-ipa")) and not source in stress_comes_before_vowel: # it's a stress mark that should be moved from after the vowel to before it
                    i=len(ret)
                    while i and (ret[i-1] in dest_consonants or ret[i-1].endswith("*added")): i -= 1
                    if i: i-=1
                    ret.insert(i,toAdd)
                    if dest_syllable_sep: ret.append(dest_syllable_sep) # (TODO: this assumes stress marks are at end of syllable rather than immediately after vowel; correct for Festival; check others; probably a harmless assumption though; mac-uk is better with syllable separators although espeak basically ignores them)
                    toAdd = ""
                # attempt to sort out the festival dictionary's (and other's) implicit @ (TODO or is it an implicit uh ?):
                elif ret and ret[-1] and toAdd in ['n','l'] and ret[-1] in dest_consonants: ret.append(dictionary['@']+'*added')
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
                if source=="espeak" and pronunc[:lettersToTry]=="e@" and len(pronunc)>lettersToTry and pronunc[lettersToTry]=="r" and (len(pronunc)==lettersToTry+1 or pronunc[lettersToTry+1] in espeak_consonants): lettersToTry += 1 # hack because the 'r' is implicit in other synths (but DO have it if there's another vowel to follow)
                pronunc=pronunc[lettersToTry:]
                break
    if toAddAfter: ret.append(toAddAfter)
    if ret and ret[-1]==dest_syllable_sep: del ret[-1] # spurious syllable separator at end
    if dest in space_separates_words_not_phonemes: separator = ''
    else: separator = ' '
    ret=separator.join(ret).replace('*added','')
    if dest=="cepstral": return ret.replace(" 1","1").replace(" 0","0")
    if dest=="pinyin-approx":
        for s,r in [
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
        
        ]: ret=re.sub(s,r,ret)
    if dest=="espeak": return cleanup_espeak_entry(ret)
    elif dest=="mac-uk": return ret.replace("o&U.Ol","o&Ul")
    else: return ret

def cleanup_espeak_entry(r):
    r = r.replace("k'a2n","k'@n").replace("ka2n","k@n").replace("gg","g").replace("@U","oU") # (eSpeak uses oU to represent @U; difference is given by its accent parameters)
    if r.endswith("i@r"): return r[:-3]+"i@"
    if r.endswith("U@r"): return r[:-3]+"U@"
    elif r.endswith("@r") and not r.endswith("e@r"): return r[:-2]+"3"
    if r.endswith("A:r"): return r[:-3]+"A@"
    if r.endswith("O:r"): return r[:-3]+"O@"
    # if r.endswith("@l") and not r.endswith("i@l") and not r.endswith("U@l"): return r[:-2]+"@L" # only in older versions of espeak (not valid in more recent versions)
    if r.endswith("rr") or r.endswith("3:r"): return r[:-1]
    # TODO: 'declared' & 'declare' the 'r' after the 'E' sounds a bit 'regional' (but pretty).  but sounds incomplete w/out 'r', and there doesn't seem to be an E2 or E@
    # TODO: consider adding 'g' to words ending in 'N' (if want the 'g' pronounced in '-ng' words) (however, careful of words like 'yankee' where the 'g' would be followed by a 'k'; this may also be a problem going into the next word)
    return r

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

def convert_user_lexicon(fromFormat,toFormat,outFile):
    if fromFormat=="festival": lex = eval('['+commands.getoutput("grep '^(lex.add.entry' ~/.festivalrc | sed -e 's/;.*//' -e 's/[^\"]*\"/[\"/' -e 's/\" . /\",(\"/' -e 's/$/\"],/' -e 's/[()]/ /g' -e 's/  */ /g'")+']')
    elif fromFormat=="espeak": lex = filter(lambda x:len(x)==2,[l.split()[:2] for l in open("en_extra").readlines()])
    elif fromFormat in ["acapela-uk","x-sampa"]:
        lex = []
        for l in open("acapela.txt").readlines():
            word, pronunc, ignore = l.split(None,2)
            if pronunc.startswith("#"): pronunc=pronunc[1:]
            lex.append((word,pronunc))
    elif fromFormat=="cepstral":
        lex = []
        for l in open("lexicon.txt").readlines():
            word, ignore, pronunc = l.split(None,2)
            lex.append((word,pronunc))
    else: raise Exception("Reading from '%s' lexicon file not yet implemented" % (fromFormat,))
    if toFormat=="mac": outFile.write("# I don't yet know how to add to the Apple US lexicon,\n# so here is a 'sed' command you can run on your text\n# to put the pronunciation inline:\n\nsed")
    elif "sapi" in toFormat: outFile.write("rem  You have to run this file\nrem  with ptts.exe in the same directory\nrem  to add these words to the SAPI lexicon\n\n")
    elif toFormat=="unicode-ipa": outFile.write("""<html><head><meta name="mobileoptimized" content="0"><meta name="viewport" content="width=device-width"><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></head><body><table>""")
    elif toFormat=="latex-ipa": outFile.write(r"""\documentclass[12pt,a4paper]{article} \usepackage[safe]{tipa} \usepackage{longtable} \begin{document} \begin{longtable}{ll}""")
    elif toFormat=="pinyin-approx": outFile.write("Pinyin approxmations (very approximate!)\n----------------------------------------\n")
    for word, pronunc in lex:
        pronunc = convert(pronunc,fromFormat,toFormat)
        if toFormat=="espeak": outFile.write(word+" "+pronunc+"\n")
        elif "sapi" in toFormat: outFile.write("ptts -la "+word+" \""+pronunc+"\"\n")
        elif toFormat=="cepstral": outFile.write(word.lower()+" 0 "+pronunc+"\n")
        elif toFormat=="mac": outFile.write(" -e \"s/"+word+"/[[inpt PHON]]"+pronunc+"[[inpt TEXT]]/g\"")
        elif toFormat=="bbcmicro": outFile.write("> "+word.upper()+"_"+chr(128)+pronunc) # (specifying 'whole word'; remove the space before or the _ after if you want)
        elif toFormat=="unicode-ipa": outFile.write("<tr><td>"+word+"</td><td>"+pronunc.encode("utf-8")+"</td></tr>\n")
        elif toFormat=="latex-ipa": outFile.write(word+r" & \textipa{"+pronunc+r"}\\"+"\n")
        elif toFormat=="pinyin-approx": outFile.write(word+" ~= "+pronunc+"\n")
        elif toFormat in ["acapela-uk","x-sampa"]: outFile.write(word+chr(9)+"#"+pronunc+chr(9)+"UNKNOWN\n") # TODO may be able to convert part-of-speech (NOUN etc) to/from some other formats e.g. Festival
        elif toFormat=="mac-uk": outFile.append((word,pronunc)) # (it's not really a file)
        else: raise Exception("Writing to lexicon in %s format not yet implemented" % (format,))
    if toFormat=="mac": outFile.write("\n")
    elif toFormat=="bbcmicro": close_bbclex(outFile)
    elif toFormat=="unicode-ipa": outFile.write("</table></body></html>\n")
    elif toFormat=="latex-ipa": outFile.write("\end{longtable}\end{document}\n")

bbc_charsSoFar=0 # hack for bbcmicro
first_word=True # hack for TeX
def markup_inline_word(format,pronunc):
    global first_word,bbc_charsSoFar
    if format=="espeak": return "[["+pronunc+"]]"
    elif format=="mac": return "[[inpt PHON]]"+pronunc+"[[inpt TEXT]]"
    elif "sapi" in format: return "<pron sym=\""+pronunc+"\"/>"
    elif format=="cepstral": return "<phoneme ph='"+pronunc+"'>p</phoneme>"
    elif format=="acapela-uk": return "\\Prn="+pronunc+"\\"
    elif format=="bbcmicro":
      # BBC Micro Speech program by David J. Hoskins / Superior 1985.  Took 7.5k of RAM including 3.1k of samples (49 phonemes + 1 for fricatives at 64 bytes each, 4-bit ~5.5kHz), 2.2k of lexicon, and 2.2k of machine code; "retro" by modern standards but ground-breaking at the time.
      # If you use an emulator like BeebEm, you'll need diskimg/Speech.ssd.  This can be made from your original Speech disc, or you might be able to find one but beware of copyright!  Same goes with the Model B ROM images included in BeebEm (you might want to delete the other models).  There has been considerable discussion over whether UK copyright law does or should allow "format-shifting" your own legally-purchased media, and I don't fully understand all the discussion so I don't want to give advice on it here.  The issue is "format-shifting" your legally-purchased BBC Micro ROM code and Speech disc to emulator images; IF this is all right then I suspect downloading someone else's copy is arguably allowed as long as you bought it legally "back in the day", but I'm not a solicitor so I don't know.
      # lexconvert's --phones bbcmicro option creates *SPEAK commands which you can type into the BBC Micro or paste into an emulator (e.g. BeebEm), either at the BASIC prompt or in a listing (with line numbers provided by AUTO).  You have to load the Speech program first of course.
      # To script this, first turn off the Speech disc's boot option (by turning off File / Disc options / Write protect and entering "*OPT 4,0"; use "*OPT 4,3" if you want it back later), and then you can do (e.g. on a Mac) open /usr/local/BeebEm3/diskimg/Speech.ssd && sleep 1 && (echo '*SPEECH';python lexconvert.py --phones bbcmicro "Greetings from 19 85") | pbcopy && osascript -e 'tell application "System Events" to keystroke "v" using command down'
      # or if you know it's already loaded: echo "Here is some text" | python lexconvert.py --phones bbcmicro | pbcopy && osascript -e 'tell application "BeebEm3" to activate' && osascript -e 'tell application "System Events" to keystroke "v" using command down'
      # (unfortunately there doesn't seem to be a way of doing it without giving the emulator window focus)
      if not bbc_charsSoFar or bbc_charsSoFar+len(pronunc) > 165: # 238 is max len of the immediate BASIC prompt, but get a "Line too long" message from Speech if go over 165 including the '*SPEAK ' (158 excluding it).
        if bbc_charsSoFar: r="\n"
        else: r=""
        bbc_charsSoFar = 7+len(pronunc)+1 # +1 for the space after this word.
        return r+"*SPEAK "+pronunc
      else:
        bbc_charsSoFar += len(pronunc)+1
        return pronunc
    elif format=="unicode-ipa": return pronunc.encode("utf-8") # UTF-8 output - ok for pasting into Firefox etc *IF* the terminal/X11 understands utf-8 (otherwise redirect to a file, point the browser at it, and set encoding to utf-8, or try --convert'ing which will o/p HTML)
    elif format=="latex-ipa":
      if first_word:
         first_word = False
         r=r"% In preamble, put \usepackage[safe]{tipa}"+'\n' # (the [safe] part is recommended if you're mixing with other TeX)
      else: r=''
      return r+"\\textipa{"+pronunc+"}"
    else: return pronunc

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
def close_bbclex(outFile):
  if os.environ.get("SPEECH_DISK",""):
    d=open(os.environ['SPEECH_DISK']).read()
    i=d.index('>OUS_') # if this fails, it wasn't a Speech disk
    j=d.index(">**",i)
    assert j-i==2201, "Lexicon on SPEECH_DISK is wrong size (%d). Is this really an original disk image?" % (j-i)
    outFile.write(d[i:j])
  outFile.write(">**")
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
        if format1 in space_separates_words_not_phonemes:
          for w in text.split(): print markup_inline_word(format2, convert(w,format1,format2))
        else: print markup_inline_word(format2, convert(text,format1,format2))
    elif '--convert' in sys.argv:
        i=sys.argv.index('--convert')
        fromFormat = sys.argv[i+1]
        toFormat = sys.argv[i+2]
        assert not fromFormat==toFormat, "cannot convert a lexicon to its own format (that could result in it being truncated)"
        outFile = None
        if toFormat=="cepstral": fname="lexicon.txt"
        elif toFormat in ["acapela-uk","x-sampa"]: fname="acapela.txt"
        elif "sapi" in toFormat: fname="run-ptts.bat"
        elif toFormat=="mac": fname="substitute.sh"
        elif toFormat=="bbcmicro": fname="BBCLEX"
        elif toFormat=="espeak":
            try: open("en_list")
            except: raise Exception("You should cd to the espeak source directory before running this")
            os.system("mv en_extra en_extra~ ; grep \" // \" en_extra~ > en_extra") # keep the commented entries, so can incrementally update the user lexicon only
            fname="en_extra"
            outFile=open(fname,"a")
        elif toFormat in ["unicode-ipa","latex-ipa","pinyin-approx"]:
            # just make a table of words and pronunciation
            if toFormat=="unicode-ipa":
              fname="words-ipa.html"
            elif toFormat=="pinyin-approx":
              fname="words-pinyin-approx.txt"
            else: fname="words-ipa.tex"
            try:
                open(fname)
                assert 0, fname+" already exists, I'd rather not overwrite it; delete it yourself if you want" # (if you run with python -O then this is ignored, as are some other checks so be careful)
            except IOError: pass
            outFile=open(fname,"w")
        elif toFormat=="mac-uk": raise Exception("Cannot permanently save a Mac-UK lexicon; please use the --mac-uk option to read text")
        else: raise Exception("Don't know where to put lexicon of format '%s', try using --phones or --phones2phones options instead" % (toFormat,))
        if not outFile:
            l = 0
            try: l = open(fname).read()
            except: pass
            assert not l, "File "+fname+" already exists and is not empty; are you sure you want to overwrite it?  (Delete it first if so)"
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
        print "\nAvailable pronunciation formats:",', '.join(list(table[0]))
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
