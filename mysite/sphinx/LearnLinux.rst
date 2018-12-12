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
 需要说明的是『grep 在数据中查寻一个字串时，是以 "整行" 为单位来进行数据的撷取的！』也就是说，假如一个文件内有 10 行，其中有两行具有你所搜寻的字串，则将那两行显示在萤幕上，其他的就丢弃了！


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


Regular Expression:
1. 利用中括号 [] 来搜寻集合字节
[root@www ~]# grep -n 't[ae]st' regular_express.txt
2. 如果 oo 前面有 g 的话呢？此时，可以利用在集合字节的反向选择 [^]
3. 行首与行尾字节 ^ $
4. 注意到了吧？那个 ^ 符号，在字节集合符号(括号[])之内与之外是不同的！ 在 [] 内代表『反向选择』，在 [] 之外则代表定位在行首的意义！
5. 任意一个字节 . 与重复字节 *
『g.*g』的作法，因为 * 可以是 0 或多个重复前面的字符，而 . 是任意字节，所以： 『.* 就代表零个或多个任意字节』的意思啦

你以为 sed 只有这样的能耐吗？那可不！ sed 甚至可以直接修改文件的内容呢！而不必使用管线命令或数据流重导向！ 不过，由於这个动作会直接修改到原始的文件，所以请你千万不要随便拿系统配置档来测试喔！ 我们还是使用你下载的 regular_express.txt 文件来测试看看吧



2018.11.01 Thursday

1.      Printf
2.      Awk
awk 也是一个非常棒的数据处理工具！相较於 sed 常常作用於一整个行的处理， awk 则比较倾向於一行当中分成数个『栏位』来处理。因此，awk 相当的适合处理小型的数据数据处理呢！awk 通常运行的模式是这样的：

[root@www ~]# awk '条件类型1{动作1} 条件类型2{动作2} ...' filename

整个 awk 的处理流程是：

    1.     读入第一行，并将第一行的数据填入 $0, $1, $2.... 等变量当中；
    2.     依据 "条件类型" 的限制，判断是否需要进行后面的 "动作"；
    3.     做完所有的动作与条件类型；
    4.     若还有后续的『行』的数据，则重复上面 1~3 的步骤，直到所有的数据都读完为止

3. diff 主要是以『行』为单位比对， cmp 则是以『位组』为单位去比对，这并不相同！


Shell scripts

1.  建议你一定要养成良好的 script 撰写习惯，在每个 script 的档头处记录好：
·        script 的功能；
·        script 的版本资讯；
·        script 的作者与联络方式；
·        script 的版权宣告方式；
·        script 的 History (历史纪录)；
·        script 内较特殊的命令，使用『绝对路径』的方式来下达；
·        script 运行时需要的环境变量预先宣告与配置。

除了记录这些资讯之外，在较为特殊的程序码部分，个人建议务必要加上注解说明，可以帮助你非常非常多！ 此外，程序码的撰写最好使用巢状方式，在包覆的内部程序码最好能以 [tab] 按键的空格向后推， 这样你的程序码会显的非常的漂亮与有条理！

2.  基本上，鸟哥比较建议使用这样的方式来进行运算：

var=$((运算内容))

不但容易记忆，而且也比较方便的多，因为两个小括号内可以加上空白字节喔！ 未来你可以使用这种方式来计算的呀！至於数值运算上的处理，则有：『 +, -, *, /, % 』等等。 那个 % 是取余数啦～

3.  直接命令下达 (不论是绝对路径/相对路径还是 $PATH 内)，或者是利用 bash (或 sh) 来下达脚本时， 该 script 都会使用一个新的 bash 环境来运行脚本内的命令！也就是说，使用者种运行方式时， 其实 script 是在子程序的 bash 内运行的！我们在第十一章 BASH 内谈到 export 的功能时，曾经就父程序/子程序谈过一些概念性的问题， 重点在於：『当子程序完成后，在子程序内的各项变量或动作将会结束而不会传回到父程序中』


