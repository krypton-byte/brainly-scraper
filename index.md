# Welcome to Brainly-Scraper


## Install Library
```bash
$ pip install brainly-scrapper
# Github Version
$ pip install git+https://github.com/krypton-byte/brainly-scraper
```

## <u>Search Questions </u>

Example:
```python
>>> from brainly_scraper import brainly
>>> scrap=brainly("question", amount: int)
```
## <u> get Question Text</u>
```python
>>> for i in scrap:
...    print(i.question.content)
```
## <u> get Question Media</u>
```python
>>> for i in scrap:
...    for x in i.question.attachments:
...        x.download("media.jpg") # ToFile
...        x.download() # Buffer Type
...        x.url # Media url
```
## <u> get Answer Text</u>
```python
>>> for i in scrap:
...    print(i.answers.content)
```
## <u> get Question Media</u>
```python
>>> for i in scrap:
...    for x in i.answers.attachments:
...        x.download("media.jpg") # ToFile
...        x.download() # Buffer Type
...        x.url # Media url
```
```python
>>> for i in scrap:
...    print(i.question.content)
```
