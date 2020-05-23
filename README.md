# Firefox-Crashed-Session-URLs-Extractor

`Firefox-Crashed-Session-URLs-Extractor` is a script for extract urls from a recovery.jsonlz4_converted.json file after Firefox crashed and corrupted data would not allow the session to restart

### Instructions:
Add file in the same folder location as script and run it

### Data output:

The script processes a list of tab urls for the windows that were not closed and another list of tab urls for windows that were marked as closed (some are common due to the data corruption causing the session to not recover)

The output will result in
- the tab number for each window as it is processed (logged for debugging purposes)
- a sets of (therefore unique) items representing the tabs that were open at the time of forced browser shutdown
- a sets of (therefore unique) items representing the tabs that were closed at the time of forced browser shutdown (there is overlap between the set above and this one due to the data corruption)
- a list of duplicate items found among open tabs
- a list of duplicate items found among closed tabs
- finally, and most importantly, an alphabetically sorted list of all tabs representing the union between the two sets. All items in this list are unique
