import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime
from datetime import datetime


def html_parse(get_url):
    req = requests.get(get_url)

    page_content = soup(req.content, 'html5lib')
    return page_content

def check_status(url, file_name):
    df = pd.read_csv(file_name)['amazon_url']
    df = df.to_list()
   # print(df)
    if url in df:
        status = 'Y'
    else:
        status = 'N'
    return status


def write_csv( j, url, cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8, cat9):
    select = True
    if j == 0:
        global dfObj
        global file_name
        file_name = datetime.now().strftime("%d%b%Y%H%M%S") + "_amazon_store_.csv"
        dfObj = pd.DataFrame(columns=['select', 'amazon_url', 'cat1', 'cat2', 'cat3', 'cat4', 'cat5', 'cat6', 'cat7', 'cat8', 'cat9',])
        dfObj.to_csv(file_name)
    else:
        dfObj = dfObj.append({'select': select, 'amazon_url': url, 'cat1': cat1, 'cat2': cat2, 'cat3': cat3, 'cat4': cat4, 'cat5': cat5,
                              'cat6': cat6, 'cat7': cat7, 'cat8': cat8, 'cat9': cat9,}, ignore_index=True)
        dfObj.to_csv(file_name)

def main():
    try:
        url, cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09 = '', '', '', '', '', '', '', '', '', ''
        j=0
        write_csv(j, url, cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09)
        j=2

        x = 'https://www.amazon.com'
        url = 'https://www.amazon.com/gp/site-directory?ref_=nav_shopall_btn'
        page_soup = html_parse(url)
        item_list = page_soup.findAll('div', attrs={'class': 'fsdDeptCol'})

        for item1 in item_list:
            try:
                item_list0 = item1.findAll('a')
                for item2 in item_list0:
                    url = x + item2['href']
                    status = check_status(url, file_name)           # Check url in csv to skip if exists
                    if status == 'Y':
                        continue
                    else:
                        try:
                            page1_soup = html_parse(url)
                            try:
                                cont = page1_soup.find('li', attrs={'class': 's-ref-indent-neg-micro'}).find('a')
                            except Exception:
                                try:
                                    url = page1_soup.find('ul', attrs={'class': 'a-unordered-list a-nostyle a-vertical s-ref-indent-one'}).findAll('li')[0].find('a')['href']
                                    status = check_status(url, file_name)  # Check url in csv to skip if exists
                                    if status == 'Y':
                                        continue
                                    else:
                                        cont = page1_soup.find('li', attrs={'class': 's-ref-indent-neg-micro'}).find('a')

                                except Exception:
                                    # if more cont, add more try- except and  ( # Writing cat_1 ) ---------
                                    cat_01 = item2.text.strip()
                                    print(cat_01)
                                    cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09 = '', '', '', '', '', '', '', ''

                                    write_csv(j, url, cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09)
                                    continue

                            url = cont['href']
                            cat_01 = cont.text.strip()
                            status = check_status(url, file_name)           # Check url in csv to write
                            if status == 'Y':
                                continue
                            else:
                                try:
                                    # Writing cat_1 ---------
                                    cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09 = '', '', '', '', '', '', '', ''
                                    write_csv(j, url, cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09)

                                    page2_soup = html_parse(url)
                                    cat2_list = page2_soup.find('ul', attrs={'class': 'a-unordered-list a-nostyle a-vertical s-ref-indent-one'}).findAll('li')
                                    for index2, cat_item2 in enumerate(cat2_list):
                                        try:
                                            cat2_url = cat_item2.find('a')['href']

                                            status = check_status(cat2_url, file_name)           # Check url in csv to write cat 2
                                            if status == 'Y':
                                                continue
                                            else:
                                                cat_02 = cat_item2.find('a').text.strip()
                                                cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09 = '', '', '', '', '', '', ''
                                                write_csv(j, cat2_url, cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09)

                                                page3_soup = html_parse(cat2_url)
                                                cat3_list = page3_soup.find('ul', attrs={'class': 'a-unordered-list a-nostyle a-vertical s-ref-indent-two'}).findAll('li')
                                                for index3, cat_item3 in enumerate(cat3_list):
                                                    try:
                                                        cat3_url = cat_item3.find('a')['href']
                                                        status = check_status(cat3_url, file_name)  # Check url in csv to write cat 3
                                                        if status == 'Y':
                                                            continue
                                                        else:
                                                            cat_03 = cat_item3.find('a').text.strip()
                                                            cat_04, cat_05, cat_06, cat_07, cat_08, cat_09 = '', '', '', '', '', ''
                                                            write_csv(j, cat3_url, cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09)

                                                            page4_soup = html_parse(cat3_url)
                                                            cat4_list = page4_soup.find('ul', attrs={'class': 'a-unordered-list a-nostyle a-vertical s-ref-indent-two'}).findAll('li')
                                                            for index4, cat_item4 in enumerate(cat4_list):
                                                                try:
                                                                    cat4_url = cat_item4.find('a')['href']
                                                                    status = check_status(cat4_url, file_name)  # Check url in csv to write cat 4
                                                                    if status == 'Y':
                                                                        continue
                                                                    else:
                                                                        cat_04 = cat_item4.find('a').text.strip()
                                                                        cat_05, cat_06, cat_07, cat_08, cat_09 = '', '', '', '', ''
                                                                        write_csv(j, cat4_url, cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09)

                                                                        page5_soup = html_parse(cat4_url)
                                                                        cat5_list = page5_soup.find('ul', attrs={'class': 'a-unordered-list a-nostyle a-vertical s-ref-indent-two'}).findAll('li')
                                                                        for index5, cat_item5 in enumerate(cat5_list):
                                                                            try:
                                                                                cat5_url = cat_item5.find('a')['href']
                                                                                status = check_status(cat5_url, file_name)  # Check url in csv to write cat 5
                                                                                if status == 'Y':
                                                                                    continue
                                                                                else:
                                                                                    cat_05 = cat_item5.find('a').text.strip()
                                                                                    cat_06, cat_07, cat_08, cat_09 = '', '', '', ''
                                                                                    write_csv(j, cat5_url, cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09)

                                                                                    page6_soup = html_parse(cat5_url)
                                                                                    cat6_list = page6_soup.find('ul',attrs={'class': 'a-unordered-list a-nostyle a-vertical s-ref-indent-two'}).findAll('li')
                                                                                    for index6, cat_item6 in enumerate(cat6_list):
                                                                                        try:
                                                                                            cat6_url = cat_item6.find('a')['href']
                                                                                            status = check_status(cat6_url, file_name)  # Check url in csv to write cat 6
                                                                                            if status == 'Y':
                                                                                                continue
                                                                                            else:
                                                                                                cat_06 = cat_item6.find('a').text.strip()
                                                                                                cat_07, cat_08, cat_09 = '', '', ''
                                                                                                write_csv(j, cat6_url, cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09)

                                                                                                page7_soup = html_parse(cat6_url)
                                                                                                cat7_list = page7_soup.find('ul', attrs={'class': 'a-unordered-list a-nostyle a-vertical s-ref-indent-two'}).findAll('li')
                                                                                                for index7, cat_item7 in enumerate(cat7_list):
                                                                                                    try:
                                                                                                        cat7_url = cat_item7.find('a')['href']
                                                                                                        status = check_status(cat7_url, file_name)  # Check url in csv to write cat 5
                                                                                                        if status == 'Y':
                                                                                                            continue
                                                                                                        else:
                                                                                                            cat_07 = cat_item7.find('a').text.strip()
                                                                                                            cat_08, cat_09 = '', ''
                                                                                                            write_csv(j, cat7_url, cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09)

                                                                                                            page8_soup = html_parse(cat7_url)
                                                                                                            cat8_list = page8_soup.find('ul', attrs={'class': 'a-unordered-list a-nostyle a-vertical s-ref-indent-two'}).findAll('li')
                                                                                                            for index8, cat_item8 in enumerate(cat8_list):
                                                                                                                try:
                                                                                                                    cat8_url = cat_item8.find('a')['href']
                                                                                                                    status = check_status(cat8_url, file_name)  # Check url in csv to write cat 5
                                                                                                                    if status == 'Y':
                                                                                                                        continue
                                                                                                                    else:
                                                                                                                        cat_08 = cat_item8.find('a').text.strip()
                                                                                                                        cat_09 = ''
                                                                                                                        write_csv(j, cat8_url, cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09)

                                                                                                                        ###### 9
                                                                                                                        """
                                                                                                                        page9_soup = html_parse(cat8_url)
                                                                                                                        cat9_list = page9_soup.find('ul', attrs={'class': 'a-unordered-list a-nostyle a-vertical s-ref-indent-two'}).findAll('li')
                                                                                                                        for index9, cat_item9 in cat9_list:
                                                                                                                            try:
                                                                                                                                cat9_url =cat_item9.find('a')['href']
                                                                                                                                status = check_status(cat9_url, file_name)  # Check url in csv to write cat 5
                                                                                                                                if status == 'Y':
                                                                                                                                    continue
                                                                                                                                else:
                                                                                                                                    cat_09 = cat_item9.find('a').text.strip()                                                                                                                                    
                                                                                                                                    write_csv(j, cat9_url, cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09)

                                                                                                                            except Exception:
                                                                                                                                pass
                                                                                                                        """
                                                                                                                except Exception:
                                                                                                                    pass
                                                                                                    except Exception:
                                                                                                        pass
                                                                                        except Exception:
                                                                                            pass
                                                                            except Exception:
                                                                                pass
                                                                except Exception:
                                                                    pass
                                                    except Exception:
                                                        pass
                                        except Exception:
                                            pass
                                except Exception:
                                    pass
                        except Exception:
                            pass
            except Exception:
                print('Noting Found cat 1')
                pass
    except Exception:
        print(" Very first error ...")
        pass


if __name__ == '__main__':
    main()
