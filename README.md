# plex-series-orderer

Python script for organize and clean up tv shows name. Result : Better scan from Plex for tv shows.
1. Scan folder containing your tv shows downloads
2. For each folder/file, create a symlink in another folder
    From "Breaking.Bad.S01" to "Breaking Bad Season 1"
3. Make Plex scan this folder

Works with :

"X.Y.S0x.aaaaaaa.ddddddddd/"
"X.Y.S0x.aaaaaaa.ddddddddd.avi"
"X.Y.S0x.aaaaaaa.ddddddddd.mkv"
"X.Y.S0x.aaaaaaa.ddddddddd.mp4"

To do : 

"X Y S0 aaaaaaaa dddddddddd/"
