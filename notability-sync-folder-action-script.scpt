#!/usr/bin/osascript

on adding folder items to this_folder after receiving added_items
    # run python script 
    tell application "Terminal"
        delay 5
        do shell script "python3 ~/notability-zotero-sync/sync.py"
    end tell
end adding folder items to