#Control-robot-arm

ننشئ واجهة مستخدم خاصة بالتحكم بذراع الروبوت تحتوي على ٦ محركات وزري للحفظ والتشغيل سنحتاج الى ٣ لغات برمجية ولغة ترميز واحدة ستصنف حسب الآتي

html و css الواجهة الامامية: لغتي


mysql و python :  الواجهة الخلفية لغتي

التي بدورها ستهتم بالهيكل الاساسي الذي يظهر للمستخدمين html سنبدأ بـ

    <head>
    
    <title>Control Robot Arm</title>
    
    <link rel="stylesheet" href="{{ url_for('static',filename='styles/style.css')}}">
    
    </head>
 head عنصر الـ
