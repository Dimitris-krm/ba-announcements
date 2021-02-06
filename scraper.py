import selenium
from selenium import webdriver
import time
from win10toast import ToastNotifier
import smtplib
from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart


def checksite():
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
    driver.get("https://ba.uowm.gr/category/news/")
    test = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/main/article[1]/div/header/h2/a").text
    link = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/main/article[1]/div/header/h2/a").get_attribute("href")
    print(link)
    check_news = open("news.txt", "r")

    def sendemail():
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login("wdkaramatskos@gmail.com", "mdddkfpakimltbwy")

        subject = "There's a new announcement at the Uni's website "
        body = f"There's a new announcement at the Uni's website click the link below to nagivate to it\n\n{link}"
        msg = f"Subject: {subject}\n\n{body}"

        recipients = ["wdkaramatskos@gmail.com", "wickerman43@gmail.com", "trabaxesou@gmail.com", "mariak6789@gmail.com"]
        server.sendmail("wdkaramatskos@gmail.com", recipients, msg.encode(encoding="ascii", errors="xmlcharrefreplace"))
        print("Email Sent")
        server.quit()

    if check_news.read() != str(test):
        check_news.close()
        check_news = open("news.txt", "w")
        check_news.write(str(test))
        check_news.close()
        print(test)
        check_news = open("news.txt", "r")
        check_news.read()
        check_news.close()
        sendemail()
    driver.close()


def send_notification():
    hr = ToastNotifier()
    hr.show_toast("alarm", "Βγήκε νέα ανακοίνωση στο σίτε της σχολής")


while True:
    checksite()
    time.sleep(60 * 60)
