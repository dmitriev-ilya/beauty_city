$(document).ready(function() {
	$('.salonsSlider').slick({
		arrows: true,
	  slidesToShow: 4,
	  infinite: true,
	  prevArrow: $('.salons .leftArrow'),
	  nextArrow: $('.salons .rightArrow'),
	  responsive: [
	    {
	      breakpoint: 991,
	      settings: {
	        
	      	centerMode: true,
  			//centerPadding: '60px',
	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 575,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});
	$('.servicesSlider').slick({
		arrows: true,
	  slidesToShow: 4,
	  prevArrow: $('.services .leftArrow'),
	  nextArrow: $('.services .rightArrow'),
	  responsive: [
	  	{
	      breakpoint: 1199,
	      settings: {
	        

	        slidesToShow: 3
	      }
	    },
	    {
	      breakpoint: 991,
	      settings: {
	        
	      	centerMode: true,
  			//centerPadding: '60px',
	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 575,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});

	$('.mastersSlider').slick({
		arrows: true,
	  slidesToShow: 4,
	  prevArrow: $('.masters .leftArrow'),
	  nextArrow: $('.masters .rightArrow'),
	  responsive: [
	  	{
	      breakpoint: 1199,
	      settings: {
	        

	        slidesToShow: 3
	      }
	    },
	    {
	      breakpoint: 991,
	      settings: {
	        

	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 575,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});

	$('.reviewsSlider').slick({
		arrows: true,
	  slidesToShow: 4,
	  prevArrow: $('.reviews .leftArrow'),
	  nextArrow: $('.reviews .rightArrow'),
	  responsive: [
	  	{
	      breakpoint: 1199,
	      settings: {
	        

	        slidesToShow: 3
	      }
	    },
	    {
	      breakpoint: 991,
	      settings: {
	        

	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 575,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});

	// menu
	$('.header__mobMenu').click(function() {
		$('#mobMenu').show()
	})
	$('.mobMenuClose').click(function() {
		$('#mobMenu').hide()
	})

	new AirDatepicker('#datepickerHere')

	var acc = document.getElementsByClassName("accordion");
	var i;

	for (i = 0; i < acc.length; i++) {
	  acc[i].addEventListener("click", function(e) {
	  	e.preventDefault()
	    this.classList.toggle("active");
	    var panel = $(this).next()
	    panel.hasClass('active') ?  
	    	 panel.removeClass('active')
	    	: 
	    	 panel.addClass('active')
	  });
	}


	$(document).on('click', '.service__saloons .accordion__block', function(e) {
		let thisName,thisAddress;

		thisName = $(this).find('> .accordion__block_intro').text()
		thisAddress = $(this).find('> .accordion__block_address').text()
		thisId = $(this).find('> .accordion__block_id').text()
		
		console.log(thisId)

		$(this).parent().parent().find('> button.active').addClass('selected').text(thisName + '  ' +thisAddress)
		setTimeout(() => {
			$(this).parent().parent().find('> button.active').click()
		}, 200)
		$(this).append(`<input hidden='true' name='saloon_id' value='${thisId}' />`)
		

		// console.log($(this).parent().parent().find('.panel').hasClass('selected'))
		
		// $(this).parent().parent().find('.panel').addClass('selected')
	})


	$('.service__services .accordion__block_item').click(function(e) {
		let thisName,thisAddress;
		thisName = $(this).find('> .accordion__block_item_intro').text()
		thisAddress = $(this).find('> .accordion__block_item_address').text()
		thisId = $(this).find('> .accordion__block_id').text()
		
		console.log(thisId)

		$(this).parent().parent().parent().parent().find('> button.active').addClass('selected').text(thisName + '  ' +thisAddress)
		setTimeout(() => {
			$(this).parent().parent().parent().parent().find('> button.active').click()
		}, 200)
		if ($(this).parent().find('.panel').hasClass('selected')) {
			console.log(thisName)
		}
		$(this).append(`<input hidden='true' name='service_id' value='${thisId}' />`)
	})
	

	$('.service__masters .accordion__block').click(function(e) {
		let thisName,thisAddress;
		thisName = $(this).find('> .accordion__block_master').text()
		thisProf = $(this).find('> .accordion__block_prof').text()
		thisId = $(this).find('> .accordion__block_id').text()
		
		console.log(thisId)

		$(this).parent().parent().find('> button.active').addClass('selected').text(thisName + '  ' +thisProf)
		setTimeout(() => {
			$(this).parent().parent().find('> button.active').click()
		}, 200)
		if ($(this).parent().find('.panel').hasClass('selected')) {
			console.log(thisName)
		}
		$(this).append(`<input hidden='true' name='master_id' value='${thisId}' />`)
	})

	//service
	$('.time__items .time__elems_elem .time__elems_btn').click(function(e) {
		e.preventDefault()
		thisTime = $(this).text()
		$('.time__elems_btn').removeClass('active')
		$(this).addClass('active')
		
		console.log((document.querySelectorAll('[id=input_time]')).length)
		
		$(this).append(`<input id='input_time' hidden='true' name='time' value='${thisTime}' />`)
		console.log(thisTime)
		if (((document.querySelectorAll('[id=input_time]')).length) > 1)  {
			document.getElementById('input_time').remove()
		} 
	})

	
	$('.air-datepicker .air-datepicker--content .air-datepicker-body .air-datepicker-body--cells .air-datepicker-cell').click(function(e) {
		thisDate = (this.getAttribute('data-year') + '-' + this.getAttribute('data-month')+ '-' + this.getAttribute('data-date'))
	
		console.log(thisDate)
	
		if (((document.querySelectorAll('[id=input_date]')).length) > 1)  {
			document.getElementById('input_date').remove()
		} 
		$(this).append(`<input id='input_date' hidden='true' name='date' value='${thisDate}' />`)
	})


	$(document).on('click', '.servicePage', function() {
		if($('.time__items .time__elems_elem .time__elems_btn').hasClass('active') && $('.service__masters').hasClass('selected')) {
			$('.time__btns_next').addClass('active')
		}
	})

	//popup
	$('.header__block_auth').click(function(e) {
		e.preventDefault()
		$('#authModal').arcticmodal();
		// $('#confirmModal').arcticmodal();
	})

	$('.rewiewPopupOpen').click(function(e) {
		e.preventDefault()
		$('#reviewModal').arcticmodal();
	})
	$('.payPopupOpen').click(function(e) {
		e.preventDefault()
		$('#paymentModal').arcticmodal();
	})
	$('.tipsPopupOpen').click(function(e) {
		e.preventDefault()
		$('#tipsModal').arcticmodal();
	})
	
	$('.authPopup__form').submit(function() {
		$('#confirmModal').arcticmodal();
		return false
	})


	


})
