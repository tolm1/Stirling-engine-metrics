# Метрика двигателя внешнего сгорания / МДВС

Тз)

Команда – Дремов С., Томиленко С., Трифонов М., Прозоров М.

Цель – разработать приложение для графической иллюстрации экспериментальных данных в реальном времени.

Актуальность – был двигатель стирлинга (сгорел). Физическая модель была сложная и неподвластна для студентов 1 курса. После производства двигатель пытался запустится, но не нет. Проблема заключается в изменяемых параметров, которые надо высчитывать (мертвый объем, сдвиг фаз и тд), чтобы получить наилучшие значения требуется какая-то характеристика/метрика. Это упростит проектирование таких двигателей для других желающих. 

Реализация : 
с Ардуино в реальном времени передаётся массив данных, по ним строиться график на Python. 

Отрисовывать граф к в реальном времени возможно.

Возможный стек Python, PyQt, Matlin, С++.

Уже есть проблема, из-за огромного числа измерений, шкала времени ломается (цифры сливаются в единый черный прямоугольник). Это связано с масштабом, он одинаков для разного промежутка времени, непорядок. Решение, чтобы график убегал вперед.  Или ввести единый масштаб, или скролл.

Функционал:
выбрать отрезок и приблизить
выравнивать график (убирать максимальные точки)
столбик с динамическим размером, показывающий количество оборотов в секунду (как спидометр)
несколько измерений


Этапы
1. Реализация MVP. 
  a.Требуется в реальном времени строить 1 график 
  b.масштаб 
2. Выравнивание графика, то есть убрать максимальные точки из списка.
3. Приближение куска графика (можно ли это сделать)
4. Добавление минимального GUI. Домашний экран - кнопка проверить оборудование, начать замер
  a. Кнопка проверить оборудование - проверка подключения Arduino. 
  b. Кнопка начать замер 
    i. старт работы Arduino
    ii. вывод графиков, открывается новое окно с графиком или будет на в домашнем окне. Не понятно пока.
5. Функционал для GUI
  a. На экране с графиком уже можно будет приближать. 
  b. Добавить столбец с показание количества оборотов в секунду.
6.На экране с графиком добавить еще кнопку - новое измерение.
  a. Arduino сбрасывает таймер в 0 и заново производит замер и строит график в том же поле, как и прошлый. 
  b. Столбец из п. 5 работает с новыми измерениями.
7. Отладка
8. ЗАЩИТА

Задачи и сроки
Степан -  3, 5.a

Сергей - 1, 2, 4.a, 4.b.i, 6.a

Матвей - домашний экран, 4.b.ii

Макс - 5.b, 6.b

Красная линия (redline) - MVP - 05.05, первое GUI 10.05, второе GUI 12.05 
Смертельная линия (deadline) - сдача 20.05 


