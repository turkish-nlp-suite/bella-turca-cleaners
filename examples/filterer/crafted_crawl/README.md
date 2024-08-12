## Crafted Crawl Filtering :globe_with_meridians:

Here we filter web pages. The config looks like:


```
length:
  - document:
     - word_limit: 100
quality:
  - sentence
```

The config is very simplistic. The fact that Crafted Crawl collection is a curated collection, we keep the config rather simple. 
* We throw away docs that are shorter than 100 words.
* We filter out sentences that doesn't meet the some predefined quality criterion.

The config file is located at `bella_cleaner/filterer/configs/crafted_crawl/custom.yaml`. 
The example in this directory looks like:


```
Aras Nehri yatağında, verimli topraklara sahip, ılıman iklimiyle ilçe, yüksek dağlar arasında, tarım yapmaya elverişli coğrafi konuma sahiptir. Kars'a 72 km, Iğdır'a 100 km, Erzurum'a ise 150 km uzaklıktadır. Kağızman 1972 km²'lik bir alana sahiptir. Yükseklik farklılıkları ilçe içinde fazladır. Bu yükseklikler 1100–1600 m arasında değişmektedir. Kuzeyinde Kars merkez ve Selim, doğusunda Tuzluca ve Digor, batısında Sarıkamış, güneyinde ise Ağrı merkez ile komşudur. Aras vadisindeki bir birikinti kesiti üzerinde yerleşmiş durumdadır.

İlçe coğrafi bakımdan henüz tektonik oluşumunu tamamlamamıştır. Faylar ve kırıklar üzerinde yerleşilmiştir. Dolayısıyla zaman zaman yörede depremler tehlikeli olmaktadır. 1104-1962 yılları arasında 13 deprem olmuştur. Diğer taraftan düşme, kayma ve sürünme şeklinde kütle hareketleri olmaktadır. Kötek, Çallı civarında kaya düşmesi, Camuşlu-Kozlu, Yenice-Taşburun ve Akdam köyleri civarlarında heyelan görülmektedir. Kağızman ilçesinin 62 köyü bulunmaktadır. BU DA BIR CUMLE.
```

and the filtered result is:

```
Aras Nehri yatağında, verimli topraklara sahip, ılıman iklimiyle ilçe, yüksek dağlar arasında, tarım yapmaya elverişli coğrafi konuma sahiptir. Kars'a 72 km, Iğdır'a 100 km, Erzurum'a ise 150 km uzaklıktadır. Kağızman 1972 km²'lik bir alana sahiptir. Yükseklik farklılıkları ilçe içinde fazladır. Bu yükseklikler 1100–1600 m arasında değişmektedir. Kuzeyinde Kars merkez ve Selim, doğusunda Tuzluca ve Digor, batısında Sarıkamış, güneyinde ise Ağrı merkez ile komşudur. Aras vadisindeki bir birikinti kesiti üzerinde yerleşmiş durumdadır.

İlçe coğrafi bakımdan henüz tektonik oluşumunu tamamlamamıştır. Faylar ve kırıklar üzerinde yerleşilmiştir. Dolayısıyla zaman zaman yörede depremler tehlikeli olmaktadır. 1104-1962 yılları arasında 13 deprem olmuştur. Diğer taraftan düşme, kayma ve sürünme şeklinde kütle hareketleri olmaktadır. Kötek, Çallı civarında kaya düşmesi, Camuşlu-Kozlu, Yenice-Taşburun ve Akdam köyleri civarlarında heyelan görülmektedir. Kağızman ilçesinin 62 köyü bulunmaktadır.
```

Notice that the last sentence is filtered out, because sentence filtering includes filtering sentences that are all in capitals.
