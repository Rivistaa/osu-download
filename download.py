import urllib.request
import pickle
from os import path
from multiprocessing.pool import ThreadPool


file = "output.p"
outputdir = "./output/"


def displayWarning():
    print("This script will download all the urls in a output file from filter.py")
    print("WARNING: THIS PROCESS CAN TAKE A VERY LONG TIME DEPENDING ON HOW MANY BEATMAPS ARE BEING DOWNLOADED")
    print("Also this will eat your bandwith for breakfast. Be careful if you have a datacap imposed by your ISP and attempt to download all of bloodcat")
    print("I am not responsible for abuse")


def getUrls(filename):
    return pickle.load(open(filename, "rb"))


def downloader(link):
    print(str(link)+"\n")
    urllib.request.urlretrieve('https://beatconnect.io/b/'+str(link), outputdir + str(link) + ".osz")
    return


def main():
    displayWarning()
    if path.exists(file):
        links = getUrls(file)
        print("Sucessfully loaded " + str(len(links)) + " beatmap urls")
        print("Begin download")
        counter = 0
        # Run 5 multiple threads. Each call will take the next element in urls list
        results = ThreadPool(5).imap_unordered(downloader, links)
        for r in results:
            counter = counter + 1
            print(str(counter) + "/" + str(len(links)))

        print("download complete")
        return

    else:
        print("B-baka. you need to run filter.py to generate a list to download first!")
        print("Error: idiot")
        return


if __name__ == '__main__':
    main()
