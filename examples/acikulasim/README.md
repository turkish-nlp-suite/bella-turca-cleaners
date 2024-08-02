## Academic Article Cleaning :mortar_board:

This example refers to the academic articles taken from Acik Ulasim. The config looks like:


```
replace:
  - extras: "no"
delete:
  - extras: "no"
custom_code: "yes"
crop_header_footer:
 - header
 - footer
keep_emoticon: "no"
```

* Since this is academic work, we don't expect many emoticon, but we safeguard the text in case and delete the emoticon.
* Articles from this website contains an abstract area, list of keywords and possibly bibliography lines.
* We included more cleaning code as well.
* We didn't kill any Arabic or other foreign characters, as they appear as parts of named entities.
The config file is located at `bella_cleaner/cleaner/configs/acikulasim/custom.yaml`. 

Roughly like this:


```
ARTICLE METADATA - Authors, publication date etc. PARSED OUT
ABSTRACT: ..... ....
ARTICLE BODY
BIBLIOGRAPHY  .... PARSED OUT

```

Run and play with `example.py` for more.
