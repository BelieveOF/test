import requests

from lxml import etree


class Login(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        token = selector.xpath('//*[@id="login"]/form/input[2]/@value')[0]
        print(token)
        return token

    def dynamics(self,html):
        selector = etree.HTML(html)
        urls_list = selector.xpath('//*[@id="dashboard"]/div[1]/div/div[2]/ul/li//a/@href')
        # print(urls_list)
        for url in urls_list:
            url='https://github.com/'+url
            print(url)

    def login(self, username, password):
        post_data = {
            'commit': 'Sign in',
            'utf-8': '✓',
            'authenticity_token': self.token(),
            'login': username,
            'password': password
        }

        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            print("登录成功")
            # print(response.text)
            self.dynamics(response.text)
            # 处理


if __name__ == '__main__':
    login = Login()
    # login.login(username='BelieveOF', password='liujiao1314521')
    # login.login(username='hisonny', password='a15294981618')
