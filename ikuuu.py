from util import *

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码



def ikuuu():
    try:
        driver = get_web_driver()
        driver.get("https://ikuuu.co/auth/login")
        
        #driver.find_element_by_xpath("//*[@class='nav-link dropdown-toggle nav-link-lg nav-link-user']").click()
        #driver.find_element_by_xpath("//*[@class='dropdown-item has-icon text-danger']").click()
        
        #driver.implicitly_wait(10)
        #time.sleep(5)
        
        driver.find_element_by_xpath("//*[@id='email']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//*[@class='btn btn-primary btn-lg btn-block login']").click()

        #driver.get("https://ikuuu.co/user")
        #driver.implicitly_wait(10)
        #time.sleep(5)

        driver.find_element_by_xpath("//*[@data-dismiss='modal']").click()
        #driver.implicitly_wait(10)
        driver.find_element_by_xpath("//*[@class='far fa-calendar-check']").click()
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    ikuuu()
