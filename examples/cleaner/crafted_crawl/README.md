## Crafted Crawl Cleaning :globe_with_meridians:

Here we clean web pages. The config looks like:


```
replace:
  - extras: "no"
delete:
  - extras: "no"
custom_code: "yes"
keep_emoticon: "yes"
crop_header_footer:
 - footer
kill_foreign_chars:
 - arabic
 - chinese
 - korean
```

* Web is a jungle, so we clean foreign characters, also we include custom code for further cleaning onto base cleaning.
* We crop only footers for an example. Some web articles include 
* We keep emotions.
The config file is located at `bella_cleaner/cleaner/configs/crafted_crawl/custom.yaml`. 

Roughly like this:


```
ARTICLE BODY
Yorumlar/Yorum bırak/Yorum ekle  .... PARSED OUT

```

Example in this directory looks like:


```
Bu güzel gezi bloguna hoş geldiniz😊😊😊 Bu yazıda sizlere Kastamonu'yu tanıtacağız.
Biliyorsunuz ki ben Kastamonuluyum, 각겋 ben uzun süre de orda yaşadım.

Sizlere de katıldığınız için teşekkür ederim.
Yorum bırak
Yorumlar:
2.3.16 tarihinde Şule dedi ki: Bayıldımmm harika bir yazı!!
12.2.16 tarihinde Emre dedi ki: Hocam sizce 3 günlük gezi için en iyi yerler nerelerdir?
```

and cleaned result is:

```
Bu güzel gei bloguna hoş geldiniz😊😊😊 Bu yazıda sizlere Kastamonu'yu tanıtacağız.
Biliyorsunuz ki ben Kastamonuluyum, ben uzun süre de orda yaşadım.
Sizlere de katıldığınız için teşekkür ederim.
```
