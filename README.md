# Bella Turca corpus cleaners

Welcome to Bella Turca's cleaning code. [Bella Turca](https://huggingface.co/datasets/turkish-nlp-suite/BellaTurca) is a big & diverse corpus for training Turkish models and these are the cleaning code used during creation of Bella Turca. 

## Install

Change directory to the root drectory then make a `python setup.py install`. Install Python versiob/binary up to your taste. 

## Cleaning code
### Functionality
The main class `Cleaner` has only one public functionality, cleaning text. This method is called `Cleaner.clean`.

### Code structure
The code is structured to be modular and separate data needs and the code itself. The main class `Cleaner` includes code for a basic cleaning, then code to load and run custom configuration per genre.  
At the runtime, a `Cleaner` class objects holds all the data of the given configuration. Configurations are provided by yamls under configuration directories.While creating a `Cleaner` class instance, we provide the place of the custom data directory to `__init__` and that's it.


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
Please navigate to [Examples](https://github.com/turkish-nlp-suite/bella-turca-cleaners/tree/main/examples) directory. We included examples of book, academic article and web scrape examples.


## Filtering code


## Licence
MIT licenced, feel free to use and replicate the code as you wish.

## Citation
Coming soon!

  
