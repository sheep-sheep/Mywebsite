2018.10.08 Monday

1. 在Linux系统中，每个装置都被当成一个文件来对待
2. /dev means device
3. Storage: IDE; SATA, the devices filenames are decided by the system(SATA) or by Primary or Secondary order(IDE)

4. Storage Disk
主要启动记录区(Master Boot Record, MBR)：可以安装启动管理程序的地方，有446 bytes
分割表(partition table)：记录整颗硬盘分割的状态，有64 bytes

5. TTY Definition:
Teletypewriter originally and now also means any terminal on Linux/Unix systems. It also means any serial port on Unix/Linux systems.

6.
P1:/dev/hda1
P2:/dev/hda2
L1:/dev/hda5
L2:/dev/hda6
L3:/dev/hda7
L4:/dev/hda8
L5:/dev/hda9
仔细看看，怎么装置档名没有/dev/hda3与/dev/hda4呢？因为前面四个号码都是保留给Primary或Extended用的嘛！ 所以逻辑分割槽的装置名称号码就由5号开始了！

7. 在Linux系统中，IDE硬盘最多有59个逻辑分割(5号到63号)， SATA硬盘则有11个逻辑分割(5号到15号)。

8. BIOS(Basic Input/Output System)就是在启动的时候，计算机系统会主动运行的第一个程序

9. Why deos MBR only have MBR仅有446 bytes?

10. (1)启动需要启动管理程序， 而(2)启动管理程序可以安装在MBR及Boot Sector两处

11. Mount
所谓的『挂载』就是利用一个目录当成进入点，将磁盘分区槽的数据放置在该目录下； 也就是说，进入该目录就可以读取该分割槽

12. Common Services on Linux
DHCP: Dynamic Host Configuration Protocol
Mail
WWW
Proxy
FTP
NAT: Network address translation (NAT) is a method of remapping one IP address space into another by modifying network address information in the IP header of packets while they are in transit across a traffic routing device.


13. old CPU在进行安装的时候，规划出三个磁区，分别是：
/boot
/
swap

14. 
在Linux默认的登陆模式中，主要分为两种，一种是仅有纯文本接口(所谓的运行等级run level 3)的登陆环境，在这种环境中你可以有tty1~tty6的终端界面，但是并没有图形窗口接口的环境喔。 另一种则是图形接口的登陆环境(所谓的运行等级run level 5)，这也是我们第四章安装妥当后的默认环境！ 在这个环境中你就具有tty1~tty7了！其中的tty7就是启动完成后的默认等待登陆的图形环境！

15. 
那个 ~ 符号代表的是『用户的家目录』的意思，他是个『变量！』 这相关的意义我们会在后续的章节依序介绍到。举例来说，root的家目录在/root， 所以 ~ 就代表/root的意思。而vbird的家目录在/home/vbird， 所以如果你以vbird登陆时，他看到的 ~ 就会等于/home/vbird喔！

至于提示字符方面，在Linux当中，默认root的提示字符为 # ，而一般身份用户的提示字符为 $ 。

还有，上面的第一、第二行的内容其实是来自于/etc/issue这个文件喔！


16. It can have many shell programs and Bash it one of them for Linux.

2018.10.09 Tuesday
1. 第一个被输入的数据绝对是命令或者是可运行的文件

2. Amazed by: cal, date, bc

3. Hotkeys:
发现什么事？所有以ca为开头的命令都被显示出来啦！很不错吧！那如果你输入『ls -al ~/.bash』再加两个[tab]会出现什么
[Tab] 接在一串命令的第一个字的后面，则为命令补全；
[Tab] 接在一串命令的第二个字以后时，则为『文件补齐』！

4. 

**1   使用者在shell环境中可以操作的命令或可运行文件**
2   系统核心可呼叫的函数与工具等
3   一些常用的函数(function)与函式库(library)，大部分为C的函式库(libc)
4   装置文件的说明，通常在/dev下的文件
**5   配置文件或者是某些文件的格式**
6   游戏(games)
7   惯例与协议等，例如Linux文件系统、网络协议、ASCII code等等的说明
**8   系统管理员可用的管理命令**
9   跟kernel有关的文件


5. path symbols:
./config
../config,
2018.10.10 Wednesday

1. man man
2. info info
3. nano
4. shutdown, reboot
5. drwxrwxrwx, 777
6. chgrp, chmod, chown
7. FHS标准建议：根目录(/)所在分割槽应该越小越好， 且应用程序所安装的软件最好不要与根目录放在同一个分割槽内，保持根目录越小越好。 如此不但效能较佳，根目录所在的文件系统也较不容易发生问题

FHS Definition:
/ (root, 根目录)：与开机系统有关；
/usr (unix software resource)：与软件安装/执行有关；
/var (variable)：与系统运作过程有关。

Besides above 3 main folders:
/boot:  这个目录主要在放置开机会使用到的文件，包括Linux核心文件以及开机选单与开机所需配置文件等等。 Linux kernel常用的档名为：vmlinuz (与开机相关的还有Grub)
/bin:   /bin放置的是在单人维护模式下还能够被操作的指令
/dev:   装置与接口设备都是以文件的型态存在于这个目录当中
/etc:   系统主要的配置文件几乎都放置在这个目录内，例如人员的账号密码文件、 各种服务的启始档
/sbin:  放在/sbin底下的为开机过程中所需要的，里面包括了开机、修复、还原系统所需要的指令

/lib:   放置的则是在开机时会用到的函式库， 以及在/bin或/sbin底下的指令会呼叫的函式库
/home:  系统默认的用户家目录(home directory)
/opt:   第三方协力软件放置的目录
/root:  系统管理员(root)的家目录
/srv:   service 数据
/tmp:   使用者或者是正在执行的程序暂时放置文件的地方
/proc:  本身是一个『虚拟文件系统(virtual filesystem)』喔！他放置的数据都是在内存当中， 例如系统核心、行程信息(process)、周边装置的状态及网络状态

8. 
/usr:   安装时占用大量空间
/var：   系统执行时逐渐占用空间

9.
网络文件常常提到类似『./run.sh』之类的数据，这个指令的意义为何？
答：
由于指令的执行需要变量(bash章节才会提到)的支持，若你的执行文件放置在本目录，并且本目录并非正规的执行文件目录(/bin, /usr/bin等为正规)，此时要执行指令就得要严格指定该执行档。『./』代表『本目录』的意思，所以『./run.sh』代表『执行本目录下， 名为run.sh的文件

10. 相对路径与绝对路径

11. 目录的相关操作
.         代表此层目录
..        代表上一层目录
-         代表前一个工作目录
~         代表『目前使用者身份』所在的家目录
~account  代表 account 这个使用者的家目录(account是个帐号名称)

cd：变换目录(Change Directory)
pwd：显示目前的目录(Print Working Directory)
mkdir：创建一个新的目录
rmdir：删除一个空的目录