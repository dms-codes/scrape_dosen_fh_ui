import requests
from bs4 import BeautifulSoup as bs
import csv

# Constants
BASE_URL = "https://law.ui.ac.id/staf-pengajar/"
TIMEOUT = 30
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
}

# Function to extract and clean text from an element
def extract_text(element):
    if element:
        return element.text.strip()
    return ''

# Initialize a session
s = requests.Session()

# Fetch the HTML content
html = s.get(BASE_URL, timeout=TIMEOUT, headers=HEADERS).content
soup = bs(html, 'html.parser')

# Open a CSV file for writing
with open('data_dosen_fh_ui.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    header = ['Nama', 'URL Pengajar', 'Dosen', 'Gelar', 'Bidang', 'Summary', 'Pendidikan', 'Mata Kuliah', 'Buku', 'Book Chapter', 'Jurnal', 'Publikasi Populer', 'Email']
    writer.writerow(header)

    # Iterate through the staff members
    for div in soup.find_all('div', class_='gdlr-core-accordion-item-content-wrapper'):
        tipe = extract_text(div.find('h4'))

        for a in div.find_all('a', href=True):
            pengajar = extract_text(a).replace('✅', '')
            url_pengajar = a['href']

            # Fetch the individual staff member's page
            h = s.get(url_pengajar, timeout=TIMEOUT, headers=HEADERS).content
            sp = bs(h, 'html.parser')

            name = extract_text(sp.find('h3'))
            title = extract_text(sp.find('span', class_='gdlr-core-title-item-caption gdlr-core-info-font gdlr-core-skin-caption'))

            try:
                bidang = extract_text(sp.find('div', class_='gdlr-core-text-box-item-content').find('p:contains("Bidang Studi")'))
            except:
                bidang = ''

            biografi = ''
            pendidikan = ''
            matakuliah = ''
            buku = ''
            book_chapter = ''
            jurnal = ''
            publikasi_populer = ''
            email = ''

            content_e = sp.find_all('div', class_='gdlr-core-pbf-element')

            for i, content in enumerate(content_e):
                if i in [0, 1]:
                    continue
                elif content.text == 'Biografi':
                    biografi_e = content_e[i + 1]
                    biografi = '\n'.join([p.text.strip() for p in biografi_e.find_all('p')])
                elif content.text == 'Pendidikan':
                    pendidikan_e = content_e[i + 1]
                    pendidikan = extract_text(pendidikan_e)
                elif content.text == 'Mata Kuliah':
                    matakuliah_e = content_e[i + 1]
                    matakuliah = '\n'.join([m.text.strip() for m in matakuliah_e.find_all('div', class_='gdlr-core-icon-list-content-wrap')])
                elif content.text == 'Buku':
                    buku_e = content_e[i + 1]
                    buku = '\n'.join([b.text.strip() for b in buku_e.find_all('span', class_='gdlr-core-icon-list-content')])
                elif content.text == 'Book Chapter':
                    book_chapter_e = content_e[i + 1]
                    book_chapter = '\n'.join([bc.text.strip() for bc in book_chapter_e.find_all('span', class_='gdlr-core-icon-list-content')])
                elif content.text == 'Jurnal':
                    jurnal_e = content_e[i + 1]
                    jurnal = '\n'.join([j.text.strip() for j in jurnal_e.find_all('span', class_='gdlr-core-icon-list-content')])
                elif content.text == 'Publikasi Populer':
                    publikasi_populer_e = content_e[i + 1]
                    publikasi_populer = '\n'.join([pp.text.strip() for pp in publikasi_populer_e.find_all('span', class_='gdlr-core-icon-list-content')])
                elif content.text == 'Email':
                    email_e = content_e[i + 1]
                    email = '\n'.join([e.text.strip() for e in email_e.find_all('span', class_='gdlr-core-icon-list-content')])

            # Create a row for the CSV file
            row = [name, url_pengajar, tipe, title, bidang, biografi, pendidikan, matakuliah, buku, book_chapter, jurnal, publikasi_populer, email]
            
            # Write the row to the CSV file
            writer.writerow(row)
            f.flush()
            print(name, title)

print("Scraping completed and data saved to 'data_dosen_fh_ui.csv'.")
