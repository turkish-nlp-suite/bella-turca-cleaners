from bella_cleaner.cleaner import Cleaner

cleaner = Cleaner(base_dir="/home/duygu/Desktop/Work/bella_turca/turkish-corpus-cleaner", config_name="acikulasim")


article = "Yüksek Lisans Tezi Danışmanlar: Doç. Dr. Abdullah Abdullah, Aysun Aysun. ÖZET: Bu tezde Marmara denizindeki biyolojik çeşitliliği inceledik. Vardığımız sonuçlar pek iç açıcı olmadı. Kirlilik oranının binde 8 bulduk. Burda daha fazla tez cumlesi.... \nKAYNAKÇA:\n1. Kitap 1, Yazar1 , 1988 basimi Ankara.\n2. Dergi yazisi 1, Yazar11\n3. Kitap yazisi2, Yazar3."

cleaned_article = cleaner.clean(article)

print(cleaned_article)

