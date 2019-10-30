# GROVE TERMINAL APIs

## 此API将赋予您的屏幕类似终端的打印功能
- 支持横竖屏
- 支持全局背景/前景颜色设置
- 支持数值/字符串类型在屏幕上打印
- 支持背光开启/关闭

## 公有成员清单
- <a href="#begin">void begin(bool open = true, uint8_t direction = 1)</a>
- <a href="#turn_on">void turn_on()</a>
- <a href="#turn_off">void turn_off()</a>
- <a href="#global_foreground">void global_foreground(uint16_t color)</a>
- <a href="#global_background">void global_background(uint16_t color)</a>
- <a href="#print_uint8_t">void print(uint8_t value, uint8_t base = 10)</a>
- <a href="#print_uint16_t">void print(uint16_t value, uint8_t base = 10)</a>
- <a href="#print_uint32_t">void print(uint32_t value, uint8_t base = 10)</a>
- <a href="#print_uint64_t">void print(uint64_t value, uint8_t base = 10)</a>
- <a href="#print_int8_t">void print(int8_t value, uint8_t base = 10)</a>
- <a href="#print_int16_t">void print(int16_t value, uint8_t base = 10)</a>
- <a href="#print_int32_t">void print(int32_t value, uint8_t base = 10)</a>
- <a href="#print_int64_t">void print(int64_t value, uint8_t base = 10)</a>
- <a href="#print_char">void print(char value)</a>
- <a href="#print_charp">void print(const char * str)</a>
- <a href="#print_charp_length">void print(const char * str, uint32_t length)</a>
- <a href="#print_double">void print(double value, uint8_t base = 2)</a>
- <a href="#println_uint8_t">void println(uint8_t value, uint8_t base = 10)</a>
- <a href="#println_uint16_t">void println(uint16_t value, uint8_t base = 10)</a>
- <a href="#println_uint32_t">void println(uint32_t value, uint8_t base = 10)</a>
- <a href="#println_uint64_t">void println(uint64_t value, uint8_t base = 10)</a>
- <a href="#println_int8_t">void println(int8_t value, uint8_t base = 10)</a>
- <a href="#println_int16_t">void println(int16_t value, uint8_t base = 10)</a>
- <a href="#println_int32_t">void println(int32_t value, uint8_t base = 10)</a>
- <a href="#println_int64_t">void println(int64_t value, uint8_t base = 10)</a>
- <a href="#println_char">void println(char value)</a>
- <a href="#println_charp">void println(const char * str)</a>
- <a href="#println_double">void println(double value, uint8_t = 2)</a>
- <a href="#printf">void printf(const char * fmt, ...)</a>
- <a href="#auto_flush">void auto_flush(bool enable)</a>
- <a href="#flush">void flush()</a>

---
## <strong> void begin(bool open = true, uint8_t direction = 1) </strong> 
---
<a name="begin"></a>
<strong>function description</strong>  
&emsp;&emsp;用于初始化屏幕，设置背光状态和屏幕方向  
  
<strong>open : bool = true</strong>  
&emsp;&emsp;[含义] 是否开启屏幕背光，默认是开启  
  
<strong>direction : uint8_t = 1</strong>  
&emsp;&emsp;[含义] 屏幕显示方向，默认是横屏显示  
&emsp;&emsp;&emsp;&emsp;&emsp;0 - 竖屏  
&emsp;&emsp;&emsp;&emsp;&emsp;1 - 横屏  
&emsp;&emsp;&emsp;&emsp;&emsp;2 - 倒像竖屏  
&emsp;&emsp;&emsp;&emsp;&emsp;3 - 倒像横屏  
```C++
#include<grove_terminal.h>
grove_terminal terminal;

void setup(){
    terminal.begin();
    terminal.println("Hello World!");
}
void loop(){
    ;
}
```
&nbsp;

---
## <strong> void turn_on() </strong> 
---
<a name="turn_on"></a>
<strong>function description</strong>  
&emsp;&emsp;用于开启屏幕背光  
&nbsp;

---
## <strong> void turn_off() </strong> 
---
<a name="turn_off"></a>
<strong>function description</strong>  
&emsp;&emsp;用于关闭屏幕背光  
  
<strong>useful hint</strong>  
&emsp;&emsp;关闭屏幕背光并不影响打印功能，只是屏幕没有亮度，在开启开启屏幕背光后仍能看到打印的内容  
&nbsp;

