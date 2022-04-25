from util import *

username = sys.argv[1] #  登录账号
password = sys.argv[2] #   登录密码



def edu():
    try:
        driver = get_web_driver()
        driver.get("https://wangzi.uk/auth/login")

        driver.implicitly_wait(10)
        #time.sleep(5)

        driver.find_element_by_xpath("//*[@id='email']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='passwd']").send_keys(password)
        driver.find_element_by_xpath("//*[@id='login']").click()
        #print('登录成功')
        #driver.get("https://wangzi.uk/user")
        #print('刷新成功')
        #time.sleep(5)
        #driver.find_element_by_xpath("//*[@class='waves-attach waves-effect collapsed']").click()
        driver.implicitly_wait(10)
        print('延迟成功')
        #driver.switch_to.frame(driver.find_element_by_xpath("//button[@class='btn btn-brand btn-flat']"))
        #driver.find_element_by_xpath("//*/span[@class='icon']/span]").click()
        #driver.find_element_by_xpath("//*[@id='checkin']").click()
        driver.find_element_by_xpath("//button[contains(text(),'或者摇动手机签到')]")
        print('签到成功')
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    edu()
