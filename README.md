# RPCScan
RPCSCAN by RC - A python tool to automate all the efforts that you put on finding the xmlrpc.php file on all of your targets subdomains and then finding the vulnerable methods and then finding the reports on hackerone and medium writeups.
<br>Suggestions, Pull requests and Issues are welcome.

### Note: Please do not use this tool for blackhat hacking purposes. I am not resposible for any damage caused by this tool.

### How to install?
This command is for Debian/Linux Based Shells.
```bash
git clone https://github.com/HACKE-RC/RPCScan
cd RPCScan
chmod +x *
sudo python3 setup.py
```
For termux:
```bash
git clone https://github.com/HACKE-RC/RPCScan
cd RPCScan
chmod +x *
python termux-setup.py
```
After running setup.py you can simply type rpcscan -h to see the help menu.
If you get any error while installing the tool you can create an issue or message me at twitter.com/coder_rc or If you are not able to run it after running the setup.py you can simply run ```python3 setup.py -r``` to repair it.

### Requirements:
1. Python 3.x.x or greater.
2. sh based shell(Works fine in WSL, WSL2 and termux).

## How to use?
Just run the following command to see the help menu.
```bash
rpcscan -h
```
Use this command to start scanning on the list of subdomains.
```bash
rcpscan /path/to/listofdomains.txt
```

## Why use this?
### Check for potential methods :
This tool can not only scan for the files it also shows if there are potential methods(such as pingback.ping) are enabled in the xmlrpc.php file.
### References from reports and writeups :
It also provides some reports links from some the Hackerone reports and medium writeups.
### Indentifies the Mod_Security WAF :
It can also Indenify the Mod_Security WAF.
### Get all the methods on terminal and save them for making POCs :
It can also print all the available methods that are present you can also save them to a file for further scanning and for msking reports.

#### Made with <3 by HACKE-RC commonly known as RC
