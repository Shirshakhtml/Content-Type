### Description

This code works by Using [Python's Magic Library](https://pypi.org/project/python-magic/) to identify the File Type. The Magic Library in the code helps to identify the MIME(Media Type) type of the response content. Then the code matches the Reponse Headers with the identified Content-Type and shows "Matched" or "Not Matched". If the Content-Type is incorrectly stated it will show "Not Matched".

### Prerequisites

For Windows
```
pip install python-magic-bin
```

For Linux
```
pip install python-magic
sudo apt install libmagic1
```

### Usage
```
python content-type-checker.py URL
```

### References

https://pypi.org/project/python-magic/
https://www.reddit.com/r/learnpython/comments/sjrur0/why_use_libmagic_on_windows_to_get_mimetype_is/
