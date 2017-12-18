# MeCab installation for local CDSW environment

#!conda install -y -c chezou mecab
#!pip3 install mecab-python3

import os

os.environ.get("LD_LIBRARY_PATH")
# The result should include `/home/cdsw/.conda/envs/python3.6/lib`

import MeCab

m = MeCab.Tagger()
print(m.parse("日本語のテストをしています"))
