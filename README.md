# Steam Game Recommender System

![alt text](resources/steam-image.jpg)

# Whats it all about?

## Some sample data

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

## Install required packages

Install the required packages and create a virtual environment by running the
following command if you have [uv](https://docs.astral.sh/uv/) installed:

```bash
uv sync
```
