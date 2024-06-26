# generated by datamodel-codegen:
#   filename:  github.json
#   timestamp: 2024-05-10T01:26:20+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel


class Author(BaseModel):
    displayName: str
    login: str
    path: str
    avatarUrl: str


class Author1(BaseModel):
    login: str
    displayName: str
    avatarUrl: str
    path: str


class Committer(BaseModel):
    login: str
    displayName: str
    avatarUrl: str
    path: str


class Model(BaseModel):
    oid: str
    url: str
    date: str
    bodyMessageHtml: str
    author: Author
    authors: List[Author1]
    committerAttribution: bool
    committer: Committer
    status: None
    isSpoofed: bool

import json

with open('github.json', 'r') as myfile:
    data=myfile.read()
dict1 = json.loads(data)

m = Model(dict1)
print(m)