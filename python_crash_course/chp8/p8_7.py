def make_album(name,album,num=None):
    album_name={'name':name,'album_name':album}
    if num:
        album_name['number']=num
    return album_name

name1=make_album('jaychou','taiwan',5)
print(name1)
name2=make_album('jackson','china',10)
print(name2)
name3=make_album('justin bieber','usa')
print(name3)
