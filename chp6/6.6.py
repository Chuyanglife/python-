favourite_languages={'chuyang':'python',
                     'lixiang':'c',
                     'yeehenrg':'c++',
                     'yingcong':'c#',
                     'chengkang':'java'
                    }
people_research=['chuyang','yingcong']
for name in favourite_languages.keys():
    if name in people_research:
        print(name.title()+",感谢您参加我们的这次关于编程语言的调查！ ")
       # print(f"{name.title()},感谢您参加我们的这次关于编程语言的调查！ ")
    else:
        print("亲爱的"+name.title()+",我们希望你能参与我们的这次调查！ ")