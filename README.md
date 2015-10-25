# The needs-restart program

This is a brief program that helps you detect which services on your
system need to be restarted after an upgrade or redeploy of your
software.

Here is some example output:

    [root@machine root]# needs-restart
    * unit: (no unit)
      * PID: 1
        command: /usr/lib/systemd/systemd --switched-root --system...
        * /usr/lib64/libpcre.so.1.2.5 changed inode from 5305 to 5364
    * unit: systemd-journald.service
      * PID: 257
        command: /usr/lib/systemd/systemd-journald 
        * /usr/lib64/libpcre.so.1.2.5 changed inode from 5305 to 5364
    * unit: systemd-udevd.service
      * PID: 281
        command: /usr/lib/systemd/systemd-udevd 
        * /usr/lib64/libpcre.so.1.2.5 changed inode from 5305 to 5364
    * unit: auditd.service
      * PID: 318
        command: /sbin/auditd -n 
        * /usr/lib64/libpcre.so.1.2.5 changed inode from 5305 to 5364
    * unit: icecast.service
      * PID: 336
        command: /usr/bin/icecast -c /etc/icecast.xml 
        * /usr/lib64/libpcre.so.1.2.5 changed inode from 5305 to 5364
        * /usr/lib64/libnss3.so changed inode from 3183 to 4236
        * /usr/lib64/libsmime3.so changed inode from 17534 to 4257
        * /usr/lib64/libssl3.so changed inode from 17535 to 4259
    * unit: systemd-logind.service
      * PID: 340
        command: /usr/lib/systemd/systemd-logind 
        * /usr/lib64/libpcre.so.1.2.5 changed inode from 5305 to 5364
    * unit: dbus.service
      * PID: 343
        command: /usr/bin/dbus-daemon --system --address=systemd: ...
        * /usr/lib64/libelf-0.163.so changed inode from 109 to 6302
        * /usr/lib64/libpcre.so.1.2.5 changed inode from 5305 to 5364
        * /usr/lib64/libdw-0.163.so changed inode from 17296 to 17286
