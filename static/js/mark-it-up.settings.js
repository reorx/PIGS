// mIu nameSpace to avoid conflict. //
miu = {
    markdownTitle: function(markItUp, char) {
       heading = '';
       n = $.trim(markItUp.selection||markItUp.placeHolder).length;
       for(i = 0; i < n; i++) {
           heading += char;
       }
       return '\n'+heading+'\n';
    }
}
// markitup settings //
var markitupSettings = {	
    nameSpace:          'markdown', // Useful to prevent multi-instances CSS conflict
    previewParserPath:  '~/sets/markdown/preview.php',
    onShiftEnter:       {keepDefault:false, openWith:'\n\n'},
    markupSet: [
        {name:'H1', key:"1", placeHolder:'Your title here...', closeWith:function(markItUp) { return miu.markdownTitle(markItUp, '=') } },
        {name:'H2', key:"2", placeHolder:'Your title here...', closeWith:function(markItUp) { return miu.markdownTitle(markItUp, '-') } },
        {name:'h3', key:"3", openWith:'### ', placeHolder:'Your title here...' },
        /*{name:'', key:"4", openWith:'#### ', placeHolder:'Your title here...' },
        {name:'Heading 5', key:"5", openWith:'##### ', placeHolder:'Your title here...' },*/
        {name:'h6', key:"6", openWith:'###### ', placeHolder:'Your title here...' },
        {name:'B', key:"B", openWith:'**', closeWith:'**'},
        {name:'I', key:"I", openWith:'_', closeWith:'_'},
        {name:'Code', key:"N", openWith:'(!(\t|!|`)!)', closeWith:'(!(`)!)'},
        {name:'>', openWith:'> '},
        {name:'Num', openWith:function(markItUp) { return markItUp.line+'. '; }},
        {name:'L', key:"L", openWith:'[', closeWith:'](http:// "")', placeHolder:'Your text to link here...' },
        {name:'Pic', key:"P", openWith:'![alt](http://', closeWith:' "")', placeHolder:'url'},
        {name:'-', openWith:'- ' },
        /*{name:'Picture', key:"P", replaceWith:'![[![Alternative text]!]]([![Url:!:http://]!] "[![Title]!]")'},*/
        /*{name:'Link', key:"L", openWith:'[', closeWith:']([![Url:!:http://]!] "[![Title]!]")', placeHolder:'Your text to link here...' },*/
    ]
}

