# HomeWork 5, СНАР, бригада 4: Ханиев, Попов, Цвийович.
В данной домашней работе мы выполнили установку ROS2 Humble на ОС Ubuntu 22.04 и создали математическое описание модели робота и отобразили тракторию движения в RVIZ.
***
Траектория
![Screenshot_from_2023-05-21_23-49-38](https://github.com/makspoov/HomeWork/assets/49243068/a09c665c-9457-48cd-b748-dce5e2562618)

## Инструкция по запуску
### Шаг 1: Установка пакетов
1) Создать папку рабочего пространства
```
mkdir ~/ros2_ws
cd ~/ros2_ws
```
2) Склонировать содержимое репозитория
```
git clone https://github.com/makspoov/HomeWork.git
```
3) Меняем командную оболочку с Bash на ROS2
```
source /opt/ros/humble/setup.bash
```
4) Необходимо собрать проект
```
colcon build
```
### Шаг 2: Запуск для проверки работоспособности
1) Создать 3 окна терминала, в каждом перейти в директорию рабочего пространства и сменить командную оболочку
```
cd ~/ros2_ws
source /opt/ros/humble/setup.bash
```
2) В первом терминале запустить узел TURTLEBOT3
```
export TURTLEBOT3_MODEL=waffle
ros2 launch turtlebot3_bringup rviz2.launch.py
```
3) Во втором терминале запустить публикатор узла snarbot
```
source install/local_setup.bash
ros2 run py_pubsub_hw talker
```
4) В третьем терминале запустить средство визуализации rviz
```
export TURTLEBOT3_MODEL=waffle
ros2 run turtlebot3_teleop teleop_keyboard
```

Управление роботом происходит посредством нажатия клавиш WASDX на клавиатуре в терминале с запущенным TURTLEBOT3.