4.  因为 source 对 script 的运行方式可以使用底下的图示来说明！ sh02.sh 会在父程序中运行的，因此各项动作都会在原本的 bash 内生效！这也是为啥你不注销系统而要让某些写入 ~/.bashrc 的配置生效时，需要使用『 source ~/.bashrc 』而不能使用『 bash ~/.bashrc 』是一样的啊！


5.  IF ELSE

整个程序的撰写可以是这样的：
[root@www scripts]# vi sh09.sh
#!/bin/bash
# Program:
#             Check $1 is equal to "hello"
# History:
# 2005/08/28      VBird     First release
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH
if [ "$1" == "hello" ]; then
                echo "Hello, how are you ?"
elif [ "$1" == "" ]; then
                echo "You MUST input parameters, ex> {$0 someword}"
else
                echo "The only parameter is 'hello', ex> {$0 hello}"
fi

6.  可以利用『 netstat -tuln』来取得目前主机有启动的服务
几个常见的 port 与相关网络服务的关系是：

·        80: WWW
·        22: ssh
·        21: ftp
·        25: mail
·        111: RPC(远程程序呼叫)
·        631: CUPS(列印服务功能)

4.1 利用 if .... then： 单层简单条件, 多重复杂条件, 检验$1内容, 网络状态, 退伍
4.2 利用 case ..... esac 判断
4.3 利用 function 功能


head -n 4 /etc/passwd

1.  每一个文件都具有『拥有人与拥有群组』的属性吗？没错啦～每个登陆的使用者至少都会取得两个 ID ，一个是使用者 ID (User ID ，简称 UID)、一个是群组 ID (Group ID ，简称 GID)。

那么文件如何判别他的拥有者与群组呢？其实就是利用 UID 与 GID 啦！每一个文件都会有所谓的拥有者 ID 与拥有群组 ID ，当我们有要显示文件属性的需求时，系统会依据 /etc/passwd 与 /etc/group 的内容， 找到 UID / GID 对应的账号与组名再显示出来！

先找寻 /etc/passwd 里面是否有你输入的账号？如果没有则跳出，如果有的话则将该账号对应的 UID 与 GID (在 /etc/group 中) 读出来，另外，该账号的家目录与 shell 配置也一并读出；
再来则是核对口令表啦！这时 Linux 会进入 /etc/shadow 里面找出对应的账号与 UID，然后核对一下你刚刚输入的口令与里头的口令是否相符？

如果一切都 OK 的话，就进入 Shell 控管的阶段啰！

3.  UID
0
(系统管理员)

当 UID 是 0 时，代表这个账号是『系统管理员』！ 所以当你要让其他的账号名称也具有 root 的权限时，将该账号的 UID 改为 0 即可。 这也就是说，一部系统上面的系统管理员不见得只有 root 喔！ 不过，很不建议有多个账号的 UID 是 0 啦～

1~99：由 distributions 自行创建的系统账号；
100~499：若用户有系统账号需求时，可以使用的账号 UID

一般用户的口令忘记了：这个最容易解决，请系统管理员帮忙， 他会重新配置好你的口令而不需要知道你的旧口令！利用 root 的身份使用 passwd 命令来处理即可。
root 口令忘记了：这就麻烦了！因为你无法使用 root 的身份登陆了嘛！ 但我们知道 root 的口令在 /etc/shadow 当中，因此你可以使用各种可行的方法启动进入 Linux 再去修改。 例如重新启动进入单人维护模式(第二十章)后，系统会主动的给予 root 权限的 bash 接口， 此时再以 passwd 修改口令即可；或以 Live CD 启动后挂载根目录去修改 /etc/shadow，将里面的 root 的口令字段清空， 再重新启动后 root 将不用口令即可登陆！登陆后再赶快以 passwd 命令去配置 root 口令即可。

 
2018.11.03 Sat
1.
但是 sudo 默认仅有 root 能使用啊！为什么呢？因为 sudo 的运行是这样的流程：

