# Web Scraping Wikipedia: Timeline of Programming Languages

This project is a simple Python script that uses the `requests` and `BeautifulSoup` libraries to scrape data from the [Timeline of Programming Languages](https://en.wikipedia.org/wiki/Timeline_of_programming_languages) Wikipedia page. The data is then processed and stored in a CSV file using `pandas`.

## Requirements

This project requires Python 3 and the following Python libraries installed:

- [requests](https://docs.python-requests.org/en/master/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [pandas](https://pandas.pydata.org/)

You can install these libraries using `pip`:

```bash
pip install requests beautifulsoup4 pandas
```

## Usage

1. Download the file

2. To run this script, simply execute the Python file in your terminal:

```bash
python main.py
```

This will generate a CSV file named `programming_languages.csv` in your current directory, containing the timeline of programming languages with their respective years as listed on Wikipedia.

## Dataset

The output dataset contains the following columns:

- `Year`: The year when the programming language was conceived or first used.
- `Language`: The name of the programming language.
