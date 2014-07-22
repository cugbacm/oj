title: HTML基础篇
date: 2014-07-09 16:31:44
tags: [HTML]
categories: HTML
toc: true
---
# 简介

---

**什么是 HTML？**
HTML 是用来描述网页的一种语言。
- HTML 指的是超文本标记语言 (Hyper Text Markup Language)
- HTML 不是一种编程语言，而是一种**标记语言** (markup language)
- 标记语言是一套**标记标签** (markup tag)
- HTML 使用**标记标签**来描述网页

---

**HTML 标签**
HTML 标记标签通常被称为 HTML 标签 (HTML tag)。
- HTML 标签是由**尖括号**包围的关键词，比如 `<html>`
- HTML 标签通常是**成对**出现的，比如 `<b>` 和 `</b>`
- 标签对中的第一个标签是**开始标签**，第二个标签是**结束标签**
- 开始和结束标签也被称为**开放标签**和**闭合标签**

---

**HTML 文档 = 网页**
- HTML 文档**描述**网页
- HTML 文档**包含 HTML 标签**和纯文本
- HTML 文档也被称为**网页**
Web 浏览器的作用是读取 HTML 文档，并以网页的形式显示出它们。浏览器不会显示 HTML 标签，而是使用标签来解释页面的内容：
```
<html>
<body>

<h1>My First Heading</h1>

<p>My first paragraph.</p>

</body>
</html>
```

**例子解释**
- `<html>` 与 `</html>` 之间的文本描述网页
- `<body>` 与 `</body>` 之间的文本是可见的页面内容
- `<h1>` 与 `</h1>` 之间的文本被显示为标题
- `<p>` 与 `</p>` 之间的文本被显示为段落

---

# 基础

## HTML 标题

HTML 标题（Heading）是通过 `<h1>` - `<h6>` 等标签进行定义的。

**实例**

```
<h1>This is a heading</h1>
<h2>This is a heading</h2>
<h3>This is a heading</h3>
```

## HTML 段落

HTML 段落是通过 `<p>` 标签进行定义的。

**实例**

```
<p>This is a paragraph.</p>
<p>This is another paragraph.</p>
```

## HTML 链接

HTML 链接是通过 `<a>` 标签进行定义的。

**实例**

```
<a href="http://www.w3school.com.cn">This is a link</a>
```

**注释**
在 href 属性中指定链接的地址。
（您将在本教程稍后的章节中学习更多有关属性的知识）。

## HTML 图像
HTML 图像是通过 `<img>` 标签进行定义的。

**实例**

```
<img src="w3school.jpg" width="104" height="142" />
```

**注释**
图像的名称和尺寸是以属性的形式提供的。

---

# 元素

**HTML 元素语法**
- HTML 元素以**开始标签**起始
- HTML 元素以**结束标签**终止
- **元素的内容**是开始标签与结束标签之间的内容
- 某些 HTML 元素具有**空内容（empty content）**
- 空元素在**开始标签中进行关闭**（以开始标签的结束而结束）
- 大多数 HTML 元素可拥有**属性**

---

# 属性

**HTML 属性**
HTML 标签可以拥有**属性**。属性提供了有关 HTML 元素的**更多的信息**。
属性总是以名称/值对的形式出现，比如：`name="value"`。
属性总是在 HTML 元素的**开始标签**中规定。

---

# 标题

**HTML 标题**

标题（Heading）是通过 `<h1>` - `<h6>` 等标签进行定义的。
`<h1>` 定义最大的标题。
`<h6>` 定义最小的标题。

**HTML 水平线**

`<hr />` 标签在 HTML 页面中创建水平线。
`hr` 元素可用于分隔内容。

>HTML 提示 - 如何查看源代码
您一定曾经在看到某个网页时惊叹道 “WOW! 这是如何实现的？”
如果您想找到其中的奥秘，只需要单击右键，然后选择“查看源文件”（IE）或“查看页面源代码”（Firefox），其他浏览器的做法也是类似的。这么做会打开一个包含页面 HTML 代码的窗口。

---

# 段落

**HTML 段落**

段落是通过 `<p>` 标签定义的。不要忘记加上`</p>`

---

# 格式化

---

# 编辑器
使用 `Notepad` 或 `TextEdit` 来编写 HTML
可以使用专业的 HTML 编辑器来编辑 HTML：
- Adobe Dreamweaver
- Microsoft Expression Web
- CoffeeCup HTML Editor
不过，我们同时推荐使用文本编辑器来学习 HTML，比如 `Notepad (PC)` 或 `TextEdit (Mac)`。我们相信，使用一款简单的文本编辑器是学习 HTML 的好方法。

---

# 样式

## 如何使用样式

