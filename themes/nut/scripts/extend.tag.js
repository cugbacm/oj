var render = hexo.render,
  tag = hexo.extend.tag,
  helper = hexo.extend.helper;

/**
* margin note tag
*
* Syntax:
* {% mnote index %}
* Margin note string
* {% endmnote %}
*/
var mnote = function(args, content){
  if (args){
    var index = args[0];
    mnote = '<span class="note-marker"><sup>' + index + '</sup></span> <span class="block note-outer"><span class="block note-inner"><span class="note"><span class="note-marker">' + index + '</span>' + content + '</span></span></span>';
  } else {
    mnote = '<span class="block note-outer"><span class="block note-inner"><span class="note">' + content + '</span></span></span>';
  }

  var text = render.renderSync({text: mnote, engine: 'markdown'});
  text = text.substring(3, text.length-5);

  return text;
};

/**
* margin image tag
*
* Syntax:
* {% mimg url text index %}
*/
var mimg = function(args, content){
  var url = args[0];
  var text = args[1];
  var index = args[2];

  return '<span class="block note-outer"><span class="block note-inner"><span class="block note"><img src=' + url + ' alt="' + text + '" /></span><div class="note-banner"><b>Fig.' + index + '</b> ' + text + '</div></span></span>';
};

/**
* info tag
*
* Syntax:
* {% info caption [style] %}
* Alert string
* {% endalert %}
*/
var info = function(args, content){
  var caption = args[0];
  var style;
  if (args.length > 1)
    style = args[1];
  else
    style = "info";

  var text = '<div class="alert alert-' + style + '"><i class="fa fa-info-circle"></i><strong>' + caption + '</strong>' + content + '</div>';

  return render.renderSync({text: text, engine: 'markdown'});
};

/**
* label tag
*
* Syntax:
* {% label text [style] %}
*/
var label = function(args, content){
  var text = args[0];
  var style;
  if (args.length > 1)
    style = args[1];
  else
    style = "primary";

  return '<span class="label label-' + style +'">' + text + '</span>'
};

/**
* local image tag
*
* Syntax:
* {% limg image [style] %}
*/
var limg = function(args, content){
  var imageName = args[0];

  var src   = '/images/' + imageName;
  var cls = args[1] || 'post-image';

  return '<img src="' + src + '" class="' + cls + '" />';
};

/**
* local file tag
*
* Syntax:
* {% attach file [path] %}
*/
var attach = function(args, content){
  var fileName = args[0];
  var path = args[1] || 'downloads';
  var fullPath = hexo.config.root + path + '/' + fileName;

  return '<a href="' + fullPath + '" download="' + fileName + '">' + fileName + '</a>'
}

tag.register('mnote', mnote, true);
tag.register('mimg', mimg, false);
tag.register('info', info, true);
tag.register('label', label, false);
tag.register('limg', limg, false);
tag.register('attach', attach, false);
