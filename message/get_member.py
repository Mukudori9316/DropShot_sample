from urllib import request
from bs4 import BeautifulSoup


class GetMember:
    url = "http://ustt-2011.com/buinnshoukai.html"          # Pythonの公式ページのURL
    mem_page = request.urlopen(url).read()
    members = []
    year_choices, name_choices = [], []
    soup = BeautifulSoup(mem_page, "html.parser")
    div = soup.div
    table = div.find_all("td", align="center", height="30")
    member_list = []
    for p in table:
        member = p.string
        member_list.append(member[:-1])
    year = member_list[2::4]
    names = member_list[3::4]
    for y, n in zip(year, names):
        members.append((y, n))
        year_choices.append((y, y))
        name_choices.append((n, n))
    year_choices, name_choices = tuple(year_choices), tuple(name_choices)
