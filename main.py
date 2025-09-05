import requests, uuid, re, random
wi = str(uuid.uuid4())
import time, hmac, hashlib, secrets
proxies = None 
import requests
import time, string
from colorama import Fore, init
init()

def ng(length):
    # تحديد مجموعة الأحرف الممكنة (حروف صغيرة، حروف كبيرة، أرقام، رموز)
    characters = string.ascii_letters + string.digits
    # توليد سلسلة عشوائية من الأحرف
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def random_string(length=12):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def email():
    headers1 = {'User-Agent': 'Dart/3.5 (dart:io)','Content-Type': 'application/json'}
    json_data1 = {
        'deviceId': f'bec286a6-7971-4284-8248-{ng(12)}',
        'expirationMinutes': 60,
    }
    response = requests.post('https://api.evapmail.com/v1/accounts/create', headers=headers1, json=json_data1)
    token = (response.json()['token'])
    email = (response.json()['email'])
    return email, token

def login_and_follow(username, password, target_user):
    tim = str(time.time()).split(".")[0]
    cookies = {
        'dpr': '1.25',
        'mid': 'aFBIjQALAAEh7Z7lNQP1AsnnKAzM',
        'datr': 'jEhQaH4M6mQUyf0NwUeU9tVg',
        'ig_did': 'D86A17DA-7F67-41AF-B7E2-962C48B51A40',
        'ig_nrcb': '1',
        'ps_l': '1',
        'ps_n': '1',
        'rur': '"LDC\\05475476384448\\0541781796423:01fe3ba5238877e4a34222a5a55a21392ddde2e75e71d2187d11b8364eae6d39817936b1"',
        'csrftoken': 'B7CnyvYwpVgvk5tQlKbtRLqH9mdQkoJs',
        'wd': '982x730',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.instagram.com',
        'priority': 'u=1, i',
        'referer': 'https://www.instagram.com/',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="137.0.7151.104", "Chromium";v="137.0.7151.104", "Not/A)Brand";v="24.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
        'x-asbd-id': '359341',
        'x-csrftoken': 'B7CnyvYwpVgvk5tQlKbtRLqH9mdQkoJs',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': '1023966789',
        'x-requested-with': 'XMLHttpRequest',
        'x-web-session-id': 'ltyp6p:km604s:1e693a',
    }
    
    data = {
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(tim, password),
        'caaF2DebugGroup': '0',
        'isPrivacyPortalReq': 'false',
        'loginAttemptSubmissionCount': '0',
        'optIntoOneTap': 'false',
        'queryParams': '{}',
        'trustedDeviceRecords': '{}',
        'username': username,
        'jazoest': '23015',
    }

    response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', cookies=cookies, headers=headers, data=data)
    cookies_dict = response.cookies.get_dict()
    
    try:
        sessionid = cookies_dict['sessionid']
        print(Fore.GREEN + f" [+] Login success / Session ID : {sessionid}")
        
        # Get user ID to follow
        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'referer': f'https://www.instagram.com/{target_user}/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'x-asbd-id': '129477',
            'x-csrftoken': 'S1tFXRCsflUJCBKWav6rP8d0DsnfiEMP',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR07T_Q0xaDQfazO_ogFm4DlAfLnCNNeQ0b0skK1F4sWzJzO',
            'x-requested-with': 'XMLHttpRequest',
        }
        
        r = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={target_user}', headers=headers).json()
        try:
            id = r["data"]["user"]["id"]
            print(Fore.YELLOW + f" [+] Found target user ID: {id}")
        except:
            print(Fore.RED + " [-] User not found")
            return False

        # Follow the user
        cookies = {
            'csrftoken': 'y56zSqwwsO03xe9SmxQTIe',
            'dpr': '1.25',
            'mid': 'aFBIjQALAAEh7Z7lNQP1AsnnKAzM',
            'datr': 'jEhQaH4M6mQUyf0NwUeU9tVg',
            'ig_did': 'D86A17DA-7F67-41AF-B7E2-962C48B51A40',
            'ig_nrcb': '1',
            'ds_user_id': '75476384448',
            'sessionid': sessionid,
            'wd': '982x730',
            'rur': '"LDC\\05475476384448\\0541781796027:01fe80a67ab9413a50ef2eff61d18583a4c10c7722de44836d82586c0c5bd1b46d8b1fe5"',
        }

        headers = {
            'accept': '*/*',
            'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'priority': 'u=1, i',
            'referer': f'https://www.instagram.com/{target_user}/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-full-version-list': '"Google Chrome";v="137.0.7151.104", "Chromium";v="137.0.7151.104", "Not/A)Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"15.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
            'x-asbd-id': '359341',
            'x-bloks-version-id': 'b029e4bcdab3e79d470ee0a83b0cbf57b9473dab4bc96d64c3780b7980436e7a',
            'x-csrftoken': 'y56zSqwwsO03xe9SmxQTIe',
            'x-fb-friendly-name': 'usePolarisFollowMutation',
            'x-fb-lsd': 'tmHDMd3M-A8Hb4MeYLgjGY',
            'x-ig-app-id': '936619743392459',
            'x-root-field-name': 'xdt_create_friendship',
        }

        data = {
            'av': '17841475373454548',
            '__d': 'www',
            '__user': '0',
            '__a': '1',
            '__req': '5n',
            '__hs': '20257.HYP:instagram_web_pkg.2.1...0',
            'dpr': '1',
            '__ccg': 'GOOD',
            '__rev': '1023966789',
            '__s': 'ka47ei:2i0gtv:d17ad6',
            '__hsi': '7517300840350867610',
            '__dyn': '7xeUjG1mxu1syaxG4Vp41twWwIxu13wvoKewSAwHwNw9G2Saxa0DU6u3y4o0B-q1ew6ywMwto2awgo9oO0n24oaEnxO1ywOwv89k2C1Fwc60AEC1TwQzXw8W58jwGzEaE2iwNwh8lwuEjUlwhEe88o5i7U1oEbUGdG1QwTU9UaQ0z8c86-3u2WE5B08-269wr86C1mgcEed6goK2OubK5V89FbxG1oxe6UaUaE2xyUC4o16UsAxCaCwHw',
            '__csr': 'hsegd4RigHsoxkBu-yEGayN3Oc_kzRLp94KCiOp9AAQF4CilACQjAVp5AAADJ8Om8GQy9CnqhCmLKmQuyJQaFi2WyWGuuXCZtt5pp_jBDKt2F4AhGaR-KnG8DyFXAG9KFtKmAt5GiRLJVVEL--nV6i8tikibV8KmFUF4yeF8jx6qbAyqWAheqp2pUjUjzuHAAgOaKjWm4p8jx2im00kpC3p0pU3cwuDS8yHwmo3aG0-y7z8662swkxJ0863q20HDgG12xNUO58yr5j0JwnC2SrhonKc-ut8G4wFwFwCx2UG5o9KrD4BwMwhwxxq8xa08sbVU7G0gK0_8nw7NwTg1Z80wF1W2cw3vwaoM7l4-NwOuewn4V5gEjwa8qnz45A13w7lwhUhgjl0uC5Uy0hV122p0EwbF0348vwpU0B60ccBxq4Hmbxy1dyfyo-7401luwkE1Oy6wMwa22u0EUB02g9rAg4G1LKGy89Udo3Iwbi0bQU0kFxiE19o',
            '__hsdp': 'gdY8_f5h79nkxih5EWiWii3oMI-NO6i4Ln0L66dkPlReLe51p2hbDihsIfdhO0LSNYGQqi-yDiiaoKG6lc2vopu2e2xpFpob8wwgggWy64bm78S9wNxbwByofA4h0ixm18wOyouxu4UjGfwCCwGxe0NUeE-FE4W1TwXwm82Zw5jxy1nw25ohg88660Eo5e10wto2kwa60goE2tU7m12oswAw8K3C1PK1gwWz8o47wiU88',
            '__hblp': '1616AwZwyxWA6Ei-u7Ekw8V6DxrHxq3i9woQ2e9CDgjyF8-rVEaUSdwxwCGKAGzpojDyUnzt3oWueypqBQ9LxCemGzfzEgK9GVrwyAy8-49eEkG4FK2vyF47GyoWfxuii9Lx-EqgzAxaEjxi6UK22bwJwAx-czEy4kE-ErwICBxK1rxu4Egwmawi8PwoF9EmweucAyaxuE-685u0FoS6E2Myo2bByQUiyofU8o9GAg8EnwDzE4G8wg8GaU5Sm0zEnxm26qewXwzwTwzwvVywAxG264-az99RgmwXwxzEW2hG6oK68vhEaodrACxa6E9E98889oK5UhwwCxacG4G46jy8G3efDy8',
            '__comet_req': '7',
            'fb_dtsg': 'NAfueqBj_KJNiq4GOsxIF7OwoGQLYq7G2dmV4DALzPJlX-zn3jXudlQ:17865379441060568:1750179099',
            'jazoest': '26334',
            'lsd': 'tmHDMd3M-A8Hb4MeYLgjGY',
            '__spin_r': '1023966789',
            '__spin_b': 'trunk',
            '__spin_t': '1750257993',
            '__crn': 'comet.igweb.PolarisProfilePostsTabRoute',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'usePolarisFollowMutation',
            'variables': '{"target_user_id":"'+id+'","container_module":"profile","nav_chain":"PolarisClipsTabDesktopContainer:reelsTab:2:topnav-link,PolarisProfilePostsTabRoot:profilePage:3:unexpected,PolarisProfilePostsTabRoot:profilePage:12:unexpected,PolarisProfilePostsTabRoot:profilePage:13:unexpected"}',
            'server_timestamps': 'true',
            'doc_id': '9740159112729312',
        }

        response = requests.post('https://www.instagram.com/graphql/query', cookies=cookies, headers=headers, data=data)
        print(Fore.GREEN + f" [+] Follow response: {response.json()}")
        print(Fore.GREEN + f" [+] Successfully followed {target_user}")
        return True
        
    except Exception as e:
        print(Fore.RED + f" [-] Error in login/follow process: {e}")
        return False

