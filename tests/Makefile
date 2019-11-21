# Tests lexconvert's basic convert and phones2phones options in both Python 2 and Python 3.
# (Separate make rules in case need two separate containers for Python 2 and Python 3.)
# Does not perform any tests that require eSpeak, Mac, or the BBC Micro disk image
# (those still need manual testing).

SHELL=/bin/bash

test-lexconvert: test2 test3
	@echo All tests passed

test2:
	python2 ../lexconvert.py --help >/dev/null
	python2 ../lexconvert.py --htmlhelp >/dev/null
	[ "$$(python2 -c 'import sys;sys.path.insert(0,"..");import lexconvert; print(lexconvert.convert("\xcb\x88\xc9\x9b\xcb\x90r\xc9\x99n","unicode-rough","unicode-ipa").encode("utf-8"))')" = "ˈɛːɹən" ]
	[ "$$(python2 ../lexconvert.py --phones2phones acapela-uk festival 'S eI " d r { k')" = "(((sh ei) 1) ((d r a k) 0))" ]
	[ "$$(python2 ../lexconvert.py --phones2phones acapela-uk bbcmicro 'S eI " d r { k')" = "*SPEAKSHAY4DRAEK" ]
	[ "$$(python2 ../lexconvert.py --phones2phones acapela-uk bbcmicro-cc 'S eI " d r { k')" = "*UTTER <1> SH *A D R a K" ]
	[ "$$(SPEAKJET_SYM=1 python2 ../lexconvert.py --phones2phones acapela-uk speakjet 'S eI " d r { k')" = "SH EY DO RR AY KO" ]
	[ "$$(python2 ../lexconvert.py --phones2phones acapela-uk speakjet 'S eI " d r { k')" = "189 130 175 148 132 195" ]
	[ "$$(echo $$(SPEAKJET_BINARY=1 python2 ../lexconvert.py --phones2phones acapela-uk speakjet 'S eI " d r { k'|hexdump -x |head -1))" = "0000000 82bd 94af c384 000a" ]
	[ "$$(python2 ../lexconvert.py --phones2phones acapela-uk unicode-ipa 'S eI " d r { k')" = "ʃˈeɪdɹæk" ]
	[ "$$(python2 ../lexconvert.py --phones2phones acapela-uk kana-approx 'S eI " d r { k')" = "しぇいーづらく" ]
	[ "$$(KANA_TYPE=katakana python2 ../lexconvert.py --phones2phones acapela-uk kana-approx 'S eI " d r { k')" = "シェイーヅラク" ]
	[ "$$(python2 ../lexconvert.py --phones2phones acapela-uk braille-ipa 'S eI " d r { k')" = ",7:_BE/D#%K7'" ]
	[ "$$(BRAILLE_UNICODE=1 python2 ../lexconvert.py --phones2phones acapela-uk braille-ipa 'S eI " d r { k')" = "⠠⠶⠱⠸⠃⠑⠌⠙⠼⠩⠅⠶⠄" ]
	[ "$$(python2 ../lexconvert.py --phones2phones unicode-ipa festival ʃˈeɪdɹæk)" = "(((sh ei) 1) ((d r a k) 0))" ]
	[ "$$(python2 ../lexconvert.py --phones2phones braille-ipa festival ",7:_BE/D#%K7'")" = "(((sh ei) 1) ((d r a k) 0))" ]
	[ "$$(python2 ../lexconvert.py --phones2phones braille-ipa festival ⠠⠶⠱⠸⠃⠑⠌⠙⠼⠩⠅⠶⠄)" = "(((sh ei) 1) ((d r a k) 0))" ]
	[ "$$(python2 ../lexconvert.py --phones2phones bbcmicro festival SHAY4DRAEK)" = "(((sh ei) 1) ((d r a k) 0))" ]
	[ "$$(python2 ../lexconvert.py --phones2phones bbcmicro doubletalk SHAY4DRAEK)" = "*DSH / EY D R AE K*T" ]
	rm -rf obj
	mkdir obj
	cd obj && python2 ../../lexconvert.py --convert example espeak && cd .. && diff -u en_extra obj/en_extra && rm obj/en_extra
	cd obj && python2 ../../lexconvert.py --convert example sapi && cd .. && diff -u run-ptts.bat obj/run-ptts.bat && rm obj/run-ptts.bat
	cd obj && python2 ../../lexconvert.py --convert example cepstral && cd .. && diff -u lexicon.txt obj/lexicon.txt && rm obj/lexicon.txt
	cd obj && python2 ../../lexconvert.py --convert example mac && cd .. && diff -u substitute.sh obj/substitute.sh && rm obj/substitute.sh
	cd obj && python2 ../../lexconvert.py --convert example x-sampa && cd .. && diff -u acapela.txt obj/acapela.txt && rm obj/acapela.txt
	cd obj && python2 ../../lexconvert.py --convert example vocaloid && cd .. && diff -u vocaloid.txt obj/vocaloid.txt && rm obj/vocaloid.txt
	cd obj && python2 ../../lexconvert.py --convert example keynote && cd .. && diff -u keynote.dat obj/keynote.dat && rm obj/keynote.dat
	cd obj && python2 ../../lexconvert.py --convert example audapter && cd .. && diff -u audapter.dat obj/audapter.dat && rm obj/audapter.dat
	cd obj && python2 ../../lexconvert.py --convert example bbcmicro && cd .. && diff -u BBCLEX obj/BBCLEX && diff -u BBCLEX.key obj/BBCLEX.key && rm obj/BBCLEX*
	cd obj && python2 ../../lexconvert.py --convert example unicode-ipa && cd .. && diff -u words-ipa.html obj/words-ipa.html && rm obj/words-ipa.html
	cd obj && python2 ../../lexconvert.py --convert example braille-ipa && cd .. && diff -u words-ipa.brl obj/words-ipa.brl && rm obj/words-ipa.brl
	cd obj && BRAILLE_UNICODE=1 python2 ../../lexconvert.py --convert example braille-ipa && cd .. && diff -u words-ipa.txt obj/words-ipa.txt && rm obj/words-ipa.txt
	cd obj && python2 ../../lexconvert.py --convert example latex-ipa && cd .. && diff -u words-ipa.tex obj/words-ipa.tex && rm obj/words-ipa.tex
	cd obj && python2 ../../lexconvert.py --convert example pinyin-approx && cd .. && diff -u words-pinyin-approx.txt obj/words-pinyin-approx.txt && rm obj/words-pinyin-approx.txt
	cd obj && HOME=$$(pwd) python2 ../../lexconvert.py --convert example festival && cd .. && diff -u festivalrc obj/.festivalrc && rm obj/.festivalrc
	cp festivalrc obj/.festivalrc && cd obj && HOME=$$(pwd) python2 ../../lexconvert.py --convert festival espeak && tr -d % < en_extra > 1 && tr -d % < ../en_extra > 2 && diff -u 1 2 && rm 1 2 en_extra .festivalrc && cd .. # ignore syllable separators in this diff
	cp en_extra obj/ && cd obj && HOME=$$(pwd) python2 ../../lexconvert.py --convert espeak festival && diff -u ../festivalrc .festivalrc && rm en_extra .festivalrc && cd ..
	cp lexicon.txt obj/ && cd obj && python2 ../../lexconvert.py --convert cepstral espeak && [ "$$(cat en_extra)" == "shadrach S'eI%drak"$$'\n'"meshach m'i:%Sak"$$'\n'"abednego Vb'E%dni:goU" ] && rm en_extra lexicon.txt && cd .. # approximation + lower
	rmdir obj
	rm -f yinghan-ipa.py
	python2 ../lexconvert.py --convert example yinghan
	[ "$$( (echo "*** ";echo "ehw Meshach")|python2 yinghan-ipa.py)" = $$'*** \nehw Meshach\nipa mˈiʃæk' ]
	rm yinghan-ipa.py
	@echo All Python 2 tests passed
test3:
	python3 ../lexconvert.py --help >/dev/null
	python3 ../lexconvert.py --htmlhelp >/dev/null
	[ "$$(python3 -c 'import sys;sys.path.insert(0,"..");import lexconvert; print(lexconvert.convert("ˈɛːrən".encode("utf-8"),"unicode-rough","unicode-ipa"))')" = "ˈɛːɹən" ]
	[ "$$(python3 ../lexconvert.py --phones2phones acapela-uk festival 'S eI " d r { k')" = "(((sh ei) 1) ((d r a k) 0))" ]
	[ "$$(python3 ../lexconvert.py --phones2phones acapela-uk bbcmicro 'S eI " d r { k')" = "*SPEAKSHAY4DRAEK" ]
	[ "$$(python3 ../lexconvert.py --phones2phones acapela-uk bbcmicro-cc 'S eI " d r { k')" = "*UTTER <1> SH *A D R a K" ]
	[ "$$(SPEAKJET_SYM=1 python3 ../lexconvert.py --phones2phones acapela-uk speakjet 'S eI " d r { k')" = "SH EY DO RR AY KO" ]
	[ "$$(python3 ../lexconvert.py --phones2phones acapela-uk speakjet 'S eI " d r { k')" = "189 130 175 148 132 195" ]
	[ "$$(echo $$(SPEAKJET_BINARY=1 python3 ../lexconvert.py --phones2phones acapela-uk speakjet 'S eI " d r { k'|hexdump -x |head -1))" = "0000000 82bd 94af c384 000a" ]
	[ "$$(python3 ../lexconvert.py --phones2phones acapela-uk unicode-ipa 'S eI " d r { k')" = "ʃˈeɪdɹæk" ]
	[ "$$(python3 ../lexconvert.py --phones2phones acapela-uk kana-approx 'S eI " d r { k')" = "しぇいーづらく" ]
	[ "$$(KANA_TYPE=katakana python3 ../lexconvert.py --phones2phones acapela-uk kana-approx 'S eI " d r { k')" = "シェイーヅラク" ]
	[ "$$(python3 ../lexconvert.py --phones2phones acapela-uk braille-ipa 'S eI " d r { k')" = ",7:_BE/D#%K7'" ]
	[ "$$(BRAILLE_UNICODE=1 python3 ../lexconvert.py --phones2phones acapela-uk braille-ipa 'S eI " d r { k')" = "⠠⠶⠱⠸⠃⠑⠌⠙⠼⠩⠅⠶⠄" ]
	[ "$$(python3 ../lexconvert.py --phones2phones unicode-ipa festival ʃˈeɪdɹæk)" = "(((sh ei) 1) ((d r a k) 0))" ]
	[ "$$(python3 ../lexconvert.py --phones2phones braille-ipa festival ",7:_BE/D#%K7'")" = "(((sh ei) 1) ((d r a k) 0))" ]
	[ "$$(python3 ../lexconvert.py --phones2phones braille-ipa festival ⠠⠶⠱⠸⠃⠑⠌⠙⠼⠩⠅⠶⠄)" = "(((sh ei) 1) ((d r a k) 0))" ]
	[ "$$(python3 ../lexconvert.py --phones2phones bbcmicro festival SHAY4DRAEK)" = "(((sh ei) 1) ((d r a k) 0))" ]
	[ "$$(python3 ../lexconvert.py --phones2phones bbcmicro doubletalk SHAY4DRAEK)" = "*DSH / EY D R AE K*T" ]
	rm -rf obj
	mkdir obj
	cd obj && python3 ../../lexconvert.py --convert example espeak && cd .. && diff -u en_extra obj/en_extra && rm obj/en_extra
	cd obj && python3 ../../lexconvert.py --convert example sapi && cd .. && diff -u run-ptts.bat obj/run-ptts.bat && rm obj/run-ptts.bat
	cd obj && python3 ../../lexconvert.py --convert example cepstral && cd .. && diff -u lexicon.txt obj/lexicon.txt && rm obj/lexicon.txt
	cd obj && python3 ../../lexconvert.py --convert example mac && cd .. && diff -u substitute.sh obj/substitute.sh && rm obj/substitute.sh
	cd obj && python3 ../../lexconvert.py --convert example x-sampa && cd .. && diff -u acapela.txt obj/acapela.txt && rm obj/acapela.txt
	cd obj && python3 ../../lexconvert.py --convert example vocaloid && cd .. && diff -u vocaloid.txt obj/vocaloid.txt && rm obj/vocaloid.txt
	cd obj && python3 ../../lexconvert.py --convert example keynote && cd .. && diff -u keynote.dat obj/keynote.dat && rm obj/keynote.dat
	cd obj && python3 ../../lexconvert.py --convert example audapter && cd .. && diff -u audapter.dat obj/audapter.dat && rm obj/audapter.dat
	cd obj && python3 ../../lexconvert.py --convert example bbcmicro && cd .. && diff -u BBCLEX obj/BBCLEX && diff -u BBCLEX.key obj/BBCLEX.key && rm obj/BBCLEX*
	cd obj && python3 ../../lexconvert.py --convert example unicode-ipa && cd .. && diff -u words-ipa.html obj/words-ipa.html && rm obj/words-ipa.html
	cd obj && python3 ../../lexconvert.py --convert example braille-ipa && cd .. && diff -u words-ipa.brl obj/words-ipa.brl && rm obj/words-ipa.brl
	cd obj && BRAILLE_UNICODE=1 python3 ../../lexconvert.py --convert example braille-ipa && cd .. && diff -u words-ipa.txt obj/words-ipa.txt && rm obj/words-ipa.txt
	cd obj && python3 ../../lexconvert.py --convert example latex-ipa && cd .. && diff -u words-ipa.tex obj/words-ipa.tex && rm obj/words-ipa.tex
	cd obj && python3 ../../lexconvert.py --convert example pinyin-approx && cd .. && diff -u words-pinyin-approx.txt obj/words-pinyin-approx.txt && rm obj/words-pinyin-approx.txt
	cd obj && HOME=$$(pwd) python3 ../../lexconvert.py --convert example festival && cd .. && diff -u festivalrc obj/.festivalrc && rm obj/.festivalrc
	cp festivalrc obj/.festivalrc && cd obj && HOME=$$(pwd) python3 ../../lexconvert.py --convert festival espeak && tr -d % < en_extra > 1 && tr -d % < ../en_extra > 2 && diff -u 1 2 && rm 1 2 en_extra .festivalrc && cd .. # ignore syllable separators in this diff
	cp en_extra obj/ && cd obj && HOME=$$(pwd) python3 ../../lexconvert.py --convert espeak festival && diff -u ../festivalrc .festivalrc && rm en_extra .festivalrc && cd ..
	cp lexicon.txt obj/ && cd obj && python3 ../../lexconvert.py --convert cepstral espeak && [ "$$(cat en_extra)" == "shadrach S'eI%drak"$$'\n'"meshach m'i:%Sak"$$'\n'"abednego Vb'E%dni:goU" ] && rm en_extra lexicon.txt && cd .. # approximation + lower
	rmdir obj
	rm -f yinghan-ipa.py
	python3 ../lexconvert.py --convert example yinghan
	[ "$$( (echo "*** ";echo "ehw Meshach")|python3 yinghan-ipa.py)" = $$'*** \nehw Meshach\nipa mˈiʃæk' ]
	rm yinghan-ipa.py
	@echo All Python 3 tests passed