当浏览器读到一个样式表，它就会按照这个样式表来对文档进行格式化。有以下三种方式来插入样式表：

### 外部样式表

当样式需要被应用到很多页面的时候，外部样式表将是理想的选择。使用外部样式表，你就可以通过更改一个文件来改变整个站点的外观。

```
<head>
<link rel="stylesheet" type="text/css" href="mystyle.css">
</head>
```

### 内部样式表

当单个文件需要特别样式时，就可以使用内部样式表。你可以在 head 部分通过 `<style>` 标签定义内部样式表。

```
<head>
<style type="text/css">
body {background-color: red}
p {margin-left: 20px}
</style>
</head>
```

### 内联样式
当特殊的样式需要应用到个别元素时，就可以使用内联样式。 使用内联样式的方法是在相关的标签中使用样式属性。样式属性可以包含任何 CSS 属性。以下实例显示出如何改变段落的颜色和左外边距。

```
<p style="color: red; margin-left: 20px">
This is a paragraph
</p>
```

---

# 链接

## HTML 超链接

超链接可以是一个字，一个词，或者一组词，也可以是一幅图像，您可以点击这些内容来跳转到新的文档或者当前文档中的某个部分。
当您把鼠标指针移动到网页中的某个链接上时，箭头会变为一只小手。
我们通过使用 `<a>` 标签在 HTML 中创建链接。
有两种使用 `<a>` 标签的方式：
1. 通过使用 href 属性 - 创建指向另一个文档的链接
2. 通过使用 name 属性 - 创建文档内的书签

## HTML 链接 - name 属性

name 属性规定锚（anchor）的名称。
您可以使用 name 属性创建 HTML 页面中的书签。
书签不会以任何特殊方式显示，它对读者是不可见的。
当使用命名锚（named anchors）时，我们可以创建直接跳至该命名锚（比如页面中某个小节）的链接，这样使用者就无需不停地滚动页面来寻找他们需要的信息了。

**命名锚的语法：**

```
<a name="label">锚（显示在页面上的文本）</a>
```

**提示**：锚的名称可以是任何你喜欢的名字。
**提示**：您可以使用 id 属性来替代 name 属性，命名锚同样有效。

---

# 图像

**图像标签（`<img>`）和源属性（`Src`）**

在 HTML 中，图像由 `<img>` 标签定义。
`<img>` 是空标签，意思是说，它只包含属性，并且没有闭合标签。
要在页面上显示图像，你需要使用源属性（`src`）。`src` 指 `"source"`。源属性的值是图像的 URL 地址。

---

# 表格

## 表格

表格由 `<table>` 标签来定义。每个表格均有若干行（由 `<tr>` 标签定义），每行被分割为若干单元格（由 `<td>` 标签定义）。字母 td 指表格数据（table data），即数据单元格的内容。数据单元格可以包含文本、图片、列表、段落、表单、水平线、表格等等。

```
<table border="1">
<tr>
<td>row 1, cell 1</td>
<td>row 1, cell 2</td>
</tr>
<tr>
<td>row 2, cell 1</td>
<td>row 2, cell 2</td>
</tr>
</table>
```

在浏览器显示如下：

<table border="1">
<tr>
<td>row 1, cell 1</td>
<td>row 1, cell 2</td>
</tr>
<tr>
<td>row 2, cell 1</td>
<td>row 2, cell 2</td>
</tr>
</table>

## 表格和边框属性

如果不定义边框属性，表格将不显示边框。有时这很有用，但是大多数时候，我们希望显示边框。
使用边框属性来显示一个带有边框的表格：

```
<table border="1">
<tr>
<td>Row 1, cell 1</td>
<td>Row 1, cell 2</td>
</tr>
</table>
```

## 表格的表头

表格的表头使用 `<th>` 标签进行定义。
大多数浏览器会把表头显示为粗体居中的文本：

```
<table border="1">
<tr>
<th>Heading</th>
<th>Another Heading</th>
</tr>
<tr>
<td>row 1, cell 1</td>
<td>row 1, cell 2</td>
</tr>
<tr>
<td>row 2, cell 1</td>
<td>row 2, cell 2</td>
</tr>
</table>
```

在浏览器显示如下：

<table border="1">
<tr>
<th>Heading</th>
<th>Another Heading</th>
</tr>
<tr>
<td>row 1, cell 1</td>
<td>row 1, cell 2</td>
</tr>
<tr>
<td>row 2, cell 1</td>
<td>row 2, cell 2</td>
</tr>
</table>

## 表格中的空单元格

在一些浏览器中，没有内容的表格单元显示得不太好。如果某个单元格是空的（没有内容），浏览器可能无法显示出这个单元格的边框。

