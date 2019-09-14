# The Conference and Workshop on Neural Information Processing Systems
# (abbreviated as NeurIPS and formerly NIPS) is
# a machine learning and computational neuroscience conference held every December.
# The conference is currently a double-track meeting (single-track until 2015) that
# includes invited talks as well as oral and poster presentations of refereed papers,
# followed by parallel-track workshops that up to 2013 were held at ski resorts
# Conference website:https://nips.cc/Conferences/2018
# Paper link:https://nips.cc/Conferences/2018/Schedule?type=Poster(or Oral)
import os
import re
import urllib.request

def Parse_Url(url, modul, year):
    pass

if __name__ == '__main__':
    NIPS = 'https://nips.cc/Conferences/20'
    Types = ['Oral', 'Poster']
    dir  = os.getcwd()
    for i in range(17, 19):
        for type in Types:
            Save_Pdf_Path = dir + '\\' + 'NIPS20' + str(i) + '\\' + type
            if not os.path.exists(Save_Pdf_Path):
                os.makedirs(Save_Pdf_Path)
            print(Save_Pdf_Path)
            level_one_of_url = NIPS + str(i) + '/Schedule?type=' + type
            temp_one = urllib.request.urlopen(level_one_of_url).read().decode('UTF-8')
            model = re.compile(r'(?<=<a href=").*?(?=" class="btn btn-default btn-xs href_PDF" title="Paper">)')### 2015-2016 title="PDF"
            url_list = model.findall(temp_one)
            #print(url_list[0])#The element of url_list is full page.
            for index in url_list:
                try:
                    print(index)
                    temp_two = urllib.request.urlopen(index).read().decode('UTF-8')
                    print('1')
                    model_pdf_name = re.compile(r'(?<=<title>).*?(?=</title>)')
                    model_pdf_url  = re.compile(r'(?<=<a href=").*?(?=">\[PDF\]</a>)')
                    pdf_name = model_pdf_name.findall(temp_two)[0]
                    print(pdf_name)
                    pdf_name = re.sub('[!@#$“”，。！？<>,/:?]', '', pdf_name).replace('  ', ' ')
                    pdf_url = 'http://papers.nips.cc'+ model_pdf_url.findall(temp_two)[0]
                    print(pdf_url)
                    print(pdf_name +'----'+pdf_url)
                    if pdf_url:
                        print('ready')
                        r = urllib.request.urlopen(pdf_url).read()
                        print('ok!!!!')
                        with open(Save_Pdf_Path + '\\' + pdf_name.lower().strip() + '.pdf', 'wb') as f:
                            f.write(r)
                except:
                    print('The url '+ index + ' has error!!')