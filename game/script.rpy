init:
    $ m = Character("[m_name]", color="#8ce2ef")
    $ f = Character("Лиля", color="#82f182")
    $ k = Character("Преподаватель", color="#e54141")
    define fadehold = Fade(0.5, 1.0, 0.5)

    image mel happy:
        "mel happy.png"
        zoom 0.2
    image mel surprised:
        "mel surprised.png"
        zoom 0.2
    image mel sad:
        "mel sad.png"
        zoom 0.2

    image mel uni_happy:
        "mel uni_happy.png"
        zoom 0.2
    image mel uni_surprised:
        "mel uni_surprised.png"
        zoom 0.2
    image mel uni_sad:
        "mel uni_sad.png"
        zoom 0.2


# The game starts here.
label start:

    play music "audio/spokoynaya-fonovaya-muzyika-dlya-povsednevnyih-del-1021.mp3" fadein 1.0 volume 0.2
    scene bg room

    $ m_name = renpy.input("Введите имя своего персонажа").capitalize().strip()

    show mel happy:
        xpos -100 ypos 100
        linear .3 xpos 0 ypos 50
        linear .3 xpos 30 ypos 100
        linear .3 xpos 60 ypos 50
        linear .3 xpos 90 ypos 100
        linear .3 xpos 120 ypos 50
        linear .3 xpos 150 ypos 100
        linear .3 xpos 180 ypos 50
        linear .3 xpos 210 ypos 100

    m "Ох, какой чудесный день! Надо придумать, что бы поделать."

    show mel surprised
    play sound "audio/c3cf4f6cf7f066e.mp3"
    m "О нет! Я совсем забыла! У меня же экзамен через две недели!\nНадо начинать готовиться..."

    show mel sad
    m "Ну вот, придется садиться за билеты..."

    show mel sad:
        xpos 210 ypos 100
        linear .7 xpos 1000 ypos 100

    play sound "audio/8307-obemnyi-stuk-v-dver.mp3" volume 5
    m "Так..."

    m "Это еще кто?"

    show lily happy:
        xpos -100 ypos 100
        linear .5 xpos 150 ypos 100
    f "Привет, [m_name]!"
    with fade

    show mel happy

    m "О, Лиля, привет! Какими судьбами?"
    with fade

    f "Надеюсь, ты не занята, потому что у меня есть к тебе предложение."
    with fade

    m "Нуу.. Я вся во внимании!"
    with fade

    f "Сейчас такое время, что надо выбираться из дома!\nПредлагаю походить по клубам и познакомиться с новыми людьми! Что думаешь?"
    with fade

    play sound "audio/c858f9b13c7c5bf.mp3"
    show mel sad
    m "Блин, это звучит очень классно! Но, кажется, ты забыла, что у нас скоро экзамен..."
    with fade

    play sound "smeh.mp3"
    f "Только не говори, что ты переживаешь по этому поводу!\nЯ сама еще не готовилась и даже не парюсь, бери пример!"
    f "Ну так что скажешь? Нужен ответ сейчас. Пойдешь ли со мной?"

    "Как мне быть?"
    menu:
        "Остаться дома и готовиться к экзамену.":
            return
        "Устроить тур по клубам, конечно!":
            jump pumpum


