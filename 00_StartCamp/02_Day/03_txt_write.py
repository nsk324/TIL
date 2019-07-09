# #1. 파일 쓰기(옛날 방식)

# f = open('ssafy.txt','w') ## w가 쓰겟다는 말임
# for i in range(10):
#     f.write(f'This is line {i}.\n')
#     #\n하면 엔터친거처럼 개행됨.. r 붙여주면 그대로드간대..
# f.close() #반드시 해줘야함.... 열엇으면...닫기...

#2. 파일쓰기(최신방식)
with open('with_ssafy.txt','w') as f: 
    for i in range(10):
        f.write(f'This is line {i}.\n')
