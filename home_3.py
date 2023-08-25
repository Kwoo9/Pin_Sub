#1. chatgpt에 크롤링 코드 작성 요청

'''
# search word
SSAFY

# URL of the web page to be crawled
https://search.naver.com/search.naver?where=news&sm=tab_jum&query=SSAFY

# Elements containing example article titles
(Example 1)
<a href="https://www.sedaily.com/NewsView/29TAXOGMQC" class="news_tit" target="_blank" onclick="return goOtherCR(this, 'a=nws*e.tit&r=1&i=88000108_000000000000000004223126&g= 011.0004223126&u='+urlencode(this.href));" title="Samsung, 85 billion won to build 3078 medium-sized smart factories for 8 years">Samsung, 85 billion won to build 3078 medium-sized smart factories for 8 years</a>

(Example 2)
<a href="https://www.itbiznews.com/news/articleView.html?idxno=106558" class="news_tit" target="_blank" onclick="return goOtherCR(this, 'a=nws*f. tit&r=2&i=8819br2x_000000000000000000029884&g=5795.0000029884&u='+urlencode(this.href));" title="Pickit, development-related Q&A event held... Direct response from SSAFY developer">Pickit, development-related Q&A event held... <mark>SSAFY</mark>Direct response from developers</a>


# Div with page address information
<div class="sc_page_inner"><a href="?where=news&sm=tab_pge&query=SSAFY&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=24&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p: all,a:all&start=1" onclick="return goOtherCR(this, 'a=nws.paging&r=1&u='+urlencode(urlexpand(this.href)));" role="button" class="btn" aria-pressed="true">1</a><a href="?where=news&sm=tab_pge&query=SSAFY&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=24&mynews =0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=11" onclick="return goOtherCR(this, 'a=nws.paging&r=2&u='+urlencode(urlexpand(this.href) ));" role="button" class="btn" aria-pressed="false">2</a><a href="?where=news&sm=tab_pge&query=SSAFY&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=24&mynews =0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=21" onclick="return goOtherCR(this, 'a=nws.paging&r=3&u='+urlencode(urlexpand(this.href) ));" role="button" class="btn" aria-pressed="false">3</a><a href="?where=news&sm=tab_pge&query=SSAFY&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=24&mynews =0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=31" onclick="return goOtherCR(this, 'a=nws.paging&r=4&u='+urlencode(urlexpand(this.href) ));" role="button" class="btn" aria-pressed="false">4</a><a href="?where=news&sm=tab_pge&query=SSAFY&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=24&mynews =0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=41" onclick="return goOtherCR(this, 'a=nws.paging&r=5&u='+urlencode(urlexpand(this.href) ));" role="button" class="btn" aria-pressed="false">5</a><a href="?where=news&sm=tab_pge&query=SSAFY&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=24&mynews =0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=51" onclick="return goOtherCR(this, 'a=nws.paging&r=6&u='+urlencode(urlexpand(this.href) ));" role="button" class="btn" aria-pressed="false">6</a><a href="?where=news&sm=tab_pge&query=SSAFY&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=24&mynews =0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=61" onclick="return goOtherCR(this, 'a=nws.paging&r=7&u='+urlencode(urlexpand(this.href) ));" role="button" class="btn" aria-pressed="false">7</a><a href="?where=news&sm=tab_pge&query=SSAFY&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=24&mynews =0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=71" onclick="return goOtherCR(this, 'a=nws.paging&r=8&u='+urlencode(urlexpand(this.href) ));" role="button" class="btn" aria-pressed="false">8</a><a href="?where=news&sm=tab_pge&query=SSAFY&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=24&mynews =0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=81" onclick="return goOtherCR(this, 'a=nws.paging&r=9&u='+urlencode(urlexpand(this.href) ));" role="button" class="btn" aria-pressed="false">9</a><a href="?where=news&sm=tab_pge&query=SSAFY&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=24&mynews =0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=91" onclick="return goOtherCR(this, 'a=nws.paging&r=10&u='+urlencode(urlexpand(this.href) ));" role="button" class="btn" aria-pressed="false">10</a></div>

# Requirements
Extract only the title text of articles that exist from page 1 to page 10 of the web page you want to crawl, convert it into a text in a single line, and write a text file with the search term as the title in Python code.
'''



#2. 결과물 확인
import requests
from bs4 import BeautifulSoup

# URL of the web page to be crawled
url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=SSAFY"

# Fetch the webpage content
response = requests.get(url)
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Initialize an empty list to store article titles
article_titles = []

# Find all elements with the class "news_tit"
article_elements = soup.find_all("a", class_="news_tit")

# Extract and append article titles to the list
for article in article_elements:
    title = article.get_text(strip=True)  # Get text and remove any extra spaces
    article_titles.append(title)

# Convert the list of titles to a single string
titles_text = "\n".join(article_titles)

# Write the titles to a text file
search_term = "SSAFY"
output_filename = f"{search_term}_article_titles.txt"

with open(output_filename, "w", encoding="utf-8") as f:
    f.write(titles_text)

print(f"Article titles extracted and saved to '{output_filename}'.")



#3. 코드 수정 재요청
import requests
from bs4 import BeautifulSoup

# Initialize an empty list to store article titles
article_titles = []

# Loop through pages 1 to 10
for page in range(1, 11):
    # URL of the web page to be crawled
    url = f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query=SSAFY&start={(page - 1) * 10 + 1}"

    # Fetch the webpage content
    response = requests.get(url)
    html_content = response.text

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all elements with the class "news_tit"
    article_elements = soup.find_all("a", class_="news_tit")

    # Extract and append article titles to the list
    for article in article_elements:
        title = article.get_text(strip=True)  # Get text and remove any extra spaces
        article_titles.append(title)

# Convert the list of titles to a single string
titles_text = "\n".join(article_titles)

# Write the titles to a text file
search_term = "SSAFY"
output_filename = f"{search_term}_article_titles_fixed.txt"

with open(output_filename, "w", encoding="utf-8") as f:
    f.write(titles_text)

print(f"Article titles extracted and saved to '{output_filename}'.")
