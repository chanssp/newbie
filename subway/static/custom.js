/* select all checkbox */
function toggle(source) {
  checkboxes = document.getElementsByName('foo');
  for(var i=0, n=checkboxes.length;i<n;i++) {
    checkboxes[i].checked = source.checked;
  }
}


var base = document.getElementById('orderbtn')

base.onclick = function (e) {
	e.preventDefault();
	var checkedMenu = document.querySelector('.menu:checked');
	var checkedBread = document.querySelector('.bread:checked');
	if (checkedMenu && checkedBread) {
		base.href += encodeURIComponent(checkedMenu.value);
		base.href += encodeURIComponent(' with ');
		base.href += encodeURIComponent(checkedBread.value);
		window.location.replace(base.href);
	}
	else {
		alert('Please Check a Menu and Bread!');
	}
}