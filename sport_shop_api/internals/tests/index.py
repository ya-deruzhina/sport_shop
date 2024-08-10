import pytest

class Index():
    @pytest.fixture(autouse=True)
    def spam_index(self, elasticsearch):
        elasticsearch.indices.create(index='search')
        elasticsearch.indices.put_mapping(body={
                    'properties': {
                        'id': {
                            'type': 'keyword'
                        },
                        'category': {
                            'type': 'text',
                            'fields': {
                                'id': {
                                    'type': 'keyword',
                                },
                                'category': {
                                    'type': 'text',
                                }
                            }
                        },
                        'subcategory': {
                            'type': 'text',
                            'fields': {
                                'id': {
                                    'type': 'keyword',
                                },
                                'subcategory': {
                                    'type': 'text',
                                }
                            }
                        },
                        'name': {
                            'type': 'text'
                        },
                        'description': {
                            'type': 'text'
                        },
                        'price': {
                            'type': 'float'
                        },
                        'amount': {
                            'type': 'integer'
                        }
                    }
                }, doc_type='_doc', index='spam_test')