import webbrowser

idol=["드림케쳐", "우주소녀", "AB6", "워너원"]

for i in idol:
    print(i)
    webbrowser.open_new_tab('https://search.naver.com/search.naver?query='+i)
    print(type(i))