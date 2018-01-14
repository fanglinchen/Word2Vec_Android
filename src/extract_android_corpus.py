import xml.etree.ElementTree

import configparser
import datetime
import re
from xml.etree import ElementTree
import tempfile
from db_connector import DBConnector
import io

parser = configparser.RawConfigParser()
u = io.open('settings.ini').read().decode("utf-8-sig").encode("utf-8")
fp = tempfile.TemporaryFile()
fp.write(u)
fp.seek(0)
parser.readfp(fp)


def should_be_skipped_by_tag(tags):
    if not tags:
        return True
    if parser.get('TAGS', 'TAGNAME') not in tags:
        return True
    else:
        return False


def should_be_skipped(attributes):
    if str(attributes['PostTypeId']) == '1':
        if should_be_skipped_by_tag(attributes['Tags']):
            return True
        if attributes['Score'] < 0:
            return True
        if attributes['Score'] == 0 and attributes['AnswerCount'] == 0:
            return True
        if "android" not in attributes['Tags']:
            return True
    if str(attributes['PostTypeId']) == '2':
        return True
    return False


class StackoverflowDumpToDBService:
    def __init__(self):
        self.db = DBConnector()

    def import_posts_from_file(self, from_date, until_date, file_path, table_name):
        f = io.open(file_path, 'r', encoding="utf8")
        f.readline()
        f.readline()

        row_nums = 0
        scanned_row_nums = 0
        counter = 0
        while True:
            current_line = f.readline()
            if not current_line:
                break
            try:
                root = ElementTree.fromstring(current_line.encode('utf-8'))
            except Exception as e:
                print(e)
                print("----------------------------------------------------------------------")
                # print("this line contains error")
                # print(current_line)
                # print("----------------------------------------------------------------------")
                continue
                
            attributes = root.attrib
            attributes['CreationDate'] = re.sub(r'\.\d+', '', attributes['CreationDate'].replace('T', ' '))
            attributes['LastEditDate'] = re.sub(r'\.\d+', '', attributes['CreationDate'].replace('T', ' '))
            attributes['LastActivityDate'] = re.sub(r'\.\d+', '', attributes['CreationDate'].replace('T', ' '))
            attributes['CommunityOwnedDate'] = re.sub(r'\.\d+', '', attributes['CreationDate'].replace('T', ' '))
            attributes['AcceptedAnswerId'] = attributes.get('AcceptedAnswerId')
            attributes['ViewCount'] = attributes.get('ViewCount', 0)
            attributes['LastEditorDisplayName'] = attributes.get('LastEditorDisplayName')
            attributes['Title'] = attributes.get('Title')
            attributes['Tags'] = attributes.get('Tags')
            attributes['OwnerUserId'] = attributes.get('OwnerUserId')
            attributes['AnswerCount'] = attributes.get('AnswerCount', 0)
            attributes['FavoriteCount'] = attributes.get('FavoriteCount', 0)
            attributes['LastEditorUserId'] = attributes.get('LastEditorUserId')
            attributes['Score'] = int(attributes.get('Score'))
            attributes['ParentId'] = attributes.get('ParentId', None)
            creation_date = datetime.datetime.strptime(attributes['CreationDate'], '%Y-%m-%d  %H:%M:%S')
            scanned_row_nums +=1
            if scanned_row_nums % 1000 ==0:
                print("scanned_row_nums:"+str(scanned_row_nums))
            if creation_date < from_date:
                continue
            if creation_date >= until_date:
                break

            if should_be_skipped(attributes):
                continue
            try:
                query = '''
                INSERT INTO ''' + table_name + ''' (id,PostTypeId,AcceptedAnswerId,CreationDate,Score,ViewCount,Body,OwnerUserId,
                LastEditorUserId,LastEditorDisplayName,LastEditDate,LastActivityDate,Title,Tags,AnswerCount,CommentCount,FavoriteCount,CommunityOwnedDate,ParentId)
                VALUES (%(Id)s,%(PostTypeId)s,%(AcceptedAnswerId)s,%(CreationDate)s,%(Score)s,%(ViewCount)s,%(Body)s,
                    %(OwnerUserId)s,%(LastEditorUserId)s,%(LastEditorDisplayName)s,
                    %(LastEditDate)s,%(LastActivityDate)s,%(Title)s,%(Tags)s,%(AnswerCount)s,%(CommentCount)s,
                    %(FavoriteCount)s,%(CommunityOwnedDate)s,%(ParentId)s)'''
                self.db.get_cursor().execute(query, attributes)

            except Exception as e:
                print(attributes)
                raise e

            row_nums += 1
            counter += 1
            if row_nums == 1000:
                self.db.get_connection().commit()
                row_nums = 0
                print("%s records has been inserted! last date was %s" % (counter, creation_date))

        self.db.get_connection().commit()
        self.db.get_cursor().close()


stackoverflowDumpToDBService = StackoverflowDumpToDBService()
stackoverflowDumpToDBService.import_posts_from_file(
    from_date=datetime.datetime(2010, 1, 1, 0, 0, 0),
    until_date=datetime.datetime(2018, 1, 1, 0, 0, 0),
    file_path=parser.get('DATASET', 'PATH'),
    table_name=parser.get('DATABASE', 'TABLENAME'))
