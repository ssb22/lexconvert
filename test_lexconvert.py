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

import sys
import io
import lexconvert

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
