from selenium.common import exceptions
import time
import math
from seleniumbase import SB
from bs4 import BeautifulSoup 
from utils.function_utils import *

def data2csv(pddata,filename,index=False,col=True):
    pddata.to_csv(filename, sep=',', index=index,header=col)


def checkCloudFlare(sb,url,save_path,index):
    source_code = sb.get_page_source()
    bs = BeautifulSoup(source_code,"html.parser")  
    title=bs.title.get_text()
    if "Just a moment" in title:
        if sb.is_element_visible('input[value*="Verify"]'):
            sb.click('input[value*="Verify"]')
        elif sb.is_element_visible('iframe[title*="challenge"]'):
            sb.switch_to_frame('iframe[title*="challenge"]')
            sb.click("span.mark")
        else:
            passCloudFlare(url,save_path,index) 
              
        get_gpt_info(sb,url,save_path,index)
    else:
        get_gpt_info(sb,url,save_path,index)
    
def get_gpt_info(sb,url,save_path,index):
    source_code = sb.get_page_source()
    bs = BeautifulSoup(source_code,"html.parser")
    title=bs.title
    if title is None:
        with open(save_path, mode='w', encoding='utf-8') as html_file:
            html_file.write("No page found")  
        print(index)
    else:
        title=title.get_text()
        if "GPTStore" in title:
            with open(save_path, mode='w', encoding='utf-8') as html_file:
                html_file.write(source_code)
            print(index)
        else: 
            passCloudFlare(url,save_path,index)
            

def passCloudFlare(url,save_path,index):
    with SB(uc_cdp=True, guest_mode=True, locale_code="en_us",headless=True) as sb:
        sb.open(url)
        try:
            checkCloudFlare(sb,url,save_path,index)
        except exceptions.NoSuchElementException:
            passCloudFlare(url,save_path,index)
        except exceptions.NoSuchFrameException:
            passCloudFlare(url,save_path,index)
        except exceptions.NoSuchWindowException:
            passCloudFlare(url,save_path,index)
        except Exception:
            passCloudFlare(url,save_path,index)