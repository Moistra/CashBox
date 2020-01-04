# CashBox patterns
### Singletone
Данный паттерн очень популярен при разработке ПО, особенно в фреймворках, использующих Inversion of Control. Механизм Dependency Injection (для данного проекта это механизм в Spring Framework и Angular Framework) манипулирует бинами и выполняет их внедрение при обращении из различных классов. В данном проекте, используя scope бинов, реализован данный паттерн (все бины являются синглтонами). При объявлении бина с помощью аннотации, если явно не указать scope бина, то он по умолчанию устанавливается как singleton. Это означает, что контейнер Spring IoC создаёт только один экземпляр объекта определённого в бине. Этот экземпляр помещается в кэш таких же бинов (синглетонов) и все последующие вызовы бина с таким именем будут возвращать объект из кэша..

Объявление бина с scope singleton, устанавливаемым по умолчанию
![Singleton](https://github.com/IlyaMarkevichV/ISchedule/blob/master/DesignPatterns/Screens/singleton.jpg)
### Factory

### MVC
Паттерн MVC (Model View Controller) является одним из классических паттернов проектирования.
Его идея состоит в разделении прложения на три основополагающих модуля: модель, контроллер и представление.
В данном паттерне проектирования модель выполняет роль представления данных и манипулирования с ними. Модель никак не связана с представлением. Контроллер является прослойкой между моедлью и представлением, а так же играет роль связующего связана между пользователм и программой.Представлние, в свою очередь, осуществляет отображение интформации для пользователя, в обработке данных не учвствует.
На данной картинке приведена типичная схема реализации MVC

![MVC](https://github.com/Moistra/CashBox/blob/master/Patterns/Screens/mvc_pic.png)

Модель
![Model](https://github.com/IlyaMarkevichV/ISchedule/blob/master/DesignPatterns/Screens/model.png)

Контроллер
![Controller](https://github.com/IlyaMarkevichV/ISchedule/blob/master/DesignPatterns/Screens/controller.png)

Вид
![ViewHtml](https://github.com/IlyaMarkevichV/ISchedule/blob/master/DesignPatterns/Screens/group-tab-html.png)
![ViewTs](https://github.com/IlyaMarkevichV/ISchedule/blob/master/DesignPatterns/Screens/group-tab-ts.png)
### Observer
Данный паттерн был реализован при создании frontendа. Идея заключается в создании класса наблюдателя за другим классом. Наблюдатель подписывается на изменение состояния наблюдаемого объекта и реакции на него. Для примера можно взять любой компонент frontend.Для примера рассмотрим table-model.service-ts. Метод getFaculties() выполняет запрос, данный метод возвращает Observable<Faculty[]>, на который подписывается метод getFaculties(). После изменения состояния страница обновляет содержимое в зависимости от результата метода получения факультетов.
