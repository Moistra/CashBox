# План тестирования
---


# Cодержание
1 [Введение](#introduction)  
2 [Объект тестирования](#items)  
3 [Риски](#risk)  
4 [Аспекты тестирования](#features)  
5 [Подходы к тестированию](#approach)  
6 [Представление результатов](#pass)  
7 [Выводы](#conclusion)  

<a name="introduction"/>

# 1 Введение

Данный документ описывает план тестировани desktop приложения CashBox . Данный документ предназначен для тестировщиков. Цель тестирования: проверить соответствие приложения [требованиям](../docs/project_requirements.md)

<a name="items"/>

# 2 Объект тестирования

В процессе тестирования предполагается проверить выполение требоаний SRS, а так же соответствие повеения приложения, завленым правилам игры.  
В качестве объектов тестирования можно выделить основные функциональные требования, требования к удобству использования(../Requirements/Reqests.md).  
Атрибуты качества:  
1. Функциональная пригодность:  
* функциональная полнота;  
* функциональная корректность;  
* функциональная целесообразность;  
2. Удобство использования:  
* поняность использования
* удобство испоьзования 
* удобство восприятия


<a name="risk"/>

# 3 Риски

К рискам можно отнести:  
* повреждение файлов базы данных;
* в теории возможная нехватка места для баз данных на носителе памяти;


<a name="features"/>

# 4 Аспекты тестирования

В ходе тестирования планируется проверить реализацию основных аспектов работы приложения.  
К основным функциям можно отнести следующие пункты:  
* создание денежной операции;  
* удаление денежной операции;  
* возможность просматривания статистики;
* возможность сохранять свои действия для возвращения к использованию в будущем.

<a name="approach"/>

# 5 Подходы к тестированию

Предполагается использовать ручное тестирование.

<a name="pass"/>

# 6 Представление результатов

Результаты тестирования представлены в документе ["Представление результатов"](../Testing/TestResults.md).

<a name="conclusion"/>

# 7 Выводы

Приложение соответствует основным функциональным требования, однако стоит отметить, что возможноти приложения могут быть заметно расширены, а дизайн создан более приятным пользователю.