#!/usr/bin/python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

import os

# DummyTagger (EXAMPLE) ################################################################################################

# Setup the tuple: module name (ending with the filename the class defined in),
# class, friendly name, args (tuple), kwargs (dict)
em_dummy = ('emdummy.dummytagger', 'DummyTagger', 'EXAMPLE (The friendly name of DummyTagger used in REST API form)',
            ('Params', 'goes', 'here'),
            {'source_fields': {'Source field names'}, 'target_fields': ['Target field names']})

# emToken ##############################################################################################################

em_token = ('emtokenpy.emtokenpy', 'EmTokenPy', 'emToken', (), {'source_fields': set(), 'target_fields': ['form', 'wsafter']})

# emMorph ##############################################################################################################

em_morph = ('emmorphpy.emmorphpy', 'EmMorphPy', 'emMorph', (), {'source_fields': {'form'}, 'target_fields': ['anas']})

# Hunspell #############################################################################################################

hunspellpy = ('hunspellpy.hunspellpy', 'HunspellPy', 'HunspellPy', (),
              {'source_fields': {'form'}, 'target_fields': ['spell', 'hunspell_anas']})

# emTag ################################################################################################################

em_tag = ('purepospy.purepospy', 'PurePOS', 'emTag (PurePOS)', (),
          {'source_fields': {'form', 'anas'}, 'target_fields': ['lemma', 'xpostag']})

# emMorph2Dep ##########################################################################################################

em_morph2ud = ('emmorph2ud.emmorph2ud.converter', 'EmMorph2UD', 'emmorph2ud', (),
               {'source_fields': {'form', 'lemma', 'xpostag'}, 'target_fields': ['upostag', 'feats']})

# emChunk ##############################################################################################################

model_name = os.path.join(os.path.dirname(__file__), 'HunTag3', 'models', 'maxnp.szeged.emmorph')
cfg_file = os.path.join(os.path.dirname(__file__), 'HunTag3', 'configs', 'maxnp.szeged.emmorph.yaml')
target_field = 'NP-BIO'

em_chunk = ('HunTag3.huntag.tagger', 'Tagger', 'emChunk', ({'cfg_file': cfg_file, 'model_name': model_name},),
            {'source_fields': set(), 'target_fields': [target_field]})

# emNER ################################################################################################################

model_name = os.path.join(os.path.dirname(__file__), 'HunTag3', 'models', 'ner.szeged.emmorph')
cfg_file = os.path.join(os.path.dirname(__file__), 'HunTag3', 'configs', 'ner.szeged.emmorph.yaml')
target_field = 'NER-BIO'

em_ner = ('HunTag3.huntag.tagger', 'Tagger', 'emNER', ({'cfg_file': cfg_file, 'model_name': model_name},),
          {'source_fields': set(), 'target_fields': [target_field]})

# emDep ################################################################################################################

em_depud = ('emdeppy.emdeppy', 'EmDepPy', 'emDep', (),
            {'source_fields': {'form', 'lemma', 'upostag', 'feats'}, 'target_fields': ['id', 'deprel', 'head']})

# emCons ###############################################################################################################

em_cons = ('emconspy.emconspy', 'EmConsPy', 'emCons', (),
           {'source_fields': {'form', 'lemma', 'xpostag'}, 'target_fields': ['cons']})

# emUDPipe tok-parse ###################################################################################################

emudpipe_tok_parse = ('emudpipe.emudpipe', 'UDPipe', 'UDPipe tokenizer, POS tagger and dependency parser as a whole',
                      (), {'task': 'tok-parse', 'source_fields': set(), 'target_fields': ['form', 'lemma', 'upostag',
                           'feats', 'head', 'deprel', 'deps']})

# emUDPipe tok-pos #####################################################################################################

emudpipe_tok_pos = ('emudpipe.emudpipe', 'UDPipe', 'UDPipe tokenizer and POS tagger as a whole',
                    (), {'task': 'tok-pos', 'source_fields': set(),
                         'target_fields': ['form', 'lemma', 'upostag', 'feats']})

