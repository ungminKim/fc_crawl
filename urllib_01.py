from urllib import request

img_url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxNjExMjNfMTY0%2FMDAxNDc5ODg1NTM5NDU4._ZoLGT-B2oWIbIGeKFoCTSf4Gr7DCLdwmKmawazLY4kg.UUPj_K2iuAnOq3SqEtBeY6pYzDwV313sNieRLwjdrccg.PNG.travelart%2F161123_%25BA%25A3%25B4%25CF%25BD%25BA%25BF%25A9%25C7%25E0%25B8%25ED%25BC%25D2_5.png&type=b400'
html_url = 'https://naver.com'

save_path1 = 'C:/users/user/fc_web_crawl/test_img.jpg'
save_path2 = 'C:/users/user/fc_web_crawl/test_html.html'

try:
    file1, header1 = request.urlretrieve(img_url, save_path1)
    file2, header2 = request.urlretrieve(html_url, save_path2)
except Exception as e:
    print("Download Failed")
    print(e)
else:
    print(header1)
    print(header2)

    print('Filename1 {}'.format(file1))
    print('Filename2 {}'.format(file2))
    print()

    print("Download Succeed")



