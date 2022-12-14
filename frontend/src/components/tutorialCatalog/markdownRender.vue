<template>
  <div class="container">
    <markdown-it-vue class="md-body" :content="content" :options="options" />
  </div>
</template>

<script>
import MarkdownItVue from "markdown-it-vue";
import "markdown-it-vue/dist/markdown-it-vue.css";

export default {
  components: {
    MarkdownItVue,
  },
  data() {
    return {
      content: `
# markdown-it-vue
## Image size and Viewer
![gvf](https://ucarecdn.com/05f649bf-b70b-4cf8-90f7-2588ce404a08/-/format/auto/ =150x150)
## GitHub Table of Contents
[toc]
Note: Only \`h2\` and \`h3\` are shown in toc.
## alter
Markup is similar to fenced code blocks. Valid container types are \`success\`, \`info\`, \`warning\` and \`error\`.
::: success
You have got it.
:::
::: info
You have new mail.
:::
::: warning
You have new mail.
:::
::: error
Staying up all night is bad for health.
:::
## mermaid charts
### mermaid Flowchart
[Flowchart Syntax](http://knsv.github.io/mermaid/#flowcharts-basic-syntax)
\`\`\`mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
\`\`\`
\`\`\`
sequenceDiagram
    participant Alice
    participant Bob
    Alice->John: Hello John, how are you?
    loop Healthcheck
        John->John: Fight against hypochondria
    end
    Note right of John: Rational thoughts <br/>prevail...
    John-->Alice: Great!
    John->Bob: How about you?
    Bob-->John: Jolly good!
\`\`\`
## Definition list
Term 1
  ~ Definition 1
Term 2
  ~ Definition 2a
  ~ Definition 2b
[Definition List Syntax](http://pandoc.org/README.html#definition-lists)
## AsciiMath
Inline AsciiMath: \`@(1/2[1-(1/2)^n])/(1-(1/2))=s_n@\`
\`\`\`AsciiMath
oint_Cx^3 dx+4y^2 dy
2=(((3-x)xx2)/(3-x))
sum_(m=1)^oosum_(n=1)^oo(m^2 n)/(3^m(m3^n+n3^m)
\`\`\`
\`\`\`ASCIIMath
phi_n(kappa) = 1/(4pi^2 kappa^2)
 int_0^oo (sin(kappa R))/(kappa R)
 del/(del R)
[R^2 (del D_n (R))/(del R)] del R
\`\`\`
[AsciiMath Documentation](http://asciimath.org/)
## Subscript: H~2~O
You can also use inline math: \`$H_2O$\`
## Superscript: 29^th^
You can also use inline math: \`$29^{th}$\`
## Emoji: :panda_face: :sparkles: :camel: :boom: :pig:
[Emoji Cheat Sheet](http://www.emoji-cheat-sheet.com/)
## Fontawesome: :fa-car: :fa-flag: :fa-bicycle: :fa-leaf: :fa-heart:
[All the Font Awesome icons](http://fontawesome.io/icons/)
## Echarts
[Documentation for Echarts](http://echarts.baidu.com)
The width and height is the size for chart container.
\`\`\`echarts
{
  "width": 500,
  "height": 400,
  "series": [
    {
      "name": "????????????",
      "type": "pie",
      "radius": "55%",
      "data": [
        {
          "value": 235,
          "name": "????????????"
        },
        {
          "value": 274,
          "name": "????????????"
        },
        {
          "value": 310,
          "name": "????????????"
        },
        {
          "value": 335,
          "name": "????????????"
        },
        {
          "value": 400,
          "name": "????????????"
        }
      ]
    }
  ]
}
\`\`\`
## code
### c
\`\`\`c
#include <stdio.h>
int main(int argc char* argv[]) {
  printf("Hello, World!");
  return 0;
}
\`\`\`
### json
\`\`\`json
{
  "name": "markdown-it-vue"
}
\`\`\`
### javascript
\`\`\`json
import MarkdownItVue from 'markdown-it-vue'
export default {
  components: {
    MarkdownItVue
  }
}
\`\`\`
### bash
\`\`\`bash
npm install markdown-it-vue
\`\`\`
## table
| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
## flowchart.js
\`\`\`flowchart.js
st=>start: Start|past:>http://www.google.com[blank]
e=>end: End:>http://www.google.com
op1=>operation: My Operation|past
op2=>operation: Stuff|current
sub1=>subroutine: My Subroutine|invalid
cond=>condition: Yes
or No?|approved:>http://www.google.com
c2=>condition: Good idea|rejected
io=>inputoutput: catch something...|request
para=>parallel: parallel tasks
st->op1(right)->cond
cond(yes, right)->c2
cond(no)->para
c2(true)->io->e
c2(false)->e
para(path1, bottom)->sub1(left)->op1
para(path2, right)->op2->e
st@>op1({"stroke":"Red"})@>cond({"stroke":"Red","stroke-width":6,"arrow-end":"classic-wide-long"})@>c2({"stroke":"Red"})@>op2({"stroke":"Red"})@>e({"stroke":"Red"})
\`\`\`
`,
      options: {
        markdownIt: {
          linkify: true,
        },
        linkAttributes: {
          attrs: {
            target: "_self",
            rel: "noopener",
          },
        },
      },
    };
  },
};
</script>

<style scoped>
.container {
  width: 100%;
}
</style>