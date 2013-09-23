import hashlib

def computemd5hash(audio):
    """
    Method returns MD5 hex digest for an audio file as string.
    Method takes path to audio file as a string input.
    """
    f = open(audio, 'rb')
    audiostring = str(f.readlines())
    f.close()
    return hashlib.md5(audiostring).hexdigest()

##print computemd5hash('/Users/muthu/Music/The Beatles/1/Beatles - 01 - Love Me Do.mp3')

