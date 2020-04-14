# CheatSheet

## Linux

`sudo !!` - Redo same command as `sudo`

`(any command)` - Leading space will not put it into history

`cat file | tee -a log | cat > /dev/null` - Here `tee` intercepts into pipe and logs what was streamed

Notable or unobvious linux dirs:

- `/bin` - Executbles of all users
- `/dev` - Devices
- `/etc` - Configuration files
- `/opt` - Various software
- `/root` - Homedir of root user
- `/tmp` - Tmp files, will be wiped out after reboot
- `/usr` - Mini file-system, which overrides for user
- `/var` - Mostly log files

What process is listening on which port:

`sudo netstat -tulpn`

Stop and remove all docker containers:

`docker stop $(docker ps -a -q)` and then `docker rm $(docker ps -a -q)`
