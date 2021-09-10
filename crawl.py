import requests 
import re
import os
import time




# Get URL
def get_parse_page(pn,name):

    for i in range(int(pn)):
        # 1.Get pages
        print('Getting Page {}'.format(i+1))

        # Baidu image homepage url
        # name: keyword
        # pn: number of pages

        url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%s&pn=%d' %(name,i*20)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400'}

        # Send request and get response
        response = requests.get(url, headers=headers)
        html = response.content.decode()
        # print(html)

        # 2. Get links using REGEX
        # "objURL":"http://n.sinaimg.cn/sports/transform/20170406/dHEk-fycxmks5842687.jpg"
        results = re.findall('"objURL":"(.*?)",', html) # A list

        # Save to local
        save_to_txt(results, name, i)


# Save image to local
def save_to_txt(results, name, i):

    j = 0
    # Create directory
    if not os.path.exists('./' + name):
        os.makedirs('./' + name)

    # Download image
    for result in results:
        print('Storing Image {}'.format(j))
        try:
            pic = requests.get(result, timeout=5)
            time.sleep(1)
        except:
            print('Cannot download the current image')
            j += 1
            continue


        # Save images to folder
        file_full_name = './' + name + '/' + str(i) + '-' + str(j) + '.jpg'
        with open(file_full_name, 'wb') as f:
            f.write(pic.content)

        j += 1



# main
if __name__ == '__main__':

    name = input('Keyword：')
    pn = input('How many pages（1 page has 60 images）:')
    get_parse_page(pn, name)

