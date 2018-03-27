#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import os
import io
import yaml
from pprint import pprint

def sortDict(dict):
    items = dict.items()
    items.sort()
    return items

def generateJson(data):
    chinese = sortDict(data["zh-cn"])
    try:
        english = data["en"]
    except BaseException:
        english = {}
    json_object = {}
    json_object["zh-cn"] = {}
    json_object["en"] = {}
    for (key, value) in chinese:
        json_object["zh-cn"][key] = value
        if key in english:
            json_object["en"][key] = english[key]
        else:
            json_object["en"][key] = ""
    return json_object

# Frontend
for subdir, dir, files in os.walk("frontend"):
    print("Building frontend translations...")
    for file in files:
        data = json.load(open('frontend/' + file))
        json_object = generateJson(data)
        with io.open('frontend/' + file, 'w', encoding='utf-8') as outfile:
            data = json.dumps(json_object, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(unicode(data))
# Backend
print("Building backend translations...")
chinese = sortDict(yaml.load(open('backend/messages.zh.yaml')))
english = yaml.load(open('backend/messages.en.yaml'))
chineseObject = {}
englishObject = {}
for (key, value) in chinese:
    chineseObject[key] = value
    if key in english:
        englishObject[key] = english[key]
    else:
        englishObject[key] = ""
with io.open('backend/messages.zh.yaml', 'w', encoding='utf-8') as outfile:
    data = json.dumps(chineseObject, ensure_ascii=False)
    outfile.write(unicode(data))
with io.open('backend/messages.en.yaml', 'w', encoding='utf-8') as outfile:
    data = json.dumps(englishObject, ensure_ascii=False)
    outfile.write(unicode(data))
