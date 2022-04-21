from util import *

username = sys.argv[1] #  登录账号
password = sys.argv[2] #   登录密码



def edu():
    try:
        driver = get_web_driver()
        driver.get("https://wangzi.uk/auth/login")

        time.sleep(5)

        driver.find_element_by_xpath("//*[@id='email']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='passwd']").send_keys(password)
        driver.find_element_by_xpath("//*[@id='login']").click()

        time.sleep(10)

        #driver.find_element_by_xpath("//*[@data-dismiss='modal']").click() 

        driver.find_element_by_xpath("//*[@id='checkin']").click()
        print('签到成功')
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    edu()