label pumpum:
    "И правда, сидеть дома довольно скучно, кому это надо!"

    m "Хорошо, погнали!"

    show lily happy_bl
    f "Отлично"

    stop music fadeout 1.0

    show image "images/tomorrow.png"
    play music "audio/orkestr.mp3" fadein 1.0 volume 1.0
    pause 3.0
    scene miserable
    hide image "images/tomorrow.png"
    stop music fadeout 1.0

    play music "audio/morning.mp3" fadein 1.0 volume 0.5
    m "Ядрен батон!"
    m "Уже 12 часов дня! Завтра экзамен, а я даже не начинала готовиться..."
    m "Там 27 билетов, я не успею все их выучить...\nНо если сейчас начну, может быть, отвечу хотя бы на четверочку."
    m "Решено! Челлендж выучить 27 билетов за ночь принят!"

    scene day
    m "Ну все, открываем билеты, учим!"

    menu:
        "Учить билеты":
            $ choice = 1
        "Досмотреть сериал":
            $ choice = 2
    if choice == 1:
        m "Ненадолго отвлекусь, а потом сразу начну билеты."
    if choice == 2:
        m "Всего одну серию. Потом обязательно учить."

    menu:
        "Поиграть в игру":
            $ choice = 1
        "Почитать билеты":
            $ choice = 2

    if choice == 1:
        m "Пять минуточек, а потом сразу за билеты."
    if choice == 2:
        m "Да попозже! Еще времени навалом!"
    stop music fadeout 1.0

    scene night
    play music "audio/saspens.mp3" fadein 1.0 volume 0.2
    m "Вот и день прошел."
    m "Ой, уже стемнело..."
    m "12 часов ночи.. Можно открывать билеты."
    m "Так, посмотрим-с, что тут у нас..."

    scene bilet1
    m "О, что такое сложное предложение?"
    m "Это мы знаем, это мы проходили. Что там дальше?"
    play sound "audio/list.mp3" fadein 1.0 volume 1.0

    scene bilet2
    with fade
    m "О, ССП!"
    m "П-ф-ф, какая-то легкотня эти ваши билеты!"
    m "Можно не учить, мне и так все понятно."
    m "Посмотрим с конца."
    play sound "audio/list.mp3" fadein 1.0 volume 1.0

    scene bilet20
    with fade
    m "..."
    m "Это еще что?"
    m "Что-то не припомню такого на лекциях..."
    m "Ладно, наверное, случайно попался такой. Идем дальше."
    play sound "audio/list.mp3" fadein 1.0 volume 1.0

    scene bilet19
    with fade
    m "..."
    m "......."
    m "Эм... Что за..."
    play sound "audio/list.mp3" fadein 1.0 volume 1.0

    scene bilet16
    with fade
    m "..."
    m "......."
    m "............"
    with fade

    menu:
        "Зарыдать":
            return
        "Разорвать билет на части!":
            jump dontworrybehappy

    stop music

label dontworrybehappy:

    play sound "audio/zvuk-jenskogo-krika-korotkiy_[Pro-Sound.org].mp3"

    scene ripping:
        zoom 1.5
    ""

    play sound "audio/razryiv-bumagi11.mp3" loop

    scene ripped:
        zoom 1.5
    ""

    stop music fadeout 2
    stop sound fadeout 1.5
    scene black
    ""

    play sound "audio/cricket-sound.mp3" loop

    scene night1:
        zoom 5
    show sun:
        xpos 200 ypos 2000
        linear 2.5 xpos 1000 ypos 100

    "Ночь была печальна, временами невыносима..."

    scene day1:
        zoom 5

    show sun:
        xpos 1000 ypos 100

    play sound "audio/bell-sound.mp3"

    "Но наступление утра было неизбежным..."

    play music "audio/spokoynaya-fonovaya-muzyika-dlya-povsednevnyih-del-1021.mp3" fadein 1.0 volume 0.2

    play sound "audio/jg-032316-sfx-breath-and-big-yawn-female.mp3"

    scene bg room
    show mel surprised
    m "Кошмар, уже утро, а я так ничего и не выучила..."
    show mel sad
    m "Ладно, радует, что я всяко такая не одна. Пора собираться на экзамен."

    with fadehold
    show mel uni_sad
    m "Хоть внешне готова."

    scene bg corridor

    show mel uni_sad:
        xpos 3000 ypos 100
        linear 2 xpos 1250 ypos 100

    m "Вот я и тут, мда... Заходить на сдачу совсем скоро."
    m "О, Лиля!"

    show lily happy:
        xpos -600 ypos 100
        linear 1 xpos 150 ypos 100

    f "Привет-привет, [m_name]! Ты как?"
    m "Ну как тебе сказать... Как твоя готовность?"
    f "По нулям."
    m "Аналогично... Мы же с тобой заходим следующими, да?"
    f "Ага, с минуты на минуту"

    stop music fadeout 2

    play music "audio/d00afd0d2142077.mp3" fadein 3.0 loop

    show mel uni_surprised
    k "Заходят следующие, время не тянем!"

    m "О боже.."

    scene black
    ""

    scene classroom

    show lily happy:
        xpos 3000 ypos 100
        linear 2 xpos 500 ypos 100
    show mel uni_sad:
        xpos 3000 ypos 100
        linear 2 xpos 1250 ypos 100

    k "Тяните билет и садитесь готовиться к ответу."

    show lily happy:
        xpos 500 ypos 100
        linear 1 xpos -600 ypos 100

    m "Ладно, хоть бы нормальный билет..."

    scene bilet
    play sound "audio/c2a97f460ec968f.mp3"
    m "Да ладно, вы прикалываетесь?"

    scene classroom

    show mel uni_sad

    "Ну и что же делать? Я не отвечу на этот билет."
    menu:
        "Попытаться ответить на этот билет":
            return
        "Попросить поменять билет, куда уж хуже":
            jump consequencies

