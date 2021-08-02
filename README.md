#Control-robot-arm

ننشئ واجهة مستخدم خاصة بالتحكم بذراع الروبوت تحتوي على ٦ محركات وزري للحفظ والتشغيل سنحتاج الى ٣ لغات برمجية ولغة ترميز واحدة ستصنف حسب الآتي

html و css الواجهة الامامية: لغتي


mysql و python :  الواجهة الخلفية لغتي

التي بدورها ستهتم بالهيكل الاساسي الذي يظهر للمستخدمين html سنبدأ بـ

    <head>
    
    <title>Control Robot Arm</title>
    
    <link rel="stylesheet" href="{{ url_for('static',filename='styles/style.css')}}">
    
    </head>
    
 :يحتوي على معلومات الصفحة مثل head عنصر الـ

tital عنوان الصفحة المتواجد داخل عنصر الـ

الذي يقوم بالربط بين لغتي الواجهة الأمامية link وعنصر الـ

فهي المسؤولة عن ظهور الشكل الجمالي للهيكل الذي قمنا بإنشائه ويتم الربط فيما بينهم  css هي المسؤولة عن بناء الهيكيل الأساسي اما لغة html لغة الترميز 

     <body>
     <div>
     <form action="/my-link/" method="POST">
     <p> محرك ١ </p>
     <div class="main">
     <input name="R1" type="range" min="0" max="180" value="90" id="slider" oninput='document.getElementById("demo1").innerHTML = this.value' />
     <p id='demo1'>90</p>
     </div>
     </body>
     
     
     
    
