from urllib import request
from urllib.error import URLError, HTTPError

path_list = ["C:/users/user/fc_web_crawl/test_img2.jpg", "C:/users/user/fc_web_crawl/test_html2.html"]

target_url = [
    "http://post.phinf.naver.net/MjAxOTEyMzFfMTI3/MDAxNTc3NzU2MDg0OTU1.MYwD2jPH0MumL3wfrt0sWPJ3lKs3JX8hSWaloIUidGog.vX6HGCX_z5-fmQS1_gvr7qmwOw2PEqC_8n8i1dNCGaQg.PNG/IluNGm0O5PeOgCVlLyR6NxhKPHDg.jpg",
    "https://google.co.kr"
]

for i, url in enumerate(target_url):
    try:
        response = request.urlopen(url)
        contents = response.read()

        print("-" * 50)

        print('Header Info - {}'.format(response.info()))
        print('HTTP Status Code {}'.format(response.getcode()))
        
        print("-" * 50)

    except URLError as e:
        print("Download Failed")
        print(e)
    except HTTPError as e:
        print("Download Failed")
        print(e)
    else:
        print()
        print("Download Succeed")