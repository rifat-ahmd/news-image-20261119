# World news of Thursday 19 November 2026, in one image

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/rifat-ahmd/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/rifat-ahmd/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Built for the make.fun bounty [Sum up 19 November's world news in one image](https://make.fun/bounty/news-image-20261119).

38 stories from Thursday 19 November 2026, each checked in two sources: four drawn lead stories
(Trump–Xi–Putin summit, the ICJ's Myanmar genocide ruling, Anthropic's Nasdaq debut, GTA VI's release),
14 drawn tiles grouped by region (Asia, Middle East, Europe, Americas, Africa) and 20 one-line briefs, a key-number strip and a date check.

- `page.html`: the front page, with original inline SVG drawings
- `render.py`: renders it to `entry.png` (1024x1024) with headless Chrome + Pillow
- `main.ts`: copies `entry.png` to `$MAKEFUN_OUTPUT_DIR` (default `/output`)

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
