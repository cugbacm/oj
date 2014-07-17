title: CSS（层叠样式表）基础知识
date: 2014-07-12 0:02:08
categories: CSS
toc: true
---
CSS 指层叠样式表 (Cascading Style Sheets)。样式定义如何显示 HTML 元素。它通常存储在样式表中，把样式添加到 HTML 4.0 中，解决内容与表现分离的问题。

**当同一个 HTML 元素被不止一个样式定义时，会使用哪个样式呢？**

一般而言，所有的样式会根据下面的规则层叠于一个新的虚拟样式表中，其中数字 4 拥有最高的优先权。
1. 浏览器缺省设置
2. 外部样式表
3. 内部样式表（位于 <head> 标签内部）
4. 内联样式（在 HTML 元素内部）
因此，内联样式（在 HTML 元素内部）拥有最高的优先权，这意味着它将优先于以下的样式声明：<head> 标签中的样式声明，外部样式表中的样式声明，或者浏览器中的样式声明（缺省值）。

# CSS 语法
CSS 规则由两个主要的部分构成：选择器，以及一条或多条声明。
`selector {declaration1; declaration2; ... declarationN }`
选择器通常是您需要改变样式的 HTML 元素。
每条声明由一个属性和一个值组成。
属性（`property`）是您希望设置的样式属性（`style attribute`）。每个属性有一个值。属性和值被冒号分开。
`selector {property: value}`
下面这行代码的作用是将 `h1` 元素内的文字颜色定义为红色，同时将字体大小设置为 14 像素。
在这个例子中，`h1` 是选择器，`color` 和 `font-size` 是属性，`red` 和 `14px` 是值。
`h1 {color:red; font-size:14px;}`
下面的示意图为您展示了上面这段代码的结构：

