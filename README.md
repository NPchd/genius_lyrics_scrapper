# Genius Lyrics Scrapper
Collect all the lyrics from an Artist.
- All lines from a solo track
- Artists lines from a collaboration

## Installation
use the packaged manager pip3 to install beautifulsoup

```bash
pip3 install beautifulsoup4
```
## Usage
Save in Artist.csv the name the geniusId of an artist
Then just use python3 to compile the scrapper

```bash
python3 src/genius_scrapper.py
```

## Review and foreseen improvement
- Find a way to extract the geniusId of an artist with the genius API available.
- Search again when lyrics are not found. Lyrics lost percentage for an artist can go up to 25%. We consider the remaining data sufficient for the analysis we undertake.
- Call the genius_scrapper with an Artist name as a parameter
```bash
python3 src/genius_scrapper.py artist_name
```