当用户运行 sudo 时，系统于 /etc/sudoers 文件中搜寻该使用者是否有运行 sudo 的权限；
若使用者具有可运行 sudo 的权限后，便让使用者『输入用户自己的口令』来确认；
若口令输入成功，便开始进行 sudo 后续接的命令(但 root 运行 sudo 时，不需要输入口令)；
若欲切换的身份与运行者身份相同，那也不需要输入口令。
所以说，sudo 运行的重点是：『能否使用 sudo 必须要看 /etc/sudoers 的配置值， 而可使用 sudo 者是透过输入用户自己的口令来运行后续的命令串』喔！由于能否使用与 /etc/sudoers 有关， 所以我们当然要去编辑 sudoers 文件啦！不过，因为该文件的内容是有一定的规范的，因此直接使用 vi 去编辑是不好的。 此时，我们得要透过 visudo 去修改这个文件喔！

2.

很多时候我们需要大量运行很多 root 的工作，所以一直使用 sudo 觉得很烦ㄟ！那有没有办法使用 sudo 搭配 su ， 一口气将身份转为 root ，而且还用用户自己的口令来变成 root 呢？是有的！而且方法简单的会让你想笑！ 我们创建一个 ADMINS 帐户别名，然后这样做：
[root@www ~]# visudo
User_Alias  ADMINS = pro1, pro2, pro3, myuser1
ADMINS ALL=(root)  /bin/su -
接下来，上述的 pro1, pro2, pro3, myuser1 这四个人，只要输入『 sudo su - 』并且输入『自己的口令』后， 立刻变成 root 的身份！不但 root 口令不会外流，用户的管理也变的非常方便！ 这也是实务上面多人共管一部主机时常常使用的技巧呢！这样管理确实方便，不过还是要强调一下大前提， 那就是『这些你加入的使用者，全部都是你能够信任的用户』！

3.
这玩意儿的 shell 就是使用 /sbin/nologin ，重点在于系统账号是不需要登陆的！所以我们就给他这个无法登陆的合法 shell。 使用了这个 shell 的用户即使有了口令，你想要登陆时他也无法登陆，因为会出现如下的信息喔：

This account is currently not available.
我们所谓的『无法登陆』指的仅是：『这个使用者无法使用 bash 或其他 shell 来登陆系统』而已， 并不是说这个账号就无法使用其他的系统资源喔！ 举例来说，各个系统账号，打印作业由 lp 这个账号在管理， WWW 服务由 apache 这个账号在管理， 他们都可以进行系统程序的工作，但是『就是无法登陆主机』而已啦

4.


[vbird1@www ~]$ write root
write: root has messages disabled
了解乎？如果想要解开的话，再次下达『 mesg y 』就好啦！想要知道目前的 mesg 状态，直接下达『 mesg 』即可！瞭呼？ 相对于 write 是仅针对一个使用者来传『简讯』，我们还可以『对所有系统上面的用户传送简讯 (广播)』哩～ 如何下达？用 wall 即可啊！他的语法也是很简单的喔！

[root@www ~]# wall "I will shutdown my linux server..."
然后你就会发现所有的人都会收到这个简讯呢！


2018.11.04 Sun
1. 程序与程序作个总结：

程序 (program)：通常为 binary program ，放置在储存媒体中 (如硬盘、光盘、软盘、磁带等)， 为实体文件的型态存在；

程序 (process)：程序被触发后，运行者的权限与属性、程序的程序码与所需数据等都会被加载内存中， 操作系统并给予这个内存内的单元一个识别码 (PID)，可以说，程序就是一个正在运行中的程序。

2. 『咦！明明我将有问题的程序关闭了，怎么过一阵子他又自动的产生？ 而且新产生的那个程序的 PID 与原先的还不一样，这是怎么回事呢？』不要怀疑，如果不是 crontab 工作排程的影响，肯定有一支父程序存在，所以你杀掉子程序后， 父程序就会主动再生一支！那怎么办？正所谓这：『擒贼先擒王』，找出那支父程序，然后将他删除就对啦！

3. (1)系统先以 fork 的方式复制一个与父程序相同的缓存程序，这个程序与父程序唯一的差别就是 PID 不同！ 但是这个缓存程序还会多一个 PPID 的参数，PPID 如前所述，就是父程序的程序识别码啦！然后(2)缓存程序开始以 exec 的方式加载实际要运行的程序，以上述图示来讲，新的程序名称为 qqq ，最终子程序的程序码就会变成 qqq 了

