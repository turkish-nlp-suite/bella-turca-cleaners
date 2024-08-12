## Articles Filtering :mortar_board:

Here we filter scientific articles. The config looks like:


```
length:
  - document:
     - word_limit: 20
quality:
  - document
lang:
  - sentence
  - document
```

The config is very basic due to the fact that these scientific articles hence we don't need to filter by topic. However we wanna filter out some docs that contain OCR errors.
* We throw away docs that are shorter than 20 words.
* We throw away docs that are bad quality, either due to OCR errors and by other specs.
* We filter out English sentences, as well as throw away the docs in English.

The config file is located at `bella_cleaner/filterer/configs/articles/custom.yaml`. 
The first example in this directory looks like:


```
Aras Nehri yatağında, verimli topraklara sahip, ılıman iklimiyle ilçe, yüksek dağlar arasında, tarım yapmaya elverişli coğrafi konuma sahiptir. Kars'a 72 km, Iğdır'a 100 km, Erzurum'a ise 150 km uzaklıktadır. Kağızman 1972 km²'lik bir alana sahiptir. Yükseklik farklılıkları ilçe içinde fazladır. Bu yükseklikler 1100–1600 m arasında değişmektedir. Kuzeyinde Kars merkez ve Selim, doğusunda Tuzluca ve Digor, batısında Sarıkamış, güneyinde ise Ağrı merkez ile komşudur. Aras vadisindeki bir birikinti kesiti üzerinde yerleşmiş durumdadır.

İlçe coğrafi bakımdan henüz tektonik oluşumunu tamamlamamıştır. Faylar ve kırıklar üzerinde yerleşilmiştir. Dolayısıyla zaman zaman yörede depremler tehlikeli olmaktadır. 1104-1962 yılları arasında 13 deprem olmuştur. Diğer taraftan düşme, kayma ve sürünme şeklinde kütle hareketleri olmaktadır. Kötek, Çallı civarında kaya düşmesi, Camuşlu-Kozlu, Yenice-Taşburun ve Akdam köyleri civarlarında heyelan görülmektedir. Kağızman ilçesinin 62 köyü bulunmaktadır.  Bu cumlededegercektencokuzunaraliksizyazilmisbazisozcuklervar.
```

and the filtered result is `None`, as this doc contains a very long string, some words concatenated without much spaces.

The second example:

```
Little is known of the early history of Kars beyond the fact that, during medieval times, it had its own dynasty of Armenian rulers and was the capital of a region known as Vanand. Medieval Armenian historians referred to the city by a variety of names, including Karuts’ k’aghak’ ('Kars city'), Karuts’ berd, Amrots’n Karuts’, Amurn Karuts’ (all meaning 'Kars Fortress').[2] At some point in the ninth century (at least by 888) it entered into the domains of the Armenian Bagratunis. Kars was the capital of the Bagratid kingdom of Armenia between 929 and 961.[9] During this period, the town's cathedral, later known as the Church of the Holy Apostles, was built.[10]

In 963, shortly after the Bagratuni seat was transferred to Ani, Kars became the capital of a separate independent kingdom, again called Vanand. However, the extent of its actual independence from the Kingdom of Ani is uncertain: it was always in the possession of the relatives of the rulers of Ani, and, after Ani's capture by the Byzantine Empire in 1045, the Bagratuni title King of Kings held by the ruler of Ani was transferred to the ruler of Kars.
```

and also returns `None`, as this doc is in English and thrown away.

Now comes the third example:

```
Little is known of the early history of Kars beyond the fact that, during medieval times, it had its own dynasty of Armenian rulers and was the capital of a region known as Vanand. Buraya kadar İngilizce cümleler vardı, şimdi Türkçesi var. Bence de Kars harika bir şehirdir, yalnızca kışları oldukça soğuktur. Şimdi İngilizceyle devam ediyoruz. During this period, the town's cathedral, later known as the Church of the Holy Apostles, was built.

Türkiye'nin Kafkasya'ya açılan kapısı konumundaki bu şehir, Kafkas Üniversitesinin açılmasıyla hızla gelişmeye başlamış ve zaman içinde bir öğrenci kenti durumuna gelmiştir. Ayrıca şehir merkezine altı kilometre uzaklıktaki havalimanı sayesinde de bölgesinde ulaşım ağının kesiştiği bir noktada yer alır. Bunun dışında kara ve demir yolu ağlarıyla ülkenin diğer yerleşim birimlerine ulaşımda da bir sorun yoktur.
```
the result is:

```
Buraya kadar İngilizce cümleler vardı, şimdi Türkçesi var. Bence de Kars harika bir şehirdir, yalnızca kışları oldukça soğuktur. Şimdi İngilizceyle devam ediyoruz.
Türkiye'nin Kafkasya'ya açılan kapısı konumundaki bu şehir, Kafkas Üniversitesinin açılmasıyla hızla gelişmeye başlamış ve zaman içinde bir öğrenci kenti durumuna gelmiştir. Ayrıca şehir merkezine altı kilometre uzaklıktaki havalimanı sayesinde de bölgesinde ulaşım ağının kesiştiği bir noktada yer alır. Bunun dışında kara ve demir yolu ağlarıyla ülkenin diğer yerleşim birimlerine ulaşımda da bir sorun yoktur.
```
as one sees the English sentences are filtered out.





