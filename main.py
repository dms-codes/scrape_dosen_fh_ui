import requests
from bs4 import BeautifulSoup as bs
import csv, time

BASE_URL = "https://law.ui.ac.id/staf-pengajar/"
TIMEOUT = 30 
HEADERS = {
    'authority': 'www.dickssportinggoods.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9',
}


s = requests.Session()
html = s.get(BASE_URL, timeout=TIMEOUT, headers=HEADERS).content
soup = bs(html, 'html.parser')

with open('data_dosen_fh_ui.csv','w',newline='') as f:
    writer = csv.writer(f)
    header = 'Nama', 'URL Pengajar','Dosen', 'Gelar', 'Bidang', 'Summary', 'Pendidikan', 'Mata Kuliah', 'Buku', 'Book Chapter', 'Jurnal', 'Publikasi Populer', 'Email'
    writer.writerow(header)

    for div in soup.find_all('div', class_='gdlr-core-accordion-item-content-wrapper'):
        tipe  = div.find('h4').text
        for a in div.find_all('a', href=True):
            name = ''
            tipe_dosen = tipe
            title = ''
            bidang = '' 
            biografi = ''
            pendidikan = ''
            matakuliah = ''
            buku = ''
            book_chapter = ''
            jurnal = ''
            publikasi_populer = ''
            email = ''
            pengajar = a.text.replace('✅','')
            url_pengajar = a['href']
            #print(tipe, pengajar, url_pengajar)
            h = s.get(url_pengajar, timeout=TIMEOUT, headers=HEADERS).content
            sp = bs(h, 'html.parser')
            name_e = sp.find('h3')
            name = name_e.text
            try:
                title_e = sp.find('span', class_='gdlr-core-title-item-caption gdlr-core-info-font gdlr-core-skin-caption')
                title = title_e.text
            except:
                print('Failed to extract title.')

            print(name, title)

            try:
                bidang_e = sp.find('div', class_='gdlr-core-text-box-item-content')
                bidang = bidang_e.text.split('Bidang Studi')[1].replace('.','').strip()
                #print(bidang)
            except:
                print('Failed to extract bidang.')

            content_e = sp.find_all('div', class_='gdlr-core-pbf-element')

            for i, content in enumerate(content_e):
                if i in [0,1]:
                    continue
                elif content.text == 'Biografi':
                    biografi_e = content_e[i+1]
                    for p in biografi_e.find_all('p'):
                        biografi += p.text + '\n'
                    #print(biografi)
                elif content.text == 'Pendidikan':
                    pendidikan_e = content_e[i+1]
                    pendidikan = pendidikan_e.text
                    #print(pendidikan)
                elif content.text == 'Mata Kuliah':
                    for matakuliah_e in content_e[i+1].find_all('div', class_='gdlr-core-icon-list-content-wrap'):
                        matakuliah += matakuliah_e.text + '\n'
                    #print(matakuliah)
                elif content.text == 'Buku':
                    for buku_e in content_e[i+1].find_all('span', class_='gdlr-core-icon-list-content'):
                        buku += buku_e.text + '\n'
                    #print(buku)
                elif content.text == 'Jurnal':
                    for jurnal_e in content_e[i+1].find_all('span', class_='gdlr-core-icon-list-content'):
                        jurnal += jurnal_e.text + '\n'
                    #print(jurnal)
                elif content.text=='Publikasi Populer':
                    for publikasi_populer_e in content_e[i+1].find_all('span', class_='gdlr-core-icon-list-content'):
                        publikasi_populer += publikasi_populer_e.text + '\n'
                    #print(publikasi_populer)
                elif content.text=='Book Chapter':
                    for book_chapter_e in content_e[i+1].find_all('span', class_='gdlr-core-icon-list-content'):
                        book_chapter += book_chapter_e.text + '\n'
                    #print(book_chapter)
                elif content.text=='Email':
                    for email_e in content_e[i+1].find_all('span', class_='gdlr-core-icon-list-content'):
                        email += email_e.text + '\n'
                    #print(email) 

                row = name, url_pengajar, tipe_dosen, title, bidang, biografi, pendidikan, matakuliah, buku, book_chapter, jurnal, publikasi_populer, email
                if row:
                    writer.writerow(row)
                    #print(row)
                f.flush()
