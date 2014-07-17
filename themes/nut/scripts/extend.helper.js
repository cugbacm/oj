var _ = require('lodash'),
  path = require('path'),
  config = hexo.config,
  helper = hexo.extend.helper;

var ct_name_to_id = function(ct){
  return ct.toLowerCase().replace(/[\s]+/g, '-');
};

var _list_cats_tags = function(cts, options){
  if (!options){
    options = tags;
    tags = this.site.tags;
  }

  if (!cts.length) return '';

  var options = _.extend({
    show_count: true,
    class: 'ct',
    label: true,
    anchor: false
  }, options);

  var showCount = options.show_count,
    className = options.class,
    showLabel = options.label,
    linkTarget = options.anchor,
    root = hexo.config.root,
    label_style = ['primary', 'success', 'info', 'warning', 'danger'],
    rtn = '<ul class="' + className + '-list">',
    link_class = '',
    target = '',
    arr = [];

    cts.sort('name', 1).each(function(ct, i){
      if (showLabel) {
        link_class = className + '-list-link label label-' + label_style[i % 5];
      } else {
         link_class = className + '-list-link';
      }
      anchorName = ct.name.toLowerCase().replace(/[\s]+/g, '-');
      target = linkTarget ? '#' + anchorName : root + ct.path;
      arr.push('<li class="' + className + '-list-item">'
        + '<a class="' + link_class +'" href="' + target + '">' + ct.name
        + (showCount ? '<span class="' + className + '-list-count">' + ct.length + '</span>' : '') + '</a>' + '</li>');
    });
    rtn += arr.join('') + '</ul>';

    return rtn;
};

var post_home = function(post){
  post = post.replace(/<div [^><]*info[^><]*>.*<\/div>/g, "");
  post = post.replace(/<span [^><]*note-outer[^><]*>.*<\/span>/g, "");

  return post;
};

var post_toc = function(post){
  var info = post.match(/<div [^><]*info[^><]*>.*<\/div>/) || '';
  var tmp = post;
  if (info.length){
    tmp = post.replace(/<div [^><]*info[^><]*>.*<\/div>/, "");
  }
  var t = helper.store.toc(post, {list_number: false, class: 'article-toc'});

  var rtn;
  if (t.length) {
    rtn = info + '<div id="toc"><span class="toc-header">Contents</span>'
      + t + '</div>' + tmp;
  } else {
    rtn = tmp;
  }

  return rtn;
};

var post_summary = function(str, n){
  var r = /[^\x00-\xff]/g;
  if(str.replace(r, "mm").length <= n){return str;}

  var m = Math.floor(n / 2);
  for(var i = m; i < str.length; i++){
    if(str.substr(0, i).replace(r, "mm").length >= n){
      return str.substr(0, i)+"...";
    }
  }

  return str;
};

var is_page = function(){
  var pages = this.theme.pages,
    rtn = false,
    reg = '';

  for(var i in pages){
    reg = new RegExp('^' + pages[i] + '\\/');
    if (reg.test(this.path)){return true;}
  }

  return false;
};

var is_wiki = function(){
  var wikiDir = this.theme.wiki_dir + '/',
    reg = new RegExp('^' + wikiDir);

  return reg.test(this.path);
};

var wiki_category = function(wiki){
  var dirName = path.dirname(wiki.path);
  var cat = path.basename(dirName);

  var w = path.dirname(dirName);

  if (w != 'wiki') {
    throw new Error("Wiki: Error path for wiki, we only support one level category.");
  }

  return cat;
};

var thumbnail = function(post, cls){
  var img =  post.match(/<img [^><]*\/*>/);

  if (img){
    var rtn = '<div class="' + cls + '">' + img + '</div>';
  }

  return rtn;
};

helper.register('ct_name_to_id', ct_name_to_id);
helper.register('_list_tags', _list_cats_tags);
helper.register('_list_categories', _list_cats_tags);
helper.register('post_home', post_home);
helper.register('post_toc', post_toc);
helper.register('post_summary', post_summary);
helper.register('is_page', is_page);
helper.register('is_wiki', is_wiki);
helper.register('wiki_category', wiki_category);
helper.register('thumbnail', thumbnail);
