function worng_form(form,value,message,alt,cond){
	if(form.val() == value){	
		cond.cond+=1
		form.attr("style","border:#f00 solid 1px")
		form.attr("placeholder",message)		
	}
	else{
		form.attr("style","border:#fff solid 1px")
		form.attr("placeholder",alt)
	}
}
function worng_form(form,value,message,alt){
	if(form.val() == value){	
		form.attr("style","border:#f00 solid 1px")
		form.attr("placeholder",message)		
	}
	else{
		form.attr("style","border:#fff solid 1px")
		form.attr("placeholder",alt)
	}
}