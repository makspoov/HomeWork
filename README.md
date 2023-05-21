# HomeWork 5, СНАР, бригада 4: Ханиев, Попов, Цвийович.
В данной домашней работе мы выполнили установку ROS2 Humble на ОС Ubuntu 22.04 и создали математическое описание модели робота и отобразили тракторию движения в RVIZ.
***
__Траектория__

![Screenshot_from_2023-05-21_23-49-38](https://github.com/makspoov/HomeWork/assets/49243068/a09c665c-9457-48cd-b748-dce5e2562618)
***


## Инструкция по запуску
Управление роботом происходит посредством нажатия клавиш WASDX на клавиатуре, после введения нужной команды в терминале с запущенным TURTLEBOT3. Важно не переходить в другие окна терминала и оставить то окно активным (последнее взаимодействие мышкой), в котором была введена команда для управления с клавиатуры. 
### Установка пакетов
+ Создайте папку workspace:
```
mkdir ~/ros2_ws
cd ~/ros2_ws
```
+ Загрузите содержимое репозитория:
```
git clone https://github.com/makspoov/HomeWork.git
```
+ Поменяйте командную оболочку с Bash на ROS2:
```
source /opt/ros/humble/setup.bash
```
+ Соберите проект:
```
colcon build
```
### Проверка при запуске
+ Создайте 3 окна терминала, в каждом перейдите в директорию рабочего пространства и смените командную оболочку:
```
cd ~/ros2_ws
source /opt/ros/humble/setup.bash
```
+ В первом терминале запустите узел TURTLEBOT3:
```
export TURTLEBOT3_MODEL=waffle
ros2 launch turtlebot3_bringup rviz2.launch.py
```
+ Во втором окне терминала запустите публикатор узла py_pubsub_hw:
```
source install/local_setup.bash
ros2 run py_pubsub_hw talker
```
+ В третьем окне терминала запустите средство визуализации rviz:
```
export TURTLEBOT3_MODEL=waffle;
ros2 run turtlebot3_teleop teleop_keyboard
```
## Заключение
В результате проделанной работы был произведен процесс установки ROS2 Humble.
Команды работают корректно, движение происходит согласно поставленной задаче в соответствии математическому описанию в репозитории преподавателя.









