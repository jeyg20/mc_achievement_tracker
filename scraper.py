import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

retries = 3


def fetch_page_content():
    url: str = "https://minecraft.wiki/w/Advancement"
    for n in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()

            break

        except HTTPError as exc:
            error_code = exc.response.status_code
            print(error_code)

    return response


def get_achievements():
    names = []
    achievements = []
    imgs = []
    keywords = ["story", "nether", "end", "adventure", "husbandry"]
    response = fetch_page_content()
    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.select("table tbody")

    for element in elements:
        code_tags = element.find_all("code")
        b_tags = element.find_all("b")
        img_tags = element.find_all("img")

        filter_code_tags = [item for item in code_tags if "#" not in item.get_text()]

        for name, code, img in zip(b_tags, filter_code_tags, img_tags):
            names.append(name.get_text())
            imgs.append("https://minecraft.wiki/" + img["src"])
            if code.get_text():
                achievements.append("minecraft:" + code.get_text())

    return names, achievements, imgs


print(get_achievements())
