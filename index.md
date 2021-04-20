# Welcome to Brainly-Scraper


## Install Library
```bash
$ pip install brainly-scrapper
# Github Version
$ pip install git+https://github.com/krypton-byte/brainly-scraper
```
<u><h2> Search Questions </h2></u>

Example:
```python
>>> from brainly_scraper import brainly
>>> scrap=brainly("question", amount: int)
```
<u><h2> get Question Text</h2></u>
```python
>>> for i in scrap:
...    print(i.question.content)
```
<u><h2> get Question Media</h2></u>
```python
>>> for i in scrap:
...    for x in i.question.attachments:
...        x.download("media.jpg") # ToFile
...        x.download() # Buffer Type
...        x.url # Media url
```
<u><h2> get Answer Text</h2></u>
```python
>>> for i in scrap:
...    print(i.answers.content)
```
<u><h2> get Question Media</h2></u>
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
