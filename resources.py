resources = [
        ('Новостной портал nur.kz', 'https://nur.kz/latest, scrolling 2 0.5',
         'block-infinite js-infinite, div, article-preview-category__content, a',
         'formatted-body__content--wrapper, div',
         'main-headline js-main-headline, h1', '%Y-%m-%dT%H:%M:%S%z, time::attr(datetime)')
]


# Резервные переменные

# nur.kz
# resource_name = 'Новостной портал nur.kz'
# resource_url = 'https://nur.kz/latest, scrolling 4 2'
# top_tag = 'block-infinite js-infinite, div, article-preview-category__content, a'
# bottom_tag = 'formatted-body__content--wrapper, div'
# title_cut = 'main-headline js-main-headline, h1'
# date_cut = '%Y-%m-%dT%H:%M:%S%z, time::attr(datetime)'

# scientificrussia.ru
# resource_name = 'Новостной портал scientificrussia.ru'
# resource_url = 'https://scientificrussia.ru/news, pagination 1134 1130 -1 f"https://scientificrussia.ru/news/{i}"'
# top_tag = 'image, div, , a'
# bottom_tag = 'article-text, div'
# title_cut = ', h1'
# date_cut = '%Y-%m-%d %H:%M, time::attr(datetime)'

# tengrinews.kz
# resource_name = 'Новостной портал tengrinews.kz'
# resource_url = 'https://tengrinews.kz/news, pagination 1 5 1 f"https://tengrinews.kz/news/page/{i}"'
# top_tag = 'tn-article-grid, div, tn-link, a'
# bottom_tag = 'tn-news-content, div'
# title_cut = 'tn-content-title, h1'
# date_cut = '(СегодняOrВчераOr%d%b%Y)comma%H:%M, time::text'


# from dateparser import parse
# date_string = 'Вчера, 13:26'
# try:
#     date = parse(date_string)
#     print(date)
# except:
#     print('Дата не может быть разобрана')

# import time
# from dateutil.relativedelta import relativedelta
# from dateparser.parse import parse

# import time
# from dateparser import parse
# date_string='Вчера, 13:31'
# date = parse(date_string)
# print(int(time.mktime(date.timetuple())))
# print(date.strftime('%d-%m-%Y'))


# import yaml
# with open("nurkz.yaml") as file:
#     loaded_yaml = yaml.load(file, Loader=yaml.FullLoader)
#     print(loaded_yaml['extract_samples']['fields'])
#     print(loaded_yaml)
#     print(loaded_yaml['configuration']['settings']['crawl_strategy']['type'])
# # for key, value in loaded_yaml.items():
# #     print(f"{key}: {value}")
# # print()



# from urllib.request import urlopen
#
# url = 'http://mining.kz/robots.txt'
# content = urlopen(url).read().decode('utf-8')
# print(content)

# from requests_toolbelt import disable_verify
# import requests
# url = "http://www.mining.kz"
# response = requests.get(url, verify=False)
# print(response.text)

# from requests_toolbelt import disable_verify
# import requests
#
# url = "http://www.mining.kz"
# response = requests.get(url, verify=False)
# print(response.text)