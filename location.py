import requests
from pyfiglet import Figlet
import folium

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()


        data = {
            '[IP]': response.get('query'),
            '[City]': response.get('city'),
            '[Country]': response.get('state'),
            '[Region]': response.get('regionName'),
            '[ZIP]': response.get('zip'),
            '[Latitude]': response.get('lat'),
            '[Longitude]': response.get('lon'),
        }

        for k, v in data.items():
            print(f'{k}: {v}')

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print("[!] Error connecting to server")

def main():
    preview_text= Figlet(font='slant')
    print(preview_text.renderText('IP INFO BY APACHE'))
    ip = input("Enter ip address: ")
    get_info_by_ip(ip=ip)

if __name__ == '__main__':
    main()
