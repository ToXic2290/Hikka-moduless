from .. import loader

import random

class jarvis_Lib(loader.Library):
  developer = "@ToXicUse"
  version = (0, 0, 1)

  jokes = [
  """
Родился ребенок… И сходу выдает врачам в роддоме:
— Давайте я вам решу квадратное уравнение?
— Давай ты ебало заткнешь?
  """,
  """
  Мама занята на кухне, но краем уха слушает, как её семилетний сын играет со своим новым электрическим паровозиком. Паровозик останавливается — и сынок говорит: - Та-а-ак, все ублюдки, которым надо выходить — жопу от кресел оторвали и нехрен в проходе вафлить — это последняя перед Бостоном остановка… А те сучьи дети, которым в этот сраный город приспичило —тоже нефиг яйца чесать, быстро подорвались в вагон, мы через две минуты отходим. Мама в совершенном шоке бежит в гостиную: - Сынок, ты что! Так дома нельзя разговаривать! Иди сейчас же в комнату и ДВА ЧАСА подумай над тем, что ты сейчас сказал. Когда выйдешь — можешь снова играть с паровозиком… Два часа спустя сынок выходит из своей комнаты и снова играет с паровозиком. Вот паровозик останавливается и мама слышит: - Напоминаем всем пассажирам, покидающим наш поезд, не забывать своих вещей… Благодарим Вас за то, что Вы путешествовали с нами и надеемся вновь увидеть Вас. Уважаемых пассажиров, направляющимся в Бостон, просим занять места; напоминаем, что багаж можно разместить под сиденьями. Просим Вас не курить в поезде. Потом, после небольшой паузы: - А если кого сильно ебет, что поезд с отправкой на два часа опоздал — идите и сами с той пиздой на кухне разбирайтесь.
  """,
  '''
  повадил медведь на пасеку мёд воровать. пасечник уже не знает что и делать: только ружьё в руки берёт, так сразу медведь на дерево залазит, не достать. ну увидел в газете объявление: помогу с любой живностью. вызвал этого мастера, через час приезжает здоровенный мужик с ружьём наперевес и маленькой таксой.
представляет дружка своего:
— это снежок, он нам очень поможет
ну и идут на пасеку к медведю, а тот завидел их — и сразу на дерево. мужик даёт пасечнику ружьё и объясняет:
— я сейчас на дерево залезу и сброшу медведя, а снежок залезет ему в жопу и всё разорвёт. понял?
— понял, а ружьё-то зачем?
— если я раньше упаду — ебашь снежка
  ''',
  '''
  Бежал мальчик по лесу, увидел речку и переплыл ее. Идет дальше.
Потом вспомнил, что он не умеет плавать, вернулся и утонул.
  ''',
  '''
  Пришëл как-то осëл ко льву, и спросил:
— Слушай, а почему это ты царь зверей, а не я? 
— Потому что я тебя заебашить могу и сожрать нахуй. 
— А.
  ''',
  '''
  Поспорили как то американец и русский, чья комната страха страшнее. Зашел, значит, русский в их комнату: скелеты всякие, привидения – в общем, ничего интересного.
Заходит теперь американец к нам, видит: длиннющий темный коридор, а в самом конце грузин на корточках сидит, в руке держит горящую свечку.
Грузин:
- Попа мыл?
- Нет
Грузин молча достаёт тазик с водой...
  ''',
  '''
  Застрял Лев яйцами в коряге, выбраться никак не может. Бежит мимо заяц. Лев кричит:
— Зайчик, помоги! Застрял, выбраться не могу никак.
— Ага, щас, я тебе помогу, вытащу, а ты меня потом съешь.
— Неет, что ты! Клянусь — будешь моей правой рукой!
Ну спас его заяц, а лев, как и обещал, устроил собрание, созвал всех зверей и говорит:
— С сегодняшнего дня Заяц - моя правая рука.
И давай люто-бешено дрочить Зайцем!
  ''',
  '''
  Пришёл чукча в сексшоп и говорит:
— Мне пизда
  ''',
  '''
  Трахают два бизнесмена старика, и один другому говорит:
— Спасибо, что согласились стать моим партнером, с вами приятно иметь деда.
  ''',
  '''
  Загадка: В здании их четверо, и только один работает.
Отгадка: Три чиновника и вентилятор.
  ''',
  '''
  Молодой человек пришел к Великому Мастеру.
— Великий Мастер, научите меня КунгФу.
Великому Мастеру было лениво. Но отказывать в просьбе он не стал, а сказал:
— Да, хорошо, я научу тебя КунгФу. Но я не беру щас учеников. Приходи через год.
Молодой человек ушел. Но через год возвращается.
— Великий Мастер, научите меня КунгФу.
Великий мастер помрачнел и говорит:
— Да, я научу тебя КунгФу. но для этого ты должен работать над собой. В течение 3 лет каждое утро созерцай как восходит солнце, и каждый вечер созерцай как оно садится.
Молодой человек ушел. Но через 3 года возвращается.
— Великий Мастер! Три года каждое утро я смотрел как восходит солнце и каждый вечер- как оно садится. Научите меня КунгФу.
— Да,-сказал Великий Мастер.-Но прежде ты должен научиться зависать на высоте 5 метров от земли.
Молодой человек ушел. Но через 5 лет вернулся.
— Великий Мастер. 5 лет каждый день я посвящал себя тренировкам, и теперь я могу зависать над землей,- сказал молодой человек и завис на высоте 5 метров от земли.
— Нихуя себе - сказал Великий мастер
  ''',
  '''
  В чём сходство между детьми и сотовой связью?
.
.
.
.
.
.
.
.
.
Они пропадают в лесу
  ''',
  '''
  Экзамен по анатомии.
Студенты опускают по очереди руку в анатомический мешок и на ощупь
определяют органы…
Одна студентка долго щупает, краснеет и выдает растерянно:
— Сосиска…
Два старых профессора переглядываются и говорят:
— Вы не спешите, хорошо подумайте…
— Ну сосиска, я Вам говорю…
Девчонка вынимает руку из мешка, а там действительно сосиска!
Один профессор другому:
— Послушайте, Станислав, а мы вчера хуев наелись.
  ''',
  '''
  ебутся два гея в сраку, один другого спрашивает:
— чувствуешь, как глубоко?
— да-а
— а в курсах программирования от skillbox уровень изучения наиболее востребованных языков ещё более углублённый, лови два занятия по промокоду бесплатно
  ''',
  '''
  Выбирает электрик в магазине стремянку.
Продавец:-Вам полтора метра иди два с половиной?
Электрик:-Мне до лампочки.
  ''',
  '''
  Умирает человек, попадает в рай. Его встречает апостол Петр.
Человек: Простите, что вас беспокою, но у меня к вам есть один вопрос
Апостол: Слушаю вас
Ч: Я прожил довольно долгую жизнь, но так и не понял одного. Скажите, в чем был смысл моей жизни?
А: Вам правда нужно это знать?
Ч: Очень
А: Помните, вы 1973 году ехали в поезде Москва-Краснодар?
Ч: Э-э.. ну..
А: И вы еще познакомились в купе с попутчиками
Ч: Наверное..
А: И вы пошли вместе в вагон-ресторан
Ч: Да..
А: И за соседним столиком сидела женщина
Ч: Возможно..
А: И она попросила вас передать ей соль
Ч: И я ей передал соль.
А: И вы передали ей соль
Ч: Передал.
А: Ну и вот..
  ''',
  '''
  Пока не начинаешь в солнечный день наблюдать за жизнью муравьев через увеличительное стекло, тебе и в голову не приходит, как часто эти создания вдруг ни с того ни с сего вспыхивают огнем.
  ''',
  '''
  Спорят двое мужиков в кафе. один другому:
— Хрухт
— Нет, Трухт
— Нет, Прухт
Рядом сидящая женщина слышит это и решает им помочь и говорит:
— Наверное "Фрукт!", "Фрукт!" так правильнее звучит!
Мужчина спрашивает:
— Ну а вы то откуда знаете как пердит жираф?
  ''',
  '''
  Попал мужик в матрицу. К нему подходит негр в очках, протягивает руки с пилюлями в руках и говорит:
-Если примешь красную, то у тебя будет член 40 см
-А если синюю?
-А нахуя тебе синяя?
Ну мужик взял красную, съел и вырубился. Негр, снимая штаны:
- Я же не уточнил, ГДЕ он у тебя будет, и ЧЕЙ это будет член.
  ''',
  '''
  В семье лимонов горе - семейный бизнес отжали, компанию выдавили с рынка, отец устал и выжат, а у матери кислое настроение
  ''',
  '''
  Ебет мужик тянку и тут хуяк бьет ей по ебалу, она спрашивает за что?, он отвечает - да сиськи у тебя маленькие, повернись, ебет ее уже сзади и тут снова хуяк ей по затылку, она спрашивает а это за что? Он отвечает да жопа у тебя маленькая, повернись на бок, ебе ее уже боком и тут хуяк ей по по почках, она спрашивает да за что сейчас то? Он говорит -да ты вся маленькая, а она отвечает, - ну а хули ты в дай винчике знакомишься
  ''',
  '''
  Лев гуляет по лесу. 
Встречает жирафа: 
- Эй, длинношеий! Кто самый храбрый в лесу? 
- Ты, лев! 
Лев довольно улыбнулся и идет дальше. 
Видит зебру: 
- Эй, полосатая! Кто самый красивый в лесу? 
- Конечно ты, лев! 
Лев, гордый, пошел дальше.
Видит слона: 
- Эй, длинноносый! Кто самый умный в лесу? 
Слон берет льва хоботом, перебрасывает через свою спину и зашвыривает в болото. Лев вылазит, отряхивается от тины и говорит: 
- Ну зачем же так нервничать? Мог бы просто сказать "Я не знаю".
  ''',
  '''
  Под новый год Лупа и Пупа купили сосну и ёлку. Лупа решил украшать сосну, а Пупа ёлку. Но жена Лупы сказала, что не любит сосны, и предложила им поменяться.
С неизменной готовностью помочь другу, Пупа гордо воскликнул: "Ради друга я даже возьму и сосну за Лупу!"
  ''',
  '''
  Когда-то в одной очень хорошей семье родился мальчик. Он рос очень правильным и послушным сыном. Школу закончил на одни пятерки. Пошел в армию и в одной из переделок потерял ногу - ампутировали ниже колена. Но жизнь ведь на этом не кончается. Демобилизовался и приехал назад в родной город. Нашел себе работу, и однажды познакомился с одной очень хорошей девочкой из одной очень интеллигентной семьи. Они долго-долго встречались. Ходили в театры, филармонию, на выставки и в кафе кушать мороженое. Молодой человек не позволял себе никаких вольностей по отношению к своей девушке. Они познакомили друг друга со своими родителями. И он, и она им понравились. Только вот молодой человек стеснялся как-то сказать любимой девушке о своем увечье. И вот наконец через полтора года они решили пожениться. После веселой и красивой свадьбы пришло время первой брачной ночи. Девушка первой ушла в спальню, разделась и легла. Молодой человек, войдя в комнату, выключил свет, присел на кровать и, незаметно отстегнув и сняв протез с ноги, скользнул под одеяло к возлюбленной. Нежно поцеловав ее в лоб и, взяв ее руку в свою, он, немного смущаясь, положил ее руку себе на культю и сказал: - Милая, ты знаешь, я давно уже хотел сказать тебе... И... услышал в ответ: - Хуйня! Влезет!
  ''',
  '''
  Мужик пожал плечьми, ничего не понял и пошел своей дорогой. А навстречу идет бабка и спрашивает: "Сынок ты здесь козы негде не видел?". "Да 2 секунды назад прыгнула в колодец". Бабка аж ахнула: "Как в колодец? Я ж ее к рельсе привязала!".
  ''',
  '''
  Всплеск был такой, что аж вода выплеснулась наружу - КРАСОТА. Вдруг смотрит по полю с бешеной скоростью несется коза и со всего размаху прыг в колодец.
  ''',
  '''
  Ему понравилось - он нашел кирпич и бросил его в колодец, всплеск удался на славу. Мужику очень понравилось, посмотрел вокруг - лежит кусок рельсы, он и его туда-же.
  ''',
  '''
  Идет мужик по полю, смотрит - колодец. Заглянул, а там так глубоко, что даже воды не видно. Бросил мужик маленький камушек и начал считать время - 20 сек.
  ''',
  '''
  У парня по имени Ответ с детства были жутчайшие комплексы по поводу лишнего веса. И вот как то он влюбился в девушку и это вылилось в женитьбу. Первые годы все шло чудесно, они жили в мире, но как-то жена Ответа решила его подколоть. И говорит мужу: — Ну и пузо ты отрастил! Ответ убил.
  ''',
  '''
  Три алкоголика поспорили, у кого больше руки дрожат.
Первый говорит:
- Я, когда из бутылки в стакан наливаю, так в стакан только 100 грамм попадает, все остальное мимо.
Второй говорит:
- Я, когда из бутылки в стакан наливаю, так в стакан только 50 грамм попадает.
Третий говорит:
- А я когда писаю, так три раза кончаю.
  ''',
  '''
  Стояли третьеклассники на перемене и спорили кто круче:
-У меня есть колонка JBL!! - сказал один из них
-А у меня есть девушка!! - сказал второй
-А я с другом ходил в стриптиз клуб!!! - сказал третий
Все ахнули от удивления. Спрашивают у него:
-И как там, что делал?
А он им в ответ:
-Я просто маму ждал на работе
  ''',
  '''
  Одна тётка как-то пыталась купить в Германии мышеловку, хотя немецкого не знала. Она подошла к продавцу и довольно громко произнесла:
– Микки Маус капут!
  ''',
  '''
  В психушке один псих подходит к другому и говорит:
— Слушай, я тут книгу написал, хочешь почитаем?
Уединились они в палате и начали читать. Первый псих спрашивает:
— Ну как, понравилось?
— Классно, только действующих лиц много.
Тут заходит медсестра и говорит:
— Психи, кто из вас спер телефонный справочник?
  ''',
  '''
  Мужик приходит к председателю колхоза и говорит: "Возьмите меня зоотехником" — А что ты умеешь делать? — Я понимаю язык животных. — Ну ладно, пойдем на ферму. Подходят к корове. Мужик: "Му-у-у!" Корова: "Му-у-у!" — Она сказала, что дала 15 литров молока. Доярка сдала 10, а 5 домой отнесла. Пришли к доярке, обыскали, так и есть — 5 литров в заначке. 

Подходят к свинье. Мужик: "Хрю-ю-ю!" Свинья: "Хрю-ю-ю!" — Она говорит, что принесла 7 поросят, но свинарка двух унесла домой. Обыск и свинарки, находят двух поросят. 
— Ну ладно, беру тебя, — говорит председатель. 
Идут по улице. Навстречу собака: "Гав-гав-гав!". Мужик:
— Скажите, у вас живёт в селе некий "Кац"?
  ''',
  '''
  Водитель троллейбуса съел сникерс и не тормозил 10 остановок
  ''',
  '''
  Бог прокрастинации обрушил на землю великий потом.
  ''',
  '''
  Умерли в одно время русский бурый медведь и американский гризли и угодили в преисподнюю. Там их встретил чёрт и спросил:
— Так, у вас есть выбор: каждый из вас может пойти либо в русский, либо в американский ад.
Медведи переглянулись и спросили:
— А чем они отличаются?
— Всё просто. В американском аду нужно гореть в машине по часу в день, а в русском — по два часа.
Гризли выбрал свой ад, а бурый , поразмыслив, решил, что и так всю жизнь прожил в России, нечего и в загробном мире что-то менять, и выбрал русский ад.
Через месяц гризли и бурый медведь встретились и стали обмениваться впечатлениями. Сначала рассказал гризли:
— В нашем аду прекрасные условия! Утром сгорел за час, и всё, гуляй свободно целый день! А у вас как?
— Ой, а у нас как всегда, — ответил бурый, — то огня на всех не хватит , то машин не завезли …
  ''',
  '''
  - Паш, слушай, у тебя ведь фамилия Черный?
- Ну да.
- Назови сына Плащом! Прикинь, в школе:
"Еблан с тупым именем, к доске!".
  ''',
  '''
  Мужик приперся к доктору и говорит:
- Доктор, сегодня утром просыпаюсь, член стоит, сходил в туалет, он упал!
- Ну это нормально, у многих по утрам стоит, а после мочеиспускания падает...
- Ну не в унитаз же!
  ''',
  '''
  Oдин 80-лeтний стapик пришел к врачу на медосмотр.
- Ну, как вы себя чувствуете? - спрашивает его врач.
- Лучше, чем когда-либо, - браво отвечает старичок, - у меня 18-летняя подруга, она беременна и скоро родится наш ребенок. Ну, что скажете, доктор?
Ничего не ответил доктор, лишь молча пошевелил хуем в жене старика
  ''',
  '''
  Мужик спрашивает у араба:
— Слушай, вот никак не могу понять, зачем вашим женщинам эта тряпка на голове - паранджа или как её?... Лица не видно, дышать невозможно, есть сложно... Ну нафига?
Араб молча достаёт из кармана две шоколадные конфеты и протягивает на ладони. Одна в обёртке, другая без. Та, что без фантика, уже слегка облупившаяся, к ней какой-то мусор из кармана прилип, крошки...
— Вот ты бы какую выбрал?
— Без обёрттки.
— Блядь.
  ''',
  '''
  Мужик спрашивает у араба:
— Слушай, вот никак не могу понять, зачем вашим женщинам эта тряпка на голове - паранджа или как её?... Лица не видно, дышать невозможно, есть сложно... Ну нафига?
Араб молча достаёт из кармана две шоколадные конфеты и протягивает на ладони. Одна в обёртке, другая без. Та, что без фантика, уже слегка облупившаяся, к ней какой-то мусор из кармана прилип, крошки...
— Вот ты бы какую выбрал?
— Со всем уважением, но твоя аналогия не имеет ничего общего с реальностью. В настоящей жизни люди и в частности женщины не теряют в своих качествах, если ходят без обертки в виде паранджи. Это унизительно, что ключевым качеством для мужчины в выборе партнера является то, что женщина обязана подчиняться и быть полностью зависимой от одного мужчины, который упивается удовольствием от обладания такой "вещью". В здоровых отношениях оба партнера имеют равные возможности для участия в отношениях и не навязывают друг другу свои взгляды.
Араб молча пошевелил бомбу хуем.
  ''',
  '''
  - Марь Иванна, у меня нет ручки!
- Петров, ты нам про свой Вьетнам каждый день рассказывать будешь?
  ''',
  '''
  Переполненный автобус в Киеве. Стоит хохол в шароварах с гарными усами. На сиденье напротив сидит 100%-ный негр и читает газету "Жовтневий прапор" на украiiнской мовi.
Хохол его так осторожно спрашивает: А шо, пан розумие нашу мову?
Негр: А як же.
Хохол, после раздумья: Так може пан ще й хохол?
Негр: А як же.
Хохол, после долгого раздумья : А я тоди кто ж?
Негр: Та може и москаль...
  ''',
  '''
  Бежал мальчик по лесу, увидел речку,переплыл ее. Идет дальше.
Потом вспомнил, что он не умеет плавать, вернулся и утонул.
  ''',
  '''
  Приходит домой очень пьяный режиссёр театра. Жена
открывает дверь, он ей с порога:
- Тазик, блевать-с буду!!!
Жена метнулась за тазиком, приносит, режиссёр, подняв
указательный палец:
- СТОП! Концепция изменилась! Я ОБОСРАЛСЯ!
  ''',
  '''
  На призывной медкомиссии:
- Вы всегда заикаетесь?
- Н-н-нет, т-т-только к-к-когда г-г-говорю.
  ''',
  '''
  Купили раввин и батюшка вскладчину автомобиль. Чтобы не спорить, решили, что ни к какой конфессии их покупка относится не будет. Но батюшка не утерпел и тайком от раввина все-таки окропил машину святой водицей. Наутро просыпается, а у машины выхлопная труба на 5 сантиметров обрезана.
  ''',
  '''
  Новый год.
Сидит салат в желудке, вдруг на него что-то сверху падает. Он спрашивает:
– Ты кто?
– Водка!
– За кого пили?
– За Иван Иваныча!
Через некоторое время снова что-то падает сверху.
Салат:
– Ты кто?
– Водка!
– За кого пили?
– За Иван Иваныча!
И опять падает. Салат:
– Ты кто?
– Водка!
– За кого пили?
– За Иван Иваныча!
– Ну-ка, пойду посмотрю, что там за Иван Иваныч!
  ''',
  '''
  Новосибирск, зима. Около запорошенного снегом гаишника останавливается иномарка, из неё выходит японец и говорит: — Оясуминасай, сумимасэн, омавару-сан, доко-дэ ватаси-ва коно юкитоси-ни Кока-Кола-но кан-о коубаймас-ка?. На что гаишник ему отвечает: — Извините, я не понял. Вы спрашиваете, где в этом печальном заснеженном городе купить бутылочку чего?
  ''',
  '''
  Трахаются в общаге студенты - в комнате 5 парней и 5 девочек, охи, ахи, скрип кроватей, все без слов. Вдруг один парень подает голос: - Хотите, анекдот расскажу? Девушка: - Только не пошлый!
  ''',
  '''
  Однажды Бернард Шоу обронил фразу, что все женщины продажны. Английская королева, узнав об этом, при встрече с Шоу спросила:
- Верно ли, сэр, что вы утверждаете, будто все женщины продажны?
- Да, ваше величество.
- И я тоже?! — возмутилась королева.
- И вы тоже, ваше величество, — спокойно ответил Шоу.
- Ну бля, сколько?! — вырвалось у королевы.
- Немало, — тут же определил Шоу.
- Бля, ты мне мозги не еби, я спрашиваю сколько?! — возмутилась королева.
- Ну эээ... 65 плюс ещё 20 и эээ..., — пробормотал драматург.
- Лан, заткнись. — подытожила разговор королева.
  ''',
  '''
  На работе женщины решили, из щепетильности, процесс когда их хорошо оттрахали называть не "Сексом", а ``Приветом``.
Приходит одна на следующий день на работу и говорит ``Привет``!
Приходит другая - ``Привет, привет``! Все вокруг с завистью - вот муж как любит жену!
Приходит третья - ``Привет, привет, большой привет и утром два привета``!
Мимо проходит начальник и говорит:
-- Мистер Анджело?
— Да…
— Мистер Сальери передаёт вам привет!
  ''',
  '''
  Мужик уезжает на один день в командировку и просит товарища проследить в бинокль за его женой. Вернувшись слушает доклад друга:
— Устроился я, значит, на чердаке с биноклем. Жду. В семь вечера идёт твоя жена в прихожую, открывает дверь. Заходит какой-то грузин в белом костюме, с цветами и вином. Накрыли стол, поужинали при свечах. Потанцевали. А потом грузин её поднял и понёс в спальню.
— А в спальне-то что было?
— Я не видел — они сразу окна зашторили.
Мужик, яростно мастурбируя:
— Ну так, блять, придумай же что-нибудь!
  ''',
  '''
  Сидит мужик на двух хуях, в руках тоже держит две пары хуёв, отсасывает хуй своим ртом и при это одновременно со всем этим вокруг него стоят мужики и наяривают на него.
Заходит в этот момент парень в эту комнату и говорит всем:
- Ребята, а вы смотрите аниме?
Мужик вытаскивает два хуя со рта и говорит ему:
- Пошёл нахуй пидор
  ''',
  '''
  Приехал мужик в Японию. По-японски ни слова. И вот ему захотелось что-нибудь почитать. Приходит он в магазин,а там продавец черный. Он подходит к продавцу и говорит: "дай манги"
  ''',
  '''
  Экзамен по анатомии.
Студенты опускают по очереди руку в анатомический мешок и на ощупь
определяют органы…
Одна студентка долго щупает, краснеет и выдает растерянно:
— Сосиска…
Два старых профессора переглядываются и говорят:
— Вы не спешите, хорошо подумайте…
— Ну сосиска, я Вам говорю…
Девчонка вынимает руку из мешка, а там действительно сосиска!
Один профессор другому:
— Послушайте, Станислав, а мы вчера хуев наелись.
  ''',
  '''
  Один грузин хотел поебаться, а как будет "женщина" по-русски забыл. Подходит он к мамке в борделе и спрашивает:
— Трап без хуя есть?
  ''',
  '''
  Жена развелась с индейцем из-за его нелепого имени, но дети остались с Разбитым Ебалом
  ''',
  '''
  Почему Джорджа Флойда уволили из компании?

Не пришел на брифинг
  ''',
  '''
  В класс заходит новый учитель с огромным косяком, садится, запаливает, тянет…
— Дети, я ваш новый учитель биологии, Пётр Сергеевич…
Затягивается, выдыхает…
— Сегодня я расскажу вам про рыбу–пилу…
Затягивается…
— Эта рыба обитает на са–а–амом дне океана, у дна, в вечной мгле…
…ещё тяжка…
— Но иногда она выходит на берег, и начинает пилить деревья…
Затягивается, выдыхает… задумчиво:
— Пиздец… Ебанутая рыба…
  ''',
  '''
  Два брата грузина купили себе по лошади. Катались до вечера. Загнали в конюшню и говорят:
- Как мы их различать будем?
- Давай я своему ухо отрежу. У меня будет конь с одним ухом, а у тебя с двумя.
- Хорошо.
Подслушивал их сосед и завидовал. Запрыгнул в конюшню и отрезал ухо. На следующий день братья приходят и видят двух коней без одного уха. Покатались и говорят:
- Как их теперь различать будем?
- Давай я своему ухо отрежу. Будет у тебя конь с одним ухом, а у меня конь без ушей.
- Хорошо.
Подслушивал их сосед. Запрыгнул в конюшню и отрезал ухо. На следующий день братья приходят и видят двух коней без ушей. Покатались и говорят:
- Как их теперь различать будем?
- Давай я своему хвост отрешу. У будет конь без ушей с хвостом, а у меня без ушей без хвоста.
- Хорошо.
Подслушивал их сосед. Запрыгнул в конюшню и отрезал хвост коню. На следующий день братья приходят и видят двух коней без ушей и без хвостов. Говорят:
- Как мы их теперь различать будем?
- Давай твой тот чёрный , а мой белый.
  ''',
  '''
  Ехал мужик на машине и приспичило ему посрать. Он остановился, вышел в поле и сел. Тут к нему подбегает мышка и говорит:
— Я мышиный король и могу исполнить любое твое желание.
Мужик отвечает:
— Построй передо мной народ свой мышиный.
Король привел к нему весь свой народ, а мужик берет мышек горстью и начинает ими жопу вытирать. А король ему кричит:
— Остановись, долбоеб, у нас бумага есть!
  ''',
  '''
  Женщина ловит такси. Конец рабочего дня. Таксисты едут в парк. 
Вдруг один останавливается и спрашивает: 
— Если подвезу, за щеку возьмешь? 
— Да, ради Бога, - отвечает женщина и залезает в машину. 
Приезжают на место. Женщина вылезает из машины, треплет таксиста за щеку и говорит: 
— Смешной вы народ, таксисты!
  ''',
  '''
  Стоит наркоман, дует. Вдруг увидел мента и побежал, мент за ним. Наркоман забегает в открытый подъезд, заходит в подвал и видит, что он весь застален старинными греческими статуями. Ну наркоман и решил раздеться и встать как статуя, чтобы не нашли. Разделся, встал, и тут одна статуя ему говорит:
— Носки сними, а то всех спалишь
  ''',
  '''
  Мужик возвращается из командировки, заходит в комнату - жена в кровати, а рядом с кроватью стоит голый грузин в кепке и радостно так улыбается. Охреневший муж грузину:
– Ты кто?
Грузин (уже не улыбаясь):
– Я Аянами Рэй
  ''',
  '''
  - На следующей выходите?
- Нет..
- Зря! Охуенная остановка!
  ''',
  '''
  Я не верю в эволюцию. Если бы это было правдой, то чёрные уже давно были бы пуленепробиваемыми.
  ''',
  '''
  Два мужика сидят в баре.
— Как ты определяешь, когда пора делать уборку в квартире?
— Я засовываю руку в трусы. Если там до сих пор есть хуй, значит ещё не пора
  ''',
  '''
  Час пик. Метро. Тут в толпе начинает орать мужик:
- Люди, помогите! Мой сын подавился пятаком и задыхается!
Тут сквозь толпу проламывается толстая такая тетка, хватает пацаненка за яйца и сильно сжимает их!
У пацана тут же из глотки вылетает пять рублей и дикий вопль «А-а-а-а-а!!!!!»
Отец – тетке, с уважением:
- Вот это да! Вы, наверное, работаете в скорой помощи?..
- Да нет. В налоговой.
  ''',
  '''
  Шутить над жирными карлицами - это толсто и низко
  ''',
  '''
  Едет значит таксист вечером. Его останавливает сексапильная дама и просит довезти. Таксист соглашается. Доезжают до места она ему говорит:
- Слушай, мужик, понимешь, денег нет. Может натурой возьмешь?
- Да ты что??!!! Ты у меня уже восьмая такая сегодня. Никаких сил на вас не хватит. Ладно, подожди, щас все оформим.
Выходит из машины, ловит первого попавшегося прохожего и говорит:
- Эй, приятель, хочешь девку за полтиник?
- Давай конечно.
- Вон там в машине сидит, скучает.
Мужик пошел, залез в машину, делает свое дело. И тут идет наряд милиции.
Один из ментов светит фонариком в машину и говорит:
- Ты что это делаешь?
- А ты не видишь, жену трахаю.
- Ааааа. А я думал бл@дь.
- Да я тоже так думал, пока ты фонариком не посветил...
  ''',
  '''
  Маленький мальчик ел суп в кафе под открытым небом. И никак не мог его доесть. А потом дождь закончился.
  ''',
  '''
  Призвал бог к себе трех грузинов и говорит:
— У меня для вас есть задание. Кто его первым выполнит — тому я исполню любое желание.
А они нихуя иврит не понимают. Постояли так и ушли обратно.
  ''',
  '''
  Междyнаpодные автогонки. Крутой поворот перед самым финишем.
Янки сбрасывает скорость до 100км/ч и аккуратно вписывается
в поворот. Следом за ним едет француз - притормаживает до 150
и все-таки вписывается, но с трудом - по самому бортику.
Следом едет русский. Топчет тапочкой пол, на 300 км/ч спокойно
обходит соперников самой короткой тропой и успевает к финишу
первым. Hа финише вокруг него мечутся журналисты
- Как же вам это удалось?
- Чо удалось?
- Ну скорость же большая, радиус поворота маленький - значит,
центробежная сила большая, должна сносить. Это законы физики,
с ними не поспоришь
- У меня по физике 3 была
  ''',
  '''
  На каннибал шоу "Поле чудес" бабушка привезла 5 килограмм маринованного внука.
  ''',
  '''
  Штирлиц шел по лесу. Увидел человека в фуфайке и на лыжах.
Фуфлыжник, - подумал Штирлиц.
  ''',
  '''
  Приходит чукча с сыном к врачу и говорит: 
– Доктор, мой сын ничего не ест: ни масла, ни мяса, ни хлеба. 
– Почему? 
– Нету.
  ''',
  '''
  Заблудились два вегана в лесу.
В итоге один перестал быть веганом, а другому Цаствие Небесное.
  ''',
  '''
  Идет лекция по математике, в аудитории лектор и 3 студента. 
Внезапно встают 5 человек и уходят. 
Лектор: 
- Вот сейчас придут еще двое, и вообще никого не останется.
  ''',
  '''
  — Какая разница между коммунистом и антикоммунистом? 
— Коммунист — это человек прочитавший работы Маркса и Ленина, а антикоммунист — это тот, кто их понял.
  ''',
  '''
  Заходит мужик в еврейский ресторан, а там плакат:"Ешьте, пейте бесплатно. За вас заплатят правнуки! "
Мужик наелся, напился.
Официант приносит счёт, .
- Но ведь за меня заплатят правнуки!?
- Да, но это счет вашего прадедушки.
  ''',
  '''
  Два электрика на столбе сидят, на земле провод валяется.
Смотрят: бабулька идёт.
Они ей:
— Бабка, ты аниме смотришь?
Бабулька кричит:
— Да ну, милок, это кринж
Один другому:
— Я говорил "кринж", а ты "база-база"...
  ''',
  '''
  Мой муж — мой непосредственный руководитель на работе.
В этом есть свои плюсы — можно переспать с начальником, и ничего тебе за это не будет.
Но есть и минусы — можно переспать с начальником, и ничего тебе за это не будет.
  ''',
  '''
  Умерла проститутка. Похороны. Двое мужчин разговаривают:

- Наконец они вместе ..

- Кто?

- Ноги.
  ''',
  '''
  Решил поиграть в симс

Запер семью в комнате с камином

Все сгорели

Запустил симс
  ''',
  '''
  Джин говорит парню
-Я исполню любое твое желание, но у твоего врага будет это же желание но в двойне, дак что же ты хочешь?
-Отца
  ''',
  '''
  — Дорогой, скажи, меня эти джинсы не полнят? 
— Ты не обидишься, если я скажу правду? 
— Ну что ты, нет. 
— Я сплю с твоей сестрой.
  ''',
  '''
  Говорила мать Егору, что его привычка совать пальцы в розетку до добра не доведёт.
Слова её оказались пророческими. Однажды, Егор был жестоко изнасилован.
  ''',
  '''
  Заходит человек в магазин тканей:
— Отмерьте мне 4 метра этой ткани в горошек
Продавец отмеряет
— Теперь порежьте на полоски, чтоб горошинки не порезать
Продавец режет
— Теперь порежьте на квадратики, чтоб в каждом была горошинки
Продавец режет
— Теперь вырезайте горошинки
— Молодой человек, вы ебанутый?!
— Да, вот справка
  ''',
  '''
  Был один парень, которого заколдовала колдунья, и он мог говорить только одно слово в год. И когда этот парень влюбился, он не говорил 8 лет и сказал ей
-я могу говорить только одно слово в год
-почему?
  ''',
  '''
  Идёт армянин по улице. Смотрит - его сосед на дереве сидит, а под ним носорог спит, рядом машина соседская развороченная, а в районе его дома дым. Армянин подбегает к дереву:
-Ашот, дарагой, чьто слючилось, откуда зверюг этот взялся?
-Эээ, Вазген, как брата тэбя прошу, найди блэт ту сюку, которая мине вместо нард этот Джуманджи подсунула!
  ''',
  '''
  Приходит как-то девушка к Конфуцию и говорит:
— Конфуций, почему многожёнство это нормально, а многомужество - плохо?
Конфуций от неожиданности поперхнулся чаем и крикнул:
— Да ёб твою мать, опять забыл дверь на щеколду закрыть! Иди отсюда!
  ''',
  '''
  Сержант прибегает к прапорщику:
- Товарищ прапорщик! Солдаты в казарме ебут вола!!! Нужно что-
то делать!
Разъярённый прапорщик врывается в казарму и всех строит.
- Ну-ка, сволочи, кто ебал вола - шаг вперёд!!!!
Из строя вышли все, кроме одного солдата.
- Вот молодец! - обращается прапорщик к оставшемуся, - Не смотря на
трудности, связанные с отсутствием женского пола, остался настоящим
солдатом! Как фамилия, сынок?
- Вол.
  ''',
  '''
  у моей большие сиськи!
- А у моей классная попка!
"А у моей огромный член", - подумал Игорь, но перед пацанами хвастаться
не стал...
  '''

  ]