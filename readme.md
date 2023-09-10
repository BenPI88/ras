# RAS (Remote Access Software)
## How to install

 1. Open your terminal to the `~` directory.
 2. Clone the GitHub repo with `git clone https://github.com/BenPI88/ras`
 3. Go into the repo with `cd ras`
 4. Run the setup script with `sudo python3 setup.py`
 5. After restarting, copy the server program to the file server with `cp ras/server.py /srv/samba/ras/`
 6. Go to the file share with `cd /srv/samba/ras`
 7. Run the server with `python3 server.py`
 8. On another computer, navigate to the file browser and click `Other Locations`
 9. Click the hostname of the server.
 10.  Sign in with root.
 11. Add a file named `shellcode.sh` and in the file, write code that you want to be executed.
 12. In a web browser, navigate to `http://<hostname>.local:5000` and watch your code execute. Of course changing `hostname` to whatever your hostname is.

> Written with [StackEdit](https://stackedit.io/).