---
## <strong> void global_foreground(uint16_t color) </strong> 
---
<a name="global_foreground"></a>
<strong>function description</strong>  
&emsp;&emsp;设置全局前景色，并刷新屏幕内容。  
  
<strong>color : uint16_t</strong>  
&emsp;&emsp;[含义] RGB565彩色值  
&nbsp;

---
## <strong> void global_background(uint16_t color) </strong> 
---
<a name="global_background"></a>
<strong>function description</strong>  
&emsp;&emsp;设置全局背景色，并刷新屏幕内容。  
  
<strong>color : uint16_t</strong>  
&emsp;&emsp;[含义] RGB565彩色值  
&nbsp;

---
## <strong> void print(uint8_t value, uint8_t base = 10) </strong> 
---
<a name="print_uint8_t"></a>
<strong>function description</strong>  
&emsp;&emsp;打印指定进制的数字。  
  
<strong>value : uint8_t</strong>  
&emsp;&emsp;[含义] 要在屏幕打印的自然数，取值范围为0~255  
  
<strong>base : uint8_t</strong>  
&emsp;&emsp;[含义] 进制模式，默认值是10，表示以十进制的方式打印数值，有效取值范围为2~36
&nbsp;

---
## <strong> void print(uint16_t value, uint8_t base = 10) </strong> 
---
<a name="print_uint16_t"></a>
<strong>function description</strong>  
&emsp;&emsp;打印指定进制的数字。  
  
<strong>value : uint16_t</strong>  
&emsp;&emsp;[含义] 要在屏幕打印的自然数，取值范围为0~65535  
  
<strong>base : uint8_t</strong>  
&emsp;&emsp;[含义] 进制模式，默认值是10，表示以十进制的方式打印数值，有效取值范围为2~36
&nbsp;

---
## <strong> void print(uint32_t value, uint8_t base = 10) </strong> 
---
<a name="print_uint32_t"></a>
<strong>function description</strong>  
&emsp;&emsp;打印指定进制的数字。  
  
<strong>value : uint32_t</strong>  
&emsp;&emsp;[含义] 要在屏幕打印的自然数，取值范围为0~4294967295  
  
<strong>base : uint8_t</strong>  
&emsp;&emsp;[含义] 进制模式，默认值是10，表示以十进制的方式打印数值，有效取值范围为2~36
&nbsp;

---
## <strong> void print(uint64_t value, uint8_t base = 10) </strong> 
---
<a name="print_uint64_t"></a>
<strong>function description</strong>  
&emsp;&emsp;打印指定进制的数字。  
  
<strong>value : uint64_t</strong>  
&emsp;&emsp;[含义] 要在屏幕打印的自然数，取值范围为0~18446744073709551615  
  
<strong>base : uint8_t</strong>  
&emsp;&emsp;[含义] 进制模式，默认值是10，表示以十进制的方式打印数值，有效取值范围为2~36
&nbsp;

---
## <strong> void print(int8_t value, uint8_t base = 10) </strong> 
---
<a name="print_int8_t"></a>
<strong>function description</strong>  
&emsp;&emsp;打印指定进制的数字。  
  
<strong>value : int8_t</strong>  
&emsp;&emsp;[含义] 要在屏幕打印的整数，取值范围为-128~127
  
<strong>base : uint8_t</strong>  
&emsp;&emsp;[含义] 进制模式，默认值是10，表示以十进制的方式打印数值，有效取值范围为2~36
&nbsp;

---
## <strong> void print(int16_t value, uint8_t base = 10) </strong> 
---
<a name="print_int16_t"></a>
<strong>function description</strong>  
&emsp;&emsp;打印指定进制的数字。  
  
<strong>value : int16_t</strong>  
&emsp;&emsp;[含义] 要在屏幕打印的整数，取值范围为-32768~32767
  
<strong>base : uint8_t</strong>  
&emsp;&emsp;[含义] 进制模式，默认值是10，表示以十进制的方式打印数值，有效取值范围为2~36
&nbsp;

---
## <strong> void print(int32_t value, uint8_t base = 10) </strong> 
---
<a name="print_int32_t"></a>
<strong>function description</strong>  
&emsp;&emsp;打印指定进制的数字。  
  
<strong>value : int32_t</strong>  
&emsp;&emsp;[含义] 要在屏幕打印的整数，取值范围为-2147483648~2147483647
  
