// 获取所有导航项
var navItems = document.querySelectorAll('.nav-item');

navItems.forEach(function(item) {
    item.addEventListener('mouseenter', function() {
        var dropdown = this.querySelector('.dropdown');
        if (dropdown) {
            dropdown.style.display = 'block';
        }
    });

    item.addEventListener('mouseleave', function() {
        var dropdown = this.querySelector('.dropdown');
        if (dropdown) {
            dropdown.style.display = 'none';
        }
    });
	item.addEventListener('mouseenter', function() {
		console.log('mouseenter triggered');
		// 其他代码
	});
});