1.复习
	html标签：
	  标签分类：
	    块级元素：独占一行，宽高可以设置 div p ul li 			
	    行内元素：一行可以放多个，宽高不可以设置，由内容决定  span a em i
	    行内-块级元素：一行可以放多个，宽高可以设置  img input button

	    标签类型转换：
	    	display: block;  设置成块级元素
	    			 inline; 设置成行内元素
	    			 inline-block; 设置成行内-块级元素
	    			 none;   隐藏
	  写法分类：
	  	单标签：只有一个标签，自带结束标识 , <img />  <input /> <br /> <hr />
	  	双标签：成对出现，有开始有结束的，大部分是双标签，<div></div> <p></p> <span></span>
	表格：
		table
		  caption	:设置表头
		  th		:设置每一列的表头
		  tr		:行
		  td		:列

	列表：
		不显示列表项前面的符号，需要设置 list-style:none
		有序列表：ol ,列表项 li 
		无序列表：ul ,列表项 li
		图文混排：dl ,列表项 dt：列表头部  dd：列表内容

	form表单：
		form 
		  用户输入：input type='text' placeholder='提示语句' name='username'
		  密码：    input type='password'
		  单选按钮： input type='radio'
		  多选按钮： input type='checkbox'
		  下拉框：   select > option
		  文本域：   textarea 
		  提交：		input type='submit'
		  重置：		input type='reset'
		  按钮：		button

		提交数据时，数据的键名是由name属性提供的，数据的键值是由value属性提供的。所有非用户输入的标签，需要给定value属性的值，如单选按钮，多选按钮，下拉框。用户输入的，不用给默认value属性值，如input type='text' textarea。

		form标签属性：
			action:url地址，数据提交的地址
			method:get/post ，提交数据的方式


2. css样式
	css样式作用装饰html,使页面美化。
	css样式的写法有三种：
		第一种：行内样式
			把样式写在标签内部，需要在标签中添加一个属性style，在style中定义样式
		第二种：内部样式表
			在head中定义一个style标签，在这个标签中写当前页面的样式
		第三种：外部样式表
			在html文件外创建.css结尾的文件，在文件中写css样式，引入页面需要使用link标签

	css样式：
		1.设置字体大小和颜色
		  font-size:12px;
		  color: 值可以是英文单词 red green yellow
		  			  是rgb()	rgb(0,0,0) rgb(255,255,255)
		  			  是rgba()	带透明度的颜色值 rgba(0,255,123,0.3)
		  			  是#000 	

3.选择器：
	id选择器：需要在标签上添加 id 属性，给id属性一个变量名 <div id='container'></div>
			  css中通过 #container 找到对应元素，然后可以设置样式
	类选择器：需要在标签上添加 class 属性，给class属性一个变量名 <div class='box'></div>
			  css中通过 .box 找到对应的元素，然后设置样式
	标签选择器：直接找标签的名称(div,span,a,p,input)，然后设置样式
	通用选择器：* 代表所有
	子集选择器：父级>子集
	后代选择器：父级 后代
	伪类选择器：选择器:before/:after
					 :nth-child(n)
					 :nth-of-type(n)
				<div class='box'>
					<p><a></a></p>
					<p></p>
				</div>

				.box:before{

				}
				.box p:nth-child(2){
					选中第二个p标签
				}
	注意：id选择器一次只能选中 1 元素，页面中id不能出现同名
		 class、标签选择器每次选中的是多个，class相同类名可以出现多次
		 nth-child/nth-of-type ：只适用于class/标签选择器,选中的是class/标签的兄弟元素


4.盒模型
	content : 写入内容的地方
	padding：内边距,撑开内容和边框直接的距离
	border：边框
	margin：外边距

	块级元素、行内-块级元素可以设置宽高，这里设置的宽和高指的是content的宽高
	padding/margin/border都是是四个方向上，四个方向上的值可以不同
	四个方向：上为top 下为bottom 左为left 右为right
	border由三个属性组成：宽度(border-width)、样式(border-style)、颜色(border-color)

	border的简写方式：border:1px solid/dotted/dashed #000;
					border-bottom:3px red solid;
	padding/margin的简写：
		第一种形式：只有一个值，这时四个方向都使用这个值		padding:10px;
		第二种形式：两个值，这时上和下10px,左和右是20px; 	padding:10px 20px; 
		第三种形式：三个值，这时上10，左右20px，下30px 		padding:10px 20px 30px; 
		第四种形式：四个值，上10 ，右20 ，下30，左40		padding:10px 20px 30px 40px;


5.字体
	font-family: 设置字体(宋体、微软雅黑)
	font-size:字体大小
	font-weight:字体粗细

6.背景
	background
	背景颜色：比背景图片更靠近底层。background-color:
	背景图片：background-image:url('图片路径')
	背景图片大小：background-size:x轴方向 y轴方向
	背景定位：background-position:x轴方向 y轴方向
	背景重复：background-repeat:no-repeat; repeat-x; repeat-y;

7.其他小知识点：
	宽：width
	高：height
	行高：line-height
	文字对齐效果：text-align:center/left/right
	溢出隐藏：overflow:hidden
	垂直对齐方式：vertical-align：top
								middle
								bottom




