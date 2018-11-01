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



2018.10.30
1. 那么命令别名与变量有什么不同呢？命令别名是『新创一个新的命令， 你可以直接下达该命令』的，至于变量则需要使用类似『 echo 』命令才能够呼叫出变量的内容！

2. 如果你要查询隐藏档，并且需要长的列出与一页一页翻看，那么需要下达『 ls -al | more 』这个命令

3. 基本上 history 的用途很大的！但是需要小心安全的问题！尤其是 root 的历史纪录文件，这是 Cracker 的最爱！因为不小心的 root 会将很多的重要数据在运行的过程中会被纪录在 ~/.bash_history 当中，如果这个文件被解析的话，后果不堪吶！无论如何，使用 history 配合『 ! 』曾经使用过的命令下达是很有效率的一个命令下达方法！

4. 如果一个命令 (例如 ls) 被下达时， 到底是哪一个 ls 被拿来运行？很有趣吧！基本上，命令运行的顺序可以这样看：

1) 以相对/绝对路径运行命令，例如『 /bin/ls 』或『 ./ls 』；
2) 由 alias 找到该命令来运行；
3) 由 bash 内建的 (builtin) 命令来运行；
4) 透过 $PATH 这个变量的顺序搜寻到的第一个命令来运行。

5. 如果想要了解命令搜寻的顺序，其实透过 type -a ls 也可以查询的到啦！

6. 你要注意的是，除了 /etc/issue 之外还有个 /etc/issue.net 呢！这是啥？这个是提供给 telnet 这个远程登录程序用的。 当我们使用 telnet 连接到主机时，主机的登陆画面就会显示 /etc/issue.net 而不是 /etc/issue 呢！

至于如果您想要让使用者登陆后取得一些信息，例如您想要让大家都知道的信息， 那么可以将信息加入 /etc/motd 里面去！

7. 其他相关配置文件
/etc/man.config
~/.bash_history
~/.bash_logout

8. 
eof   : End of file 的意思，代表『结束输入』。
erase : 向后删除字符，
intr  : 送出一个 interrupt (中断) 的讯号给目前正在 run 的程序；
kill  : 删除在目前命令列上的所有文字；
quit  : 送出一个 quit 的讯号给目前正在 run 的程序；
start : 在某个程序停止后，重新启动他的 output
stop  : 停止目前屏幕的输出；
susp  : 送出一个 terminal stop 的讯号给正在 run 的程序。

