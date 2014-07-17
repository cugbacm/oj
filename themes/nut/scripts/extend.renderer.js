var marked = require('marked'),
  renderer = new marked.Renderer();

var heading_anchor = function(data, options, callback){
  var src = data.text.toString();
  renderer.heading = function (text, level) {
    var escapedText = text.toLowerCase().replace(/[\s]+/g, '-');

    return '<h' + level + ' id="' + escapedText + '">' + text + '</h' + level + '>';
  };

  return marked(src, {renderer: renderer});
};

hexo.extend.renderer.register('md', 'html', heading_anchor, true);
hexo.extend.renderer.register('markdown', 'html', heading_anchor, true);
hexo.extend.renderer.register('mkd', 'html', heading_anchor, true);
hexo.extend.renderer.register('mkdn', 'html', heading_anchor, true);
hexo.extend.renderer.register('mdwn', 'html', heading_anchor, true);
hexo.extend.renderer.register('mdtxt', 'html', heading_anchor, true);
hexo.extend.renderer.register('mdtext', 'html', heading_anchor, true);
