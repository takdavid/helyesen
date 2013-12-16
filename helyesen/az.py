# -*- encoding: utf-8 -*-

def say(uni):
    return generate(classify(featurize(uni))) + u' ' + uni

def generate(label):
    return label

def featurize(inp):
    return { "unigram": inp[0:1], "bigram": inp[0:2] }

def classify(featureset) :
    if "unigram" in featureset:
      if featureset["unigram"] == u'&': return u'a'
      elif featureset["unigram"] == u'-': return u'az'
      elif featureset["unigram"] == u'1': return u'az'
      elif featureset["unigram"] == u'3': return u'a'
      elif featureset["unigram"] == u'a': return u'az'
      elif featureset["unigram"] == u'b': return u'a'
      elif featureset["unigram"] == u'c': return u'a'
      elif featureset["unigram"] == u'd': return u'a'
      elif featureset["unigram"] == u'e': return u'az'
      elif featureset["unigram"] == u'f': return u'a'
      elif featureset["unigram"] == u'g': return u'a'
      elif featureset["unigram"] == u'h': return u'a'
      elif featureset["unigram"] == u'i': return u'az'
      elif featureset["unigram"] == u'j': return u'a'
      elif featureset["unigram"] == u'k': return u'a'
      elif featureset["unigram"] == u'l': return u'a'
      elif featureset["unigram"] == u'm': return u'a'
      elif featureset["unigram"] == u'n': return u'a'
      elif featureset["unigram"] == u'o': return u'az'
      elif featureset["unigram"] == u'p': return u'a'
      elif featureset["unigram"] == u'r': return u'a'
      elif featureset["unigram"] == u's': return u'a'
      elif featureset["unigram"] == u't': return u'a'
      elif featureset["unigram"] == u'u': return u'az'
      elif featureset["unigram"] == u'v': return u'a'
      elif featureset["unigram"] == u'w': return u'a'
      elif featureset["unigram"] == u'z': return u'a'
      elif featureset["unigram"] == u'\xe1': return u'az'
      elif featureset["unigram"] == u'\xe9': return u'az'
      elif featureset["unigram"] == u'\xed': return u'az'
      elif featureset["unigram"] == u'\xf3': return u'az'
      elif featureset["unigram"] == u'\xf6': return u'az'
      elif featureset["unigram"] == u'\xfa': return u'az'
      elif featureset["unigram"] == u'\xfc': return u'az'
      elif featureset["unigram"] == u'\u0151': return u'az'
      elif featureset["unigram"] == u'\u0171': return u'az'
    return u'a'