```
<table border="1">
<tr>
<td>row 1, cell 1</td>
<td>row 1, cell 2</td>
</tr>
<tr>
<td></td>
<td>row 2, cell 2</td>
</tr>
</table>
```

浏览器可能会这样显示：

<table border="1">
<tr>
<td>row 1, cell 1</td>
<td>row 1, cell 2</td>
</tr>
<tr>
<td></td>
<td>row 2, cell 2</td>
</tr>
</table>

**注意**：这个空的单元格的边框没有被显示出来。为了避免这种情况，在空单元格中添加一个空格占位符，就可以将边框显示出来。

```
<table border="1">
<tr>
<td>row 1, cell 1</td>
<td>row 1, cell 2</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>row 2, cell 2</td>
</tr>
</table>
```

在浏览器中显示如下：
<table border="1">
<tr>
<td>row 1, cell 1</td>
<td>row 1, cell 2</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>row 2, cell 2</td>
</tr>
</table>

---

# 列表

## 无序列表

无序列表是一个项目的列表，此列项目使用粗体圆点（典型的小黑圆圈）进行标记。
无序列表始于 `<ul>` 标签。每个列表项始于 `<li>`。

## 有序列表

同样，有序列表也是一列项目，列表项目使用数字进行标记。
有序列表始于 `<ol>` 标签。每个列表项始于 `<li>` 标签。

## 定义列表

自定义列表不仅仅是一列项目，而是项目及其注释的组合。
自定义列表以 `<dl>` 标签开始。每个自定义列表项以 `<dt>` 开始。每个自定义列表项的定义以 `<dd>` 开始。

---

# 块

## HTML 块元素

大多数 HTML 元素被定义为块级元素或内联元素。
编者注：“块级元素”译为 block level element，“内联元素”译为 inline element。
块级元素在浏览器显示时，通常会以新行来开始（和结束）。
例子：`<h1>`, `<p>`, `<ul>`, `<table>`

## HTML 内联元素

内联元素在显示时通常不会以新行开始。
例子：`<b>`, `<td>`, `<a>`, `<img>`

## HTML `<div>` 元素

HTML `<div>` 元素是块级元素，它是可用于组合其他 HTML 元素的容器。
`<div>` 元素没有特定的含义。除此之外，由于它属于块级元素，浏览器会在其前后显示折行。
如果与 CSS 一同使用，`<div>` 元素可用于对大的内容块设置样式属性。
`<div>` 元素的另一个常见的用途是文档布局。它取代了使用表格定义布局的老式方法。使用 `<table>` 元素进行文档布局不是表格的正确用法。`<table>` 元素的作用是显示表格化的数据。

## HTML `<span>` 元素

HTML `<span>` 元素是内联元素，可用作文本的容器。
`<span>` 元素也没有特定的含义。
当与 CSS 一同使用时，`<span>` 元素可用于为部分文本设置样式属性。

---

# 布局

## 网站布局

大多数网站会把内容安排到多个列中（就像杂志或报纸那样）。
可以使用 `<div>` 或者 `<table>` 元素来创建多列。CSS 用于对元素进行定位，或者为页面创建背景以及色彩丰富的外观。

**提示**：即使可以使用 HTML 表格来创建漂亮的布局，但设计表格的目的是呈现表格化数据 - 表格不是布局工具！

## HTML 布局 - 有用的提示

提示：使用 CSS 最大的好处是，如果把 CSS 代码存放到外部样式表中，那么站点会更易于维护。通过编辑单一的文件，就可以改变所有页面的布局。

**提示**：由于创建高级的布局非常耗时，使用模板是一个快速的选项。通过搜索引擎可以找到很多免费的网站模板（您可以使用这些预先构建好的网站布局，并优化它们）。

---

# 表单

## 表单

表单是一个包含表单元素的区域。
表单元素是允许用户在表单中（比如：文本域、下拉列表、单选框、复选框等等）输入信息的元素。
表单使用表单标签（`<form>`）定义。

## 输入
多数情况下被用到的表单标签是输入标签（`<input>`）。输入类型是由类型属性（type）定义的。大多数经常被用到的输入类型如下：

### 文本域（Text Fields）

当用户要在表单中键入字母、数字等内容时，就会用到文本域。

```
<form>
First name: 
<input type="text" name="firstname" />
<br />
Last name: 
<input type="text" name="lastname" />
</form>
```

浏览器显示如下：

<form>
First name: 
<input type="text" name="firstname" />
<br />
Last name: 
<input type="text" name="lastname" />
</form>

**注意**：表单本身并不可见。同时，在大多数浏览器中，文本域的缺省宽度是20个字符。

### 单选按钮（Radio Buttons）

当用户从若干给定的的选择中选取其一时，就会用到单选框。