4. 常驻在内存当中的程序通常都是负责一些系统所提供的功能以服务使用者各项任务，因此这些常驻程序就会被我们称为：服务 (daemon)。系统的服务非常的多， 不过主要大致分成系统本身所需要的服务，例如刚刚提到的 crond 及 atd ，还有 syslog 等等的。还有一些则是负责网络连线的服务

5. 那么如果我在 Linux 下以文字界面登陆，在萤幕当中显示错误信息后就挂了～动都不能动，该如何是好！？ 这个时候那默认的七个窗口就帮上忙啦！你可以随意的再按 [Alt]+[F1].....[F7] 来切换到其他的终端机界面，然后以 ps -aux 找出刚刚的错误程序，然后给他 kill 一下，哈哈，回到刚刚的终端机界面！恩～棒！又回复正常罗！
多人多工的系统资源分配问题考虑：
多人多工确实有很多的好处，但其实也有管理上的困扰，因为使用者越来越多， 将导致你管理上的困扰哩！另外，由於使用者日盛，当使用者达到一定的人数后， 通常你的机器便需要升级了，因为 CPU 的运算与 RAM 的大小可能就会不敷使用！

6. Job Control
总之，要进行 bash 的 job control 必须要注意到的限制是：

这些工作所触发的程序必须来自於你 shell 的子程序(只管理自己的 bash)；
前景：你可以控制与下达命令的这个环境称为前景的工作 (foreground)；
背景：可以自行运行的工作，你无法使用 [ctrl]+c 终止他，可使用 bg/fg 呼叫该工作；
背景中『运行』的程序不能等待 terminal/shell 的输入(input)

让工作在背景下的状态变成运行中： bg
我们刚刚提到，那个 [ctrl]-z 可以将目前的工作丢到背景底下去『暂停』， 那么如何让一个工作在背景底下『 Run 』呢？我们可以在底下这个案例当中来测试！ 注意喔！底下的测试要进行的快一点！^_^

范例一：一运行 find / -perm +7000 > /tmp/text.txt 后，立刻丢到背景去暂停！
[root@www ~]# find / -perm +7000 > /tmp/text.txt
# 此时，请立刻按下 [ctrl]-z 暂停！
[3]+  Stopped                 find / -perm +7000 > /tmp/text.txt

范例二：让该工作在背景下进行，并且观察他！！
[root@www ~]# jobs ; bg %3 ; jobs
[1]-  Stopped                 vim ~/.bashrc
[2]   Stopped                 find / -print
[3]+  Stopped                 find / -perm +7000 > /tmp/text.txt
[3]+ find / -perm +7000 > /tmp/text.txt &  <==用 bg%3 的情况！
[1]+  Stopped                 vim ~/.bashrc
[2]   Stopped                 find / -print
[3]-  Running                 find / -perm +7000 > /tmp/text.txt &

kill -l
特别留意一下， -9 这个 signal 通常是用在『强制删除一个不正常的工作』时所使用的， -15 则是以正常步骤结束一项工作(15也是默认值)，两者之间并不相同呦

所以，工作管理的背景依旧与终端机有关啦！ 在这样的情况下，如果你是以远程连线方式连接到你的 Linux 主机，并且将工作以 & 的方式放到背景去， 请问，在工作尚未结束的情况下你离线了，该工作还会继续进行吗？答案是『否』！不会继续进行，而是会被中断掉。

pstree -nh this is a really useful command to check processes.

7. Jobs Check
直接背两个比较不同的选项， 一个是只能查阅自己 bash 程序的『 ps -l 』一个则是可以查阅所有系统运行的程序『 ps aux 』

除此之外，我们必须要知道的是『僵尸 (zombie) 』程序是什么？ 通常，造成僵尸程序的成因是因为该程序应该已经运行完毕，或者是因故应该要终止了， 但是该程序的父程序却无法完整的将该程序结束掉，而造成那个程序一直存在内存当中。 如果你发现在某个程序的 CMD 后面还接上 <defunct> 时，就代表该程序是僵尸程序啦

