# Nut

A new theme for [Hexo](http://zespia.tw/hexo/) based on the new default theme [Landscape](https://github.com/hexojs/hexo-theme-landscape), and get some ideas form [HaHack](http://www.hahack.com/)

- [Preview](http://nutinn.com/)

## Installation

### Install

``` bash
$ git clone https://github.com/seff/nut.git themes/nut
```

**Nut requires Hexo 2.4 and above.**

**lodash and marked modules are required by Nut**
``` sh
npm install lodash --save
npm install marked --save
```

### Enable

Modify `theme` setting in `_config.yml` to `nut`.

### Update

``` bash
cd themes/nut
git pull
```

## Configuration
Most of the configurations are the same with Landscape, but the following.

``` yml
pages:
- about
- wiki

wiki_dir: wiki
wiki_info:

home_widgets:
- search
- category
- tag
- archive
- blogroll
act_widgets:
- search
- recent_posts
- blogroll
post_widgets:
- nav
- post_date
- post_category
- post_tag

links:
- name: My Github
  url: https://github.com/
  logo: github
```

- **pages** - Pages that will appear on navigation bar, you must create it first.
- **wiki_dir** - Wiki directory name which locates in the `source` directory, the root directory of wiki should not create any file, the index file is generated automatically.
- **wiki_info** - Description of your wiki.
- **home_widgets** - Widgets displaying in the home page.
- **act_widgets** - Widgets displaying in the archives page, categories page and tags page.
- **post_widgets** - Widgets displaying in the post page.
- **links** - Links displaying in the blogroll widget.
	- **name** - The name of the link.
	- **url** - The url of the link.
	- **logo** - The logo of the link,  which should place the last words of the Font Awesome style, for example, you should assign `github` here for the github page link whose Font Awesome style is `fa fa-github`.

## Features

### All features of the Landscape theme

### Bootstrap

Nut uses [Bootstrap](http://getbootstrap.com/) framework, which is **The most popular front-end framework for developing responsive, mobile first projects on the web**.

### Sidebar

You can configure different pages with different widgets.

### Wiki
You can write your personal wiki on your blog now, not complex, write just like writing a post.

**How to**

- Make a directory in the source directory named **wiki** or the other name that you configure in the `_config.yml` file above.
- Make a sub directory in the wiki directory, whose name is the category of this wiki page.
- Copy the page template in the **scaffolds** directory to the current path, then start your writing.

By default, the directory name is the category of the wiki page, and we only support one level sub directory now.

### Tags
There are a few custom tags for writing post, you can check the syntax by reading the `extend.tag.js` in `scripts` directory.