```
<form>
<input type="radio" name="sex" value="male" /> Male
<br />
<input type="radio" name="sex" value="female" /> Female
</form>
```

浏览器显示如下：

<form>
<input type="radio" name="sex" value="male" /> Male
<br />
<input type="radio" name="sex" value="female" /> Female
</form>

**注意**：只能从中选取其一。

### 复选框（Checkboxes）

当用户需要从若干给定的选择中选取一个或若干选项时，就会用到复选框。

```
<form>
<input type="checkbox" name="bike" />
I have a bike
<br />
<input type="checkbox" name="car" />
I have a car
</form>
```

浏览器显示如下：

<form>
<input type="checkbox" name="bike" />
I have a bike
<br />
<input type="checkbox" name="car" />
I have a car
</form>

### 表单的动作属性（Action）和确认按钮

当用户单击确认按钮时，表单的内容会被传送到另一个文件。表单的动作属性定义了目的文件的文件名。由动作属性定义的这个文件通常会对接收到的输入数据进行相关的处理。

```
<form name="input" action="html_form_action.asp" method="get">
Username: 
<input type="text" name="user" />
<input type="submit" value="Submit" />
</form>
```

浏览器显示如下：

<form name="input" action="html_form_action.asp" method="get">
Username: 
<input type="text" name="user" />
<input type="submit" value="Submit" />
</form>
假如您在上面的文本框内键入几个字母，然后点击确认按钮，那么输入数据会传送到 `html_form_action.asp` 的页面。该页面将显示出输入的结果。

---

# 框架

通过使用框架，你可以在同一个浏览器窗口中显示不止一个页面。每份HTML文档称为一个框架，并且每个框架都独立于其他的框架。

**框架结构标签（`<frameset>`）**

- 框架结构标签（`<frameset>`）定义如何将窗口分割为框架
- 每个 `frameset` 定义了一系列行**或**列
- `rows/columns` 的值规定了每行或每列占据屏幕的面积
- 
**基本的注意事项 - 有用的提示：**

假如一个框架有可见边框，用户可以拖动边框来改变它的大小。为了避免这种情况发生，可以在 `<frame>` 标签中加入：`noresize="noresize"`。
为不支持框架的浏览器添加 `<noframes>` 标签。

**重要提示**：不能将 `<body>` `</body>` 标签与 `<frameset>` `</frameset>` 标签同时使用！不过，假如你添加包含一段文本的 `<noframes>` 标签，就必须将这段文字嵌套于 `<body>` `</body>` 标签内。

---

# 内联框架

## 添加 iframe 的语法

```
<iframe src="URL"></iframe>
```

URL 指向隔离页面的位置。

## Iframe - 设置高度和宽度

`height` 和 `width` 属性用于规定 `iframe` 的高度和宽度。
属性值的默认单位是像素，但也可以用百分比来设定（比如 "80%"）。

## 使用 iframe 作为链接的目标

iframe 可用作链接的目标（target）。
链接的 target 属性必须引用 iframe 的 name 属性：

**实例**

```
<iframe src="demo_iframe.htm" name="iframe_a"></iframe>
<p><a href="http://www.w3school.com.cn" target="iframe_a">W3School.com.cn</a></p>
```

---

# 背景

## 背景（Backgrounds）

`<body>` 拥有两个配置背景的标签。背景可以是颜色或者图像。

## 背景颜色（Bgcolor）

背景颜色属性将背景设置为某种颜色。属性值可以是十六进制数、RGB 值或颜色名。

```
<body bgcolor="#000000">
<body bgcolor="rgb(0,0,0)">
<body bgcolor="black">
```

以上的代码均将背景颜色设置为黑色。

## 背景（Background）

背景属性将背景设置为图像。属性值为图像的URL。如果图像尺寸小于浏览器窗口，那么图像将在整个浏览器窗口进行复制。

```
<body background="clouds.gif">
<body background="http://www.w3school.com.cn/clouds.gif">
```

URL可以是相对地址，如第一行代码。也可以使绝对地址，如第二行代码。

**提示**：如果你打算使用背景图片，你需要紧记一下几点：
- 背景图像是否增加了页面的加载时间。小贴士：图像文件不应超过 10k。
- 背景图像是否与页面中的其他图象搭配良好。
- 背景图像是否与页面中的文字颜色搭配良好。
- 图像在页面中平铺后，看上去还可以吗？
- 对文字的注意力被背景图像喧宾夺主了吗？

**基本的注意事项 - 有用的提示：**

`<body>` 标签中的背景颜色（bgcolor）、背景（background）和文本（text）属性在最新的 HTML 标准（HTML4 和 XHTML）中已被废弃。W3C 在他们的推荐标准中已删除这些属性。
应该使用层叠样式表（CSS）来定义 HTML 元素的布局和显示属性。