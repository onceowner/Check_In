from util import *

username = sys.argv[1] # 登录账号 sys.argv[1]
password = sys.argv[2] # 登录密码 sys.argv[2]



def jiji():
    try:
        driver = get_web_driver()
        driver.get("https://a.luxury/signin")
        #print("加载成功")
        #driver.find_element_by_xpath("//*[@class='nav-link dropdown-toggle nav-link-lg nav-link-user']").click()
        #driver.find_element_by_xpath("//*[@class='dropdown-item has-icon text-danger']").click()
        
        #driver.implicitly_wait(10)
        #time.sleep(5)
        
        driver.find_element_by_xpath("//*[@name='email']").send_keys(username)
        driver.find_element_by_xpath("//*[@class='el-input__inner']").send_keys(password)
        driver.find_element_by_xpath("//*[@class='el-button el-button--primary']").click()
        #print("登录成功")
        driver.get("https://a.luxury/user")
        driver.implicitly_wait(10)
        #time.sleep(5)

        driver.find_element_by_xpath("//*[@class='el-button el-button--primary']").click()
        print("登录2成功")
        #time.sleep(5)
        driver.implicitly_wait(10)
        #driver.find_element_by_xpath("//*/ul[@class='ui button purple tiny mt-2 pio-tip mr-0 fontsize']/li[text()='签到流量']").click()
        #driver.find_element_by_xpath("//*[@data-pio='每天签到 800MB~5200MB，祝君好运！1 级用户每月 2 号重置流量为 10G']").click()
        #driver.find_element_by_link_text("签到流量").click()
        #driver.find_element(By.LINK_TEXT,"签到流量").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div[2]/div[1]/div/div[2]/div/div[6]").click()
        print("签到成功")
    except:
        raise
    finally:
        driver.quit()
        exit()

if __name__ == '__main__':
    jiji()
