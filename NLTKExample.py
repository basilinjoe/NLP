import nltk
from nltk.corpus import wordnet as wn
def pos_token(string):
    tok=nltk.word_tokenize(string)
    tags=nltk.pos_tag(tok)
    n=len(tags)
    dictn={}
    dicts={}
    i=0;
    #print tags
    for a in tags:
       # print a
        if a[1]=='NN' or a[1]=='VBG':
            if a[1]=='VBG':
                ab=wn.morphy(a[0], wn.VERB)
                print ab
                dicts[i]=(ab)
                i+=1
            else:
                dicts[i]=(a[0])
                i+=1
    return dicts
     
print pos_token("I cannot drink warm milk")
