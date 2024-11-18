# Review based Recommender System for Steam

<div align="center">
    <img src="resources/Collaborative-Recommender-System.webp" width="800" height="400" />
</div>
<div align="center">
    <img src="resources/steam.gif" width="400" height="400" />
    <img src="resources/steam-wallet-sad.gif" width="400" height="400" />
</div>

# Whats it all about?

Recommendation Systems are widely used throughout the
world in all kinds of software. Well known platforms such as
Netflix or Showmax where series/movies are recommended
to you based on certain criteria. Gaming has also picked
up largely since the rapid increase of computation since the
early 2000s. Covid in 2020 also has played a large role in
introducing more people to online entertainment. Online
entertainment while being watching series and/or movies,
is also gaming. This repository provides an investigation into
recommendation systems and how they can be applied to the
online platform Steam, which is the most well known online
platform to acquire games for Desktop/Laptop gaming.

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

### Install required packages

Install the required packages and create a virtual environment by running the
following command if you have [uv](https://docs.astral.sh/uv/) installed:

```bash
uv sync
```

Dependencies can be found in pyproject.toml


## Explore Juypter Notebooks

```bash
├── src
│   ├── main
│   │   ├── games.ipynb
│   │   ├── recommendation_system.ipynb
│   │   └── reviews.ipynb
```