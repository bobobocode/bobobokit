## Vim

    Ctr-w
    Ctr-u
    ctrl+v：矩形选择

    >G
    C
    S
    I
    &
    gggqG

    @:
    :normal
    :shell
    :read !{cmd}
    :2,$!sort -t',' -k2

    :save <file name>
    :f <file name>

    :%s/\(world\), change \(mind\)/\2, change \1/g
    :%s/_\([a-z]\)/\U\1/g
    :let i=997|g/abcdefg/s//\=i/|let i=i-1

    :so $MYVIMRC
    :e ++enc=gbk
    :%!xxd
    :noh

    % 当前完整的文件名
    %:h 文件名的头部，即文件目录.例如../path/test.c就会为../path
    %:t 文件名的尾部.例如../path/test.c就会为test.c
    %:r 无扩展名的文件名.例如../path/test就会成为test
    %:e 扩展名

    m ——创建标记
    ' ——移动到标记的文本行首
    ` ——移动到标记的光标位置
    :marks ——列示所有标记
    :delmarks ——删除指定标记
    :delmarks! ——删除所有标记

## sed

    sed -i "" 's/webmobileapi\.bainianaolai\.com/m\.bainianaolai\.com/g' `grep "webmobileapi.bainianaolai.com" -rl .`

## awk

    awk -F "[分隔符 分隔符]" '{print $1,"=",$2;}' filename

## cscope

cscope -Rbq

:cs find {querytype} {name}

     {querytype} 即相对应于实际的cscope行接口数字，同时也相对应于nvi命令：
        0或者s   —— 查找这个C符号
        1或者g  —— 查找这个定义
        2或者d  —— 查找被这个函数调用的函数（们）
        3或者c  —— 查找调用这个函数的函数（们）
        4或者t   —— 查找这个字符串
        6或者e  —— 查找这个egrep匹配模式
        7或者f   —— 查找这个文件
        8或者i   —— 查找#include这个文件的文件（们）
        ## ctag

## ctags

    ctags --totals=yes -f /Users/James/code/tags/kit.tags -R /Users/James/code/kit/py/ --exclude=+.pyc,+.swp,+.md,LISENCE
    find . -name "*.go" | xargs gotags -L - -f tags
    find . -name "*.java" | xargs ctags -L -

## files

    gzip -dc myfile.gz | grep abc
    diff -rq  <path> <path> > difftxt
    find . -size +100M
    find . -path './ignore' -prune -o -type f -print
    grep 'model name' /proc/cpuinfo | wc -l
    grep -ABC
    grep -v

