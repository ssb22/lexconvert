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
import lexconvert
from mock import patch

def test_p2p_cmu_espeak(capsys):
    testargs = ["--phones2phones", "cmu", "espeak", "T AH M AA 1 T OW"]
    with patch.object(sys, 'argv', testargs):
        lexconvert.main()
        captured = capsys.readouterr()
        assert "[[tVm'A:%toU]]" == captured.out.strip()
        assert "" == captured.err
