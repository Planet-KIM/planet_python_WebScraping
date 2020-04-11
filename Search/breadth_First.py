import pymysql

conn = pymysql.connect(host='127.0.0.1',
                       user='root',
                       passwd='rlaehdnjs12!',
                       db='mysql',
                       charset='utf8')

cur = conn.cursor()
cur.execute('USE wikipedia')

#페이지 id를 받아서 데이터베이스에서 url을 가져오는 보조 함수
def getUrl(pageId):
    cur.execute('SELECT url FROM pages WHERE id = %s', (int(pageId)))
    return cur.fetchone()[0]

#현재 페이지를 나타내는 정수를 입력 받아서 현재 페이지에서 링크한 id를 전부가져옵니다.
def getLinks(fromPageId):
    fromId = int(fromPageId)
    cur.execute('SELECT toPageId FROM links WHERE fromPageId = %s', (fromId))
    if cur.rowcount == 0:
        return []
    return [x[0] for x in cur.fetchall()]

#검색 페이지에서 출발해 대상 페이지까지 도달하는 경로를 만날 때까지, 재귀적으로 동작하면서 가능한 경로를 전부 리스트에 추가합니다.
def searchBreadth(targetPageId, paths=[[1]]):
    newPaths = []
    for path in paths:
        links = getLinks(path[-1])
        for link in links:
            if link == targetPageId:
                return path + [link]
            else:
                newPaths.append(path+[link])
    return searchBreadth(targetPageId, newPaths)

nodes = getLinks(1)
targetPageId = 1159
pageIds = searchBreadth(targetPageId)
for pageId in pageIds:
    print(getUrl(pageId))