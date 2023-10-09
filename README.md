# Python Web Scraping for Law Faculty Staff Information

This Python script is designed to scrape information about staff members from the Law Faculty of the University of Indonesia's website. It collects data such as names, titles, fields of study, biographies, education, courses taught, books, book chapters, journals, popular publications, and email addresses of the staff members. The data is then stored in a CSV file for further analysis.

## Prerequisites

Before running the script, make sure you have the following Python libraries installed:

- `requests`: Used to make HTTP requests to the website.
- `BeautifulSoup` (imported as `bs`): A library for parsing HTML content.
- `csv`: Used to write data to a CSV file.

You can install these libraries using `pip`:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Clone this repository or download the Python script to your local machine.

2. Open the script in your favorite text editor or integrated development environment (IDE).

3. Customize the script if needed:

   - `BASE_URL`: The URL of the Law Faculty staff page you want to scrape.
   - `TIMEOUT`: The timeout for HTTP requests (in seconds).
   - `HEADERS`: HTTP headers for requests.

4. Run the script:

   ```bash
   python your_script_name.py
   ```

   Replace `your_script_name.py` with the actual name of the script.

5. The script will start scraping staff information and print the names and titles of each staff member as it progresses. Once completed, the data will be saved to a CSV file named `data_dosen_fh_ui.csv` in the same directory as the script.

## Output

The CSV file `data_dosen_fh_ui.csv` will contain the following columns:

- `Nama`: Staff member's name.
- `URL Pengajar`: URL to the staff member's profile.
- `Dosen`: Type of staff member.
- `Gelar`: Title or academic degree.
- `Bidang`: Field of study or specialization.
- `Summary`: Biography or summary of the staff member.
- `Pendidikan`: Education background.
- `Mata Kuliah`: Courses taught by the staff member.
- `Buku`: Books authored or co-authored.
- `Book Chapter`: Chapters in books authored or co-authored.
- `Jurnal`: Journal publications.
- `Publikasi Populer`: Popular publications.
- `Email`: Staff member's email address.

## Note

- Make sure to respect the website's terms of use and scraping policies.
- This script is provided as-is and may require adjustments to work with different websites or changes to the target website's structure.

---

**Disclaimer**: This README is provided for informational purposes only. The use of web scraping tools and techniques to collect data from websites may be subject to legal and ethical considerations. Always ensure that you have the necessary permissions and comply with applicable laws and terms of service when scraping websites.