9. 符号  内容
#   批注符号：这个最常被使用在 script 当中，视为说明！在后的数据均不运行
\   跳脱符号：将『特殊字符或通配符』还原成一般字符
|   管线 (pipe)：分隔两个管线命令的界定(后两节介绍)；
;   连续命令下达分隔符：连续性命令的界定 (注意！与管线命令并不相同)
~   用户的家目录
$   取用变量前导符：亦即是变量之前需要加的变量取代值
&   工作控制 (job control)：将命令变成背景下工作
!   逻辑运算意义上的『非』 not 的意思！
/   目录符号：路径分隔的符号
>, >>   数据流重导向：输出导向，分别是『取代』与『累加』
<, <<   数据流重导向：输入导向 (这两个留待下节介绍)
' ' 单引号，不具有变量置换的功能
" " 具有变量置换的功能！
` ` 两个『 ` 』中间为可以先运行的命令，亦可使用 $( )
( ) 在中间为子 shell 的起始与结束
{ } 在中间为命令区块的组合！

2018.10.31
1. 数据流重导向可以将 standard output (简称 stdout) 与 standard error output (简称 stderr) 分别传送到其他的文件或装置去，而分别传送所用的特殊字符则如下所示：

标准输入　　(stdin) ：代码为 0 ，使用 < 或 << ；
标准输出　　(stdout)：代码为 1 ，使用 > 或 >> ；
标准错误输出(stderr)：代码为 2 ，使用 2> 或 2>> ；

2. 运行『 find /home -name .bashrc > list 』 会有什么结果？呵呵，你会发现 list 里面存了刚刚那个『正确』的输出数据， 至于屏幕上还是会有错误的信息出现呢！伤脑筋！如果想要将正确的与错误的数据分别存入不同的文件中需要怎么做？

范例三：承范例二，将 stdout 与 stderr 分存到不同的文件去
[dmtsai@www ~]$ find /home -name .bashrc > list_right 2> list_error

3. 屏幕输出的信息很重要，而且我们需要将他存下来的时候；
背景运行中的程序，不希望他干扰屏幕正常的输出结果时；
一些系统的例行命令 (例如写在 /etc/crontab 中的文件) 的运行结果，希望他可以存下来时；
一些运行命令的可能已知错误信息时，想以『 2> /dev/null 』将他丢掉时；
错误信息与正确信息需要分别输出时。

4. 在命令与命令中间利用分号 (;) 来隔开，这样一来，分号前的命令运行完后就会立刻接着运行后面的命令了。 这真是方便啊～

5.
范例三：我不清楚 /tmp/abc 是否存在，但就是要创建 /tmp/abc/hehe 文件
[root@www ~]# ls /tmp/abc || mkdir /tmp/abc && touch /tmp/abc/hehe
上面这个范例三总是会创建 /tmp/abc/hehe 的喔！不论 /tmp/abc 是否存在。那么范例三应该如何解释呢？ 由于Linux 底下的命令都是由左往右运行的

6.
由于命令是一个接着一个去运行的，因此，如果真要使用判断， 那么这个 && 与 || 的顺序就不能搞错。一般来说，假设判断式有三个，也就是：

command1 && command2 || command3


7. Pipe:
这个管线命令『 | 』仅能处理经由前面一个命令传来的正确信息，也就是 standard output 的信息，对于 stdandard error 并没有直接处理的能力

管线命令仅会处理 standard output，对于 standard error output 会予以忽略
管线命令必须要能够接受来自前一个命令的数据成为 standard input 继续处理才行。

8. cut 
主要的用途在于将『同一行里面的数据进行分解！』最常使用在分析一些数据或文字数据的时候！ 这是因为有时候我们会以某些字符当作分割的参数，然后来将数据加以切割，以取得我们所需要的数据。 鸟哥也很常使用这个功能呢！尤其是在分析 log 文件的时候！不过，cut 在处理多空格相连的数据时，可能会比较吃力一点

9. grep
 grep 可以解析一行文字，取得关键词，若该行有存在关键词，就会整行列出来！

范例二：承上题，如果我还想要知道每个人的登陆总次数呢？
[root@www ~]# last | cut -d ' ' -f1 | sort | uniq -c
      1
     12 reboot
     41 root
      1 wtmp
# 从上面的结果可以发现 reboot 有 12 次， root 登陆则有 41 次！
# wtmp 与第一行的空白都是 last 的默认字符，那两个可以忽略的！

10.  Windows 操作系统下，你要将文件分割需要如何作？伤脑筋吧！在 Linux 底下就简单的多了！你要将文件分割的话，那么就使用 -b size 来将一个分割的文件限制其大小，如果是行数的话，那么就使用 -l line 来分割！


11. 在管线命令当中，常常会使用到前一个命令的 stdout 作为这次的 stdin ， 某些命令需要用到文件名 (例如 tar) 来进行处理时，该 stdin 与 stdout 可以利用减号 "-" 来替代， 举例来说：
[root@www ~]# tar -cvf - /home | tar -xvf -
上面这个例子是说：『我将 /home 里面的文件给他打包，但打包的数据不是纪录到文件，而是传送到 stdout； 经过管线后，将 tar -cvf - /home 传送给后面的 tar -xvf - 』。后面的这个 - 则是取用前一个命令的 stdout， 因此，我们就不需要使用 file 了！这是很常见的例子喔！注意注意！
