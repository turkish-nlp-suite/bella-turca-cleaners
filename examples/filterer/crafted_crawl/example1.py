from bella_cleaner.filterer import Filterer

filterer = Filterer(base_dir="/home/duygu/Desktop/Work/bella_turca/turkish-corpus-cleaner", config_name="crafted_crawl")


article = "Aras Nehri yatağında, verimli topraklara sahip, ılıman iklimiyle ilçe, yüksek dağlar arasında, tarım yapmaya elverişli coğrafi konuma sahiptir. Kars'a 72 km, Iğdır'a 100 km, Erzurum'a ise 150 km uzaklıktadır. Kağızman 1972 km²'lik bir alana sahiptir. Yükseklik farklılıkları ilçe içinde fazladır. Bu yükseklikler 1100–1600 m arasında değişmektedir. Kuzeyinde Kars merkez ve Selim, doğusunda Tuzluca ve Digor, batısında Sarıkamış, güneyinde ise Ağrı merkez ile komşudur. Aras vadisindeki bir birikinti kesiti üzerinde yerleşmiş durumdadır.\nİlçe coğrafi bakımdan henüz tektonik oluşumunu tamamlamamıştır. Faylar ve kırıklar üzerinde yerleşilmiştir. Dolayısıyla zaman zaman yörede depremler tehlikeli olmaktadır. 1104-1962 yılları arasında 13 deprem olmuştur. Diğer taraftan düşme, kayma ve sürünme şeklinde kütle hareketleri olmaktadır. Kötek, Çallı civarında kaya düşmesi, Camuşlu-Kozlu, Yenice-Taşburun ve Akdam köyleri civarlarında heyelan görülmektedir. Kağızman ilçesinin 62 köyü bulunmaktadır. BU DA BIR CUMLE."

filtered_article = filterer.filter(article)

print(filtered_article)