![img](https://raw.githubusercontent.com/cugbacm/oj/gh-pages/img/wiki/ct_css_selector.gif)

提示：请使用花括号来包围声明。

# 选择器的分组
你可以对选择器进行分组，这样，被分组的选择器就可以分享相同的声明。用逗号将需要分组的选择器分开。在下面的例子中，我们对所有的标题元素进行了分组。所有的标题元素都是绿色的。

```
h1,h2,h3,h4,h5,h6 {
  color: green;
  }
```

# 继承及其问题

根据 CSS，子元素从父元素继承属性。但是它并不总是按此方式工作。看看下面这条规则：


```
body {
     font-family: Verdana, sans-serif;
     }
```

根据上面这条规则，站点的 body 元素将使用 Verdana 字体（假如访问者的系统中存在该字体的话）。
通过 CSS 继承，子元素将继承最高级元素（在本例中是 body）所拥有的属性（这些子元素诸如 p, td, ul, ol, ul, li, dl, dt,和 dd）。不需要另外的规则，所有 body 的子元素都应该显示 Verdana 字体，子元素的子元素也一样。并且在大部分的现代浏览器中，也确实是这样的。
但是在那个浏览器大战的血腥年代里，这种情况就未必会发生，那时候对标准的支持并不是企业的优先选择。比方说，Netscape 4 就不支持继承，它不仅忽略继承，而且也忽略应用于 body 元素的规则。IE/Windows 直到 IE6 还存在相关的问题，在表格内的字体样式会被忽略。我们又该如何是好呢？

# 派生选择器

**通过依据元素在其位置的上下文关系来定义样式，你可以使标记更加简洁。**

在 CSS1 中，通过这种方式来应用规则的选择器被称为上下文选择器 (contextual selectors)，这是由于它们依赖于上下文关系来应用或者避免某项规则。在 CSS2 中，它们称为派生选择器，但是无论你如何称呼它们，它们的作用都是相同的。
派生选择器允许你根据文档的上下文关系来确定某个标签的样式。通过合理地使用派生选择器，我们可以使 HTML 代码变得更加整洁。
比方说，你希望列表中的 strong 元素变为斜体字，而不是通常的粗体字，可以这样定义一个派生选择器：
```
li strong {
    font-style: italic;
    font-weight: normal;
  }
```

请注意标记为`<strong>`的蓝色代码的上下文关系：

```
<p><strong>我是粗体字，不是斜体字，因为我不在列表当中，所以这个规则对我不起作用</strong></p>
<ol>
<li><strong>我是斜体字。这是因为 strong 元素位于 li 元素内。</strong></li>
<li>我是正常的字体。</li>
</ol>
```
在上面的例子中，只有 li 元素中的 strong 元素的样式为斜体字，无需为 strong 元素定义特别的 class 或 id，代码更加简洁。

# id 选择器

**id 选择器可以为标有特定 id 的 HTML 元素指定特定的样式。**

**id 选择器以 "#" 来定义。**

*需要注意的是：每一个id只能在同一html文档出现一次。*

在 CSS 中，类选择器以一个点号显示：
`.center {text-align: center}`
在上面的例子中，所有拥有 center 类的 HTML 元素均为居中。
在下面的 HTML 代码中，h1 和 p 元素都有 center 类。这意味着两者都将遵守 ".center" 选择器中的规则。
```
<h1 class="center">
This heading will be center-aligned
</h1>

<p class="center">
This paragraph will also be center-aligned.
</p>
```
注意：类名的第一个字符不能使用数字！它无法在 Mozilla 或 Firefox 中起作用。

要灵活运用各种类型CSS的使用，以及结合。

# 如何插入样式表
当读到一个样式表时，浏览器会根据它来格式化 HTML 文档。插入样式表的方法有三种：
## 外部样式表
当样式需要应用于很多页面时，外部样式表将是理想的选择。在使用外部样式表的情况下，你可以通过改变一个文件来改变整个站点的外观。每个页面使用 `<link>` 标签链接到样式表。`<link>` 标签在（文档的）头部：

```
<head>
<link rel="stylesheet" type="text/css" href="mystyle.css" />
</head>
```

浏览器会从文件 `mystyle.css` 中读到样式声明，并根据它来格式文档。
外部样式表可以在任何文本编辑器中进行编辑。文件不能包含任何的 html 标签。样式表应该以 `.css` 扩展名进行保存。下面是一个样式表文件的例子：

```
hr {color: sienna;}
p {margin-left: 20px;}
body {background-image: url("images/back40.gif");}
```

不要在属性值与单位之间留有空格。假如你使用 “margin-left: 20 px” 而不是 “margin-left: 20px” ，它仅在 IE 6 中有效，但是在 Mozilla/Firefox 或 Netscape 中却无法正常工作。

## 内部样式表
当单个文档需要特殊的样式时，就应该使用内部样式表。你可以使用 `<style>` 标签在文档头部定义内部样式表，就像这样:
```
<head>
<style type="text/css">
  hr {color: sienna;}
  p {margin-left: 20px;}
  body {background-image: url("images/back40.gif");}
</style>
</head>
```

## 内联样式
由于要将表现和内容混杂在一起，内联样式会损失掉样式表的许多优势。请慎用这种方法，例如当样式仅需要在一个元素上应用一次时。
要使用内联样式，你需要在相关的标签内使用样式（style）属性。Style 属性可以包含任何 CSS 属性。本例展示如何改变段落的颜色和左外边距：
```
<p style="color: sienna; margin-left: 20px">
This is a paragraph
</p>
```

## 多重样式
如果某些属性在不同的样式表中被同样的选择器定义，那么属性值将从更具体的样式表中被继承过来。
例如，外部样式表拥有针对 h3 选择器的三个属性：
```
h3 {
  color: red;
  text-align: left;
  font-size: 8pt;
  }
```
而内部样式表拥有针对 h3 选择器的两个属性：
```
h3 {
  text-align: right; 
  font-size: 20pt;
  }
```
假如拥有内部样式表的这个页面同时与外部样式表链接，那么 h3 得到的样式是：
```
color: red; 
text-align: right; 
font-size: 20pt;
```
即颜色属性将被继承于外部样式表，而文字排列（text-alignment）和字体尺寸（font-size）会被内部样式表中的规则取代。