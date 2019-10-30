import os
import re
import sys


def generate(input_file_name):
    file = open(input_file_name, 'r')
    name = os.path.splitext(input_file_name)[0]
    for i in range(0, 128):
        if i == 0:
            f = name + '.md'
        else:
            f = (name + '%d.md') % i
        if (os.path.exists(f)):
            continue
        gen = open(f, 'w')
        break

    i = 0
    buf = []
    gen.write('## Public Functions\n')
    for line in file.readlines():
        line = line.replace('\n', '')
        gen.write('- <a href="#a%d">%s</a>\n' % (i, line))
        buf.append('&nbsp;')
        buf.append('<a name="a%d"></a>' % i)
        buf.append('')
        buf.append('---')
        buf.append('## <strong> %s </strong>' % line)
        buf.append('---')
        buf.append('<strong>function description</strong>  ')
        buf.append('&emsp;&emsp;==============================')
        buf.append('  ')
        l = line.index('(')
        r = line.index(')')
        if (l + 1 < r):
            print(line)
            for arg in line[l + 1:r].split(','):
                v = re.split(' |=', arg)
                v = filter(None, v)
                v = list(v)
                i = -2 if arg.find('=') >= 0 else -1
                s = '%s : %s' % (v[i], ' '.join(v[0:i]))
                if i == -2:
                    s = s + '= ' + v[-1]
                buf.append('<strong>%s</strong>  ' % s)
                buf.append('&emsp;&emsp;[meaning] =======================  ')
                buf.append('  ')
            ret = line.split(' ')[0]
            if (ret != 'void'):
                buf.append('<strong>return : %s</strong>  ' % ret)
                buf.append('&emsp;&emsp;[meaning] =======================  ')
        i = i + 1
    gen.write('\n'.join(buf))
    gen.close()


generate(sys.argv[1])
