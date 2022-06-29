1.js基本语法
	1.js引入方式
	js是脚本语言，可以在浏览器中执行。js文件是以.js为结尾的，引入html文件中时使用script标签，这时script需要添加一个属性src，src中写js文件的路径；但是js还可以直接写在html当中，在html中需要使用<script></script>标签中写js代码

	在html内部写js时，script标签可以放在head中，可以放在body中，还可以放在body后

	2.js基本语法
		js执行顺序，默认是顺序结构，是从上到下，从左到右执行
		js一般一行放一条语句，语句后结束标识是 ";" ,但是结束标识不强制写
		js中换行要求：没有换行要求，最标准的缩进是一个tab。
		js中 if选择/for循环/函数function 后面的语句块都是由 {} 包裹的

	3.变量和常量
		定义变量：var 变量名 
				 let 变量名
		定义常量：const 常量名
		变量名的命名规范：
			1.组成：字母、数字、下划线、$
			2.首字符不能是数字
			3.不能使用关键字
			4.建议使用驼峰命名法

		使用变量或常量：
			1.直接访问：变量名或常量名
			2.重新赋值：常量不能被重新赋值。变量可以重新赋值，变量中只会保存最后一次赋值。

	4.注释：
		第一种：单行注释： // 注释内容
		第二种：多行注释： /* 中间注释内容 */
		第三种：多行文本注释： /** 注释内容 */


	5.基本数据类型
		1.数字类型(int float) : 1,2,3  3.14
		2.字符串类型(string) : 单引号或双引号引起来的字符，单引号双引号作用一样，没区别
		3.布尔类型(bealoon): true(1) 表示真  false(0) 表示假
		4.undefined类型(undefined)： 变量或对象的属性没有赋值时，默认值就是undefined
		5.null类型(null):表示空
		6.对象类型：
			数组(array): 类似python中的List，定义方式 [1,'a',true]，通过下标访问元素
			对象(object):类似python中的dict ，定义{"username":"小明","age":18}，通过键名访问
			正则表达式:同python
		检查数据类型方法：typeof 
			注意：typeof 检测对象类型时，不管是数组还是对象，返回的都是Object


	6.输出方式：
		alert()：小括号中写变量或语句，窗口弹出
		console.log():在控制台输出 F12->console


	7.运算符：
		1.算数运算： + - * / %
			除法： 会运算到小数位 ，没有 // 求整
			取余： 运算到该加小数点时的余数
		2.关系运算： > >= < <= == === != !== 
			===和==区别:
				==是不判断数据类型： 1 == '1'   返回值 true
				===判断数据类型： 1 === '1'	返回值 false
		3.逻辑运算： &&(逻辑与)  ||(逻辑或)  !(逻辑非)
			没有and / or
			逻辑与、逻辑或都会存在短路运算：
				逻辑与 左边为false，右边不判断直接返回false，左边为true，返回值是右边
				逻辑或 左边为true，右边不判断直接返回 true，左边为false，返回值是右边

		4.赋值运算： = += -= *= /= %= ++(自增) --(自建)
			++ 、 --：
				用法1： 变量名++ ： 本次不改变，下次使用时改变
				用法2： ++变量名 ： 先改变后使用，当次生效

	8.parseInt() parseFloat()
		parseInt() ： 取小括号中整数部分
		parseFloat() : 取小括号中整数+小数部分

2.流程控制语句
	1.选择结构
		if
			单分支：if(表达式){} 
			双分支：if(表达式){语句} else{语句}
			多分支：if(表达式1){} else if(表达式2){} else{}

		switch
			switch(表达式){
				case 值: 语句块 ;break;
				case 值2: 语句块； break；
				default:语句
			}
	2.循环结构
		for
			普通for循环：
				for(表达式1;表达式2;表达式3){循环体}
				表达式1：循环条件的初始值
				表达式2：循环条件的终止值
				表达式3：循环条件的步长

				for(let i=0; i<3 ; i+=1){

				}

			for-in循环：
				for(let i in [1,2,3]){

				}
		while
			表达式1
			while(表达式2){
				循环体;
				表达式3
			}


	3.数学方法：
		Math.random() [0,1) 
	4.获取字符串或数组的长度：
		通过.length 属性获取
		'abcd'.length
		[1,2,'a','b'].length

3.js选择器
	选择器作用：找页面中的标签
	  选择器类型：id选择器
	  				document.getElementById('id名')
	  				返回值：1个具体的标签元素
	  			 class选择器
	  			 	document.getElementsByClassName('class名');
	  			 	返回值：所有具有指定class名称的元素，是多个，以类数组形式存在，使用某一个元素时通过下标来获取
	  			 标签选择器
	  			 	document.getElmentsByTagName('标签名');
	  			 	返回值：所有指定标签的集合

4.操作基本dom
	1.获取标签中值
		第一类：获取双标签中的值(div,span,p) 
			    .innerHTML 来获取

		第二类：获取input标签中的值()
				.value 来获取
		特殊的一个标签：
			textarea 文本域：是双标签，但是获取他的值时使用.value属性
									 设置值使用 .innerHTML

    2.添加点击事件
    	事件：是一个具有某些功能的函数
    	点击事件：鼠标点击某个元素的时候触发的功能
    	添加点击事件方法：
    		1.找到元素
    		2.元素.onclick = function(){}


    3.设置值
    	第一类：设置双标签的值
    		元素.innerHTML = '新值'
    	第二类：设置input标签的值
    		元素.value = '新值'

    4.获取属性和修改属性值
    	属性有：id , class , name , src ,href , style
    	1.获取属性
    		元素.getAttribute('属性名')
    	2.设置属性值
    		元素.setAttribute('属性名','值')


    5.获取和修改css样式
    	1.获取css样式
    		第一类 行内样式： 元素.style.样式名称
    		第二类 内部、外部样式： window.getComputedStyle(元素)['样式名称']

    	2.设置css样式
    		元素.style.样式名 = 新值

    	注意：获取或设置 font-size 类型的样式时，需要变成驼峰命名法(fontSize)


	体质指数（BMI）= 体重（kg）÷ 身高^2（m）
	当BMI指数为18.5～23.9时属正常