from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import functions
import time
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
keyword = "포항 오도리"
del_text = "[:!@#$%^&*()_+\}{?><'=/.,`~0-9a-zA-Z\n]"

add_noun = ['오도리','오도리오도시','오도리해수욕장']
no_word = ['볼','맛집','바다','진짜','포항','오도리','그','후','원','분','곳','어요','해','하는','뭐','약','곳','층','해','날','맛','존','앞','핫','때','내','넌','것','요','거','린','위','저','탑','또','된','잘']

steps=[True,True] #0 : 수집, 1 : 워드클라우드

if steps[0]:
    options= webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    # options.add_argument('disable-gpu')

    driver = webdriver.Chrome('./chromedriver',chrome_options=options)
    action = webdriver.common.action_chains.ActionChains(driver)

    f =functions.function(driver)
    blog_search_address = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='


    file = open(keyword+".txt",'w',encoding='utf-8-sig')
    cnt = 0

    #시작!!
    driver.get(blog_search_address+keyword)
    for page in range(30):
        for i in range(1,11):
            title=driver.find_element_by_xpath("//ul[@id='elThumbnailResultArea']/li[@id='sp_blog_" + str(i) + "']/dl/dt/a").get_attribute('title')
            ispass = f.pass_auction_article(title)
            if ispass:
                continue
            driver.find_element_by_xpath("//ul[@id='elThumbnailResultArea']/li[@id='sp_blog_"+str(i)+"']/dl/dt").click()
            f.tap_change_sub()
            time.sleep(0.2)
            try:
                driver.switch_to.frame("mainFrame")
                text = driver.find_element_by_xpath("//div[@id='whole-body']").text
                text = f.cleanText(text,del_text)

                print(text)
                cnt +=1
            except:
                text =''
            file.write(text)
            driver.close()
            f.tap_change_main()
        driver.find_element_by_xpath("//*[@class='next']").click()
        time.sleep(0.1)

    file.write('\nEnd count : '+str(cnt))
    print('\nEnd count : '+str(cnt))
    file.close()
    driver.close()

if steps[1]:
    #word cloud 만들기
    import matplotlib.pyplot as plt
    from ckonlpy.tag import Twitter
    from wordcloud import WordCloud
    from wordcloud import ImageColorGenerator
    from matplotlib import font_manager, rc
    from PIL import Image
    import numpy as np

    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)

    tager = Twitter()


    for add in add_noun:
        tager.add_dictionary(add,'Noun')

    text = open(keyword+'.txt',encoding='utf-8-sig').read()

    tokens = tager.pos(text)

    wordlist =[]
    for word in tokens:
        if word[1] in ['Noun']:
            if word[0] not in no_word :
                wordlist.append(word[0])

    words = nltk.Text(wordlist,name=keyword)
    top_words=words.vocab().most_common(1000)
    words_dic = dict(top_words)

    mask = np.array(Image.open("shape.png"))
    wordcloud = WordCloud(font_path='c:/Windows/Fonts/malgun.ttf',mask=mask,relative_scaling=0.2,height=1020,width=1020,max_font_size=300,background_color='white').generate_from_frequencies(words_dic)
    plt.figure(figsize=(12,12))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
    wordcloud.to_file(keyword+'.png')