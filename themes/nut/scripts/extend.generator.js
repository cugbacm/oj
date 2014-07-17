var generator = hexo.extend.generator,
  config = hexo.config;

var tagIndex = function(locals, render, callback){

  var tagDir = config.tag_dir + '/';

  var tags = locals.tags;

  render(tagDir, ['tag', 'archive', 'index'], {tags: tags, type: 'index'});

  callback();
};

var catIndex = function(locals, render, callback){

  var catDir = config.category_dir + '/';

  var cats = locals.categories;

  render(catDir, ['category', 'archive', 'index'], {cats: cats, type: 'index'});

  callback();
};

var archiveIndex = function(locals, render, callback){

  var archiveDir = config.archive_dir + '/';

  var posts = locals.posts;

  render(archiveDir, ['archive', 'index'], {posts: posts, type: 'index'});

  callback();
};

var wikiIndex = function(locals, render, callback){
  var wikiDir = hexo._themeConfig.wiki_dir + '/',
    reg = new RegExp('^' + wikiDir),
    wikis = new Array();

  var pages = locals.pages;

  pages.each(function(page){
    if (reg.test(page.path)){
      wikis.push(page);
    }
  });

  render(wikiDir, ['wiki', 'index'], {wikis: wikis, title: 'Wiki'});

  callback();
};

generator.register(tagIndex);
generator.register(catIndex);
generator.register(archiveIndex);
generator.register(wikiIndex);
