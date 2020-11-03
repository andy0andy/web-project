from selenium import webdriver


'''
对接 WebDriver 反爬，检测到使用 WebDriver 就不显示页面，适合用作 WebDriver 反爬练习。
'''



def run():
    url = "https://antispider1.scrape.center/"


    driver = webdriver.Chrome()

    # 设置window.navigator.webdriver 的值为 undefined
    # 非常有效

    # execute_cdp_cmd()：执行开发者工具协议API
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source":
            """
             Object.defineProperty(navigator, 'webdriver', {
               get: () => undefined
             })
           """
    })

    driver.get(url)







if __name__ == '__main__':
    run()
    input()
