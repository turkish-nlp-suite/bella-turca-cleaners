from bella_cleaner.filterer import Filterer

filterer = Filterer(base_dir="/home/duygu/Desktop/Work/bella_turca/turkish-corpus-cleaner", config_name="articles")


article = "Little is known of the early history of Kars beyond the fact that, during medieval times, it had its own dynasty of Armenian rulers and was the capital of a region known as Vanand. Medieval Armenian historians referred to the city by a variety of names, including Karuts’ k’aghak’ ('Kars city'), Karuts’ berd, Amrots’n Karuts’, Amurn Karuts’ (all meaning 'Kars Fortress').[2] At some point in the ninth century (at least by 888) it entered into the domains of the Armenian Bagratunis. Kars was the capital of the Bagratid kingdom of Armenia between 929 and 961.[9] During this period, the town's cathedral, later known as the Church of the Holy Apostles, was built.[10]\nIn 963, shortly after the Bagratuni seat was transferred to Ani, Kars became the capital of a separate independent kingdom, again called Vanand. However, the extent of its actual independence from the Kingdom of Ani is uncertain: it was always in the possession of the relatives of the rulers of Ani, and, after Ani's capture by the Byzantine Empire in 1045, the Bagratuni title King of Kings held by the ruler of Ani was transferred to the ruler of Kars."

filtered_article = filterer.filter(article)

print(filtered_article)

