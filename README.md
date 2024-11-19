README Created for:
https://github.com/SharkmanZA/SteamDeepDive

# Recommender System using review-based Collaborative Filtering for Steam

<div align="center">
    <img src="resources/Collaborative-Recommender-System.webp" width="600" height="300" />
</div>
<div align="center">
    <img src="resources/steam.gif" width="300" height="300" />
    <img src="resources/steam-wallet-sad.gif" width="300" height="300" />
</div>

# Whats it all about?

Steam is a large online platform for PC/laptop games. It is one of the most well known platforms for PC gamers. Finding a new game to play can be a tedious process as there is so much to choose from. For this reason recommendation systems have been put in place.

This project provides an investigation into a recommendation system to see how it can be applied to steam reviews. Steam does not have actual review scores but review comments(text) from users. We have performed sentiment analysis on the reviews to create pseudo-ratings:


```md
|------------|-------------------|
| Sentiment  | Generated Rating  |
|------------|-------------------|
| Positive   |        5          |
|------------|-------------------|
| Neutral    |        3          |
|------------|-------------------|
| Negative   |        1          |
|------------|-------------------|
```

## Data
- Broken original data can be found at https://github.com/kang205/SASRec?tab=readme-ov-file
- The fixed unpreprocessed data is stored on <a href="https://drive.google.com/drive/folders/1b5pLtggyl_XHIwTMnu3I1kbe2_O81_-6?usp=sharing">google drive</a> which will be downloaded programatically. No need for manual placement of the data into a folder.

Moving the data from a broken to a valid state was an iterative and tedious process that cannot be recreated without great lengths of effort. The scripts used to convert the broken JSON data to CSV format can be found under **src/utils** which will be used for normal preprocesing techniques and EDA.


## Sample data for 'Portal 2'

### Game
```json
{
    "app_name": "Portal 2", 
    "developer": "Valve", 
    "early_access": false, 
    "genres": ["Action", "Adventure"], 
    "id": "620", 
    "metascore": 95, 
    "price": 19.99, 
    "publisher": "Valve", 
    "release_date": "2011-04-18", 
    "reviews_url": "http://steamcommunity.com/app/620/reviews/?browsefilter=mostrecent&p=1", 
    "sentiment": "Overwhelmingly Positive", 
    "specs": ["Single-player", "Co-op", "Steam Achievements", "Full controller support", "Steam Trading Cards", "Captions available", "Steam Workshop", "Steam Cloud", "Stats", "Includes level editor", "Commentary available"], 
    "tags": ["Puzzle", "Co-op", "First-Person", "Sci-fi", "Comedy", "Singleplayer", "Adventure", "Online Co-Op", "Funny", "Science", "Female Protagonist", "Action", "Story Rich", "Multiplayer", "Atmospheric", "Local Co-Op", "FPS", "Strategy", "Space", "Platformer"], 
    "title": "Portal 2", 
    "url": "http://store.steampowered.com/app/620/Portal_2/"
}
```

### Review
```json
{
  "compensation": null,
  "date": "2017-02-04",
  "early_access": true,
  "found_funny": null,
  "hours": 16.5,
  "page": 97,
  "page_order": 5,
  "product_id": 296300,
  "products": 620.0,
  "text": "This game deserves more attention! Really fun and priced appropriately.",
  "user_id": null,
  "username": "EXiTiUM"
}
```

## How to run this project?

### Clone the repository 

```bash
git clone https://github.com/SharkmanZA/SteamDeepDive.git
```
or unzip the zipped code

### Install required packages

Install the required packages and create a virtual environment by running the
following command if you have [uv](https://docs.astral.sh/uv/) installed:

```bash
uv sync
```

## Repository structure

### Folders:
- **data/final**: Final preprocessed data
- **data/raw**: Preprocessed but unfiltered data
- **resources**: Images used for README
- **src/main**: Juypter notebooks used for EDA of games, reviews and then the recommendation system
- **src/utils**: Python files used to fix and manipulate data from JSON to CSV format.

### Files:
- **pyproject.toml**: uv metadata file also containing libraries used
- **uv.lock**: universal cross-platform lock file created by uv

```bash
.
├── LICENSE
├── README.md
├── data
│   ├── final
│   │   ├── steam_games.csv
│   │   └── steam_reviews.csv
│   └── raw
│       ├── org_steam_reviews.csv
│       ├── raw_steam_games.csv
│       └── raw_steam_reviews.csv
├── pyproject.toml
├── resources
│   ├── Collaborative-Recommender-System.webp
│   ├── steam-image.jpg
│   ├── steam-wallet-sad.gif
│   └── steam.gif
├── src
│   ├── main
│   │   ├── games.ipynb
│   │   ├── recommendation_system.ipynb
│   │   └── reviews.ipynb
│   └── utils
│       ├── cleanup_steam_games.py
│       ├── cleanup_steam_reviews.py
│       ├── games_to_csv.py
│       ├── reviews_to_csv.py
│       └── sample_data.py
└── uv.lock
```
## Explore Juypter Notebooks

```bash
├── src
│   ├── main
│   │   ├── games.ipynb
│   │   ├── recommendation_system.ipynb
│   │   └── reviews.ipynb
```
