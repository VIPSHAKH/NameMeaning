import urllib.request
import html.parser
import urllib.parse

class MyHTMLParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.is_target = False
        self.result = ""

    def handle_starttag(self, tag, attrs):
        if tag == "div" and ("class", "space-y-4") in attrs:
            self.is_target = True

    def handle_endtag(self, tag):
        if tag == "div":
            self.is_target = False

    def handle_data(self, data):
        if self.is_target:
            self.result += data.strip()

def ism_manosi(ism):
    url = f"https://ismlar.com/name/{ism}"
    
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode()
        
        parser = MyHTMLParser()
        parser.feed(html)
        
        return parser.result if parser.result else "Ma'lumot topilmadi."
    
    except Exception:
        return "Xatolik yuz berdi yoki ism topilmadi."
    
def create_image(name: str, meaning: str) -> str:
    base_url = "https://rest.apitemplate.io/55b77b233e707b82@9nGa07Pq/image.png"
    params = {
        'text_quote.text': meaning,
        'text_author.text': name
    }
    encoded_params = urllib.parse.urlencode(params)
    full_url = f"{base_url}?{encoded_params}"
    return full_url
