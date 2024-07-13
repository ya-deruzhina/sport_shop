from elasticsearch_dsl import Q
from apps.search.documents import CatalogDocument


# Выполняет поиск всех статей, в названии которых есть «How to».
query = 's'
q = Q(
     'multi_match',
     query=query,
     fields=[
         'name'
     ])
search = CatalogDocument.search().query(q)
response = search.execute()

# распечатать все хиты
for hit in search:
    print(hit.title)