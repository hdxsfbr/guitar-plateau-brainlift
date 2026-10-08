import re,unicodedata,sys
def norm(s):
    s=unicodedata.normalize('NFKC',s)
    s=re.sub(r'\]\([^)]*\)',']',s)
    s=re.sub(r'[\x00-\x1f\u00a0\u2009\u202f\u200a\u2002\u2003]',' ',s)
    s=re.sub(r'[*_`#>]','',s)
    s=s.replace('\u2212','-').replace('–','-').replace('—','-')
    s=s.replace('“','"').replace('”','"').replace('’',"'").replace('‘',"'")
    return re.sub(r'\s+',' ',s).strip()
def dehyph(s): return re.sub(r'(\w)- (\w)',r'\1\2',s)
def check(quote,text):
    """return yes/near/no"""
    nt=norm(text); segs=[x.strip(' .') for x in re.split(r'\s*(?:…|\.\.\.)\s*',norm(quote)) if x.strip(' .')]
    if all(s in nt for s in segs): return 'yes'
    dt=dehyph(nt)
    if all(dehyph(s) in dt for s in segs): return 'near'
    dt2=re.sub(r' \d{1,3}(?=[A-Za-z])',' ',dt)  # stray line numbers
    if all(dehyph(s) in dt2 for s in segs): return 'near'
    return 'no'
