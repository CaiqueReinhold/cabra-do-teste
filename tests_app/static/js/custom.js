jQuery(document).ready(function() {
    function showTestBtn(response) {
        var $form = $('#do_test_form');
        if ($form.length && response.status == 'connected') {
            $('.facebook').remove();
            if ($form.find('input').length) {
                $form.find('input[name="token"]').remove();
            }
            var $inp = $('<input>').
                attr('type', 'hidden').
                attr('name', 'token').
                val(response.authResponse.accessToken);
            $form.append($inp);
            $form.removeClass('hide');
        } else if ($form.length) {
            if (!$form.hasClass('hide')) {
                $form.addClass('hide');
            }
            var $connectBtn = $($('#btn-template').html());
            $connectBtn.insertAfter($form);
            $connectBtn.on('click', function() {
                fbLogin();
            });
        }
    }

    function fbLogin() {
        FB.login(function(response) {
                statusChangeCallback(response);
            }, {scope: 'public_profile,email,user_friends'});
    }

    function statusChangeCallback(response) {
        if (response.status === 'connected') {
            cleanNav();
            showUser();
        } else {
            cleanNav();
            showLogin();
        }
        showTestBtn(response);
    }

    function cleanNav() {
        $('.custom_nav').empty();
    }

    function showLogin() {
        var $loginBtn = $($('#login-template').html());
        $('.custom_nav').append($loginBtn);
        $('#fb_login').on('click', function() {
            fbLogin();
        });
    }

    function showUser() {
        FB.api('/me?fields=id,name,email,picture', function(meResponse) {
            var $user = $($('#user-template').html());
            $user.find('span').html(meResponse.name);
            $user.find('img').attr('src', meResponse.picture.data.url);
            $('.custom_nav').append($user);
            dropdownHover();
            $('#logout').on('click', function() {
                FB.logout(function() {
                    statusChangeCallback({status: 'not_authorized'});
                });
            });
        });
    }

    function fbSetup() {
        $.ajaxSetup({ cache: true });
        $.getScript('//connect.facebook.net/pt_BR/sdk.js', function(){
            FB.init({
              appId: '321342751577427',
              cookie: true,
              xfbml: false,
              version: 'v2.8'
            });
            FB.getLoginStatus(statusChangeCallback);
        });
    }

    $('.share').on('click', function() {
        FB.ui({
            method: 'share',
            href:'http://' + window.location.hostname + '/' + window.location.pathname
        });
    });

    fbSetup();
    $(window).scroll(function() {
        if ($(this).scrollTop() > 300) {
            $('.scrollToTop').fadeIn();
        } else {
            $('.scrollToTop').fadeOut();
        }
    });
    $('.scrollToTop').click(function() {
        $('html, body').animate({
            scrollTop: 0
        }, 800);
        return false;
    });
});

wow = new WOW({
    animateClass: 'animated',
    offset: 100
});
wow.init();

function dropdownHover() {
    $('ul.nav li.dropdown').hover(function() {
        $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeIn(200);
    }, function() {
        $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeOut(200);
    });
}

jQuery(window).load(function() {
    $('#status').fadeOut();
    $('#preloader').delay(700).fadeOut('slow');
    $('body').delay(700).css({
        'overflow': 'visible'
    });
})