事实上，通常僵尸程序都已经无法控管，而直接是交给 init 这支程序来负责了，偏偏 init 是系统第一支运行的程序， 他是所有程序的父程序！我们无法杀掉该程序的 (杀掉他，系统就死掉了！)，所以罗，如果产生僵尸程序， 而系统过一阵子还没有办法透过核心非经常性的特殊处理来将该程序删除时，那你只好透过 reboot 的方式来将该程序抹去了！

8. Top
默认的情况下，每次升级程序资源的时间为 5 秒，不过，可以使用 -d 来进行修改。 top 主要分为两个画面，上面的画面为整个系统的资源使用状态，基本上总共有六行，显示的内容依序是：

第一行(top...)：这一行显示的资讯分别为：
目前的时间，亦即是 17:03:09 那个项目；
启动到目前为止所经过的时间，亦即是 up 7days, 16:16 那个项目；
已经登陆系统的使用者人数，亦即是 1 user项目；
系统在 1, 5, 15 分钟的平均工作负载。我们在第十六章谈到的 batch 工作方式为负载小於 0.8 就是这个负载罗！代表的是 1, 5, 15 分钟，系统平均要负责运行几个程序(工作)的意思。 越小代表系统越闲置，若高於 1 得要注意你的系统程序是否太过繁复了！

第二行(Tasks...)：显示的是目前程序的总量与个别程序在什么状态(running, sleeping, stopped, zombie)。 比较需要注意的是最后的 zombie 那个数值，如果不是 0 ！好好看看到底是那个 process 变成僵尸了吧？

第三行(Cpus...)：显示的是 CPU 的整体负载，每个项目可使用 ? 查阅。需要特别注意的是 %wa ，那个项目代表的是 I/O wait， 通常你的系统会变慢都是 I/O 产生的问题比较大！因此这里得要注意这个项目耗用 CPU 的资源喔！ 另外，如果是多核心的设备，可以按下数字键『1』来切换成不同 CPU 的负载率。

第四行与第五行：表示目前的实体内存与虚拟内存 (Mem/Swap) 的使用情况。 再次重申，要注意的是 swap 的使用量要尽量的少！如果 swap 被用的很大量，表示系统的实体内存实在不足！

第六行：这个是当在 top 程序当中输入命令时，显示状态的地方。

看到不同处了吧？底线的地方就是修改了之后所产生的效果！一般来说，如果鸟哥想要找出最损耗 CPU 资源的那个程序时，大多使用的就是 top 这支程序啦！然后强制以 CPU 使用资源来排序 (在 top 当中按下 P 即可)， 就可以很快的知道啦！ ^_^。多多爱用这个好用的东西喔！


9. pstree
由 pstree 的输出我们也可以很清楚的知道，所有的程序都是依附在 init 这支程序底下的！ 仔细看一下，这支程序的 PID 是一号喔！因为他是由 Linux 核心所主动呼叫的第一支程序！所以 PID 就是一号了。 这也是我们刚刚提到僵尸程序时有提到，为啥发生僵尸程序需要重新启动？ 因为 init 要重新启动，而重新启动 init 就是 reboot 罗！

如果还想要知道 PID 与所属使用者，加上 -u 及 -p 两个参数即可。我们前面不是一直提到， 如果子程序挂点或者是老是砍不掉子程序时，该如何找到父程序吗？呵呵！用这个 pstree 就对了！ ^_^

kill -signal PID
kill 可以帮我们将这个 signal 传送给某个工作 (%jobnumber) 或者是某个 PID (直接输入数字)。 要再次强调的是： kill 后面直接加数字与加上 %number 的情况是不同的！ 这个很重要喔！因为工作控制中有 1 号工作，但是 PID 1 号则是专指『 init 』这支程序！你怎么可以将 init 关闭呢？ 关闭 init ，你的系统就当掉了啊！所以记得那个 % 是专门用在工作控制的喔！ 我们就活用一下 kill 与刚刚上面提到的 ps 来做个简单的练习吧

10. nice and priority
由於 PRI 是核心动态调整的，我们使用者也无权去干涉 PRI ！那如果你想要调整程序的优先运行序时，就得要透过 Nice 值了！Nice 值就是上表的 NI 啦！一般来说， PRI 与 NI 的相关性如下：

