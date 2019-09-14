# -*- coding: utf-8 -*-
#The International Conference on Computer Vision (ICCV)
# is a research conference sponsored by the
# Institute of Electrical and Electronics Engineers (IEEE)
# held every other year.
# It is considered, together with CVPR, the top level conference
# in computer vision.
## Conference Website: http://iccv2019.thecvf.com/
## Paper link: http://openaccess.thecvf.com/menu.py
import os
import re
import urllib.request

if __name__ == '__main__':
    ICCV = 'http://openaccess.thecvf.com/ICCV20'
    year = ['17']
    dir = os.getcwd()
    for i in year:
        ICCV_url = ICCV + i + '.py'
        Save_Pdf_Path = dir + '\\' + 'ICCV20' + i
        if not os.path.exists(Save_Pdf_Path):
            os.makedirs(Save_Pdf_Path)
        print(Save_Pdf_Path)
        print(ICCV_url)
        temp_one = urllib.request.urlopen(ICCV_url).read().decode('gbk')
        #print(temp_one)
        model = re.compile(r'(?<=\[<a hr)[\s\S]*?(?=\(ICCV\)\},<br>)')
        name_url_list = model.findall(temp_one)
        print(name_url_list[0].replace('\n', ' '))
        for name_url in name_url_list:
            try:
                model_name = re.compile(r'(?<=title = ).*?(?=,<br>)')
                model_url  = re.compile(r'(?<=ef=").*?(?=">pdf</a>)')
                print('1')
                pdf_name = model_name.findall(name_url.replace('\n', ' '))[0].replace('{', '').replace('}', '')
                pdf_name = re.sub('[!@#$“”，。！？<>,/:?]', '', pdf_name).replace('  ', ' ')
                print('ok-pdf_name'+'------' + pdf_name)
                pdf_url  = 'http://openaccess.thecvf.com/' + model_url.findall(name_url.replace('\n', ' '))[0]
                print('ok-pdf_url'+'------' + pdf_url)
                if pdf_url:
                    r = urllib.request.urlopen(pdf_url.replace('"', '')).read()
                    print('OK-r')
                    with open(Save_Pdf_Path+'\\'+pdf_name.strip() + '.pdf', 'wb') as f:
                        f.write(r)
            except:
                print('The page has error!!')