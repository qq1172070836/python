## 1_数据类型
### Number
    int
        0box
        int,bin,oct,hex
    float
        1/1 => float
        decimal
        math.ceil(1.1) == 2
    bool
        True, False
    complex
        a+bj, complex(a, b)

### String
    '', "", ''''''
    \r\n
    r''
    + * 切片 ord
    方法：
        增
            +, %, format, join
        删
            replace
        改
            upper,lower,capitalize,title,strip,split
        查
            count, index
        判断
            isalpha,isdigit,isupper,islower,startswith,endswith
            
### List
    []
    len max min,+,*,in,切片,迭代
    方法：
        增
            +,append,insert,entend
        删
            remove,pop,del,clear
        改
            索引赋值
        查
            count, index
        排序反转
            sort, reverse

### Tuple
    ()
    (1,)
    count, index

### Set
    {1,2,3} set(1,2,3)
    - & |
    差 交 并

### Dict
    {}
    keys values items

## 2_运算符
    算术运算符
    位运算符
    比较运算符
    赋值运算符
    身份运算符
    成员运算符
    逻辑运算符

## 3_变量
    三大属性
        type, value, id

    浅拷贝和深拷贝
    1、浅拷贝只拷贝多层列表的最外层，改变内存列表，原列表也会跟着改变
    2、深拷贝是将原列表克隆一份新的

## 4_控制语句
    判断 if
    循环 for while
    中断 continue break