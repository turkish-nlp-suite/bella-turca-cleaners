# Bella Turca corpus cleaners

Welcome to Bella Turca's cleaning code. [Bella Turca](https://huggingface.co/datasets/turkish-nlp-suite/BellaTurca) is a big & diverse corpus for training Turkish models and these are the cleaning code used during creation of Bella Turca. 

## Install

Change directory to the root drectory then make a `python setup.py install`. Choose Python version/binary and environment settings up to your taste. 

## Cleaning code
### Functionality
The main class `Cleaner` has only one public functionality, cleaning text. This method is called `Cleaner.clean`.

### Code structure
The code is structured to be modular and separate data needs and the code itself. The main class `Cleaner` includes code for a basic cleaning, then code to load and run custom configuration per genre.  
At the runtime, a `Cleaner` class objects holds all the data of the given configuration. Configurations are provided by yamls under configuration directories. While creating a `Cleaner` class instance, we provide the place of the custom data directory to `__init__` and that's it.
Here's how the custom config directories that we used look like this:

```
duygu@turkish-corpus-cleaner/bella_cleaner/cleaner/configs$ ls books/
custom_clean.py  custom.yaml  __init__.py  page.py

duygua/turkish-corpus-cleaner/bella_cleaner/cleaner/configs$ ls crafted_crawl/
custom_clean.py  custom.yaml  footer.py  __init__.py  __pycache__

duygu@turkish-corpus-cleaner/bella_cleaner/cleaner/configs$ ls dergipark/
custom.yaml  footer.py  header.py  __init__.py  split_into_sentences.py

duygu@turkish-corpus-cleaner/bella_cleaner/cleaner/configs$ ls forums/
custom_clean.py  custom.yaml  __init__.py

duygu@turkish-corpus-cleaner/bella_cleaner/cleaner/configs$ ls web_crawl/
custom_clean.py  custom.yaml  __init__.py
```

### Usage
Following the design above, one has to create a `Cleaner` class object. This class takes two arguments, the base directory and a config name. Looks like this:

```
base_dir = "/home/duygu/Desktop/Work/bella-turca-cleaners"  # should be the root directory of the package
config_name = "acik_ulasim"

cleaner = Cleaner(base_dir=base_dir, config_name=config_name)
text = "Hello, this is Duygu!"
text = cleaner.clean(text)
``` 

Config name can be `None`, then a basic cleaning is made. Configs that are used creating Bella Turca can be found under `bella_cleaner/cleaner/configs`.  
When you want to create a new config for a new genre, make a directory under `bella_cleaner/cleaner/configs/` . Create a `custom.yaml` under this directory accordingly. If one wants a custom cleaning, a config directory is a must. A custom yaml looks like this:

```
replace:
  - extras: "no"
delete:
  - extras: "no"
custom_code: "yes"
keep_emoticon: "no"
kill_foreign_chars:
 - arabic
 - chinese
 - korean
has_pages: "yes"
```

Fields are as follows:  

**replace:** Whether you have custom replacements. The value can be `override` or `append`. Append will add custom replacements to the base replacements and override will override the base replacements.  
**delete:** Whether you have custom deletions. The values are the same with replacements.  
**custom_code:** Whether you have custom code you wanna add on top of the basic cleaning code.  
**keep_emoticon:** Whether you wanna kill or keep emoticon characters. For web crawl type genres, we kep emoticons and for academical text we killed emoticon.  
**kill_foreign_chars:** Whether you wanna kill or keep some special alphabet characters From Arabic, Chinese or Korean alphabet. We kept these sort of characters in AcademiaCrawl, because they refer to entity names. In web crawl type grenres, usually they're trash and we delete them.  
**has_pages**: This parameter is for book and article types where there are several pages. We processed the first and the last page individually as first page usually contains book metadata and last pages might contain bibliography. Also one can make processing per page, such as deleting page numbers and headers.    

For each of these fields, if you want to include custom code you put it under that directory. Please navigate to `bella_cleaner/cleaner/configs/` for the examples.


### Examples
Please navigate to [Examples](https://github.com/turkish-nlp-suite/bella-turca-cleaners/tree/main/examples/cleaner) directory. We included examples of book, academic article and web scrape collection filtering.


## Filtering code
### Functionality
The main class `Filterer` has only one public functionality, cleaning text. This method is called `Filterer.filter`.

### Code structure
The code structure and configuration is same with `Cleaner` class. Here's how an example custom config directory looks like:

```
duygu@turkish-corpus-cleaner/bella_cleaner/filterer/configs$ ls books/
custom.yaml  filter_religion.py  quality_document.py  quality_sentence.py  topic_document.py
```

### Usage
Usage is also the same with `Cleaner` class. One creates a `Filterer` object and calls the `filter` method. Again, if one wants a custom cleaning, a config directory is a must. A custom yaml looks like this:

```
topic:
  - document
  - sentence
length:
  - document:
     - char_limit: 100
     - word_limit: 20
     - sentence_limit: 5
  - sentence:
    - word_limit: 5
    - char_limit: 25
quality:
  - document
  - sentence
lang:
  - sentence
  - document
```

Fields are as follows:

**topic:** Whether you wanna filter out the whole document or some sentences from the document of specific topics. Topic filtering code can be anything, a statistical method or keyword filtering as long as it's a boolean function.  

**length:** Here one can filter too short documents and too short sentences. The minimum length can be in word count or character count.  
**quality:" Whether you wanna filter out the whole document or some sentences according to quality criterion.  
**lang:**: Filter out non-Turkish documents as a whole, or just filter out non-Turkish sentences.


For each of these fields, if you want to include custom code you put it under that directory. Please navigate to `bella_cleaner/filterer/configs/` for the examples.

### Examples
Please navigate to [Examples](https://github.com/turkish-nlp-suite/bella-turca-cleaners/tree/main/examples/filterer) directory. We included examples of academic article and web scrape collection filtering.


## Licence
MIT licenced, feel free to use and replicate the code as you wish.

## Citation
Coming soon!

  
