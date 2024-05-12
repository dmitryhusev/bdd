from copy import deepcopy


kw = dict(
    name='mum',
    act='running',
    city='zhyt'
)

dict1 = {
    "oid": "b6b26982a97bdc67eb0d6c400d485ab28fa49d9d",
    "url": "/dmitryhusev/qa-challenge/commit/b6b26982a97bdc67eb0d6c400d485ab28fa49d9d",
    "date": "2023-08-28T13:54:01.000+02:00",
    "bodyMessageHtml": "",
    "author": {
        "displayName": "dmitryhusev",
        "login": "dmitryhusev",
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
            "hey": "prekol"
        }
    ],
    "committerAttribution": False,
    "committer": {
        "login": "dmitryhusev",
        "displayName": "dmitryhusev",
        "avatarUrl": "https://avatars.githubusercontent.com/u/8916334?v=4",
        "path": "/dmitryhusev"
    },
    "status": None,
    "isSpoofed": False
}



def compare2(dict1):
    res = []
    # dict_resolve = deepcopy(dict1)

    def _compare(dict_inner):

        for k, v in dict1.items():
            if isinstance(v, str | bool | None):
                res.append({k: v})
                continue
            elif isinstance(v, list):
                for i in v:
                    for k2, v2 in i.items():
                        if isinstance(v2, str | bool | None):
                            res.append({k2: v2})
                            continue
            elif isinstance(v, dict):
                    for k3, v3 in v.items():
                        if isinstance(v3, str | bool | None):
                            res.append({k3: v3})
                            continue
    _compare(dict1)
    return res



for i in compare2(dict1):
    print(i)