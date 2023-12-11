"""
Мощной особенностью интерпретатора является возможность перенаправления
ввода и вывода команд в другие команды и файлы и обратно. Чтобы связать
команду, интерпретатор применяет метасимволы

Метасимвол
    это печатный символ с особым значением для командного интерпретатора:
    он соединяет и расширяет команды.
К метасимволам относятся символ конвейера (|), амперсанд (&), точка с
запятой (;), правая скобка ()), левая скобка ((), знаки «меньше» (<) и «больше» (>).
В следующих разделах мы рассмотрим, как использовать метасимволы в командной
строке для смены поведения команд.

Расширение команд с помощью конвейера
    Метасимвол конвейера (|) соединяет выходные данные одной команды с
    входными данными другой. Таким образом одна из команд может предоставлять данные,
    а другая — результаты. Вот пример командной строки, которая включает в себя
    конвейеры:
        cat /etc/passwd | sort | less
    Эта команда выводит список содержимого файла /etc/passwd и передает выходные
    данные в команду sort . Команда sort собирает имена пользователей,
    которые начинаются с каждой строки файла /etc/passwd, сортирует их в алфавитном
    порядке и передает выходные данные команде less (чтобы пролистать выходные данные).

Последовательные команды
    Может потребоваться выполнить последовательность команд, причем предшествующая
    команда должна завершаться до начала следующей. Это возможно,
    если ввести несколько команд в виде одной командной строки, разделив их точкой
    с запятой (;):
        date; troff -me verylargedocument | lpr; date
    В этом примере я форматировал огромный документ и хотел знать, сколько
    времени это займет. Первая команда (date) показывала дату и время до начала
    форматирования. Команда troff отформатировала документ, а затем передала
    вывод на печать. Когда процесс форматирования закончился, дата и время отобразились снова,
    так я узнал, сколько времени потребовалось команде troff для его завершения.

Выполнение команд в фоновом режиме
    Выполнение отдельных команд может занять некоторое время. Однако бывает, что
    интерпретатор необходим и для других дел и нет возможности дожидаться окончания
    работы такой команды. В таких случаях можно запустить команды в фоновом режиме с помощью
    амперсанда (&).
    Далее приведен пример команды, выполняемой в фоновом режиме:
        troff -me verylargedocument | lpr &
    Не закрывайте интерпретатор, пока процесс не закончится или не будет завершен принудительно.

Расширение команд
    С помощью подстановки команд можно получить выходные данные команды,
    которые интерпретирует оболочка, а не сама команда. В таком случае стандартный вывод одной
    команды может стать аргументом для другой. Две формы
    подстановки команд — это $(command) и `command` (обратные кавычки, а не одинарные).
    Команда в этом случае может включать параметры, метасимволы и аргументы.
    Далее приведен пример использования подстановки команд:
        vi $(find /home | grep xyzzy)

!!!ВНИМАНИЯ!!!
    Разница между ; и && в том, что если первая команда провалится, 2я в любом случае будет
    вызвана благодаря ;, а с && 2я команда выполняется только если 1я команда отработала успешно

Выполнение арифметических операций
    Бывает, необходимо передать команде арифметические результаты. Существуют
    две формы для расширения арифметического выражения и передачи его в интерпретатор: $[выражение]
    например:
        echo "I'm $[$(date +%Y) - 2001] years old"
    Другой пример:
        echo "There are $(ls | wc -l) files in this directory."
        echo "There are $(cat PycharmProjects/NeuroGPT/requirements.txt | wc -l) requirements"
"""
