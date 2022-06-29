1.复习
	1.盒模型：
	  任何一个标签都是一个盒模型，每个盒模型都有四个方向，是个矩形
	  盒模型组成部分：
	  	content: 内容部分，经常设置宽高(块级、行内-块级元素有效，行内元素无效)
	  	padding: 内边距，内容部分和边框直接的距离
	  	border:  边框
	  	margin:  外边距，撑开不同盒模型直接的距离

	  pading/border/margin都有四个方向可以设置
	  四个方向：上top 下bottom 左left 右right

	  设置方式：
	  	1.有四个值：上右下左四个方向的值 padding: 10px 20px 30px 40px;  
	  	2.设三个值：上10 下30 左右20   padding:10px 20px 30px;
	  	3.设两个值：上下10 左右20  padding:10px 20px;
	  	4.设一个值：上下左右都是这个值 padding:10px;

	  	margin:10px auto;  让元素在页面中水平方向上居中显示
	  border的组成：
	  	宽度：border-width
	  	样式：border-style: solid(实线) dotted(点线) dashed(虚线)
	  	颜色：red / #000 / rgb() / rgba()
	  	简写形式：border:1px solid #000;

	2.字体：
		font-family: 设置使用什么字体
		font-size: 16px;
		font-weight:100/200/400/bold

	3.背景
		background:设置背景的复合属性
		分开的属性有：
			background-color: 背景颜色
			background-image: 背景图片
			background-size:  背景大小
			background-position: 背景定位
			background-repeat: 背景是否重复
	4.其他知识点
		text-algin : left/right/center
		line-height: 行高
		vertical-align: top/ middle / bottom 垂直方向上对齐方式
		overflow:hidden 溢出隐藏

	5.选择器：
		id选择器： id要具有唯一性 ，通过 #id名 设置样式
		类选择器： class,不具备唯一性，可以存在多个，  通过 .class名 设置样式
		元素选择器：标签 ， 通过 标签名 设置样式
		子集选择器： 父级>子集
		后代选择器： 父级 后代
		伪类选择器： 元素:before/:after 当前元素前后添加的伪类
					元素:nth-child(n) 查找当前元素的兄弟元素
					元素:nth-of-type(n) 查找当前元素的兄弟元素


2.浮动
	让元素脱离文档流，“漂”起来。
	
	文档流：前端页面在浏览器中展示时是从左上角开始排练，横向从左到右依次排练行内元素或行内块元素，纵向是从上到下依次排练块级元素。

	浮动关键字：float: left / right

	浮动后：元素会脱离文档流，"漂"在离它最近的上一个块级元素之后，变成行内-块级元素
	元素浮动后一个问题：
		浮动元素后面元素会受浮动影响，使用浮动后需要清除浮动
		清除浮动方案：
			1.添加一个空标签，给空标签设置clear属性 clear:left / right / both
			2.给有浮动的元素添加一个父级元素，然后让父级元素清除浮动(overflow: hidden;)
3.定位
	定位关键字：position
	定位：相对定位、绝对定位、固定定位
	相对定位(relative)：是元素本身相对自己的一个偏移量，但不脱离文档流
	绝对定位(absolute)：是元素相当于父级(会有一个相对定位)的一个偏移量，是脱离文档流的
	固定定位(fixed)：相当于浏览器窗口定位，不会随页面滚动发生位置改变，也是脱离文档流的

	定位有四个方向：
		top:相对顶部的偏移量
		bottom:相对顶部的偏移量
		left:相对左边的偏移量
		right:相对右边的偏移量


hover属性：鼠标放上去的效果，鼠标离开后会恢复到原来的效果
	元素:hover{

	}


3.css3 转换、过渡、动画

	转换：transform
		位置转换：translate(x,y)
		角度转换：rotate(20deg)
		缩放： scale(x,y)  0~正无穷  0~1:缩小  1~正无穷：放大
		翻转：skew()

	过渡：transition
		过渡类型：transition-property :all 所有的类型
		过渡时间：transition-duration :秒单位的数字 5s
		过渡曲线：transition-timing-function ：linear  匀速执行
											: ease   先慢 后快 最后再慢
		过渡延时：transition-delay ： 秒单位的数字 

	动画：animation
		动画名称：animation-name 
		动画执行时间：animation-duration
		动画曲线：animation-timing-function
		动画延时：animation-delay
		动画执行次数：animation-iteration-count ：值可以是数字，infinite无限次数播放
		动画播放周期：animation-direction
		动画是否是播放状态：animation-play-state ： playing | paused
		动画播放前和播放后的状态：animation-fill-mode 

		@keyframes:定义动画的关键帧
		@keyframes 名称:{
			from(0%):{

			}
			百分数(10%):{
			
			}
			to(100%):{

			}
		}