<strong>base : uint8_t</strong>  
&emsp;&emsp;[含义] 进制模式，默认值是10，表示以十进制的方式打印数值，有效取值范围为2~36
&nbsp;

---
## <strong> void print(int64_t value, uint8_t base = 10) </strong> 
---
<a name="print_int64_t"></a>
<strong>function description</strong>  
&emsp;&emsp;打印指定进制的数字。  
  
<strong>value : int64_t</strong>  
&emsp;&emsp;[含义] 要在屏幕打印的整数，取值范围为-9223372036854775808~9223372036854775807
  
<strong>base : uint8_t</strong>  
&emsp;&emsp;[含义] 进制模式，默认值是10，表示以十进制的方式打印数值，有效取值范围为2~36
&nbsp;

---
## <strong> void print(char value) </strong> 
---
<a name="print_char"></a>
<strong>function description</strong>  
&emsp;&emsp;打印一个字符。  
  
<strong>value : char</strong>  
&emsp;&emsp;[含义] 要在屏幕打印的字符  
&nbsp;

---
## <strong> void print(const char * str) </strong> 
---
<a name="print_charp"></a>
<strong>function description</strong>  
&emsp;&emsp;打印字符串，超过屏幕宽度或者字符串中包含换行符'\n'时折行。  
  
<strong>value : const char *</strong>  
&emsp;&emsp;[含义] 要在屏幕打印的字符串  
&nbsp;

---
## <strong> void print(const char * str, uint32_t length) </strong> 
---
<a name="print_charp_length"></a>
<strong>function description</strong>  
&emsp;&emsp;打印指定长度字符串，超过屏幕宽度或者字符串中包含换行符'\n'时折行，实际打印长度=min(length, 字符串实际长度)。  
  
<strong>value : const char *</strong>  
&emsp;&emsp;[含义] 要在屏幕打印的字符串  
  
<strong>length : uint32_t</strong>  
&emsp;&emsp;[含义] 打印长度，实际打印长度=min(length, 字符串实际长度)  
&nbsp;

---
## <strong> void print(double value, uint8_t precison = 2) </strong> 
---
<a name="print_double"></a>
<strong>function description</strong>  
&emsp;&emsp;打印指定精度的浮点数，默认保留两位小数  
  
<strong>value : double</strong>  
&emsp;&emsp;[含义] 要在屏幕打印的浮点数  
  
<strong>precison : uint8_t</strong>  
&emsp;&emsp;[含义] 设置浮点数的精度，默认保留两位小数  
&nbsp;



---
## <strong> void println(uint8_t value, uint8_t base = 10) </strong> 
---
<a name="println_uint8_t"></a>
<strong>function description</strong>  
&emsp;&emsp;打印指定进制的数字并换行。  
  
<strong>value : uint8_t</strong>  
&emsp;&emsp;[含义] 要在屏幕打印的自然数，取值范围为0~255  
  
<strong>base : uint8_t</strong>  
&emsp;&emsp;[含义] 进制模式，默认值是10，表示以十进制的方式打印数值，有效取值范围为2~36
&nbsp;

---
## <strong> void println(uint16_t value, uint8_t base = 10) </strong> 
---
<a name="println_uint16_t"></a>
<strong>function description</strong>  
&emsp;&emsp;打印指定进制的数字并换行。  
  
<strong>value : uint16_t</strong>  
&emsp;&emsp;[含义] 要在屏幕打印的自然数，取值范围为0~65535  
  
<strong>base : uint8_t</strong>  
&emsp;&emsp;[含义] 进制模式，默认值是10，表示以十进制的方式打印数值，有效取值范围为2~36
&nbsp;

---
## <strong> void println(uint32_t value, uint8_t base = 10) </strong> 
---
<a name="println_uint32_t"></a>
<strong>function description</strong>  
&emsp;&emsp;打印指定进制的数字并换行。  
  
<strong>value : uint32_t</strong>  
&emsp;&emsp;[含义] 要在屏幕打印的自然数，取值范围为0~4294967295  
  
<strong>base : uint8_t</strong>  
&emsp;&emsp;[含义] 进制模式，默认值是10，表示以十进制的方式打印数值，有效取值范围为2~36
&nbsp;

---
## <strong> void println(uint64_t value, uint8_t base = 10) </strong> 
---
<a name="println_uint64_t"></a>
<strong>function description</strong>  
&emsp;&emsp;打印指定进制的数字并换行。  
  
