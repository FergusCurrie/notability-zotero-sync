"""
Small script to sync to notability. 

Going to need to: get pdfs from /Users/ferguscurrie/Desktop/notability-sync-whatever

Search the file system of notability for corresponding pdf name

Move pdf and overwrite

Delete pdf in notability sync.
"""
import os


def get_notability_pdfs():
    return [x for x in os.listdir(notability_pdf_directory) if ".pdf" in x]


def path_to_zotero(fn):
    for sub_directory in [x for x in os.listdir(zotero_directory) if "." not in x]:
        # print(sub_directory)
        # sub_directory is a random code
        sub_directory_pdfs = [
            x for x in os.listdir(f"{zotero_directory}/{sub_directory}/") if ".PDF" in x
        ]
        if len(sub_directory_pdfs) > 0:
            sub_directory_pdf = sub_directory_pdfs[0]

            if fn == sub_directory_pdf.replace(".PDF", ".pdf"):
                return f"{zotero_directory}/{sub_directory}/{sub_directory_pdf}"


notability_pdf_directory = "/Users/ferguscurrie/Desktop/notability-zotero-sync"
zotero_directory = "/Users/ferguscurrie/Zotero/storage/"

notability_pdfs = get_notability_pdfs()

for pdf in notability_pdfs:
    dir = path_to_zotero(pdf)
    print(dir)
    if dir is None:
        continue
    else:
        # this is in notability, copy it in
        print(dir)
        os.rename(f"{notability_pdf_directory}/{pdf}", f"{dir}")
