console.log('It working')

//saving the theme that is in the local storage under application 
let theme = localStorage.getItem('theme')
//if the user has not been to the website before, default theme will be white 
//else it will be the selected theme
if(theme == null){
	setTheme('light')
}else{
	setTheme(theme)
}

let themeDots = document.getElementsByClassName('theme-dot')

//Identify that the user has clicked a button
for (var i=0; themeDots.length > i; i++){
	themeDots[i].addEventListener('click', function(){
		let mode = this.dataset.mode //let's the console know what theme dot has been selected
		console.log('Option clicked')
		setTheme(mode)
	})
}

//Passing in the mode conditions and that info will
//tell the code what theme to use 
// Need to change the location of the files if moved
function setTheme(mode){
	if(mode == 'light'){
		document.getElementById('theme-style').href = 'default.css'
	}
	if(mode == 'dark'){
		document.getElementById('theme-style').href = 'Colors/dark.css'
	}
	if(mode == 'orange'){
		document.getElementById('theme-style').href = 'Colors/orange.css'
	}
	if(mode == 'green'){
		document.getElementById('theme-style').href = 'Colors/green.css'
	}
	if(mode == 'purple'){
		document.getElementById('theme-style').href = 'Colors/purple.css'
	}

	localStorage.setItem('theme', mode) //assigning the theme value to mode and will trigger setTheme function
}