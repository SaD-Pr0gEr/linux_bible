"""
Автозавершение командной строки
    Чтобы вам не приходилось вводить множество сочетании клавиш, интерпретатор
    bash реализует различные варианты заполнения частично введенных значений.
    Чтобы заполнить значение, введите первые несколько символов и нажмите
    клавишу Tab. Вот некоторые значения, которые можно использовать из bash.

    * Команда, псевдоним или функция.
        Если вводимый текст начинается с обычных
        символов, интерпретатор попытается дополнить его командой, псевдонимом
        или названием функции.

    * Переменная.
        Если вводимый текст начинается со знака доллара ($),
        интерпретатор завершает текст переменной из текущей оболочки.

    * Имя пользователя.
        Если текст, который вы вводите, начинается с тильды (~),
        оболочка завершает текст именем пользователя. Тогда ~username указывает на
        домашний каталог пользователя.

    * Имя хоста.
        Если вводимый текст начинается с символа «эт» (@), оболочка завершает текст
        именем хоста, взятым из файла /etc/hosts

После ввода команды вся командная строка сохраняется в истории.
Чтобы просмотреть список истории, используйте команду history. Введите
команду без параметров или с числом после нее, чтобы установить предел отображения
последних команд, например:

history 8
    382 date
    383 ls /usr/bin | sort -a | more
    384 man sort
    385 cd /usr/local/bin
    386 man more
    387 useradd -m /home/chris -u 101 chris
    388 passwd chris
    389 history 8

Перед каждой командной строкой в списке стоит число. Чтобы вызвать одну из
этих команд, используйте восклицательный знак (!). Имейте в виду, что в этом случае
команда выполняется вслепую, без подтверждения оригинала команды. Существует
несколько способов немедленного запуска команды из списка, например такие.

* !n — запустить команду под номером n.
    Замените n номером командной строки, и она будет запущена.
* !! — запустить предыдущую команду.
    Запускает предыдущую командную строку.
* !?строка—? — запустить команду со строкой.
    Запускает самую последнюю команду,
    содержащую определенную строку символов. Например, можно снова
    запустить команду date, просто выполнив поиск части этой командной строки
    следующим образом:
        !?dat? => date
"""
