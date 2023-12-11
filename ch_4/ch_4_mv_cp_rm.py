"""
Перемещение, копирование и удаление файлов
Команды для перемещения, копирования и удаления файлов довольно просты.
Чтобы переместить файл, используйте команду mv . Чтобы скопировать файл,
примените команду cp. Чтобы удалить файл, выполните команду rm. Эти коман-
ды можно использовать с отдельными файлами и каталогами или рекурсивно со
множеством файлов сразу, например:
$ mv abc def
$ mv abc ~
$ mv /home/joe/mymemos/ /home/joe/Documents/
Первая команда mv перемещает файл abc в файл def в том же каталоге (по существу,
переименовывая его), тогда как вторая команда перемещает файл abc в домашний
каталог (~). Следующая команда mv перемещает каталог mymemo (и все его
содержимое) в каталог /home/joe/Documents.
По умолчанию команда mv перезаписывает все имеющиеся файлы, если файл
назначения существует. Однако многие системы Linux используют псевдоним
команды mv с параметром –i, который заставляет mv запрашивать согласие
пользователя перед перезаписью существующих файлов. Вот так можно проверить,
делает ли это ваша система:
    alias mv
    alias mv='mv -i'
Примеры применения команды cp, которая копирует файлы из одного места
в другое:
    cp abc def
    cp abc ~
    cp -r /usr/share/doc/bash-completion* /tmp/a/
    cp -ra /usr/share/doc/bash-completion* /tmp/b/
Первая команда (cp) копирует файл abc в новую папку с именем def в том же
каталоге, а вторая копирует файл abc в домашний каталог (~), сохраняя изначальное
имя. Две рекурсивные копии (-r) копируют каталог bash-completion
и все файлы, которые он содержит, в новые каталоги /tmp/a/ и /tmp/b/. Если
запустить ls -l в этих двух каталогах, то для команды cp, выполняемой с
параметром -a, метки даты/времени и права доступа наследуются. Без параметра
-a используются текущие метки даты и времени, а права доступа определяются
командой umask
Команда cp, как правило, также является псевдонимом с параметром v и предотвращает
случайную перезапись файлов.
Как и у команд cp и mv, у rm обычно есть псевдоним для параметра -i. Это помогает предотвратить
проблему непреднамеренного рекурсивного удаления (-r).
Примеры использования команды rm:
    rm abc
    rm *
Первая команда удаляет файл abc, вторая удаляет все файлы в текущем каталоге
(но не трогает каталоги и/или любые файлы, имена которых начинаются с точки).
Если нужно удалить каталог, задействуйте рекурсивный параметр -r для rm, а для
пустого каталога можно взять команду rmdir, например:
    rmdir /home/joe/nothing/
    rm -r /home/joe/bigdir/
    rm -rf /home/joe/hugedir/
Команда rmdir в этом примере удаляет каталог (nothing), только если он пуст.
Команда rm -r удаляет каталог bigdir и все его содержимое (файлы и несколько
уровней подкаталогов), каждый раз запрашивая разрешение пользователя. При
использовании параметра -f каталог hugedir и все его содержимое немедленно
удаляются без запроса.

Когда параметр -i применяется с командами mv, cp и rm, возникает риск удаления некоторых (или даже многих)
файлов по ошибке. С подстановочными знаками (например, *) и без -i ошибки еще более вероятны. Тем не менее
это не всегда актуально при удалении файлов. Вот что можно сделать.
Как уже отмечалось, с параметром -f можно принудить команду rm удалять файлы без запроса. Можно также
запустить команду rm, cp или mv с обратной косой чертой перед ней (\rm bigdir). Обратная косая черта
приводит к тому, что любая команда выполняется без псевдонимов.
Другой вариант — использовать параметр -b с командой mv. В таком случае, если файл с таким же
именем существует в месте назначения, создается резервная копия старого файла перед перемещением
нового
"""