function is_not(el,val,message,event) {
	if(el.val() == val){
		event.preventDefault()
		el.attr("style","border:#f00 solid 1px")
		el.attr("placeholder",message)				
	}	
}