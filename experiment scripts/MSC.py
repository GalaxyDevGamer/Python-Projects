# coding:shift-jis
money = [u'500円', u'100円', u'50円', u'10円']
cnt = 0
for i in money:
    cnt+=1
    print cnt, i
mg= input(u'得た金額を選択')
if mg == 1:
    sp = 500/2
if mg == 2:
    sp = 100/2
if mg == 3:
    sp = 50/2
if mg == 4:
    sp = 10/2
print u'それを二人で分けると一人当たり', sp, u'円です'
pa = input(u'一人目が持っている小銭の合計はいくらですか?')
pb = input(u'二人目が持っている小銭の合計はいくらですか?')
print u'まずは一人目の確認をします'
pa2 = raw_input(u'一人目は小銭を持っていますか? y/n')
if pa2 == 'y':
    pa3 = input(u'500円玉は何枚ですか?')
    pa4 = input(u'100円玉は何枚ですか?')
    pa5 = input(u'50円玉は何枚ですか?')
    pa6 = input(u'10円玉は何枚ですか?')
    print u'一人目が持っている小銭は、500円玉', pa3, u'枚、100円玉', pa4, u'枚、50円玉', pa5, u'枚、10円玉', pa6, u'枚の計', pa, u'円です'
else:
    print u'一人目は分け合うために出せる小銭がありません。2人目の確認に移ります'
print u'続いて二人目の確認をします。'
pb2 = raw_input(u'小銭は持っていますか? y/n')
if pb2 == 'y':
    pb3 = input(u'500円玉は何枚ですか?')
    pb4 = input(u'100円玉は何枚ですか?')
    pb5 = input(u'50円玉は何枚ですか?')
    pb6 = input(u'10円玉は何枚ですか?')
    print u'二人目が持っている小銭は、500円玉', pb3, u'枚、100円玉', pb4, u'枚、50円玉', pb5, u'枚、10円玉', pb6, u'枚の計', pb, u'円です'
else:
    print u'二人目は分け合うために出せるお金がありません。'
print u'集計します'
if pa2 and pb2 == 'n':
    print u'二人だけでは分け合えません。得たお金を両替して分け合ってください'
if sp >= pa:
    cp1 = sp-pa
    print u'一人目は分け合う額を', cp1, u'円下回った額しか所持していません'
    if sp >= pb:
        print u'二人目も額を', cp1, u'円下回った額しか持ってません'
        print u'結果：二人だけでは分け合いができません。得たお金を両替する必要があります'
    elif pb >= sp:
        cp3 = pb-sp
        print u'二人目は分け合う額を、500円玉', pb3, u'枚、100円玉', pb4, u'枚、50円玉', pb5, u'枚、10円玉', pb6, u'枚で', cp3, u'円上回った額を所持しています'
        if mg == 1:
            
elif pa >= sp:
    cp2 = pa-sp
    print u'一人目は分け合う額を', cp2, u'円上回った額を所持しています'

    
    
