#!/usr/bin/env python3

import bs4
import base64
import os

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    index_html = os.path.join(script_dir, "index.html")
    output_html = os.path.join(script_dir, "output", "index.html")

    doc = bs4.BeautifulSoup(open('index.html').read(), 'html.parser')

    # Find all images and embed them
    for img in doc.find_all('img'):
        img_file = os.path.join(script_dir, *(img.attrs['src'].split("/")))
        with open(img_file, 'rb') as i:
            encoded = base64.encodebytes(i.read())
            encoded = encoded.decode('utf-8').replace('\n','')
            img.attrs['src'] = 'data:image/png;base64,{}'.format(encoded)
    
    with open(output_html, 'wb') as output:
        output.write(bytes(str(doc), 'utf-8'))