PRI(new) = PRI(old) + nice
不过你要特别留意到，如果原本的 PRI 是 50 ，并不是我们给予一个 nice = 5 ，就会让 PRI 变成 55 喔！ 因为 PRI 是系统『动态』决定的，所以，虽然 nice 值是可以影响 PRI ，不过， 最终的 PRI 仍是要经过系统分析后才会决定的。另外， nice 值是有正负的喔，而既然 PRI 越小越早被运行， 所以，当 nice 值为负值时，那么该程序就会降低 PRI 值，亦即会变的较优先被处理。此外，你必须要留意到：

nice 值可调整的范围为 -20 ~ 19 ；
root 可随意调整自己或他人程序的 Nice 值，且范围为 -20 ~ 19 ；
一般使用者仅可调整自己程序的 Nice 值，且范围仅为 0 ~ 19 (避免一般用户抢占系统资源)；
一般使用者仅可将 nice 值越调越高，例如本来 nice 为 5 ，则未来仅能调整到大於 5；

11. 
uname：查阅系统与核心相关资讯
uptime：观察系统启动时间与工作负载
netstat ：追踪网络或插槽档 netstat -tlnp
vmstat ：侦测系统资源变化
如果改天你的服务器非常忙碌时， 记得使用 vmstat 去看看，到底是哪个部分的资源被使用的最为频繁！一般来说，如果 I/O 部分很忙碌的话，你的系统会变的非常慢！ 让我们再来看看，那么磁碟的部分该如何观察



Daemons:
系统为了某些功能必须要提供一些服务 (不论是系统本身还是网络方面)，这个服务就称为 service 。 但是 service 的提供总是需要程序的运行吧！否则如何运行呢？所以达成这个 service 的程序我们就称呼他为 daemon 啰！ 举例来说，达成循环型例行性工作排程服务 (service) 的程序为 crond 这个 daemon 啦！
stand_alone: stand alone 的 daemon 响应速度较快。常见的 stand alone daemon 有 WWW 的 daemon (httpd)、FTP 的 daemon (vsftpd) 
super_daemon

每一个服务的开发者，当初在开发他们的服务时，都有特别的故事啦！不过，无论如何，这些服务的名称被创建之后，被挂上 Linux 使用时，通常在服务的名称之后会加上一个 d ，例如例行性命令的创建的    at, 与 cron 这两个服务， 他的程序文件名会被取为 atd 与 crond，这个 d 代表的就是 daemon 的意思

系统上面有没有什么配置可以让服务与埠号对应在一起呢？那就是 /etc/service!!!!!

