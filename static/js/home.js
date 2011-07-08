$(document).ajaxSend(function (evt, request, settings){
    if (settings.type == 'POST') {
        request.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
    }
});
function DumpFormData(obj) {
    var jdic = {}
    var inputs = obj.find('input');
    var textareas = obj.find('textarea');
    if (inputs.length > 0) {
        inputs.each(function () {
            jdic[$(this).attr('name')] = $(this).val();
        });
    }
    if (textareas.length > 0) {
        textareas.each(function () {
            jdic[$(this).attr('name')] = $(this).val();
        });
    }
    return $.toJSON(jdic);
}
// Global var //
var AREA = {};
/* Nav, Side, Main {top, left, right, middle, bottom}
 * N, NT, NL, S, ST, SM, M, ML, MR
 */
var DOM = {}; // <dom></dom>
DOM.cate = {};
var DATA = {}; // data
DATA.know = {};
var UI = {}; // fn
//AREA.ifKMshow = 'false';

// calling fuction //
function noti(s) {
    AREA.noti.html(s).fadeIn(500).delay(1000).fadeOut(1000);
}
function hideKnowledgeMenu() {
    $('#knowledgeMenu').css({display:'none'});
}
function ajax_get_callback(url,DOM,callback) {
    $.ajax({
        type: 'GET',
        url: url,
        success: function(html){
            $(DOM).hide().html(html).fadeIn('500');
            loading_off();
            (callback);
        }
    });
    loading_on();
}
function ajax_get(url,Q) {
    $.ajax({
        type: 'GET',
        url: url,
        success: function(html){
            $(Q).html(html);//.fadeIn('500');
            loading_off();
        }
    });
    loading_on();
}
// page request //
function View_Category(id) {
    if (Boolean(id)) {
        DATA.know.category_id = id;
    } else {
        id = DATA.know.category_id;
    }
    $.ajax({
        type: 'GET',
        url: '/knowledge/view_category/?category='+id,
        success: function(html) {
            AREA.SM.html(html); // show info
            if(AREA.ST.css('display')=='none'){ AREA.ST.show('500'); } //change operate area
        }
    });
}
function ManageCates() {
    $.ajax({
        type: 'GET',
        url: '/know/category/',
        success: function(data) {
            json = eval(data);
            noti(json.message); // show info
            AREA.ST.html('Categorys').show();
            DOM.cate.create_form_wrap.appendTo(AREA.SM);
            DOM.cate.create_b.appendTo(AREA.SM);
        }
    });
}
function View_KnowledgeList() {
    id = DATA.know.category_id;
    var url = '/knowledge/view_k_list/?category='+id;
    var DOM = '#View';
        $.ajax({
            type: 'GET',
            url: url,
            success: function(html){
                $(DOM).hide().html(html).fadeIn('500');
                loading_off();
            }
        });
        loading_on();
        // jquery sortable //
}
function Content_Knowledge(id) {
    if (id) { DATA.know.id = id; }
    else { id = DATA.know.id }
    //
    var url =  '/knowledge/content_knowledge/?knowledge='+id;
    var DOM = '#Content_Main';
    ajax_get(url,DOM);
    //
    Extend_K_Info()
}
function Extend_K_Info() {
    var url = '/knowledge/extend_k_info/?k_id='+DATA.know.id;
    var Q = '#contentExtend';
    ajax_get(url,Q);
}
function Content_Add(what,mode) {
    var DOM1 = '#Content_Main';
    var DOM2 = '#contentExtend';
    $.ajax({
        type: 'GET',
        url: '/knowledge/editor_contentpart/',
        success: function(html){
            $(DOM1).html(html);
            //
            if (what == 'knowledge') {
                $.ajax({
                    type: 'GET',
                    url: '/knowledge/editor_extendpart/?mode=add&knowledge_id=',
                    success: function(html){
                        $(DOM2).html(html);
                        if (mode=="child") {
                            $.get('/knowledge/get_self_title/?knowledge_id='+DATA.know.id,function(html){
                                $('#InputParent').val(html);
                                loading_off();
                                //
                                DATA.know.id = '';
                            });
                        }
                        if (mode=='multiple') {
                            loading_off();
                            DATA.know.id = '';
                        }
                    }
                });
            } else { //what == 'content'
                var dom = $('#Submit_content').clone().css({'display':'block'})
                                              .click(function(){ add_content(); });
                $('.markItUpHeader').eq(0).append(dom);
            }
        }
    });
    loading_on();
}
function Content_EditPage() {
    var DOM1 = '#Content_Main';
    var DOM2 = '#contentExtend';
    $.ajax({
        type: 'GET',
        url: '/knowledge/editor_contentpart/?knowledge_id='+DATA.know.id,
        success: function(html){
            $(DOM1).html(html);
            //
            $.ajax({
                type: 'GET',
                url: '/knowledge/editor_extendpart/?mode=edit&knowledge_id='+DATA.know.id,
                success: function(html){
                    $(DOM2).html(html);
                    $('#Tips_wrap').show();
                    loading_off();
                }
            });
        }
    });
}
// main operate //
function delete_knowledge() {
    $.ajax({
        type: 'GET',
        url: '/knowledge/delete/?knowledge_id='+DATA.know.id,
        success: function(status){
            if (status=='') {
                loading_on('can\'t be deleted');
            } else {
                loading_on('delete item: '+status);
                AREA.item.remove();
            }
        }
    });
}
// setTimeout //
function $setTimeout(fn,t) {
    //var nf = fn;
    //alert('ss');
    setTimeout(fn,t);
}
////
$(document).ready(function() {
    // Golbal //
        // Knowledge
        DATA.know.id = '';
        //_Area
        AREA.noti = $('#loading');
        AREA.SM = $('#View');
        AREA.ST = $('#operate_category');
        AREA.ML = $('#Content_Main');
        AREA.k_menu_status = 0;
        // DOM
        DOM.cate.create_form = $('<div>', {
            id: 'cate-createform',
            
        }).append('<input type="text" name="name" /> <textarea id="" name="intro" rows="10" cols="30"></textarea>');
        DOM.cate.create_form_wrap = $('<div>').css('height','0px').append(DOM.cate.create_form);
        DOM.cate.create_b = $('<div>', {
            'class': 'ui-b-9',
            text: '+',
            click: function () {
                // anime: roll down
                DOM.cate.create_form_wrap.animate({
                    height: '200px',
                }, 500, function(){
                    DOM.cate.create_form.show();
                });
                $(this).html('save?').unbind().click(function () {
                    $.ajax({
                        type: 'POST',
                        url: '/know/category/db/',
                        data: 'action=create&data='+DumpFormData(DOM.cate.create_form),
                        success: function (resp) {
                            json = eval(resp);
                            noti(json.message);
                            if (resp.code == 200) {
                                alert('load ajax');
                                // anime: roll up
                                DOM.cate.create_form.hide();
                                DOM.cate.create_form_wrap.animate({
                                    height: '0px',
                                }, 500, function(){
                                    $(this).html('+');
                                });
                            }
                        }
                    });
                });
            }
        });
    // css relay //
    $('.NavTags').each(function(){
        var w = ($(this).children().eq(0).width()+1)*($(this).children().length-1)+$('#Manage_category').width();
        $(this).width(w);
    });
    $('.Nav_gap').hide();
    $('.Tag').hide();
    // UI //
        // Nav Button //
    $('.NavButton').each(function(){
        $(this).data('tagsOpen',false);
        $(this).bind('click',function(){
            var Nav = $(this).parent();
            var gap = Nav.next();
            var tags = Nav.find('.NavTags');
            ////
            if ($(this).hasClass('shadow_0')) { $(this).removeClass('shadow_0'); }
            else { $(this).addClass('shadow_0'); }
            ////
            //$('.Nav_gap').hide();
            //$('.NavTags').hide();
            ////
            function tagsOpen(tags) {
                function tagsShow(tags) {
                    tags.children().each(function(i){
                        var ii = i*200;
                        $(this).delay(ii).fadeIn();
                    });
                    tags.children().last().css({'color':'#fafafa','background':'#3a3a3a'});
                }
                function gapExtend() {
                    gap.css({display:'block',width:'0px'})
                       .animate(
                           {width:tags.width()},
                           {duration:'1000'});
                    gap.next().css({'border-left':'1px solid #000'});
                }
                ////
                gapExtend();
                setTimeout(function(){
                    tagsShow(tags);
                },300);
            }
            function tagsClose(tags) {
                function tagsHide(tags) {
                    tags.children().each(function(i){
                        var ii = (tags.children().length-i-1)*200;
                        $(this).delay(ii).fadeOut();
                    });
                }
                function gapShrink() {
                    gap.next().css({'border-left':'none'});
                    gap.animate(
                           {width:0},
                           {duration:'2000'});
                }
                ////
                tagsHide(tags);
                setTimeout(function(){
                    gapShrink();
                },800);
            }
            if (!$(this).data('tagsOpen')) {
                tagsOpen(tags);
                $(this).data('tagsOpen',true);
            } else {
                tagsClose(tags);
                $(this).data('tagsOpen',false);
            }
        });
    });
});

