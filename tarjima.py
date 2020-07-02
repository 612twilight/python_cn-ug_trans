import requests
from lxml import etree
from pypinyin import pinyin
while True:
    sz = input("سۆز كىرگۈزۈڭ : \n")
    url = "http://dict.izda.com/?a=search&type=cn_ug&q="+sz
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    html = requests.get(url, headers=header).text
    Music = etree.HTML(html)
    asl = Music.xpath("/html/body/div[6]/div[1]/div/div/div/div/div[1]/div[1]/text()")
    soz = Music.xpath("/html/body/div[6]/div[1]/div/div/div/div/div[1]/div[3]/text()")
    asl = str(asl);asl=asl[2:-2];b=""
    ip =" سىز باشقا مەنبەدىن مەزكۇر ئۇچۇرغا ئېرىشكەن ۋاقتىڭىزدا ', ' كىرىپ ، ئىزدە لۇغەت ئامبىرىغا يوللاپ بەرسىڭىز بۇلىدۇ ! سىزنىڭ ۋە بىزنىڭ تىرىشچانلىقىمىز نەتىجىسىدە ئىزدە تور لۇغىتى تېخىمۇ مۇكەممەللەشكۈسى  !"
    if asl == ip:
        print('نەتىجە تېپىلمىدى')
    else:
        asl = sz+'        '
        py = pinyin(sz)
        for i in range(0,len(py)):
            asl += py[i][0]
        soz = str(soz);soz= soz[15:-13];soz=soz.replace("'",'')
        print(asl)
        print(soz)
        break
