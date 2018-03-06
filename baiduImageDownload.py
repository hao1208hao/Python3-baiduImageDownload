import requests
import os

def getManyPages(keyword,pages):
    params=[]
    for i in range(30,30*pages+30,30):
        params.append({
                      'tn': 'resultjson_com',
                      'ipn': 'rj',
                      'ct': 201326592,
                      'is': '',
                      'fp': 'result',
                      'queryWord': keyword,
                      'cl': 2,
                      'lm': -1,
                      'ie': 'utf-8',
                      'oe': 'utf-8',
                      'adpicid': '',
                      'st': -1,
                      'z': '',
                      'ic': 0,
                      'word': keyword,
                      's': '',
                      'se': '',
                      'tab': '',
                      'width': '',
                      'height': '',
                      'face': 0,
                      'istype': 2,
                      'qc': '',
                      'nc': 1,
                      'fr': '',
                      'pn': i,
                      'rn': 30,
                      'gsm': '1e',
                      '1488942260214': ''
                  })
    url = 'https://image.baidu.com/search/acjson'
    urls = []
    for i in params:
        urls.append(requests.get(url,params=i).json().get('data'))

    
    return urls


def downloadImg(dataList, localPath):

    if not os.path.exists(localPath):  # 新建文件夹
        os.mkdir(localPath)

    x = 0
    imgType = "middleURL";    #objURL   thumbURL      middleURL   hoverURL 
    for list in dataList:
        for i in list:
            if i.get(imgType) != None:
                print('正在下载：%s' % i.get(imgType)+'\n')             
                ir = requests.get(i.get(imgType))
                open(localPath + '%d.jpg' % x, 'wb').write(ir.content)
                x += 1
            else:
                print('图片链接不存在\n')

if __name__ == '__main__':
    #参考链接：http://blog.csdn.net/qq_32166627/article/details/60882964
    #https://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=美女&cg=girl&rn=60&pn=60
    inputContent = input("请输入要搜索的图片关键字:\n");
    print("===============请稍候=================\n")
    
    dataList = getManyPages(inputContent,10)  # 参数1:关键字，参数2:要下载的页数

    
    #下载图片
    downloadImg(dataList,'d:/baiduImageDownload/') # 参数2:指定保存的路径
