import time
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


def extract_achievements() -> list:
    achievements = []
    keywords = ["story", "nether", "end", "adventure", "husbandry"]
    response = fetch_page_content()
    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.select("table tbody")

    for element in elements:
        code_tags = element.find_all("code")
        for code_tag in code_tags:
            if any(keyword in code_tag.get_text() for keyword in keywords):
                achievements.append(code_tag.get_text())

    return achievements
