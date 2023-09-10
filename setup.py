import os, time
os.system("sudo apt install samba")
config = open("/etc/samba/smb.conf")
config.append("\n\n[RAS]\ncomment = RAS file share (github/benpi88)\n    path = /srv/samba/ras\n    browsable = yes\n    guest ok = yes\n    read only = no")
config.close()
os.system("sudo mkdir -p /srv/samba/ras && sudo chown nobody:nogroup /srv/samba/ras/ && sudo systemctl restart smbd.service nmbd.service")
print("Done! Rebooting in 15 seconds...")
i = 0
while not i == 15:
  i += 1
  time.sleep(1)
os.system("shutdown -r --now")
