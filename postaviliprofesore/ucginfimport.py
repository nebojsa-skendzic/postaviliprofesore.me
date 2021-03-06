import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
import django
import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "postaviliprofesore.settings")
django.setup()

from mainapp.models import UpdatedFiles  # noqa: E402


def generatelink(href):
    return "https://www.ucg.ac.me/" + href


def getlinks(url):
    # url = ['https://www.ucg.ac.me/objave_spisak/blog/1247']
    urllong = "https://www.ucg.ac.me/objave_spisak/" + url
    print("Checking: {}".format(url))
    try:
        data = requests.get(urllong)
        data = data.text

        soup = BeautifulSoup(data, 'html.parser')

        tosave = True
        linksaved = False

        try:
            timecheck = UpdatedFiles.objects.get(webtag=url)
            try:
                timecheck = timecheck.sitedata[0]['link']
            except:
                pass
        except Exception:
            timecheck = ""
            linksaved = True

        weblinks = []
        savedata = []
        for div in soup.find_all('a', class_='col-xs-12', href=True):
            for h3 in div.find_all('h3'):
                title = h3.text
            link = generatelink(div['href'])

            if timecheck == link and not linksaved:
                tosave = False
                linksaved = True
            else:
                linksaved = True

            weblinks.append(link)
            for p in div.find_all('p'):
                p = p.text
                try:
                    date = datetime.strptime(p, "%d.%m.%Y").timestamp()
                except Exception:
                    subjecttag = p

                    continue  # Use this when getting the last tag
            content = {'title': title, 'link': link, 'date': date, 'subjecttag': subjecttag}  # Insert new items into db
            savedata.append(content)

        try:
            if tosave and linksaved:
                UpdatedFiles.objects.get(webtag=url).delete()
                saveitem = UpdatedFiles(webtag=url, sitedata=savedata)
                print("Updating {}\n".format(saveitem.webtag))
                saveitem.save()
        except Exception:
            if tosave:
                saveitem = UpdatedFiles(webtag=url, sitedata=savedata)
                print("Saving {}\n".format(saveitem.webtag))
                saveitem.save()
            else:
                pass

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
        uniquetags.append("blog/5625")  # Placeholder in case there is nothing in db

    for i in uniquetags:
        getlinks(i)
        #time.sleep(1)
# TODO: PUT THIS INTO A WHILE LOOP
