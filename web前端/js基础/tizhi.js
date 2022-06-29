// 获取按钮，身高，体重标签
var btn = document.getElementById('btn')
var ht = document.getElementById('ht')
var tz = document.getElementById('tz')

//绑定点击事件
btn.onclick = function(){
	//获取用户输入的身高和体重
	var user_height = ht.value
	var user_weight = tz.value
	var str = ''
	
	var result = document.getElementById('result')

	// 体质指数（BMI）= 体重（kg）÷ 身高^2（m）
	// 计算体质指数
	var BMI = user_weight / (user_height*user_height)

	// 判断体质指数在哪个区间  <18.5 偏瘦 18.5——23.9 正常 >23.9 偏胖
	if(BMI<18.5){
		str = '偏瘦'
		// 操作样式
		result.style.backgroundImage = "url('images/sou.jpg')"
	}else if(BMI>=18.5&&BMI<=23.9){
		str = '正常'
		result.style.backgroundImage = "url('images/zc.jpg')"
	}else{
		str = '偏胖'
		result.style.backgroundImage = "url('images/pang.jpg')"
	}
	// 把str的值设置到 id为result的p标签中
	result.innerHTML = str

}