import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "postaviliprofesore.settings")
django.setup()

from mainapp.models import UpdatedFiles  # noqa: E402


def generatelink(href):
    return "https://www.ucg.ac.me/" + href


def getlinks(url):
    # url = ['https://www.ucg.ac.me/objave_spisak/blog/1247']

    try:
        data = requests.get(url)
        data = data.text

        soup = BeautifulSoup(data, 'html.parser')

        dblinks = UpdatedFiles.objects.filter(webtag=url).values_list('link', flat=True)
        weblinks = []

        for div in soup.find_all('a', class_='col-xs-12', href=True):
            for h3 in div.find_all('h3'):
                title = h3.text
            link = generatelink(div['href'])
            weblinks.append(link)
            for p in div.find_all('p'):
                p = p.text
                try:
                    date = datetime.strptime(p, "%d.%m.%Y").date()
                except Exception:
                    subjecttag = p

                    continue  # Use this when getting the last tag
            saveitem = UpdatedFiles(title=title, link=link, date=date, subjecttag=subjecttag, webtag=url)  # Insert new items into db
            if link not in dblinks:
                saveitem.save()
                print("Saved: {}\n".format(saveitem.link))

        for i in dblinks:
            if i not in weblinks and weblinks:  # Second weblinks checks that the list isn't empty, aka the site has sent a response

                try:
                    toremove = UpdatedFiles.objects.get(link=i)
                    toremove.delete()
                    print("Deleted {}\n".format(toremove))
                except Exception:
                    "Failed to remove object\n"
                    continue

    except Exception as e:
        print(str(e))
        return ["Unable to fetch UCG website"]


# Updates the existing database by iterating through every known link, wiping the db and rewriting
if __name__ == "__main__":
    webtags = UpdatedFiles.objects.values_list('webtag', flat=True)
    uniquetags = []
    for i in webtags:
        if i not in uniquetags:
            uniquetags.append(i)

    if uniquetags == []:
        uniquetags.append("https://www.ucg.ac.me/objave_spisak/blog/1247")  # Placeholder in case there is nothing in db

    for i in uniquetags:
        getlinks(i)
# TODO: PUT THIS INTO A WHILE LOOP
