# notability-zotero-sync
Zotero is a great PDF storage software. For books I generally download from zotero to my ipad to read and annotate. However once annotated I have two different copies of the PDF and would like to read my annotatoins from my computer through zotero. Initially I aimed for a full sync but given the *pain points* section I export individual PDFs and they automatically sync to zotero.

## To Use
Export note from notability as pdf into notability destination folder "Desktop/notability-zotero-sync", notability-sync-folder-action-script.scpt is watching for folder changes
and triggers sync.py when the pdf is added. sync.py searchs the zotero storage file system for any pdfs of the same name and replaces them. 


## Pain points:
- notability stores in google drive in .note format which can only be exported to pdf
through notability client
- notability client no longer is "scriptable" in the AppleScript sense of the word.
This means using the application to automatically do this is painful
- Changing the notability name from what zotero stores results in this failing.



## Reactivating folder actions

This breaks when folder action script is updated using update_folder_action_scripts.sh.
To fix:

1. Go to the notability export destination folder "Desktop/notability-zotero-sync"
2. Right click folder and go services > folder actions setup
3. Click run service
4. Uncheck "Enable Folder Actions"
5. Check "Enable Folder Actions"
6. Hit yes 