import requests
import json
import bs4


def get_result_html():
    code_postal = input('type your po code')
    page= 'https://www.wunderground.com/cgi-bin/findweather/getForecast?query=' + code_postal
    result = requests.get(page)
    return result.text

def get_meteo(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    location = soup.find(class_ = "hi" ).get_text()
    return print(location)

#wu-value wu-value-to

def main ():
    html = get_result_html()
    #print(html)
    get_meteo(html)




if __name__ == '__main__':
    main()