def make():
    passwordd = 'yyy@R84844994'

    cookies = {
        'ig_did': '5C72BB73-7939-48C1-9F85-1B3EA1723F6D',
        'dpr': '2',
        'mid': 'aK-2xgABAAGFlH8s5ASyKX0chPqR',
        'csrftoken': 'gEBfgiHS4xJH3Wzn6PFXxE',
        'datr': 'DLivaDMocvP9eLfDkq1kKvXx',
        'wd': '360x436',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Redmi 8A Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/139.0.7258.143 Mobile Safari/537.36 Instagram 275.0.0.27.98 Android (29/10; 320dpi; 720x1369; Xiaomi; Redmi 8A; olivelite; qcom; en_GB; 458229237)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'sec-ch-ua-full-version-list': '"Not;A=Brand";v="99.0.0.0", "Android WebView";v="139.0.7258.143", "Chromium";v="139.0.7258.143"',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Android WebView";v="139", "Chromium";v="139"',
        'sec-ch-ua-model': '"Redmi 8A"',
        'sec-ch-ua-mobile': '?1',
        'x-ig-app-id': '1217981644879628',
        'x-requested-with': 'XMLHttpRequest',
        'x-instagram-ajax': '1026332911',
        'x-csrftoken': 'gEBfgiHS4xJH3Wzn6PFXxE',
        'x-web-session-id': ':bg25cy:569b65',
        'x-asbd-id': '359341',
        'sec-ch-prefers-color-scheme': 'light',
        'x-ig-www-claim': '0',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'origin': 'https://www.instagram.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.instagram.com/accounts/signup/email/?next=https%3A%2F%2Fwww.instagram.com%2F%3F__coig_restricted%3D1',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'priority': 'u=1, i',
    }
    
    email_input = input("email : ") 
    data = {
        'email': email_input,
        'jazoest': '22141',
    }

    response = requests.post('https://www.instagram.com/api/v1/web/accounts/check_email/', cookies=cookies, headers=headers, data=data)

    data = {
        'device_id': 'aK-2xgABAAGFlH8s5ASyKX0chPqR',
        'email': email_input,
        'jazoest': '22141',
    }

    response = requests.post(
        'https://www.instagram.com/api/v1/accounts/send_verify_email/',
        cookies=cookies,
        headers=headers,
        data=data,
    )

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Redmi 8A Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/139.0.7258.143 Mobile Safari/537.36 Instagram 275.0.0.27.98 Android (29/10; 320dpi; 720x1369; Xiaomi; Redmi 8A; olivelite; qcom; en_GB; 458229237)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'sec-ch-ua-full-version-list': '"Not;A=Brand";v="99.0.0.0", "Android WebView";v="139.0.7258.143", "Chromium";v="139.0.7258.143"',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Android WebView";v="139", "Chromium";v="139"',
        'sec-ch-ua-model': '"Redmi 8A"',
        'sec-ch-ua-mobile': '?1',
        'x-ig-app-id': '1217981644879628',
        'x-requested-with': 'XMLHttpRequest',
        'x-instagram-ajax': '1026332911',
        'x-csrftoken': 'gEBfgiHS4xJH3Wzn6PFXxE',
        'x-web-session-id': ':bg25cy:569b65',
        'x-asbd-id': '359341',
        'sec-ch-prefers-color-scheme': 'light',
        'x-ig-www-claim': '0',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'origin': 'https://www.instagram.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.instagram.com/accounts/signup/emailConfirmation/?next=https%3A%2F%2Fwww.instagram.com%2F%3F__coig_restricted%3D1',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'priority': 'u=1, i',
    }

    code = input("code : ")

    data = {
        'code': code,
        'device_id': 'aK-2xgABAAGFlH8s5ASyKX0chPqR',
        'email': email_input,
        'jazoest': '22141',
    }

    response = requests.post(
        'https://www.instagram.com/api/v1/accounts/check_confirmation_code/',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    
    rc = response.json()["signup_code"]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Redmi 8A Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/139.0.7258.143 Mobile Safari/537.36 Instagram 275.0.0.27.98 Android (29/10; 320dpi; 720x1369; Xiaomi; Redmi 8A; olivelite; qcom; en_GB; 458229237)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'sec-ch-ua-full-version-list': '"Not;A=Brand";v="99.0.0.0", "Android WebView";v="139.0.7258.143", "Chromium";v="139.0.7258.143"',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Android WebView";v="139", "Chromium";v="139"',
        'sec-ch-ua-model': '"Redmi 8A"',
        'sec-ch-ua-mobile': '?1',
        'x-ig-app-id': '1217981644879628',
        'x-requested-with': 'XMLHttpRequest',
        'x-instagram-ajax': '1026332911',
        'x-csrftoken': 'gEBfgiHS4xJH3Wzn6PFXxE',
        'x-web-session-id': ':bg25cy:569b65',
        'x-asbd-id': '359341',
        'sec-ch-prefers-color-scheme': 'light',
        'x-ig-www-claim': '0',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'origin': 'https://www.instagram.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.instagram.com/accounts/signup/name/?next=https%3A%2F%2Fwww.instagram.com%2F%3F__coig_restricted%3D1',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'priority': 'u=1, i',
    }
    
    username = random_string(17)
    data = {
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1756239703:{passwordd}',
        'email': email_input,
        'failed_birthday_year_count': '{}',
        'first_name': 'by #Chyo',
        'username': username,
        'seamless_login_enabled': '1',
        'use_new_suggested_user_name': 'true',
        'jazoest': '22801',
    }

    response = requests.post(
        'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/',
        cookies=cookies,
        headers=headers,
        data=data,
    )

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Redmi 8A Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/139.0.7258.143 Mobile Safari/537.36 Instagram 275.0.0.27.98 Android (29/10; 320dpi; 720x1369; Xiaomi; Redmi 8A; olivelite; qcom; en_GB; 458229237)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'sec-ch-ua-full-version-list': '"Not;A=Brand";v="99.0.0.0", "Android WebView";v="139.0.7258.143", "Chromium";v="139.0.7258.143"',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Android WebView";v="139", "Chromium";v="139"',
        'sec-ch-ua-model': '"Redmi 8A"',
        'sec-ch-ua-mobile': '?1',
        'x-ig-app-id': '1217981644879628',
        'x-requested-with': 'XMLHttpRequest',
        'x-instagram-ajax': '1026332911',
        'x-csrftoken': 'gEBfgiHS4xJH3Wzn6PFXxE',
        'x-web-session-id': ':bg25cy:569b65',
        'x-asbd-id': '359341',
        'sec-ch-prefers-color-scheme': 'light',
        'x-ig-www-claim': '0',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'origin': 'https://www.instagram.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.instagram.com/accounts/signup/birthday/?next=https%3A%2F%2Fwww.instagram.com%2F%3F__coig_restricted%3D1',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'priority': 'u=1, i',
    }

    data = {
        'day': '26',
        'month': '8',
        'year': '1985',
        'jazoest': '22801',
    }

    response = requests.post(
        'https://www.instagram.com/api/v1/web/consent/check_age_eligibility/',
        cookies=cookies,
        headers=headers,
        data=data,
    )

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Redmi 8A Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/139.0.7258.143 Mobile Safari/537.36 Instagram 275.0.0.27.98 Android (29/10; 320dpi; 720x1369; Xiaomi; Redmi 8A; olivelite; qcom; en_GB; 458229237)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'sec-ch-ua-full-version-list': '"Not;A=Brand";v="99.0.0.0", "Android WebView";v="139.0.7258.143", "Chromium";v="139.0.7258.143"',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Android WebView";v="139", "Chromium";v="139"',
        'sec-ch-ua-model': '"Redmi 8A"',
        'sec-ch-ua-mobile': '?1',
        'x-ig-app-id': '1217981644879628',
        'x-requested-with': 'XMLHttpRequest',
        'x-instagram-ajax': '1026332911',
        'x-csrftoken': 'gEBfgiHS4xJH3Wzn6PFXxE',
        'x-web-session-id': ':bg25cy:569b65',
        'x-asbd-id': '359341',
        'sec-ch-prefers-color-scheme': 'light',
        'x-ig-www-claim': '0',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'origin': 'https://www.instagram.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.instagram.com/accounts/signup/birthday/?next=https%3A%2F%2Fwww.instagram.com%2F%3F__coig_restricted%3D1',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'priority': 'u=1, i',
    }

    data = {
        'email': email_input,
        'name': 'by #Aven',
        'jazoest': '22801',
    }

    response = requests.post(
        'https://www.instagram.com/api/v1/web/accounts/username_suggestions/',
        cookies=cookies,
        headers=headers,
        data=data,
    )

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Redmi 8A Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/139.0.7258.143 Mobile Safari/537.36 Instagram 275.0.0.27.98 Android (29/10; 320dpi; 720x1369; Xiaomi; Redmi 8A; olivelite; qcom; en_GB; 458229237)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'sec-ch-ua-full-version-list': '"Not;A=Brand";v="99.0.0.0", "Android WebView";v="139.0.7258.143", "Chromium";v="139.0.7258.143"',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Android WebView";v="139", "Chromium";v="139"',
        'sec-ch-ua-model': '"Redmi 8A"',
        'sec-ch-ua-mobile': '?1',
        'x-ig-app-id': '1217981644879628',
        'x-requested-with': 'XMLHttpRequest',
        'x-instagram-ajax': '1026332911',
        'x-csrftoken': 'gEBfgiHS4xJH3Wzn6PFXxE',
        'x-web-session-id': ':bg25cy:569b65',
        'x-asbd-id': '359341',
        'sec-ch-prefers-color-scheme': 'light',
        'x-ig-www-claim': '0',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'origin': 'https://www.instagram.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.instagram.com/accounts/signup/username/?next=https%3A%2F%2Fwww.instagram.com%2F%3F__coig_restricted%3D1',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'priority': 'u=1, i',
    }

    data = {
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1756239703:{passwordd}',
        'day': '26',
        'email': email_input,
        'failed_birthday_year_count': '{}',
        'first_name': 'by #Aven',
        'month': '8',
        'username': username,
        'year': '1985',
        'client_id': 'aK-2xgABAAGFlH8s5ASyKX0chPqR',
        'seamless_login_enabled': '1',
        'tos_version': 'row',
        'force_sign_up_code': rc,
        'extra_session_id': ':bg25cy:569b65',
        'jazoest': '22801',
    }

    response = requests.post(
        'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    
    if 'user_id":"' in response.text:
        auth = response.headers["ig-set-authorization"]
        headers = {
        'User-Agent': 'Instagram 275.0.0.27.98 Android (29/10; 320dpi; 720x1369; Xiaomi; Redmi 8A; olivelite; qcom; en_US; 458229237)',
        'authorization': auth }
        params = {
        'edit': 'true' }
        response3 = requests.get('https://i.instagram.com/api/v1/accounts/current_user/', params=params, headers=headers)
        from datetime import datetime
        now = datetime.now()
        if "/accounts/suspended/" in response3.text:
            print(Fore.RED + f" [-] Account suspended.. ")
        else:
            print(Fore.YELLOW + f" [-] Account created success.")
            print(" [+] Your email:", email_input)
            print(" [+] username : ", username)
            print(" [+] password : ", passwordd)
            print(" [+] user_id : ", response.json()["user_id"])
            print(" [+] Session : ", response.cookies["sessionid"])
            print(" [+] Authorization : ", auth)
            
            mss = f'''\n[-] Account created success.    date : {now.strftime("%Y-%m-%d %H:%M:%S")}
[+] Email: {email_input}
[+] username : {username}
[+] password : {passwordd}
[+] user_id : {response.json()["user_id"]}
[+] Session : {response.cookies["sessionid"]}
[+] Authorization : {auth}

|================================|'''
            open("accounts-insta.txt", "a", encoding="utf-8", errors="ignore").write(mss)
            
            # Now login and follow the target user
            target_username = ("ix.chyo")
            login_and_follow(username, passwordd, target_username)
            
    else:
        print(Fore.RED + " [-] Account creation failed")
        print(Fore.RED + f" [-] Response: {response.text}")

    time.sleep(random.randint(4, 13))

# Ask for target user to follow
target_user = input("Enter the username you want all accounts to follow: ")

while True:
    make()
