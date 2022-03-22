# ZeLanChao_KGQA
一个基于Django,Neo4j与图谱问答技术的的中医药知识图谱与智能问答平台。
（暂取名“泽兰抄”）

## 编写环境
PyCharm 2021.1.1

## 安装说明
1. 请确保您的电脑有以下环境：python3，neo4j
2. 在想要安装的文件夹下解压djangoProject.rar，双击进入djangoProject文件夹
3. 在该目录下进入cmd，输入指令“pip install -r requirement.txt”,安装需要的python库
4. 打开medicine/qs/buidmedicalgraph.py，在第20行将password修改为您的neo4j数据库密码；打开medicine/qs/answer_search.py，在第11行将password修改为您的neo4j数据库密码。
5. 运行目录下的medicine/qs/build_medicalgraph.py，导入知识图谱
6. 在根目录下打开cmd界面，输入指令“python manage.py runserver”
7. 打开浏览器，进入https://127.0.0.1:8000/index，即可使用

注：由于数据量较大，步骤5的运行时间较长。请在进行步骤5前确保neo4j数据库在运行状态，否则无法导入数据。

## 一些碎碎念

********以下内容是正式提交之后添加的，记录了一些让我印象深刻的搞人心态的难题，写给可能看这个借鉴修改的学弟学妹********

1. 如果你是第一次搞python环境，安各种环境的时候千万记得开镜像哇…不然各种奇奇怪怪的时限报错非常搞人心态。开镜像的方法（pip例）：
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
（具体可以百度“pip镜像源”）

2. 第三步里边有个pyahocorasick包特别难安装，如果卡住了可以看看这篇博客，我是靠这个解决的：https://blog.csdn.net/weixin_40539807/article/details/105755027
这个“蔡哥学知识图谱”的系列写的特别好，看一遍绝对不亏 0w0

3. pycharm一定要下专业版，特别方便。开个学校邮箱就能免费用一年…网上的破解都不靠谱的…一年之后怎么办？你和队友轮流开呗

4. 论文看不懂不妨先把标题搜搜看有没有大佬翻过

5. 但凡报错WinError10036（由于目标计算机积极拒绝，xxxxx），网上特别杂，基本查不到解决方法。我感觉和neo4j有关的主要解决方法：一检查防火墙与杀毒软件，二检查代码里的数据库用户名密码，三检查端口设置，四检查neo4j是否启动。

加油呀！
