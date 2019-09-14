##The International Conference on Learning Representations (ICLR)
# is a machine learning conference held every Spring.
# The conference includes invited talks as well as oral and poster presentations of refereed papers.
# The first ICLR was held in Scottsdale, Arizona.
# Since its inception in 2013, ICLR has employed an open peer review process to referee paper
# submissions (based on models proposed by Yann LeCun).
# In 2019, there were 1591 paper submissions,
# of which 500 accepted with poster presentations (31%) and 24 with oral presentations (1.5%).
## Conference Website: https://iclr.cc/Conferences/2019/Schedule?type=Poster(OR Oral)
## Paper link: https://iclr.cc/Conferences/2019/Schedule?type=Poster(OR Oral)
import os
import re
import urllib.request

def Parse_Url(url, modul, year):
    pass

if __name__ == '__main__':
    ICLR = 'https://iclr.cc/Conferences/20'
    Types = ['Oral', 'Poster']
    dir  = os.getcwd()
    for i in range(18, 20):
        for type in Types:
            Save_Pdf_Path = dir + '\\' + 'ICLR20' + str(i) + '\\' + type
            if not os.path.exists(Save_Pdf_Path):
                os.makedirs(Save_Pdf_Path)
            print(Save_Pdf_Path)
            level_one_of_url = ICLR + str(i) + '/Schedule?type=' + type
            temp_one = urllib.request.urlopen(level_one_of_url).read().decode('UTF-8')
            model = re.compile(r'(?<=<a href=").*?(?=" class="btn btn-default btn-xs href_PDF" title="PDF">)')
            url_list = model.findall(temp_one)
            print(url_list[0])#The element of url_list is full page.
            for index in url_list:
                try:
                    temp_two = urllib.request.urlopen(index).read().decode('UTF-8')
                    model_pdf_name = re.compile(r'(?<=<meta name="citation_title" content=").*?(?=">)')
                    model_pdf_url  = re.compile(r'(?<=<a class="note_content_pdf citation_pdf_url" href=").*?(?=" title="Download PDF")')
                    pdf_name = model_pdf_name.findall(temp_two)[0]
                    pdf_name = re.sub('[!@#$“”，。！？<>,/:?]', '', pdf_name).replace('  ', ' ')
                    pdf_url = 'https://openreview.net'+ model_pdf_url.findall(temp_two)[0]
                    print(pdf_name +'----'+pdf_url)
                    if pdf_url:
                        print('ready')
                        r = urllib.request.urlopen(pdf_url).read()
                        print('ok!!!!')
                        with open(Save_Pdf_Path + '\\' + pdf_name.lower() + '.pdf', 'wb') as f:
                            f.write(r)
                except:
                    print('The url '+ index + ' has error!!')





