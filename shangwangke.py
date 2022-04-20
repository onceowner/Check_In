from util import *

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码



def shangwangke():
    try:
        driver = get_web_driver()
        driver.get("https://shangwangke.org/auth/login")
        driver.find_element_by_xpath("//*[@id='email']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//*[@class='btn btn-primary btn-lg btn-block login']").click()

        #time.sleep(5)

        driver.find_element_by_xpath("//*[@class='btn btn-primary']").click() 

        driver.find_element_by_xpath("//*[@onclick='checkin()']").click()
        print('签到成功')
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    shangwangke()
