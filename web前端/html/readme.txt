常见的html元素
1.html的作用：定义整个页面"长"成什么样子，相当于网站的骨架。
2.html搭骨架的标签：
	标题标签：h1~h6
	容器标签：div	:定义大的模块
	段落标签：p		：段落
	行内标签：span	：元素内容可以在同一行显示，是个行内元素
	跳转标签：a		：跳转，有个href属性，属性中放网络路径，点击时会跳转到指定的网络路径中
					  还有一个属性叫target，target属性值有 _self _blank,打开新窗口是否是当前窗口
	图片标签：img 	：src属性，要显示图片的路径，可以是本地路径也可以是网络路径。alt属性，在					图片显示不出来的时候，要显示的文字
	换行标签：br 	：多个行内元素在同一行时，如果需要换行可以使用这个标签
	分割标签：hr 	：显示一条分割线 ,width 设置分割线宽度,size：设置线的高度

	列表标签：
		不显示列表类型：list-style值为none
		有序列表：ol	：标签中嵌套li标签，li标签中放列表项,列表项前面的类型type设置，常见类型：数字,a,A,I,i

		无序列表：ul ：无序列表中列表项也是li标签包裹，前面类型不是数字、字母、I这些，是点,常见类型：disc，square，circle

		图文混排：dl	：用来显示标签项不用li，使用 dt,dd
						dt:放标题部分
						dd:放内容部分

3. 块级元素和行内元素
	块级元素：独占一行，标签的宽是浏览器屏幕的宽，高度由内容决定，常见的块级元素:div, p, ul, li, dl 

	行内元素：不独占一行，同一行可以放多个行内元素，行内元素的宽是由内容决定的，高度也是由内容决定的。 常见的行内元素： span, a, em, i

	行内-块级元素：不独占一行，宽度可以自己设置。常见元素：input, button, img

	改变元素属性方法：
		display： block;		块级元素
				  inline;	行内元素
				  inline-block;	行内-块级元素
				  none;		把元素隐藏
4.标签
	双标签：成对出现的，有开始标签，有结束标签。大部分标签是双标签，<div></div>	
	单标签：单个出现，写法 <br /> <hr /> <input /> <img />

5.表格table
	<table>
		<caption>表格标题</caption>	
		<tr> //行
			<th>表头</th>
			<th>表头</th>
			<th>表头</th>
		</tr>
		<tr>
			<td>列</td>
			<td></td>
			<td></td>
			<td></td>
		</tr>	
	</table>
	表格的属性：
		border:边框，值为数字类型
		cellpadding: 单元格内边距
		cellspacing：单元格外边距
		align:表格的对齐形式，可选值：left  左对齐
									right  右对齐
									center 居中
		align属性 如果写在table上，table表格相对浏览器页面的对齐方式；如果写tr上，td中的文字对齐方式
		width: 设置宽度。如果在table，设置的是整个table的宽；如果在td上，设置对应列的宽
	
	合并属性：
		行合并：rowspan=5  把多行合并成一行
		列合并：colspan=3  把多列合并成一列


6.表单
	form	表单标签 （设置时，name在选择中是相同的，可以理解为class ）
		区域块：fieldset > legend 设置区域块的名称
		用户输入框： input type='text'
		单选按钮：	input type='radio'
		多选按钮：	input type='checkbox'
		下拉框：		select > option
		密码：		input type='password'
		上传文件：	input type='file'
		范围数字：	input type='range'
		提交：		input type='submit'
		重置：		input type='reset'
		按钮：		button
		文本域：		textarea
	input标签属性：
		placeholder 设置提示文字
		name		设置input标签的提交数据键名
		value		设置input标签的值

	form标签属性：
		action:	url地址，数据提交的地址
		method: 提交方式， get / post ，默认是get