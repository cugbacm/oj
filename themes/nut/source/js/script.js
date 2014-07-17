(function($){

  $("#main").fitVids();

  // Share
  $('body').on('click', function(){
    $('.article-share-box.on').removeClass('on');
  }).on('click', '.article-share-link', function(e){
    e.stopPropagation();

    var $this = $(this),
      url = $this.attr('data-url'),
      encodedUrl = encodeURIComponent(url),
      id = 'article-share-box-' + $this.attr('data-id'),
      title = $this.attr('data_title'),
      summary = $this.attr('data_summary'),
      offset = $this.offset();

    if ($('#' + id).length){
      var box = $('#' + id);

      if (box.hasClass('on')){
        box.removeClass('on');
        return;
      }
    } else {
      var html = [
        '<div id="' + id + '" class="article-share-box">',
          '<div class="article-share-links">',
            '<a href="http://v.t.sina.com.cn/share/share.php?url=' + encodedUrl + '&title=' + summary + '" class="article-share-weibo" target="_blank" title="Weibo"></a>',
            '<a href="http://widget.renren.com/dialog/share?resourceUrl=' + encodedUrl + '&title=' + title + '&description=' + summary + '" class="article-share-renren" target="_blank" title="Renren"></a>',
            '<a href="https://plus.google.com/share?url=' + encodedUrl + '" class="article-share-google" target="_blank" title="Google+"></a>',
          '</div>',
        '</div>'
      ].join('');

      var box = $(html);

      $('body').append(box);
    }

    $('.article-share-box.on').hide();

    box.css({
      top: offset.top + 30,
      left: offset.left + 50
    }).addClass('on');
  }).on('click', '.article-share-box', function(e){
    e.stopPropagation();
  }).on('click', '.article-share-box-input', function(){
    $(this).select();
  }).on('click', '.article-share-box-link', function(e){
    e.preventDefault();
    e.stopPropagation();

    window.open(this.href, 'article-share-box-window-' + Date.now(), 'width=500,height=450');
  });

  // Caption
  var path = window.location.pathname;
  var reg = new RegExp('^/page\\/\\d+\\/');
  $('.article-entry').each(function(i){
    var postLink = $(this).prev().find('.article-title').attr('href');

    $(this).find('img').each(function(){
      if ($(this).parent().hasClass('fancybox')) return;

      var alt = this.alt;
      var target;
      if (path === '/'|| reg.test(path)){
        target = postLink;
      } else {
        target = this.src;
      }
//      if (alt) $(this).after('<span class="caption">' + alt + '</span>');

      $(this).wrap('<a href="' + target + '" title="' + alt + '" class="fancybox"></a>');
    });

    $(this).find('.fancybox').each(function(){
      $(this).attr('rel', 'article' + i);
    });
  });

  if ($.fancybox){
    $('.fancybox').fancybox();
  }

  // Mobile nav
  var $container = $('#container'),
    isMobileNavAnim = false,
    mobileNavAnimDuration = 200;

  var startMobileNavAnim = function(){
    isMobileNavAnim = true;
  };

  var stopMobileNavAnim = function(){
    setTimeout(function(){
      isMobileNavAnim = false;
    }, mobileNavAnimDuration);
  }

  $('#main-nav-toggle').on('click', function(){
    if (isMobileNavAnim) return;

    startMobileNavAnim();
    $container.toggleClass('mobile-nav-on');
    stopMobileNavAnim();
  });

  $('#wrap').on('click', function(){
    if (isMobileNavAnim || !$container.hasClass('mobile-nav-on')) return;

    $container.removeClass('mobile-nav-on');
  });

  //Got to top
    $(window).scroll(function () {
        var d = document.documentElement.scrollTop + document.body.scrollTop;
        if (d > 200) {
            $('#gotop').fadeIn(400)
        } else {
            $('#gotop').stop().fadeOut(400)
        }
    });
    $('#gotop').click(function () {
        $('html,body').animate({
            scrollTop: '0px'
        }, 200)
    });

  var navHeight = $('#main-nav').outerHeight(true);

  //Wiki TOC
  $('#wiki-toc-wrap').affix({
    offset: {
      top: 100
    , bottom: function () {
        return (this.bottom = $('#footer').outerHeight(true) + navHeight);
      }
    }
  });

  var $affix = $("#wiki-toc-wrap"),
    $parent = $("#wiki-sidebar"),
    affix_resize = function() {
      var wid = $parent.width() - parseInt($parent.css('paddingLeft')) - parseInt($parent.css('paddingRight'))
                        - parseInt($parent.css('marginLeft')) - parseInt($parent.css('marginRight'))
                        - parseInt($affix.css('paddingLeft')) - parseInt($affix.css('marginLeft'));
      $affix.width(wid);
    };
  $(window).resize(affix_resize);
  var affix_load = function() {
    var wid = $parent.width() - parseInt($parent.css('paddingLeft')) - parseInt($parent.css('paddingRight'));
    $affix.width(wid);
  };
  affix_load();

  $('body').scrollspy({ target: '#wiki-toc-wrap', offset: navHeight });

  $("[href^='#']").not("[href~='#']").click(function(evt){
    evt.preventDefault();
    var obj = $(this),
    getHref = obj.attr("href").split("#")[1],
    offsetSize = $("[id*='"+getHref+"']").offset().top - navHeight;
    $("html, body").animate({ scrollTop: offsetSize }, 200);
  });

})(jQuery);
