from pprint import pprint


dict1 = dict(
    name='mum',
    act='running',
    city='zhyt',
)

dict2 = {
    "city": "zhyt",
    "url": "/dmitryhusev/qa-challenge/commit/b6b26982a97bdc67eb0d6c400d485ab28fa49d9d",
    "date": "2023-08-28T13:54:01.000+02:00",
    "bodyMessageHtml": "",
    "author": {
        "displayName": "dmitryhusev",
        "act": "running",
        "path": "/dmitryhusev",
        "avatarUrl": "https://avatars.githubusercontent.com/u/8916334?s=40&v=4"
    },
    "authors": [
        {
            "login": "dmitryhusev",
            "displayName": "dmitryhusev",
            "avatarUrl": "https://avatars.githubusercontent.com/u/8916334?v=4",
            "path": "/dmitryhusev"
        },
        {
            "hey": {
                "prekol": [
                    {"name": "mum"},
                    {"two": 10000}
                ],
                'dratuti': 'dorov'
                }
        }
    ],
    "committerAttribution": False,
    "committer": {
        "login": "dmitryhusev",
        "displayName": "dmitryhusev",
        "avatarUrl": "https://avatars.githubusercontent.com/u/8916334?v=4",
        "path": "/dmitryhusev"
    },
    "act": "running",
    "isSpoofed": True
}



def resolve_dict(dikt: dict):
    res = []

    def _resolve_dict(dikt):

        for k, v in dikt.items():
            if isinstance(v, str | bool | None | int | float):
                res.append({k: v})
                continue
            elif isinstance(v, list):
                for i in v:
                    _resolve_dict(i)
            elif isinstance(v, dict):
                _resolve_dict(v)
    _resolve_dict(dikt)
    return res


def compare_dicts(to_check: dict, response_dict: dict):

    def _compare_dicts(record, collection):
        for i in collection:
            try:
                assert i == record
                return
            except AssertionError:
                continue
        raise ValueError(f"Record {record} is not in dictionary")
    
    res1 = resolve_dict(to_check)
    res2 = resolve_dict(response_dict)

    [_compare_dicts(i, res2) for i in res1]


compare_dicts(dict1, dict2)
