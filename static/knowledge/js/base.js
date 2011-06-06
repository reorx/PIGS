// Global var //
var AREA = {};
var KNOWLEDGE = {};
var INPUT = {};
var OTHER = {};
// fn //
var REORX = {};
REORX.UI = {};
//  //
AREA.ifKMshow = 'false';
/*
 * infact, it should be:
 * var REORX = {};
 * REORX.DATA = {};
 * REORX.UI = {};
 * REORX.AJAX = {};
 * REORX.,,
 * */
// document //
// calling fuction //
function loading_on(status) {
    var a = $('#loading');
    if (a.css('display')=='none') {
        a.fadeIn('500');
    }
    if (status) {
        a.html(status);
    }
}
function loading_off() {
    $('#loading').delay('200').fadeOut('500');
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
        KNOWLEDGE.category_id = id;
    } else {
        id = KNOWLEDGE.category_id;
    }
    $.ajax({
        type: 'GET',
        url: '/knowledge/view_category/?category='+id,
        success: function(html) {
            AREA.view.html(html); // show info
            if(AREA.operate_category.css('display')=='none'){ AREA.operate_category.show('500'); } //change operate area
        }
    });
}
function View_KnowledgeList() {
    id = KNOWLEDGE.category_id;
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
    if (id) { KNOWLEDGE.id = id; }
    else { id = KNOWLEDGE.id }
    //
    var url =  '/knowledge/content_knowledge/?knowledge='+id;
    var DOM = '#Content_Main';
    ajax_get(url,DOM);
    //
    Extend_K_Info()
}
function Extend_K_Info() {
    var url = '/knowledge/extend_k_info/?k_id='+KNOWLEDGE.id;
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
                            $.get('/knowledge/get_self_title/?knowledge_id='+KNOWLEDGE.id,function(html){
                                $('#InputParent').val(html);
                                loading_off();
                                //
                                KNOWLEDGE.id = '';
                            });
                        }
                        if (mode=='multiple') {
                            loading_off();
                            KNOWLEDGE.id = '';
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
        url: '/knowledge/editor_contentpart/?knowledge_id='+KNOWLEDGE.id,
        success: function(html){
            $(DOM1).html(html);
            //
            $.ajax({
                type: 'GET',
                url: '/knowledge/editor_extendpart/?mode=edit&knowledge_id='+KNOWLEDGE.id,
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
        url: '/knowledge/delete/?knowledge_id='+KNOWLEDGE.id,
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
REORX.UI.ox = function () {
    alert('ox');
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
        KNOWLEDGE.id = '';
        //_Area
        AREA.view = $('#View');
        AREA.operate_category = $('#operate_category');
        AREA.k_menu_status = 0;
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

