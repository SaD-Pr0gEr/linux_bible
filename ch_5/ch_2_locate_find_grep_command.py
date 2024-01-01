"""
Команда locate для поиска файлов по имени
    В большинстве систем Linux, включая Fedora и RHEL, команда updatedb
    выполняется один раз в день и по всей системе собирает имена файлов в базу данных.
    Запустив команду locate, можно выполнить поиск в этой базе данных и определить
    расположение файлов, хранящихся в ней
    Вот что нужно знать о поиске файлов с помощью команды locate.
        * Команда locate имеет и преимущества, и недостатки по сравнению с командой
            find. Она находит файлы быстрее, потому что ищет по готовой базе данных, а не
            по всей файловой системе. Недостатком является то, что locate не учитывает
            файлы, добавленные в систему после последнего обновления базы данных.
        * Не каждый файл файловой системы хранится в базе данных. Содержимое
            файла /etc/updatedb.conf ограничивает, какие имена файлов отсекаются в зависимости
            от выбранных типов монтирования, типов файловой системы, типов
            файлов и точек монтирования. Например, не собираются имена файлов из
            удаленных файловых систем (cifs, inf и т. д.) или локально смонтированных
            CD или DVD (iso9660). Пути, содержащие временные файлы (/tmp) и файлы
            в очереди обработки (/var/spool/cups), также исключаются. При необходимости отсекаемые
            элементы можно добавить в базы данных locate или удалить из них.

    !!!ПРИМЕЧАНИЕ!!!
    Обычный пользователь не может просматривать файлы из базы данных locate,
    которые не отображаются в файловой системе. Например, если не получается
    ввести ls для просмотра файлов в каталоге /root, то и файлы, хранящиеся в этом
    каталоге, найти не получится.

    В отличие от команды find, которая использует параметр -name для поиска имен
    файлов, команда locate находит введенную строку, если она находится в любой
    части пути к файлу. В этом примере поиск services с помощью команды locate
    находит файлы и каталоги, содержащие текстовую строку services
        $ locate services
        /etc/services
        /usr/share/services/bmp.kmgio
        /usr/share/services/data.kmgio

Поиск файлов с помощью команды find
    Команда find лучше всего находит файлы в файловой системе на основе различных атрибутов.
    После того как файлы найдены, с ними можно взаимодействовать (используя параметры -exec или -okay)
    с помощью нужных команд.
    Команда find выполняет поиск в реальном времени, из-за чего он идет медленнее, чем с командой locate,
    но по всей файловой системе. Можно задать поиск так, чтобы он начинался в определенной точке файловой
    системы: ограничив область поиска, мы ускоряем его. Практически любой атрибут файла может стать
    параметром для поиска. Можно искать имена файлов, владельца, права доступа,
    размер, время изменения и другие атрибуты, а также их комбинации.
    Примеры использования команды find:
        $ find
        $ find /etc
        # find /etc
        $ find $HOME -ls
    Специальный параметр для команды find — это -ls. Длинный список характеристик (владелец, права доступа,
    размер и т. д.) выводится с каждым файлом при использовании параметра -ls для команды find
    (он аналогичен выводу команды ls -l). Этот параметр поможет в последующих примерах, когда потребуется
    проверить, что нужные файлы (определенного владельца, размера, времени изменения или имеющие другие
    атрибуты) найдены

    !!!ПРИМЕЧАНИЕ!!!
    Если обычный пользователь выполнит поиск в той части файловой системы, к которой у него нет полного доступа
    (например, в каталоге /etc), появится множество сообщений об ошибках при поиске с помощью find. Чтобы убрать
    сообщения, направьте стандартные ошибки в файл /dev/null.
    Для этого добавьте в конец командной строки 2> /dev/null.
    Выражение 2> перенаправляет стандартную ошибку к следующему параметру — в данном
    случае файлу /dev/null, в котором выходные данные отбрасываются.

    Поиск файлов по имени
        Чтобы найти файлы по имени, используйте параметры -name и -iname. Поиск осуществляется по базовому
        имени файла, имена каталогов по умолчанию не учитываются. Чтобы сделать поиск более гибким, можно
        применить подстановочные символы, например звездочки (*) и вопросительные знаки (?), как в следующих
        примерах:
            # find /etc -name passwd
                /etc/pam.d/passwd
                /etc/passwd
            # find /etc -iname '*passwd*'
                /etc/pam.d/passwd
                /etc/passwd-
                /etc/passwd.OLD
                /etc/passwd
                /etc/MYPASSWD
                /etc/security/opasswd
        Если параметр без звездочек, как в первом примере, то будут перечислены все имеющиеся в каталоге
        /etc файлы, которые носят точное имя passwd. С параметром -iname можно сопоставить любую комбинацию
        в верхнем и нижнем регистрах. А используя звездочки, можно сопоставить с ним любое имя файла, содержащее
        слово passwd.

    Поиск файлов по размеру
        Когда диск заполняется и нужно узнать местонахождение самых больших файлов, можно выполнить поиск по
        размеру файла. Параметр -size позволяет искать файлы указанного размера, а также те,
        что меньше или больше него, например:
            $ find /usr/share/ -size +10M
            $ find /mostlybig -size -1M
            $ find /mostlybig -size +5M -size -20M

    Поиск файлов по имени пользователя
        Можно искать файлы по имени конкретного владельца (-user) или названию группы (-group).
        Например:
            $ find /home -user chris -ls
            131077 4 -rw-r--r-- 1 chris chris 379 Jun 29 2014 ./.bashrc

    Поиск файлов по правам доступа
        Поиск файлов по правам доступа — отличный способ выявить проблемы с безопасностью или доступом в системе.
        Помимо файлов, где права доступа можно изменять с помощью чисел или букв (командой chmod), существуют и
        файлы, основанные на числовых или буквенных правах доступа с параметром -perm.
        Пример:
            $ find /usr/bin -perm 755 -ls
            $ find /home/chris/ -perm -222 -ls
            $ find /myreadonly -perm /222 -type f
        При поиске с параметром -perm 755 выводятся любые файлы или каталоги с точными правами доступа
        rwxr-xr-x.
        При поиске с параметром -perm -222 выводятся только файлы, имеющие права на запись
        для пользователя, группы и других.
        Используя параметр -perm /222, можно найти любой файл (-type f), у которого есть право на запись для
        пользователя, группы или других.

    Поиск файлов по типу
        Можно искать файлы по типу файла, где d - папка, f - файл
        Пример:
            # find /opt -type f

    Поиск файлов по дате и времени
        Параметры для поиска по времени: -amin, -atime, -cmin, -ctime, -mmin, -mtime
        -amin -> минуты, когда файл в последний раз был прочитан
        -atime -> n*24 часов (т.е. день), когда файл в последний раз был прочитан
        -cmin -> минуты, когда файл в последний раз был изменен
        -ctime -> n*24 часов, когда файл в последний раз был изменен
        -mmin -> минуты, когда в последний раз был изменён inode у файла(inode описан в terms.txt)
        -mtime -> n*24 часов, когда в последний раз был изменён inode у файла

        Метки даты и времени сохраняются для каждого файла при его создании и открытии,
        изменении его содержимого или метаданных. Метаданные включают в себя
        имя владельца, название группы, отметку времени, размер файла, права доступа
        и другую информацию, хранящуюся в дескрипторе файла.
        Пример:
            $ find dir -amin -5 -type f -> находит все файлы в каталоге dir, которые были прочитаны до 5 минут назад
            $ find dir -amin +5 -type f -> находит все файлы в каталоге dir, которые были прочитаны от 5 минут назад
            $ find -name test2 -amin +5 -amin -10 -type f -> находит все файлы в каталоге dir, которые были
                прочитаны от 5 минут до 10 минут назад

    Использование ключевых слов and/or/not при поиске файлов
        С помощью параметров -not и -or(-o) можно дополнительно уточнить поиск. Бывает, что нужно найти файлы,
        принадлежащие определенному пользователю, но не назначенные определенной группе. Эти файлы могут быть
        и большего размера, чем в реальности, и меньшего, чем другие. Или нужны файлы, принадлежащие
        одному из нескольких пользователей. Параметры -not и -or могут помочь со всем этим

        * Существует общий каталог /var/allusers. Эта командная строка позволяет найти файлы, принадлежащие
        пользователям joe и chris
            $ find /var/allusers \( -user joe -o -user chris \) -ls

        * Эта командная строка выполняет поиск файлов, принадлежащих пользователю joe, но только тех, которые
         не назначены группе joe:
            $ find /var/allusers/ -user joe -not -group joe -ls

        * При поиске можно назначить несколько требований. Например, файл должен принадлежать пользователю
        joe и быть более 1 Мбайт:
            $ find /var/allusers/ -user joe -and -size +1M -ls

    Поиск файлов и выполнение команд
        Одна из самых мощных функций команды find — возможность выполнять команды для любых найденных файлов.
        С параметром -exec используемая команда выполняется для каждого выявленного файла без запроса.
        С параметром -ok команда останавливается на каждом совпадении и спрашивает, нужно ли выполнить
        команду для этого файла.

        Преимущество параметра -ok заключается в возможности убедиться в том, что пользователь подтверждает
        любое действие для каждого файла по отдельности. Синтаксис для параметров -exec и -ok один и тот же:
            $ find [ параметры ] -exec команда {} \;
            $ find [ параметры ] -ok команда {} \;

        Можно запустить команду find с любым из параметров, -exec или -ok, чтобы найти нужные файлы. В этом случае
        вводится параметр -exec или -ok, за которым следует команда, которую нужно запустить для каждого файла.
        Фигурные скобки указывают, где в командной строке читать каждый найденный файл.
        Любой файл может быть включен в командную строку не один раз. Чтобы закончить строку, нужно добавить обратную
        косую черту и точку с запятой (\;).
        Вот несколько примеров:
        * Эта команда ищет любой файл с именем passwd в каталоге /etc и включает это имя в выходные данные команды
        echo:
            $ find /etc -iname passwd -exec echo "I found {}" \;
            I found /etc/pam.d/passwd
            I found /etc/passwd
        * Такая команда находит каждый файл в каталоге /usr/share размером более 5 Мбайт. Затем перечисляет
        размеры всех файлов с помощью команды du. Дальше выходные данные find сортируются по размеру, от самого
        большого до самого маленького. При вводе параметра -exec все найденные записи обрабатываются
        без запроса:
            $ find /usr/share -size +5M -exec du {} \; | sort -nr
            116932 /usr/share/icons/HighContrast/icon-theme.cache
            69048 /usr/share/icons/gnome/icon-theme.cache
            20564 /usr/share/fonts/cjkuni-uming/uming.ttc

        Параметр -ok позволяет выбрать, будет ли каждый найденный файл обрабатываться с помощью введенной команды.
        Например, нужно найти все файлы пользователя joe в каталоге /var/allusers и его подкаталогах и переместить
        их в каталог /tmp/joe:
            # find /var/allusers/ -user joe -ok mv {} /tmp/joe/ \;
            < mv ... /var/allusers/dict.dat > ? y
            < mv ... /var/allusers/five > ? n

    Поиск по файлам с помощью grep
        Если нужно выполнить поиск файлов, содержащих определенный поисковый запрос, используйте команду grep.
        С ее помощью можно рекурсивно искать один файл или всю структуру каталогов файлов.

        В поиске нужно напечатать каждую строку, содержащую термин (стандартный вывод), или просто перечислить имена
        файлов, содержащих поисковый запрос. По умолчанию grep выполняет поиск текста с учетом регистра, хотя его можно
        и не учитывать.

        Можно использовать grep не только для простого поиска файлов, но и для поиска стандартных выходных данных.
        Если команда выдает много текста и нужно найти только строки, содержащие определенный текст, применяйте grep
        для фильтрации данных
        Несколько примеров командных строк grep:
            $ grep desktop /etc/services -> 2 строк
            $ grep -i desktop /etc/services -> 29 строк

        Для поиска строк, не содержащих выделенную текстовую строку, используйте параметр -v. В следующем примере
        отображаются все строки из файла, кроме тех, которые содержат текст tcp (без учета регистра)
            $ grep -vi tcp /etc/services

        Для рекурсивного поиска возьмите параметр -r и каталог в качестве аргумента.
        В следующем примере берется параметр -l, который просто перечисляет файлы, содержащие текст поиска,
        не отображая реальные строки. Этот поиск нашел файлы, в которых есть слово peerdns (без учета регистра):
            $ grep -rli peerdns /usr/share/doc/

        В следующем примере выполняется рекурсивный поиск термина root в каталоге /etc/sysconfig. В результате
        перечисляется каждая строка во всех файлах под каталогом, содержащим этот текст. Чтобы выделить термин root,
        добавлен параметр -color. По умолчанию цвет соответствия поиску — красный
            $ grep -ri --color root /etc/sysconfig/
"""