# emUDPipe tok #########################################################################################################

emudpipe_tok = ('emudpipe.emudpipe', 'UDPipe', 'UDPipe tokenizer', (),
                {'task': 'tok', 'source_fields': set(), 'target_fields': ['form']})

# emUDPipe pos-parse ###################################################################################################

emudpipe_pos_parse = ('emudpipe.emudpipe', 'UDPipe', 'UDPipe POS tagger and dependency parser as a whole',
                      (), {'task': 'pos-parse', 'source_fields': {'form'},
                           'target_fields': ['lemma', 'upostag', 'feats', 'head', 'deprel', 'deps']})

# emUDPipe pos #########################################################################################################

emudpipe_pos = ('emudpipe.emudpipe', 'UDPipe', 'UDPipe POS tagger', (),
                {'task': 'pos', 'source_fields': {'form'}, 'target_fields': ['lemma', 'upostag', 'feats']})

# emUDPipe parse #######################################################################################################

emudpipe_parse = ('emudpipe.emudpipe', 'UDPipe', 'UDPipe dependency parser',
                  (), {'task': 'parse', 'source_fields': {'form', 'lemma', 'upostag', 'feats'},
                       'target_fields': ['head', 'deprel', 'deps']})

# emCoNLL ##############################################################################################################

em_conll = ('emconll.converter', 'EmCoNLL', 'CoNLL-U converter', (), {'source_fields': {'form'}, 'target_fields': []})

########################################################################################################################

# Map module personalities to firendly names...
# The first name is the default. The order is the display order of the modules
tools = [(em_token, ('tok', 'emToken')),
         (em_morph, ('morph', 'emMorph')),
         (hunspellpy, ('spell', 'hunspell')),
         (em_tag, ('pos', 'emTag')),
         (em_chunk, ('chunk', 'emChunk')),
         (em_ner, ('ner', 'emNER')),
         (em_morph2ud, ('conv-morph', 'emmorph2ud')),
         (em_depud, ('dep', 'emDep-ud')),
         (em_cons, ('cons', 'emCons')),
         (em_conll, ('conll', 'emCoNLL')),
         (emudpipe_tok, ('udpipe-tok',)),
         (emudpipe_pos, ('udpipe-pos',)),
         (emudpipe_parse, ('udpipe-parse',)),
         (emudpipe_tok_pos, ('udpipe-tok-pos',)),
         (emudpipe_pos_parse, ('udpipe-pos-parse',)),
         (emudpipe_tok_parse, ('udpipe-tok-parse',)),
         (em_dummy, ('dummy-tagger', 'emDummy')),
         ]

# cat input.txt | ./main.py tok,morph,pos,conv-morph,dep -> cat input.txt | ./main.py tok-dep
presets = {'analyze': ('Full pipeline', ['tok', 'morph', 'pos', 'chunk', 'conv-morph', 'dep', 'cons']),
           'tok-morph': ('Raw text to morphologycal analysis', ['tok', 'morph']),
           'tok-pos': ('Raw text to POS-tagging in emMorph formalism', ['tok', 'morph', 'pos']),
           'tok-chunk': ('Raw text to maximal NPs chunking', ['tok', 'morph', 'pos', 'chunk']),
           'tok-ner': ('Raw text to named-entity annotation', ['tok', 'morph', 'pos', 'ner']),
           'tok-udpos': ('Raw text to POS-tagging including UDv1 form', ['tok', 'morph', 'pos', 'conv-morph']),
           'tok-dep': ('Raw text to dependency parsing', ['tok', 'morph', 'pos', 'conv-morph', 'dep']),
           'tok-dep-conll': ('Raw text to dependency parsing in CoNLL-U format',
                             ['tok', 'morph', 'pos', 'conv-morph', 'dep', 'conll']),
           'tok-cons': ('Raw text to constituent parsing', ['tok', 'morph', 'pos', 'cons']),
           }
