import pymongo
import requests
import concurrent.futures
import datetime
import os
import json
import csv

from lib.database import get_mongo_connection
# mongo = get_mongo_connection()
# MONGO_HOST = mongo.host
# MONGO_PORT = int(mongo.port)
# MONGO_USER = mongo.user
# MONGO_PWD = mongo.password
# MONGO_AUTH = mongo.auth_source
# MONGO_DB = mongo.db
# c1 = pymongo.MongoClient(MONGO_HOST, username=MONGO_USER,
#                         password=MONGO_PWD, port=MONGO_PORT, authSource=MONGO_AUTH)
# crawl1 = c1['npm']
# print(crawl1.collection_names())
# npm_d = crawl1['npm_library']
names = []
libname = set()
limit = 200
platform = 'rubygems'
number = 2000
with open('most_dep_' + str(number) + '_' + platform + '.json', 'r') as f:
    most_dep_1000 = json.load(f)
    for lib in most_dep_1000[:limit]:
        for name, versions in lib.items():
            if name in libname:
                continue
            else:
                libname.add(name)
                versionIds = []
                version_number = {}
                for version in versions:
                    if '-' in version:
                        continue
                    digits = version.split('.')
                    if len(digits) <= 2:
                        names.append(name + ':' + version)
                        continue
                    major = digits[0]
                    minor = digits[1]
                    patch = digits[2]
                    if major + '.' + minor in version_number:
                        version_number[major + '.' + minor] = version_number[major + '.' + minor] if version_number[major + '.' + minor] > patch else patch
                    else:
                        version_number[major + '.' + minor] = patch

                for mm,p in version_number.items():
                    names.append(name + ':' + mm + '.' + p)

with open('most_fork_' + str(number) + '_' + platform + '.json', 'r') as f:
    most_fork_1000 = json.load(f)
    for lib in most_fork_1000[:limit]:
        for name, versions in lib.items():
            if name in libname:
                continue
            else:
                libname.add(name)
                version_number = {}
                for version in versions:
                    if '-' in version:
                        continue
                    digits = version.split('.')
                    if len(digits) <= 2:
                        names.append(name + ':' + version)
                        continue
                    major = digits[0]
                    minor = digits[1]
                    patch = digits[2]
                    if major + '.' + minor in version_number:
                        version_number[major + '.' + minor] = version_number[major + '.' + minor] if version_number[
                                                                                                         major + '.' + minor] > patch else patch
                    else:
                        version_number[major + '.' + minor] = patch

                for mm, p in version_number.items():
                    names.append(name + ':' + mm + '.' + p)

with open('most_star_' + str(number) + '_' + platform + '.json', 'r') as f:
    most_star_1000 = json.load(f)
    for lib in most_star_1000[:limit]:
        for name, versions in lib.items():
            if name in libname:
                continue
            else:
                libname.add(name)
                version_number = {}
                for version in versions:
                    if '-' in version:
                        continue
                    digits = version.split('.')
                    if len(digits) <= 2:
                        names.append(name + ':' + version)
                        continue
                    major = digits[0]
                    minor = digits[1]
                    patch = digits[2]
                    if major + '.' + minor in version_number:
                        version_number[major + '.' + minor] = version_number[major + '.' + minor] if version_number[
                                                                                                         major + '.' + minor] > patch else patch
                    else:
                        version_number[major + '.' + minor] = patch

                for mm, p in version_number.items():
                    names.append(name + ':' + mm + '.' + p)

# with open('most_total_download.json', 'r') as f:
#     most_total = json.load(f)
#     count = 0
#     for lib in most_total:
#         name = lib['name']
#         if lib['name'] in libname:
#             continue
#         if count > limit:
#             break
#         count += 1
#         libname.add(lib['name'])
#         npm_lib = npm_d.find_one({'requested_name': lib['name']})
#         version_number = {}
#         for version in npm_lib['versions']:
#             if '-' in version:
#                 continue
#             digits = version.split('.')
#             major = digits[0]
#             minor = digits[1]
#             patch = digits[2]
#             if major + '.' + minor in version_number:
#                 version_number[major + '.' + minor] = version_number[major + '.' + minor] if version_number[
#                                                                                                  major + '.' + minor] > patch else patch
#             else:
#                 version_number[major + '.' + minor] = patch
#         for mm, p in version_number.items():
#             names.append(name + ':' + mm + '.' + p)
#
# with open('most_last_3_download.json', 'r') as f:
#     most_total = json.load(f)
#     count = 0
#     for lib in most_total:
#         name = lib['name']
#         if lib['name'] in libname:
#             continue
#         if count > limit:
#             break
#         count += 1
#         libname.add(lib['name'])
#         version_number = {}
#         npm_lib = npm_d.find_one({'requested_name': lib['name']})
#         for version in npm_lib['versions']:
#
#             if '-' in version:
#                 continue
#             digits = version.split('.')
#             major = digits[0]
#             minor = digits[1]
#             patch = digits[2]
#             if major + '.' + minor in version_number:
#                 version_number[major + '.' + minor] = version_number[major + '.' + minor] if version_number[
#                                                                                                  major + '.' + minor] > patch else patch
#             else:
#                 version_number[major + '.' + minor] = patch
#         for mm, p in version_number.items():
#             names.append(name + ':' + mm + '.' + p)
#
# with open('most_last_1_download.json', 'r') as f:
#     most_total = json.load(f)
#     count = 0
#     for lib in most_total:
#         name = lib['name']
#         if lib['name'] in libname:
#             continue
#         if count > limit:
#             break
#         count += 1
#         libname.add(lib['name'])
#         version_number = {}
#         npm_lib = npm_d.find_one({'requested_name': lib['name']})
#         for version in npm_lib['versions']:
#
#             if '-' in version:
#                 continue
#             digits = version.split('.')
#             major = digits[0]
#             minor = digits[1]
#             patch = digits[2]
#             if major + '.' + minor in version_number:
#                 version_number[major + '.' + minor] = version_number[major + '.' + minor] if version_number[
#                                                                                                  major + '.' + minor] > patch else patch
#             else:
#                 version_number[major + '.' + minor] = patch
#         for mm, p in version_number.items():
#             names.append(name + ':' + mm + '.' + p)

with open('most_download_dep_star_fork_' + str(limit) + '_' + platform + '.json', 'w') as f:
    json.dump(list(set(names)), f)
print(len(names))
print(len(libname))
