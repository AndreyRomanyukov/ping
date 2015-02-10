import urllib2
from time import gmtime, strftime, sleep


def main():
    working = True

    while working:
        try:
            response = urllib2.urlopen("http://google.com")
            page_source = response.read()
            print strftime("%H:%M:%S", gmtime()) + str(" Internet OK")
        except:
            print strftime("%H:%M:%S", gmtime()) + str(" No internet")

        sleep(5)

if __name__ == "__main__":
    main()