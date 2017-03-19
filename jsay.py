#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess
import shlex
import tempfile
import os
#import argparse

def debug_print(tag,obj):
    if __debug__:
        print('[%s]:%s'% (tag, obj))

def execute(message):

    with tempfile.NamedTemporaryFile() as temp_text_f, tempfile.NamedTemporaryFile() as temp_wav_f:
        
        temp_text_f.write(message.encode('utf-8'))
        temp_text_f.seek(0)
        
        #temp_wav_f.seek(0)
        
        debug_print('text path',temp_text_f.name)
        debug_print('wav path', temp_wav_f.name)
        debug_print('text',temp_text_f.read().decode('utf-8'))
        
        jtalk_dic_path = '/usr/local/share/open_jtalk/open_jtalk_dic_utf_8-1.09/'
        voice_path = '/usr/local/share/hts_voice/mei/mei_normal.htsvoice'

        jtalk_command = '/usr/local/bin/open_jtalk -x %s -m %s -ow %s %s' % (jtalk_dic_path, voice_path, temp_wav_f.name, temp_text_f.name)
        
        debug_print('jtalk command', jtalk_command)

        subprocess.check_call(shlex.split(jtalk_command))

        mplayer_command = '/usr/bin/mplayer %s' % (temp_wav_f.name)

        if __debug__:
            subprocess.check_call(shlex.split(mplayer_command))
        else:
            # mplayerの出力を隠す
            with open(os.devnull, 'w') as fnull:
                result = subprocess.check_call(shlex.split(mplayer_command), stdout = fnull, stderr = fnull)
        
if __name__ == '__main__':
    # argparse
    #parser = argparse.ArgumentParser(description='pyJsay')
    #parser.add
    execute('こんにちは')
    
