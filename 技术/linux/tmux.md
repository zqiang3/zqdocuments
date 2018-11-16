## 安装

```bash
sudo apt-get install tmux
```

## 命令

```bash
tmux new -s NAME
ctrl+b d             # 退出会话
tmux ls              #
tmux a -t NAME       # 进入某个会话
```

## C-b

```
C-b % 竖切分
C-b " 横切分
C-b ! 关闭所有的小窗口
C-b -> 右边窗口
C-b <- 左边窗口
```

## 修改快捷键前缀

PREFIX 默认CTRL+b
在~/.tmux.conf中加入如下行，没有~/.tmux.conf文件自己建立一个即可。 
set -g prefix C-a 
unbind C-b 
此时并没有生效，重启tmux或者在命令模式（按PREFIX : )输入 
source-file ~/.tmux.conf 