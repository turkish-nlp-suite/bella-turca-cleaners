from bella_cleaner.cleaner import Cleaner

cleaner = Cleaner(base_dir="/home/duygu/Desktop/Work/bella_turca/turkish-corpus-cleaner", config_name="crafted_crawl")


article = "Bu güzel gezi bloguna hoş geldiniz😊😊😊 Bu yazıda sizlere Kastamonu'yu tanıtacağız.\nBiliyorsunuz ki ben Kastamonuluyum, 각겋 ben uzun süre de orda yaşadım.\n\nSizlere de katıldığınız için teşekkür ederim.\nYorum bırak\nYorumlar:\n2.3.16 tarihinde Şule dedi ki: Bayıldımmm harika bir yazı!!\n12.2.16 tarihinde Emre dedi ki: Hocam sizce 3 günlük gezi için en iyi yerler nerelerdir?"

cleaned_article = cleaner.clean(article)

print(cleaned_article)

