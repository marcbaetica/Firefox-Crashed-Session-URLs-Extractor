# Firefox-Crashed-Session-URLs-Extractor

`Firefox-Crashed-Session-URLs-Extractor` is a script for extract urls from a recovery.jsonlz4_converted.json file after Firefox crashed and corrupted data would not allow the session to restart

### Instructions:
Add file in the same folder location as script and run it

### Data output:

The script processes a list of tab urls for the windows that were not closed and another list of tab urls for windows that were marked as closed (some are common due to the data corruption causing the session to not recover)

The output will result in
- the tab number for each window as it is processed in real time
- a list representing duplicates and diferences between the two lists*

*NOTE: if the duplicate list is empty, this represents a mutual exclusivity relationship between the two lists
