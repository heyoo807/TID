import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='musicChart', charset='utf8')
cur = conn.cursor()

# 테이블 생성
# cur.execute("CREATE TABLE song(songID varchar(10), songName varchar(20), genre varchar(20), lyrics TEXT(1000), albumName varchar(20), singerName varchar(20))")
# cur.execute("CREATE TABLE album(albumID varchar(20), albumName varchar(20), publishing varchar(20), agency varchar(20), releaseDate DATE)")
# cur.execute("CREATE TABLE singer(singerID varchar(20), singerName varchar(20), debut DATE)")

# 데이터 삽입 


conn.commit()
conn.close()
