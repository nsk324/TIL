# #1-1. 파일 읽기(옛날 방식) - read ()
# f = open('ssafy.txt', 'r') #읽다. 
# all_text = f.read()  #읽겠다 파일을 문자 열로 return
# print(all_text)
# f.close() # 꼭 닫아주기

# #1-2. 파일 읽기 (최신 방식) 
# with open('with_ssafy.txt','r') as f:
#     all_text = f.read()
# #     print(all_text)


# #2-1. 파일 읽기 (옛날 방식) - readlines()
# #라인을 모두 다 읽어서 리스트 만든 후 출력
# f = open('ssafy.txt', 'r')
# lines = f.readlines()

# for line in lines:
#     print(line)

# f.close()


#2-2. 파일 읽기(최신 방식) -readlines()
with open('with_ssafy.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())