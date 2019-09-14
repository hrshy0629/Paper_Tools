#The Association for Computational Linguistics (ACL) is the international
# scientific and professional society for people working on problems involving natural
# language and computation. An annual meeting is held each summer in locations where
# significant computational linguistics research is carried out.
# It was founded in 1962, originally named the Association for
# Machine Translation and Computational Linguistics (AMTCL). It became the ACL in 1968.
#http://www.acl2019.org/EN/index.xhtml
import re
import os
import urllib.request

def Parse_Url_By_years(url, model, year):
    ##The function will return the url of pdf and the name of pdf
    temp = urllib.request.urlopen(url).read().decode('UTF-8')#temp is all source code of url
    url_name = model.findall(temp)
    #print(url_name[1])
    dir  = os.getcwd()
    Save_Pdf_Path = dir + '\\' +'ACL' + '20' + str(year)
    if not os.path.exists(Save_Pdf_Path):
        os.makedirs(Save_Pdf_Path)
    print(Save_Pdf_Path)
    model_pdf  = re.compile(r'.*?(?=title="Hidden link to PDF with extension)')
    model_name = re.compile(r'(?<=<a class=align-middle).*?(?=</a>)')
    for string in url_name:
        try:
            pdf_url = model_pdf.findall(string.replace('\n', ''))[0]
            pdf_name = model_name.findall(string.replace('\n', ''))[0]
            pdf_name = re.sub(r'\<.*?\>', ' ', pdf_name)
            pdf_name = pdf_name.split('/>')[-1]
            pdf_name = re.sub('[!@#$“”，。！？<>,/:?]', '', pdf_name).replace('  ',' ')
            print(pdf_url +'_____________________'+pdf_name)
            if pdf_url:
                print('ready')
                r = urllib.request.urlopen(pdf_url[:-1]).read()
                print('ok!!!!')
                with open(Save_Pdf_Path + '\\' + pdf_name + '.pdf', 'wb') as f:
                    f.write(r)
        except:
            print('The pdf has error!')
    pass

if __name__ == '__main__':
    ACL = 'https://aclweb.org/anthology/events/acl-20'
    model = re.compile(r'(?<=</a><a class=d-none href=)[\S\s]*?(?=</strong><br><a href=)')
    for i in range(15, 19):
        ACL_url = ACL + str(i) + "/#p" +str(i) + '-1'
        print(ACL_url)
        Parse_Url_By_years(ACL_url, model, i)


