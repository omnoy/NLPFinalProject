from bs4 import BeautifulSoup


def parser(results, body) -> dict:
    key_buffer = ""
    current_key = "title"
    results[current_key] = ""

    last_key = False # If parser found 'פסק-דין' last_key = True

    for c in body:
        if ":" == c or key_buffer == "פסק-דין":
            c = ""
            if not last_key:

                results[current_key] = results[current_key][:-len(key_buffer)]

                if key_buffer in results.keys():
                    current_key = "בשם " + key_buffer
                else:
                    current_key = key_buffer


                results[current_key] = ""
                key_buffer = ""

            """ This is condition for last key """
            if current_key == "פסק-דין":
                last_key = True

        elif c in [" ", "\n", "\r"]:
            key_buffer = ""
        else:
            key_buffer += c

        results[current_key] += c

    return results


class HtmlToJson:

    def __init__(self):
        pass

    def __call__(self, html,link=None,date=None):
        if link:
            results = {"link":link.replace("\\","/")}
        else:
            results = {}

        soup = BeautifulSoup(html, 'html.parser')
        results['head'] = soup.title.string
        results['body'] = soup.body.text.strip()
        results['date'] = date
        return parser(results,results['body'])
