#!/usr/bin/python3
""" print bs4 object """
if __name__ == "__main__":
    from bs4 import BeautifulSoup as soupy
    myfile = open('python.html')
    soup = soupy(myfile, "lxml")
    print("BeautifulSoup Object: {}\na: {}\nstrong: {}".format
          (type(soup), soup.find_all('a'), soup.find_all('strong')))
    print("id: {}\ncss/class: {}\ncssprint: {}".format
          (soup.find('div', {"id":"inventor"}),
           soup.select('#inventor'), soup.select('.wow')))

    """
    notice how the print statements return single item lists
    $ ./printSoup.py
    BeautifulSoup Object: <class 'bs4.BeautifulSoup'>
    a: [<a href="https://facebook.com">here</a>]
    strong: [<strong>Friends</strong>]
    id: <div id="inventor">Mark Zuckerberg</div>
    css/class: [<div id="inventor">Mark Zuckerberg</div>]
    =========================================================
    =========================================================
    Lets get the actual content now
    """
    print("===============================================")
    print("================================================")
    fbUrl = soup.find_all('a')[0]['href']
    inventor = soup.find('div', {"id":"inventor"}).text
    spanContent = soup.select('span')[0].getText()
    print("Facebook URL: {}\nInventor: {}\nSpan content: {}".format
          (fbUrl, inventor, spanContent))

    """
    Much better! now we can easily ready the cleaned data
    that should look exactly like
    $ ./printSoup.py
    BeautifulSoup Object: <class 'bs4.BeautifulSoup'>
    a: [<a href="https://facebook.com">here</a>]
    strong: [<strong>Friends</strong>]
    id: <div id="inventor">Mark Zuckerberg</div>
    css/class: [<div id="inventor">Mark Zuckerberg</div>]
    cssprint: [<p class="wow"> Your gateway to social web! </p>]
    ===============================================
    ================================================
    Facebook URL: https://facebook.com
    Inventor: Mark Zuckerberg
    Span content: You know it's easy to get intouch with
          yourFriends on web!
    """
    
