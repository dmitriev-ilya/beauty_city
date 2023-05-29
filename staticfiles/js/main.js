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

  new AirDatepicker('#datepicker', {
    navTitles: {
        days(dp) {
            if (dp.selectedDates) {
                let date = dp.selectedDates[0];
              return `
                  <p>${dp.formatDate(date, 'dd-MM-yyyy')}</p>
                  <input hidden=true id='choisen_date'
                  name="date" value='${dp.formatDate(date, 'yyyy-MM-dd')}'
                />`;
            }
            
            return 'Choose date';
        }
    }
  })



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

	$(document).on('click',  function() {
    if($('.time__items .time__elems_elem .time__elems_btn').hasClass('active') && $('.service__masters > button').hasClass('selected') && $('.service__services > button').hasClass('selected')&& $('.service__saloons > button').hasClass('selected')) {
			$('.time__btns_next').addClass('active')
		  thisButtons = document.getElementById('btns')      
      thisButtons.removeAttribute('hidden')
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
		thisNote = document.getElementById('id_note')      
    console.log(thisNote.getAttribute('value'))
    console.log($('#paymentModal').find('.paymentPopup__form'))
    thisPopup = $('#paymentModal').find('.paymentPopup__form_elems')
		$('#paymentModal').arcticmodal();
		thisPopup.append(`<input id='id_note' hidden='true' name='note_id' value='${thisNote.getAttribute('value')}' />`)
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

function handleNextClick() {
	alert('Ваша заявка сохранена!');
}