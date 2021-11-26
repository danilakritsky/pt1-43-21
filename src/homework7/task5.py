"""Работа с файлами.

5. В файле хранятся данные с сайта IMDB. Скопированные данные
хранятся в файле ./data_hw5/ ratings.list.
a. Откройте и прочитайте файл(если его нет необходимо вывести
ошибку).
b. Найдите ТОП250 фильмов и извлеките заголовки.
c. Программа создает 3 файла top250_movies.txt – названия
файлов, ratings.txt – гистограмма рейтингов, years.txt –
гистограмма годов.
"""

from collections import Counter
from pathlib import Path
import re
from typing import Any
from typing import Callable
from zipfile import ZipFile

TOP_MOVIES_COUNT = 250
ZIP_PATH = 'data_hw5/ratings.list.zip'
FNAME = 'ratings.list'
SOURCE_ENCODING = 'latin-1'
OUTPUT_ENCODING = 'utf-8'
DELIMITER = chr(32) * 2
HIST_WIDTH = 20
OUTPUT_DIR = Path('task5_output')
RATINGS_OUTPUT = OUTPUT_DIR / 'ratings.txt'
TITLES_OUTPUT = OUTPUT_DIR / 'top250.txt'
YEARS_OUTPUT = OUTPUT_DIR / 'years.txt'


def get_data() -> list[list[str]]:
    """Return the data for top 250 movies from a zipped file."""
    try:
        line: bytes | str
        with ZipFile(ZIP_PATH, mode='r') as zip_file:
            with zip_file.open(FNAME) as file:
                for line in file:
                    if (header := line.decode(SOURCE_ENCODING)).endswith('Title\n'):
                        break
                lines = [header.strip()]
                for num, line in enumerate(file, 1):
                    lines.append(line.decode(SOURCE_ENCODING).strip())
                    if num == TOP_MOVIES_COUNT:
                        break
        # parse each row into a list of column
        parsed: list[list[str]] = []
        for line in lines:
            splitted = [col.strip() for col in line.split(DELIMITER)]
            if not parsed:  # remove the first extra column in header
                del splitted[0]
            parsed.append(splitted)
        return parsed
    except (FileNotFoundError, KeyError) as err:
        raise SystemExit('File not found.') from err


def get_column(col_name: str, map_func: Callable = lambda x: x) -> list[Any]:
    """Get a dataset's column by name."""
    header, *rows = get_data()
    col_index = header.index(col_name)
    col = [header[col_index]] + [map_func(row[col_index]) for row in rows]
    return col


def make_histogram(
        col_name: str, fname: str | Path, /,
        map_func: Callable, title: str = '') -> None:
    """Create a histogram from a data column and save it to a file."""
    header, *rows = get_column(col_name, map_func)
    bins = Counter(rows)
    max_val = max(bins.values())
    with open(fname, 'w', encoding=OUTPUT_ENCODING) as file:
        print(header if not title else title, file=file)
        for cur_bin in sorted(bins):
            print(
                cur_bin,
                '#' * int((bins[cur_bin] / max_val) * HIST_WIDTH + 1), bins[cur_bin], file=file
            )


def col_to_file(col_name: str, fname: str | Path) -> None:
    """Save a column from the dataset to a file."""
    rows = get_column(col_name)
    with open(fname, 'w', encoding=OUTPUT_ENCODING) as file:
        for row in rows:
            print(row, file=file)


def main() -> None:
    """Create 3 files with top 250 movies titles, and histograms for year and rank."""
    if not OUTPUT_DIR.exists():
        OUTPUT_DIR.mkdir(parents=True)
    col_to_file('Title', TITLES_OUTPUT,)
    make_histogram('Rank', RATINGS_OUTPUT, float)
    make_histogram(
        'Title', YEARS_OUTPUT,
        # use extra pattern to handle years like 2013/I
        lambda x: int(re.findall(r'\((\d+).*\)', x)[0]), title='Year')


if __name__ == '__main__':
    main()
