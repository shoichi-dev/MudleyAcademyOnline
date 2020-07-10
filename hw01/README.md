# MudleyAcademyOnline Homework 01

1. ติดตั้ง python(https://www.python.org/downloads)

2. ติดตั้ง vscode สำหรับเขียนโค้ด(https://code.visualstudio.com/download)

3. ติดตั้ง virtualenv คือ environment จำลองของ python เพื่อป้องกัน library ชนกัน ซึ้งอาจะเกิดขึ้นได้ถ้ามีการพัฒนาโปรแกรมหลายๆโปรแกรม อ่านเพิ่มเติมได้ที่ 
(https://medium.com/@nonthakon/virtualenv-%E0%B9%83%E0%B8%99-python-3-windows-10d3dd89a0a7)
หรือ (https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html)

เปิด command prompt(ถ้าใช้ Terminal ของ vscode จะติดปัญหาตอน activate virtualenv) แล้วเข้าไปที่ folder โปรเจ็คของเรา

![installenv](https://github.com/shoichi-dev/MudleyAcademyOnline/blob/master/install_env_by_cmd.PNG?raw=true)
```
pip3 install virtualenv

```
สร้าง virtualenv
![installenv](https://github.com/shoichi-dev/MudleyAcademyOnline/blob/master/create_env.PNG?raw=true)
```
virtualenv --python C:\Users\lenovo\AppData\Local\Programs\Python\Python38-32\python.exe venv
```

ทำการ activate virtualenv ที่เราสร้างขึ้น และติดตั้ง library ต่างๆตามต้องการ (https://github.com/shoichi-dev/MudleyAcademyOnline/blob/master/activate_venv.PNG?raw=true)
```
.\venv\Scripts\activate
```

สามารถดูวิธีใช้งานเพิ่มติมได้ที่(https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html)

ติดตั้ง library CCXT (https://github.com/ccxt/ccxt/)

```
pip install ccxt
```
![installccxt](https://github.com/shoichi-dev/MudleyAcademyOnline/blob/master/install_ccxt.PNG?raw=true)



