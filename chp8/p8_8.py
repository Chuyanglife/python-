def make_album(name,album,num=None):
    album_name={'name':name,'album_name':album}
    if num:
        album_name['number']=num
    return album_name

while True:
    print("\n(enter 'q' or 'Q' at any time to quit)")
    name=input(f'name: ')
    if name == 'q' or name=='Q':
        break
    album=input(f'album: ')
    if album == 'q' or album=='Q':
        break
    num=input(f'num: ')
    if num == 'q':
        break
    m=make_album(name,album,num)
    print(m)


