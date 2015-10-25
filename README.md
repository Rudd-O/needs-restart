The needs-restart program
=========================

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

Here is some example output in bare mode (`-b`):

    [root@machine root]# needs-restart -b
    systemd-journald.service
    systemd-udevd.service
    auditd.service
    icecast.service
    systemd-logind.service
    dbus.service

Features and options
--------------------

The online help explains:

    [user@machine needs-restart]$ ./needs-restart --help
    usage: needs-restart [-h] [-b] [-s] [-i PATH_PREFIX]

    Show services in need of restart and processes keeping files open that were
    deleted or updated since they were opened by those processes.

    optional arguments:
      -h, --help      show this help message and exit
      -b              bare form – only list the units that need restarting
      -s              only list system units – ignore user and session ones
      -i PATH_PREFIX  ignore deleted / modified mmap()ed path(s) starting with
                      this prefix; you can specify this parameter multiple times

Building and installing
-----------------------

You can run this program directly from the directory you cloned it into.

You can also install it as an RPM.  Simply type the following command
in the directory you cloned it into:

    python setup.py bdist_rpm

Source RPM and installable architecture-independent RPM will appear in
`dist/`.  You can install the architecture-independent RPM on your system now.
