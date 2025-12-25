from pathlib import Path

import requests
from pydantic_settings import BaseSettings

YEAR = 2025

URI_TEMPLATE = "http://adventofcode.com/{year}/day/{day}/input"
CACHE_DIR = Path("tmp/")


class AOCSettings(BaseSettings):
    SESSION: str
    USERAGENT: str


def _cache_input(content: str, day: int) -> None:
    (CACHE_DIR / f"day{day}.txt").write_text(content)


def _check_cache(day: int) -> str | None:
    path = CACHE_DIR / f"day{day}.txt"
    if path.exists():
        return path.read_text()
    return None


def get_puzzle_input(day: int) -> str:
    if text := _check_cache(day):
        return text
    settings = AOCSettings()
    uri = URI_TEMPLATE.format(year=YEAR, day=day)
    response = requests.get(
        uri,
        cookies={"session": settings.SESSION},
        headers={"User-Agent": settings.USERAGENT},
    )
    assert response.status_code == 200
    text = response.text
    _cache_input(text, day)
    return text


def day_from_filename(filename: str) -> int:
    return int(filename.split(".")[-2].split("day")[-1])
