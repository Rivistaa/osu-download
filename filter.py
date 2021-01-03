import json
import pickle

SRmin = 4.9
SRmax = 4.95
mode = 0
status = 1


def FilterMode(db, code):  # osu standard only!
    outdict = []
    for beatmapset in range(0, len(db)):
        for beatmap in range(0, len(db[beatmapset]["beatmaps"])):
            if int(db[beatmapset]["beatmaps"][beatmap]["mode"]) == code:
                outdict.append(db[beatmapset])
                break
    return outdict


def FilterStatus(db, code):  # ranked only!
    outdict = []
    for beatmapset in range(0, len(db)):
        for beatmap in range(0, len(db[beatmapset]["beatmaps"])):
            if int(db[beatmapset]["beatmaps"][beatmap]["status"]) == code:
                outdict.append(db[beatmapset])
                break
    return outdict


def FilterSR(db, min, max): # specific star range pls
    outdict = []
    for beatmapset in range(0, len(db)):
        for beatmap in range(0, len(db[beatmapset]["beatmaps"])):
            if min <= float(db[beatmapset]["beatmaps"][beatmap]["star"]) <= max:
                outdict.append(db[beatmapset])
                break
    return outdict


def CompileIds(db):
    outdict = []
    for beatmapset in range(0, len(db)):
        outdict.append(db[beatmapset]["id"])
    return outdict


def ExportIDs(db):
    pickle.dump(db, open("output.p", "wb"))
    return


def main():
    with open('osu.json') as f:
        database = json.load(f)
    filter1 = FilterMode(database, mode)

    print("Filter1 complete. Found " + str(len(filter1)) + " beatmap sets")
    filter2 = FilterStatus(filter1, status)
    print("Filter2 complete. Found " + str(len(filter2)) + " beatmap sets")

    filter3 = FilterSR(filter2, SRmin, SRmax)
    print("Filter3 complete. Found " + str(len(filter3)) + " beatmap sets")

    print("Generating URLs")
    id = CompileIds(filter3)

    print("Exporting links")
    ExportIDs(id)
    print("Successfully saved " + str(len(id)) + " beatmap sets")
    print("Please run download.py to download the saved beatmaps")


if __name__ == '__main__':
    main()
