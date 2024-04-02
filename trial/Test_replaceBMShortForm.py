import commons.lang.CleanText as c


txt = 'ak nak p pasar kat city mall.'

shortform_csv_path = "../data/kamus_singkatan2.csv"
shortform_list = c.get_shortform_list(shortform_csv_path)
txt2 = c.replace_malay_shortform(txt, shortform_list)
print(txt)
print(txt2)