<strong>value : uint64_t</strong>  
&emsp;&emsp;[含义] 要在屏幕打印的自然数，取值范围为0~18446744073709551615  
  
<strong>base : uint8_t</strong>  
&emsp;&emsp;[含义] 进制模式，默认值是10，表示以十进制的方式打印数值，有效取值范围为2~36
&nbsp;

---
## <strong> void println(int8_t value, uint8_t base = 10) </strong> 
---
<a name="println_int8_t"></a>
<strong>function description</strong>  
&emsp;&emsp;打印指定进制的数字并换行。  
  
<strong>value : int8_t</strong>  
&emsp;&emsp;[含义] 要在屏幕打印的整数，取值范围为-128~127
  
<strong>base : uint8_t</strong>  
&emsp;&emsp;[含义] 进制模式，默认值是10，表示以十进制的方式打印数值，有效取值范围为2~36
&nbsp;

---
## <strong> void println(int16_t value, uint8_t base = 10) </strong> 
---
<a name="println_int16_t"></a>
<strong>function description</strong>  
&emsp;&emsp;打印指定进制的数字并换行。  
  
<strong>value : int16_t</strong>  
&emsp;&emsp;[含义] 要在屏幕打印的整数，取值范围为-32768~32767
  
<strong>base : uint8_t</strong>  
&emsp;&emsp;[含义] 进制模式，默认值是10，表示以十进制的方式打印数值，有效取值范围为2~36
&nbsp;

---
## <strong> void println(int32_t value, uint8_t base = 10) </strong> 
---
<a name="println_int32_t"></a>
<strong>function description</strong>  
&emsp;&emsp;打印指定进制的数字并换行。  
  
<strong>value : int32_t</strong>  
&emsp;&emsp;[含义] 要在屏幕打印的整数，取值范围为-2147483648~2147483647
  
<strong>base : uint8_t</strong>  
&emsp;&emsp;[含义] 进制模式，默认值是10，表示以十进制的方式打印数值，有效取值范围为2~36
&nbsp;

---
## <strong> void println(int64_t value, uint8_t base = 10) </strong> 
---
<a name="println_int64_t"></a>
<strong>function description</strong>  
&emsp;&emsp;打印指定进制的数字并换行。  
  
<strong>value : int64_t</strong>  
&emsp;&emsp;[含义] 要在屏幕打印的整数，取值范围为-9223372036854775808~9223372036854775807
  
<strong>base : uint8_t</strong>  
&emsp;&emsp;[含义] 进制模式，默认值是10，表示以十进制的方式打印数值，有效取值范围为2~36
&nbsp;

---
## <strong> void println(char value) </strong> 
---
<a name="println_char"></a>
<strong>function description</strong>  
&emsp;&emsp;打印一个字符并换行。  
  
<strong>value : char</strong>  
&emsp;&emsp;[含义] 要在屏幕打印的字符  
&nbsp;

---
## <strong> void println(const char * str) </strong> 
---
<a name="println_charp"></a>
<strong>function description</strong>  
&emsp;&emsp;打印字符串并换行，超过屏幕宽度或者字符串中包含换行符'\n'时折行。  
  
<strong>value : const char *</strong>  
&emsp;&emsp;[含义] 要在屏幕打印的字符串  
&nbsp;

---
## <strong> void println(const char * str, uint32_t length) </strong> 
---
<a name="println_charp_length"></a>
<strong>function description</strong>  
&emsp;&emsp;打印指定长度字符串并换行，超过屏幕宽度或者字符串中包含换行符'\n'时折行，实际打印长度=min(length, 字符串实际长度)。  
  
<strong>value : const char *</strong>  
&emsp;&emsp;[含义] 要在屏幕打印的字符串  
  
<strong>length : uint32_t</strong>  
&emsp;&emsp;[含义] 打印长度，实际打印长度=min(length, 字符串实际长度)  
&nbsp;

---
## <strong> void println(double value, uint8_t precison = 2) </strong> 
---
<a name="println_double"></a>
<strong>function description</strong>  
&emsp;&emsp;打印指定精度的浮点数并换行，默认保留两位小数  
  
<strong>value : double</strong>  
&emsp;&emsp;[含义] 要在屏幕打印的浮点数  
  
<strong>precison : uint8_t</strong>  
&emsp;&emsp;[含义] 设置浮点数的精度，默认保留两位小数  
&nbsp;

