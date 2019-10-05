#!/usr/bin/env python2

"""test_lexconvert.py - Test lexconvert.py
(c) 2019 Zach DeCook. License: GPL
"""

#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

import io
import lexconvert
import os
import sys

def test_p2p_cmu_espeak(monkeypatch, capsys):
    testargs = ["--phones2phones", "cmu", "espeak", "T AH M AA 1 T OW"]
    monkeypatch.setattr('sys.argv', testargs)

    lexconvert.main()

    captured = capsys.readouterr()
    assert "[[tVm'A:%toU]]" == captured.out.strip()
    assert "" == captured.err


def test_p2p_stdin(monkeypatch, capsys):
    testargs = ["--phones2phones", "cmu", "espeak"]
    cmuIn = u"T AH M EY 1 T OW"
    monkeypatch.setattr('sys.stdin', io.StringIO(cmuIn))
    monkeypatch.setattr('sys.argv', testargs);

    lexconvert.mainopt_phones2phones(0)

    captured = capsys.readouterr()
    assert "[[tVm'eI%toU]]" == captured.out.strip()
    assert "" == captured.err


def test_move_stress():
    espeak = "[[k'aast]] [['O:l]] [[jO@]] [[k'e@z]] [[@p,0n]] [[h,Im]]"
    movedAfter = lexconvert.convert(espeak, source='espeak', dest='names')

    names = "k a_as_in_apple primary_stress s t close_to_or primary_stress l y var3_close_to_or k a_as_in_air primary_stress z a_as_in_ago p o_as_in_orange secondary_stress n h i_as_in_it secondary_stress m"
    assert names == movedAfter

    improperStressLocations = "B IH K AH Z 1 HH IY K ER Z 1 F AO Y UW"
    names = lexconvert.convert(improperStressLocations, source='cmu', dest='names')
    fixedStressLocations = lexconvert.convert(names, source='names', dest='cmu')
    assert "B IH K AH 1 Z HH IY K ER 1 Z F AO Y UW" == fixedStressLocations

def test_braille_unicode():
    brailleAscii = ",7A/7' ,7W_B4*NS7' ,7W4*Z7' ,7L_B4*ST7' ,7B_2+T7' ,7N_BA(7' ,7%M7' ,7F_BA(ND7'"
    value = lexconvert.ascii_braille_to_unicode(brailleAscii)
    expected = u'\u2820\u2836\u2801\u280c\u2836\u2804 \u2820\u2836\u283a\u2838\u2803\u2832\u2821\u281d\u280e\u2836\u2804 \u2820\u2836\u283a\u2832\u2821\u2835\u2836\u2804 \u2820\u2836\u2807\u2838\u2803\u2832\u2821\u280e\u281e\u2836\u2804 \u2820\u2836\u2803\u2838\u2806\u282c\u281e\u2836\u2804 \u2820\u2836\u281d\u2838\u2803\u2801\u2837\u2836\u2804 \u2820\u2836\u2829\u280d\u2836\u2804 \u2820\u2836\u280b\u2838\u2803\u2801\u2837\u281d\u2819\u2836\u2804'
    assert expected == value.replace(u'\u2800',' ')

def test_festival_group_stress():
    festival = "(((m ai) 0) ((t ai m) 1) ((h uh z) 0) ((n aa t) 0) ((y e t) 1) ((k uh m) 1))"
    value = lexconvert.convert(festival, source='festival', dest='festival-cmu')
    # TODO: See note in festival_group_stress about adding consonant to previous group.
    festcmu = "(((m ay) 0) ((t ay) 1) ((m hh ah) 0) ((z n aa) 0) ((t y eh) 1) ((t k ah m) 1))"
    assert festcmu == value

def test_hiragana_to_katakana():
    # TODO: kana-approx does not like the brackets from espeak
    espeak = "[[h,aU]] [[t@]] [[sp'i:k]]".replace('[','').replace(']','')
    os.environ['KANA_TYPE'] = ''
    value = lexconvert.convert(espeak, source='espeak', dest='kana-approx')
    expected = u'\u306f\u304a \u3064\u304a \u3059\u3074\u30fc\u304f'
    assert expected.replace(' ','') == value.replace(' ','')

    os.environ['KANA_TYPE'] = 'k'
    result = lexconvert.hiragana_to_katakana(expected)
    katakana = u'\u30cf\u30aa \u30c4\u30aa \u30b9\u30d4\u30fc\u30af'
    assert katakana == result
