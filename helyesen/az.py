# -*- encoding: utf-8 -*-

def say(uni):
    return generate(classify(featurize(uni))) + u' ' + uni

def generate(label):
    return label

def featurize(inp):
    return { "unigram": inp[0:1], "bigram": inp[0:2] }

def classify(featureset) :
    if "bigram" in featureset:
      if featureset["bigram"] == u'&h': return u'a'
      elif featureset["bigram"] == u'-o': return u'az'
      elif featureset["bigram"] == u'1.': return u'az'
      elif featureset["bigram"] == u'19': return u'az'
      elif featureset["bigram"] == u'3.': return u'a'
      elif featureset["bigram"] == u'a': return u'az'
      elif featureset["bigram"] == u'ab': return u'az'
      elif featureset["bigram"] == u'ac': return u'az'
      elif featureset["bigram"] == u'ad': return u'az'
      elif featureset["bigram"] == u'af': return u'az'
      elif featureset["bigram"] == u'ag': return u'az'
      elif featureset["bigram"] == u'aj': return u'az'
      elif featureset["bigram"] == u'al': return u'az'
      elif featureset["bigram"] == u'an': return u'az'
      elif featureset["bigram"] == u'ap': return u'az'
      elif featureset["bigram"] == u'ar': return u'az'
      elif featureset["bigram"] == u'as': return u'az'
      elif featureset["bigram"] == u'at': return u'az'
      elif featureset["bigram"] == u'au': return u'az'
      elif featureset["bigram"] == u'b': return u'a'
      elif featureset["bigram"] == u'ba': return u'a'
      elif featureset["bigram"] == u'be': return u'a'
      elif featureset["bigram"] == u'bi': return u'a'
      elif featureset["bigram"] == u'bo': return u'a'
      elif featureset["bigram"] == u'br': return u'a'
      elif featureset["bigram"] == u'bu': return u'a'
      elif featureset["bigram"] == u'b\xe1': return u'a'
      elif featureset["bigram"] == u'b\xe9': return u'a'
      elif featureset["bigram"] == u'b\xed': return u'a'
      elif featureset["bigram"] == u'b\xf3': return u'a'
      elif featureset["bigram"] == u'b\xfa': return u'a'
      elif featureset["bigram"] == u'b\xfc': return u'a'
      elif featureset["bigram"] == u'b\u0151': return u'a'
      elif featureset["bigram"] == u'b\u0171': return u'a'
      elif featureset["bigram"] == u'c': return u'a'
      elif featureset["bigram"] == u'ce': return u'a'
      elif featureset["bigram"] == u'ci': return u'a'
      elif featureset["bigram"] == u'cs': return u'a'
      elif featureset["bigram"] == u'cu': return u'a'
      elif featureset["bigram"] == u'c\xe9': return u'a'
      elif featureset["bigram"] == u'c\xed': return u'a'
      elif featureset["bigram"] == u'da': return u'a'
      elif featureset["bigram"] == u'de': return u'a'
      elif featureset["bigram"] == u'di': return u'a'
      elif featureset["bigram"] == u'do': return u'a'
      elif featureset["bigram"] == u'dr': return u'a'
      elif featureset["bigram"] == u'du': return u'a'
      elif featureset["bigram"] == u'd\xe1': return u'a'
      elif featureset["bigram"] == u'd\xe9': return u'a'
      elif featureset["bigram"] == u'd\xed': return u'a'
      elif featureset["bigram"] == u'd\xf6': return u'a'
      elif featureset["bigram"] == u'd\xfa': return u'a'
      elif featureset["bigram"] == u'd\xfc': return u'a'
      elif featureset["bigram"] == u'eb': return u'az'
      elif featureset["bigram"] == u'ed': return u'az'
      elif featureset["bigram"] == u'ef': return u'az'
      elif featureset["bigram"] == u'eg': return u'az'
      elif featureset["bigram"] == u'el': return u'az'
      elif featureset["bigram"] == u'em': return u'az'
      elif featureset["bigram"] == u'en': return u'az'
      elif featureset["bigram"] == u'ep': return u'az'
      elif featureset["bigram"] == u'er': return u'az'
      elif featureset["bigram"] == u'es': return u'az'
      elif featureset["bigram"] == u'eu': return u'az'
      elif featureset["bigram"] == u'ev': return u'az'
      elif featureset["bigram"] == u'ez': return u'az'
      elif featureset["bigram"] == u'fa': return u'a'
      elif featureset["bigram"] == u'fe': return u'a'
      elif featureset["bigram"] == u'fi': return u'a'
      elif featureset["bigram"] == u'fo': return u'a'
      elif featureset["bigram"] == u'fr': return u'a'
      elif featureset["bigram"] == u'fu': return u'a'
      elif featureset["bigram"] == u'f\xe1': return u'a'
      elif featureset["bigram"] == u'f\xe9': return u'a'
      elif featureset["bigram"] == u'f\xf6': return u'a'
      elif featureset["bigram"] == u'f\xfc': return u'a'
      elif featureset["bigram"] == u'f\u0151': return u'a'
      elif featureset["bigram"] == u'f\u0171': return u'a'
      elif featureset["bigram"] == u'ga': return u'a'
      elif featureset["bigram"] == u'ge': return u'a'
      elif featureset["bigram"] == u'gi': return u'a'
      elif featureset["bigram"] == u'go': return u'a'
      elif featureset["bigram"] == u'gu': return u'a'
      elif featureset["bigram"] == u'gy': return u'a'
      elif featureset["bigram"] == u'g\xe1': return u'a'
      elif featureset["bigram"] == u'g\xe9': return u'a'
      elif featureset["bigram"] == u'g\xf6': return u'a'
      elif featureset["bigram"] == u'g\u0151': return u'a'
      elif featureset["bigram"] == u'ha': return u'a'
      elif featureset["bigram"] == u'he': return u'a'
      elif featureset["bigram"] == u'hi': return u'a'
      elif featureset["bigram"] == u'ho': return u'a'
      elif featureset["bigram"] == u'hu': return u'a'
      elif featureset["bigram"] == u'hy': return u'a'
      elif featureset["bigram"] == u'h\xe1': return u'a'
      elif featureset["bigram"] == u'h\xe9': return u'a'
      elif featureset["bigram"] == u'h\xed': return u'a'
      elif featureset["bigram"] == u'h\xf3': return u'a'
      elif featureset["bigram"] == u'h\xfa': return u'a'
      elif featureset["bigram"] == u'h\xfc': return u'a'
      elif featureset["bigram"] == u'h\u0151': return u'a'
      elif featureset["bigram"] == u'h\u0171': return u'a'
      elif featureset["bigram"] == u'id': return u'az'
      elif featureset["bigram"] == u'if': return u'az'
      elif featureset["bigram"] == u'ig': return u'az'
      elif featureset["bigram"] == u'ij': return u'az'
      elif featureset["bigram"] == u'il': return u'az'
      elif featureset["bigram"] == u'im': return u'az'
      elif featureset["bigram"] == u'in': return u'az'
      elif featureset["bigram"] == u'ip': return u'az'
      elif featureset["bigram"] == u'ir': return u'az'
      elif featureset["bigram"] == u'is': return u'az'
      elif featureset["bigram"] == u'it': return u'az'
      elif featureset["bigram"] == u'iv': return u'az'
      elif featureset["bigram"] == u'iz': return u'az'
      elif featureset["bigram"] == u'ja': return u'a'
      elif featureset["bigram"] == u'je': return u'a'
      elif featureset["bigram"] == u'jo': return u'a'
      elif featureset["bigram"] == u'ju': return u'a'
      elif featureset["bigram"] == u'j\xe1': return u'a'
      elif featureset["bigram"] == u'j\xe9': return u'a'
      elif featureset["bigram"] == u'j\xf3': return u'a'
      elif featureset["bigram"] == u'j\xf6': return u'a'
      elif featureset["bigram"] == u'j\xfa': return u'a'
      elif featureset["bigram"] == u'k': return u'a'
      elif featureset["bigram"] == u'ka': return u'a'
      elif featureset["bigram"] == u'ke': return u'a'
      elif featureset["bigram"] == u'ki': return u'a'
      elif featureset["bigram"] == u'ko': return u'a'
      elif featureset["bigram"] == u'kr': return u'a'
      elif featureset["bigram"] == u'ku': return u'a'
      elif featureset["bigram"] == u'k\xe1': return u'a'
      elif featureset["bigram"] == u'k\xe9': return u'a'
      elif featureset["bigram"] == u'k\xed': return u'a'
      elif featureset["bigram"] == u'k\xf6': return u'a'
      elif featureset["bigram"] == u'k\xfc': return u'a'
      elif featureset["bigram"] == u'k\u0151': return u'a'
      elif featureset["bigram"] == u'l.': return u'az'
      elif featureset["bigram"] == u'la': return u'a'
      elif featureset["bigram"] == u'le': return u'a'
      elif featureset["bigram"] == u'li': return u'a'
      elif featureset["bigram"] == u'lo': return u'a'
      elif featureset["bigram"] == u'ly': return u'a'
      elif featureset["bigram"] == u'l\xe1': return u'a'
      elif featureset["bigram"] == u'l\xe9': return u'a'
      elif featureset["bigram"] == u'l\xed': return u'a'
      elif featureset["bigram"] == u'l\xf3': return u'a'
      elif featureset["bigram"] == u'ma': return u'a'
      elif featureset["bigram"] == u'me': return u'a'
      elif featureset["bigram"] == u'mi': return u'a'
      elif featureset["bigram"] == u'mo': return u'a'
      elif featureset["bigram"] == u'mr': return u'a'
      elif featureset["bigram"] == u'mu': return u'a'
      elif featureset["bigram"] == u'm\xe1': return u'a'
      elif featureset["bigram"] == u'm\xe9': return u'a'
      elif featureset["bigram"] == u'm\xf3': return u'a'
      elif featureset["bigram"] == u'm\xfa': return u'a'
      elif featureset["bigram"] == u'm\u0171': return u'a'
      elif featureset["bigram"] == u'na': return u'a'
      elif featureset["bigram"] == u'ne': return u'a'
      elif featureset["bigram"] == u'no': return u'a'
      elif featureset["bigram"] == u'ny': return u'a'
      elif featureset["bigram"] == u'n\xe1': return u'a'
      elif featureset["bigram"] == u'n\xe9': return u'a'
      elif featureset["bigram"] == u'n\u0151': return u'a'
      elif featureset["bigram"] == u"o'": return u'az'
      elif featureset["bigram"] == u'ob': return u'az'
      elif featureset["bigram"] == u'od': return u'az'
      elif featureset["bigram"] == u'ok': return u'az'
      elif featureset["bigram"] == u'ol': return u'az'
      elif featureset["bigram"] == u'or': return u'az'
      elif featureset["bigram"] == u'os': return u'az'
      elif featureset["bigram"] == u'ot': return u'az'
      elif featureset["bigram"] == u'ov': return u'az'
      elif featureset["bigram"] == u'pa': return u'a'
      elif featureset["bigram"] == u'pe': return u'a'
      elif featureset["bigram"] == u'pi': return u'a'
      elif featureset["bigram"] == u'pl': return u'a'
      elif featureset["bigram"] == u'po': return u'a'
      elif featureset["bigram"] == u'pr': return u'a'
      elif featureset["bigram"] == u'ps': return u'a'
      elif featureset["bigram"] == u'pu': return u'a'
      elif featureset["bigram"] == u'p\xe1': return u'a'
      elif featureset["bigram"] == u'p\xe9': return u'a'
      elif featureset["bigram"] == u'p\xfc': return u'a'
      elif featureset["bigram"] == u'ra': return u'a'
      elif featureset["bigram"] == u're': return u'a'
      elif featureset["bigram"] == u'ri': return u'a'
      elif featureset["bigram"] == u'ro': return u'a'
      elif featureset["bigram"] == u'ru': return u'a'
      elif featureset["bigram"] == u'r\xe1': return u'a'
      elif featureset["bigram"] == u'r\xe9': return u'a'
      elif featureset["bigram"] == u'r\xed': return u'a'
      elif featureset["bigram"] == u'r\xf3': return u'a'
      elif featureset["bigram"] == u'r\xf6': return u'a'
      elif featureset["bigram"] == u'r\xfa': return u'a'
      elif featureset["bigram"] == u'sa': return u'a'
      elif featureset["bigram"] == u'se': return u'a'
      elif featureset["bigram"] == u'sh': return u'a'
      elif featureset["bigram"] == u'so': return u'a'
      elif featureset["bigram"] == u'sp': return u'a'
      elif featureset["bigram"] == u'st': return u'a'
      elif featureset["bigram"] == u'sz': return u'a'
      elif featureset["bigram"] == u's\xe1': return u'a'
      elif featureset["bigram"] == u's\xe9': return u'a'
      elif featureset["bigram"] == u's\xed': return u'a'
      elif featureset["bigram"] == u's\xf6': return u'a'
      elif featureset["bigram"] == u's\xfa': return u'a'
      elif featureset["bigram"] == u's\xfc': return u'a'
      elif featureset["bigram"] == u's\u0171': return u'a'
      elif featureset["bigram"] == u'ta': return u'a'
      elif featureset["bigram"] == u'te': return u'a'
      elif featureset["bigram"] == u'ti': return u'a'
      elif featureset["bigram"] == u'to': return u'a'
      elif featureset["bigram"] == u'tr': return u'a'
      elif featureset["bigram"] == u'tu': return u'a'
      elif featureset["bigram"] == u'ty': return u'a'
      elif featureset["bigram"] == u't\xe1': return u'a'
      elif featureset["bigram"] == u't\xe9': return u'a'
      elif featureset["bigram"] == u't\xf3': return u'a'
      elif featureset["bigram"] == u't\xf6': return u'a'
      elif featureset["bigram"] == u't\xfa': return u'a'
      elif featureset["bigram"] == u't\xfc': return u'a'
      elif featureset["bigram"] == u't\u0151': return u'a'
      elif featureset["bigram"] == u't\u0171': return u'a'
      elif featureset["bigram"] == u'ud': return u'az'
      elif featureset["bigram"] == u'uj': return u'az'
      elif featureset["bigram"] == u'un': return u'az'
      elif featureset["bigram"] == u'ur': return u'az'
      elif featureset["bigram"] == u'ut': return u'az'
      elif featureset["bigram"] == u'va': return u'a'
      elif featureset["bigram"] == u've': return u'a'
      elif featureset["bigram"] == u'vi': return u'a'
      elif featureset["bigram"] == u'vo': return u'a'
      elif featureset["bigram"] == u'v\xe1': return u'a'
      elif featureset["bigram"] == u'v\xe9': return u'a'
      elif featureset["bigram"] == u'v\xed': return u'a'
      elif featureset["bigram"] == u'v\xf6': return u'a'
      elif featureset["bigram"] == u'wi': return u'a'
      elif featureset["bigram"] == u'za': return u'a'
      elif featureset["bigram"] == u'ze': return u'a'
      elif featureset["bigram"] == u'zo': return u'a'
      elif featureset["bigram"] == u'zs': return u'a'
      elif featureset["bigram"] == u'z\xe1': return u'a'
      elif featureset["bigram"] == u'z\xf6': return u'a'
      elif featureset["bigram"] == u'z\xfc': return u'a'
      elif featureset["bigram"] == u'z\u0171': return u'a'
      elif featureset["bigram"] == u'\xe1b': return u'az'
      elif featureset["bigram"] == u'\xe1g': return u'az'
      elif featureset["bigram"] == u'\xe1l': return u'az'
      elif featureset["bigram"] == u'\xe1r': return u'az'
      elif featureset["bigram"] == u'\xe1t': return u'az'
      elif featureset["bigram"] == u'\xe9b': return u'az'
      elif featureset["bigram"] == u'\xe9g': return u'az'
      elif featureset["bigram"] == u'\xe9h': return u'az'
      elif featureset["bigram"] == u'\xe9j': return u'az'
      elif featureset["bigram"] == u'\xe9l': return u'az'
      elif featureset["bigram"] == u'\xe9n': return u'az'
      elif featureset["bigram"] == u'\xe9p': return u'az'
      elif featureset["bigram"] == u'\xe9r': return u'az'
      elif featureset["bigram"] == u'\xe9s': return u'az'
      elif featureset["bigram"] == u'\xe9t': return u'az'
      elif featureset["bigram"] == u'\xe9v': return u'az'
      elif featureset["bigram"] == u'\xedg': return u'az'
      elif featureset["bigram"] == u'\xedr': return u'az'
      elif featureset["bigram"] == u'\xedt': return u'az'
      elif featureset["bigram"] == u'\xedz': return u'az'
      elif featureset["bigram"] == u'\xf3b': return u'az'
      elif featureset["bigram"] == u'\xf3c': return u'az'
      elif featureset["bigram"] == u'\xf3d': return u'az'
      elif featureset["bigram"] == u'\xf3g': return u'az'
      elif featureset["bigram"] == u'\xf3h': return u'az'
      elif featureset["bigram"] == u'\xf3k': return u'az'
      elif featureset["bigram"] == u'\xf3r': return u'az'
      elif featureset["bigram"] == u'\xf6b': return u'az'
      elif featureset["bigram"] == u'\xf6l': return u'az'
      elif featureset["bigram"] == u'\xf6n': return u'az'
      elif featureset["bigram"] == u'\xf6r': return u'az'
      elif featureset["bigram"] == u'\xf6s': return u'az'
      elif featureset["bigram"] == u'\xf6t': return u'az'
      elif featureset["bigram"] == u'\xf6v': return u'az'
      elif featureset["bigram"] == u'\xfae': return u'az'
      elif featureset["bigram"] == u'\xfag': return u'az'
      elif featureset["bigram"] == u'\xfaj': return u'az'
      elif featureset["bigram"] == u'\xfas': return u'az'
      elif featureset["bigram"] == u'\xfat': return u'az'
      elif featureset["bigram"] == u'\xfcd': return u'az'
      elif featureset["bigram"] == u'\xfcg': return u'az'
      elif featureset["bigram"] == u'\xfcl': return u'az'
      elif featureset["bigram"] == u'\xfcn': return u'az'
      elif featureset["bigram"] == u'\xfcr': return u'az'
      elif featureset["bigram"] == u'\xfcs': return u'az'
      elif featureset["bigram"] == u'\xfct': return u'az'
      elif featureset["bigram"] == u'\xfcv': return u'az'
      elif featureset["bigram"] == u'\xfcz': return u'az'
      elif featureset["bigram"] == u'\u0151': return u'az'
      elif featureset["bigram"] == u'\u0151k': return u'az'
      elif featureset["bigram"] == u'\u0151r': return u'az'
      elif featureset["bigram"] == u'\u0151s': return u'az'
      elif featureset["bigram"] == u'\u0171r': return u'az'
    return u'a'