---
## <strong> void printf(const char * fmt, ...) </strong> 
---
<a name="printf"></a>
<strong>function description</strong>  
&emsp;&emsp;格式化打印字符串，一次可以打印多个值，其中打印的类型可以是字符，数值，字符串。  
  
<strong>fmt : const char *</strong>  
&emsp;&emsp;[含义] 用于格式化控制的字符串  
  
<strong>... : parameter list</strong>  
&emsp;&emsp;[含义] 长度可变的参数列表，但是需要和fmt中填写的参数个数以及类型一致，一下  
&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;%d - 对应int8_t, int16_t, int32_t  
&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;%u - 对应uint8_t, uint16_t, uint32_t  
&emsp;&emsp;&emsp;&emsp;%lld - 对应int64_t  
&emsp;&emsp;&emsp;&emsp;%llu - 对应uint64_t  
&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;%c - 对应char  
&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;%s - 对应const char *  
&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;%x - 对应int8_t, int16_t, int32_t小写十六进制  
&emsp;&emsp;&emsp;&emsp;&nbsp;%X - 对应int8_t, int16_t, int32_t大写十六进制  
&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;%f - 对应float，double，默认保留6位小数，%.1f可以保留一位小数，%.2f可以保留两位小数，以此类推。  
&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;%g - 对应float，double，以科学计数法展示浮点数。  
&emsp;&emsp;&emsp;&emsp;&nbsp;%% - 两个百分号表示一个百分号，四个则表示两个百分号，以此类推。  

```C++
#include<grove_terminal.h>
grove_terminal terminal;

void setup(){
    //初始化屏幕
    terminal.begin();

    //在屏幕上打印"Hello 2020"，其中%d用2020替换
    terminal.printf("Hello %d!\n", 2020);

    //在屏幕上打印"2 + 4 = 6"，其中第一个%d用2替换，第二个%d用4替换，第三个%d用6替换
    terminal.printf("%d + %d = %d\n", 2, 4, 6);

    //在屏幕上打印"0x802a is lower hex number, 0x55AA is upper hex number"
    //其中%x会被替换成小写的十六进制值，%X会被替换成大写的十六进制值
    terminal.printf("0x%x is lower hex number, 0x%X is upper hex number\n", 0x802a, 0x55aa);

    //还可以打印浮点数，"1.500000 is a float number"，默认是保留6位小数
    terminal.printf("%f is a float number\n", 1.5);
    
    //设置成保留1位小数"1.5 is a float number"
    terminal.printf("%.1f is a float number\n", 1.5);

    //在屏幕上打印"grove ui"
    terminal.printf("%s\n", "grove ui");

    //more...
}
void loop(){
    ;
}
```
&nbsp;

---
## <strong> void auto_flush(bool enable) </strong> 
---
<a name="auto_flush"></a>
<strong>function description</strong>  
&emsp;&emsp;设置是否在打印时立即自动刷新屏幕内容，grove_terminal默认在初始化时启用自动刷新。

<strong>useful hint</strong>  
&emsp;&emsp;常规嵌入式屏幕刷新率基本都小于100fps，也就是如果每次调用打印函数都直接将内容都刷新到屏幕的话，速度是很慢的（实验测试大约每秒打印约80行整数）。所以我们提供变通的方法，可以将auto_flush设置成false，然后在打印多个内容后手动调用flush函数展示内容，你会发现打印效率提升显著 :)。

<strong>enable : bool</strong>  
&emsp;&emsp;[含义] 是否在调用print、println、printf等打印函数时是否立即展示打印的内容  
  
```C++
#include<grove_terminal.h>
grove_terminal terminal;
int32_t        i = 0;
int32_t        c = 0;
void setup(){
    //初始化屏幕
    terminal.begin();

    //取消自动刷新
    terminal.auto_flush(false);
}

void loop(){
    //每32个数值刷新一次
    if (c == 32){
        c = 0;
        terminal.flush();
    }
    terminal.println(i);
    c++;
    i++;
}
```
&nbsp;

---
## <strong> void flush() </strong> 
---
<a name="flush"></a>
<strong>function description</strong>  
&emsp;&emsp;将存在缓冲区里的打印内容刷新到屏幕上

<strong>useful hint</strong>  
&emsp;&emsp;在默认情况下，每次打印时grove_terminal内部会自动调用flush而无需用户干预。仅当用户将auto_flush设置为false时，需要手动调用该函数才能显示打印的内容。
