from util import *

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码



def ikuuuu():
    try:
        driver = get_web_driver()
        driver.get("https://ikuuu.co/auth/login")
        #print("加载成功")
        #driver.find_element_by_xpath("//*[@class='nav-link dropdown-toggle nav-link-lg nav-link-user']").click()
        #driver.find_element_by_xpath("//*[@class='dropdown-item has-icon text-danger']").click()
        
        #driver.implicitly_wait(10)
        #time.sleep(5)
        
        driver.find_element_by_xpath("//*[@id='email']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//*[@class='btn btn-primary btn-lg btn-block login']").click()
        #print("登录成功")
        driver.get("https://ikuuu.co/user")
        
        #requests.post("https://ikuuu.co/user/checkin")
        #print("提交成功")
        driver.implicitly_wait(10)
        #time.sleep(10)

        driver.find_element_by_xpath("//*[@data-dismiss='modal']").click()
        #driver.find_element_by_xpath("//*/ul[@data-dismiss='modal']/button[text()='Read']").click()
        #print("登录2成功")
        #driver.implicitly_wait(10)
        #print("ikuu前置成功")
        #driver.find_element_by_xpath("//*[@onclick='checkin()']").click()
        #print("ikuu签到成功")
    except:
        raise
    finally:
        try:
            driver.find_element_by_xpath("//*[@onclick='checkin()']").click()
            print("ikuu签到成功")
        except:
            raise
        driver.quit()

if __name__ == '__main__':
    ikuuuu()