label consequencies:
    m "Извините, пожалуйста..."

    scene her
    k "[m_name], у вас есть какие-то вопросы?"

    scene classroom
    show mel uni_sad
    m "Да, скажите пожалуйста, могу ли я поменять билет?"

    scene her
    k "Э, с какой это целью?"

    scene classroom
    show mel uni_sad
    m "Я не уверена, что смогу ответить на данную тему."

    scene her
    k "Что я могу вам сказать, тема является базовой."
    k "Ладно, но, надеюсь, вы понимаете, что за это будут списаны штрафные баллы."
    k "Можете перетянуть."

    scene classroom
    show mel uni_happy
    m "Спасибо большое!"

    scene bilet_my
    play sound "audio/c3cf4f6cf7f066e.mp3"
    m "Ну неет. Это вообще что за слова?"

    scene classroom
    show mel uni_sad
    m "Извините, пожалуйста"

    scene her
    k "Что-то еще?"

    scene classroom
    show mel uni_sad
    m "Я тут подумала, что я все же смогу ответить на вопросы предыдущего билета..."
    m "Могу ли я отвечать его?"

    scene her
    k "Извините, это уже ни в какие ворота.\nОтвечайте на последний вытянутый билет!"

    scene classroom
    show mel uni_sad
    play sound "audio/c858f9b13c7c5bf.mp3"
    m "Я вас поняла."

    "Ну что..."
    menu:
        "Посидеть над билетом":
            jump lasthope
        "Покинуть кабинет":
            return

label lasthope:
    scene bilet_my
    play sound "слеза.mp3"

    "Что ж делать-то?..."
    menu:
        "Нарисовать цветочки с правого края":
            play sound "<from 0 to 1>пишет.mp3"
            jump biletflowers
        "Почеркать листочек снизу":
            return

label biletflowers:
    scene bilet flowers
    "А теперь?..."
    menu:
        "Нарисовать цветочки с левого края":
            return
        "Посчитать свой накоп":
            jump biletmark
        "Почеркать листочек снизу":
            return

label biletmark:
    scene bilet mark
    with fade
    play sound "<from 0 to 1.5>формулу.mp3"
    m "Мда.."
    m "Видимо, придется все-таки как-то рассказывать."
    play sound "перечеркнул.mp3"
    scene bilet no mark

    m "Послушаю, как сдает Лиля. Может, как-нибудь поможет..."

    scene classroom
    with fade
    show lily happy:
        xpos 210 ypos 100
        linear .7 xpos 1000 ypos 100
    play sound "hm.mp3"
    f "Сложное предложение - это..."

    scene bilet no mark
    with fade
    play sound "слеза.mp3"
    m "Ну, конечно, мне как обычно самый легкий билет попался!"
    play sound "слеза.mp3"

    k "[m_name], ваше время вышло!"
    scene classroom
    show mel uni_sad:
        xpos 210 ypos 100
        linear .7 xpos 1000 ypos 100
    m "Настал этот час..."

    k "Ну что, рассказывайте."

    scene her
    k "Что такое структура зависимостей?"
    menu:
        "Это..":
            return
        "Ну...":
            jump well
        "Такая структура, которая зависит.":
            return

label well:
    play sound "broken.mp3" volume 5
    scene her red
    with zoomin
    with pixellate
    stop music fadeout 1


    return
