import requests
import concurrent.futures
from termcolor import colored

def check_url(base_url, word):
    url = f"{base_url}/{word}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(colored(f"[+] Found: {url}", 'green'))
        else:
            print(colored(f"[-] Not found: {url} (Status Code: {response.status_code})", 'red'))
    except requests.RequestException as e:
        print(colored(f"[-] Error accessing {url}: {e}", 'red'))

def brute_force(base_url, wordlist_file):
    # قراءة قائمة الكلمات من الملف
    with open(wordlist_file, 'r') as f:
        words = [line.strip() for line in f]

    # استخدام ThreadPoolExecutor لتنفيذ الطلبات بشكل متوازي
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(check_url, base_url, word) for word in words]
        concurrent.futures.wait(futures)

if name == "__main__":
    base_url = 'https://glob-care.com/'  # ضع هنا عنوان الموقع المستهدف
    wordlist_file = 'wordlist.txt'    # ضع هنا مسار قائمة الكلمات
    brute_force(base_url, wordlist_file)