目录：
/etc/init.d/* ：启动脚本放置处
系统上几乎所有的服务启动脚本都放置在这里
/etc/sysconfig/* ：各服务的初始化环境配置文件
/etc/* ：各服务各自的配置文件
由于系统的环境都已经帮你制作妥当，所以利用 /etc/init.d/* 来启动、关闭与观察，就非常的简单！话虽如此， CentOS 还是有提供另外一支可以启动 stand alone 服务的脚本喔，那就是 service 这个程序。 其实 service 仅是一支 script 啦，他可以分析你下达的 service 后面的参数，然后根据你的参数再到 /etc/init.d/ 去取得正确的服务来 start 或 stop 哩！他的语法是这样的啦：

[root@www ~]# service [service name] (start|stop|restart|...)
[root@www ~]# service --status-all
选项与参数：
service name：亦即是需要启动的服务名称，需与 /etc/init.d/ 对应；
start|...   ：亦即是该服务要进行的工作。
--status-all：将系统所有的 stand alone 的服务状态通通列出来

范例三：重新启动 crond 这支 daemon ：
[root@www ~]# service crond restart
[root@www ~]# /etc/init.d/crond restart
# 这两种方法随便你用哪一种来处理都可以！不过鸟哥比较喜欢使用 /etc/init.d/*

范例四：显示出目前系统上面所有服务的运行状态
[root@www ~]# service --status-all
acpid (pid 4536) 正在运行...
anacron 已停止
atd (pid 4694) 正在运行..


12. 登录文件
『详细而确实的分析以及备份系统的登录文件』是一个系统管理员应该要进行的任务之一。 那么什么是登录文件呢？简单的说，就是记录系统活动资讯的几个文件， 例如：何时、何地 (来源 IP)、何人 (什么服务名称)、做了什么动作 (信息登录罗)。 换句话说就是：记录系统在什么时候由哪个程序做了什么样的行为时，发生了何种的事件等等。
/var/log

13. Crontab and at
两种工作排程的方式：

一种是例行性的，就是每隔一定的周期要来办的事项；
一种是突发性的，就是这次做完以后就没有的那一种 (计算机大降价...)
那么在 Linux 底下如何达到这两个功能呢？那就得使用 at 与 crontab 这两个好东西罗！

at ：at 是个可以处理仅运行一次就结束排程的命令，不过要运行 at 时， 必须要有 atd 这个服务 (第十八章) 的支持才行。在某些新版的 distributions 中，atd 可能默认并没有启动，那么 at 这个命令就会失效呢！不过我们的 CentOS 默认是启动的！

crontab ：crontab 这个命令所配置的工作将会循环的一直进行下去！ 可循环的时间为分钟、小时、每周、每月或每年等。crontab 除了可以使用命令运行外，亦可编辑 /etc/crontab 来支持。 至於让 crontab 可以生效的服务则是 crond 这个服务喔！

The cron utility allows you to schedule a repetitive task to take place at any regular interval desired, and the at command lets you specify a one-time action to take place at some desired time. You might use crontab, for example, to perform a backup each morning at 2 a.m., and use at to remind yourself of an appointment later in the day.

batch：系统有空时才进行背景任务

其实 batch 是利用 at 来进行命令的下达啦！只是加入一些控制参数而已。这个 batch 神奇的地方在於：他会在 CPU 工作负载小於 0.8 的时候，才进行你所下达的工作任务啦！ 那什么是负载 0.8 呢？这个负载的意思是： CPU 在单一时间点所负责的工作数量。不是 CPU 的使用率喔！ 举例来说，如果我有一只程序他需要一直使用 CPU 的运算功能，那么此时 CPU 的使用率可能到达 100% ， 但是 CPU 的工作负载则是趋近於『 1 』，因为 CPU 仅负责一个工作嘛！如果同时运行这样的程序两支呢？ CPU 的使用率还是 100% ，但是工作负载则变成 2 了！了解乎？

所以也就是说，当 CPU 的工作负载越大，代表 CPU 必须要在不同的工作之间进行频繁的工作切换。 这样的 CPU 运行情况我们在第零章有谈过，忘记的话请回去瞧瞧！因为一直切换工作，所以会导致系统忙碌啊！ 系统如果很忙碌，还要额外进行 at ，不太合理！所以才有 batch 命令的产生！


Boot Process, MBR and Loader

简单来说，系统启动的经过可以汇整成底下的流程的：

加载 BIOS 的硬件资讯与进行自我测试，并依据配置取得第一个可启动的装置；
读取并运行第一个启动装置内 MBR 的 boot Loader (亦即是 grub, spfdisk 等程序)；
依据 boot loader 的配置加载 Kernel ，Kernel 会开始侦测硬件与加载驱动程序；
在硬件驱动成功后，Kernel 会主动呼叫 init 程序，而 init 会取得 run-level 资讯；
init 运行 /etc/rc.d/rc.sysinit 文件来准备软件运行的作业环境 (如网络、时区等)；
init 运行 run-level 的各个服务之启动 (script 方式)；
init 运行 /etc/rc.d/rc.local 文件；
init 运行终端机模拟程序 mingetty 来启动 login 程序，最后就等待使用者登陆啦；

核心与核心模块
谈完了整个启动的流程，您应该会知道，在整个启动的过程当中，是否能够成功的驱动我们主机的硬件配备， 是核心 (kernel) 的工作！而核心一般都是压缩档，因此在使用核心之前，就得要将他解压缩后， 才能加载主内存当中。

另外，为了应付日新月异的硬件，目前的核心都是具有『可读取模块化驱动程序』的功能， 亦即是所谓的『 modules (模块化)』的功能啦！所谓的模块化可以将他想成是一个『外挂程序』， 该外挂程序可能由硬件开发厂商提供，也有可能我们的核心本来就支持～不过，较新的硬件， 通常都需要硬件开发商提供驱动程序模块啦！


Boot Loader:

MBR 是整个硬盘的第一个 sector 内的一个区块，充其量整个大小也才 446 bytes 而已。 我们的 loader 功能这么强，光是程序码与配置数据不可能只占不到 446 bytes 的容量吧？那如何安装？

为了解决这个问题，所以 Linux 将 boot loader 的程序码运行与配置值加载分成两个阶段 (stage) 来运行：

Stage 1：运行 boot loader 主程序：
第一阶段为运行 boot loader 的主程序，这个主程序必须要被安装在启动区，亦即是 MBR 或者是 boot sector 。但如前所述，因为 MBR 实在太小了，所以，MBR 或 boot sector 通常仅安装 boot loader 的最小主程序， 并没有安装 loader 的相关配置档；

Stage 2：主程序加载配置档：
第二阶段为透过 boot loader 加载所有配置档与相关的环境参数文件 (包括文件系统定义与主要配置档 menu.lst)， 一般来说，配置档都在 /boot 底下。
那么这些配置档是放在哪里啊？这些与 grub 有关的文件都放置到 /boot/grub 中，那我们就来看看有哪些文件吧


initrd 的重要性与创建新 initrd 文件

我们在本章稍早之前『 boot loader 与 kernel 加载』的地方已经提到过 initrd 这玩意儿，他的目的在於提供启动过程中所需要的最重要核心模块，以让系统启动过程可以顺利完成。 会需要 initrd 的原因，是因为核心模块放置於 /lib/modules/$(uname -r)/kernel/ 当中， 这些模块必须要根目录 (/) 被挂载时才能够被读取。但是如果核心本身不具备磁碟的驱动程序时， 当然无法挂载根目录，也就没有办法取得驱动程序，因此造成两难的地步。

initrd 可以将 /lib/modules/.... 内的『启动过程当中一定需要的模块』包成一个文件 (档名就是 initrd)， 然后在启动时透过主机的 INT 13 硬件功能将该文件读出来解压缩，并且 initrd 在内存内会模拟成为根目录， 由於此虚拟文件系统 (Initial RAM Disk) 主要包含磁碟与文件系统的模块，因此我们的核心最后就能够认识实际的磁碟， 那就能够进行实际根目录的挂载啦！所以说：『initrd 内所包含的模块大多是与启动过程有关，而主要以文件系统及硬盘模块 (如 usb, SCSI 等) 为主』的啦！


The ls command, or even TAB-completion or wildcard expansion by the shell, will normally present their results in alphanumeric order. This requires reading the entire directory listing and sorting it. With ten million files in a single directory, this sorting operation will take a non-negligible amount of time.

If you can resist the urge of TAB-completion and e.g. write the names of files to be zipped in full, there should be no problems.

tune2fs has an option called dir_index that tends to be turned on by default (on Ubuntu it is) that lets you store roughly 100k files in a directory before you see a performance hit. That is not even close to the 10m files you are thinking about.

ext filesystems have a fixed maximum number of inodes. Every file and directory uses 1 inode. Use df -i for a view of your partitions and inodes free. When you run out of inodes you can not make new files or folders.

commands like rm and ls when using wildcards expand the command and will end up with a "argument list too long". You will have to use find to delete or list files. And find tends to be slow.


2018.11.07

To understand the problem of why Ctrl + C does not work, it is very helpful to understand what happens when you press it:

Most shells bind Ctrl + C to "send a SIGINT signal to the program that currently runs in the foreground". You can read about the different signals via man signal:

 SIGINT        2       Term    Interrupt from keyboard
Programs can ignore that signal, as they can ignore SIGTSTP as well:

 SIGTSTP   18,20,24    Stop    Stop typed at tty
(Which is what most shells do when you press Ctrl + Z, which is why it is not guaranteed to work.)

There are some signals which can not be ignored by the process: SIGKILL, SIGSTOP and some others. You can send these signals via the kill command. So, to kill your hanging / zombieying process, just find the process ID (PID). For example, use pgrep or ps and then kill it:

 % kill -9 PID