/*
 * the editor include tips-adding part
 */

/* Global */
KNOWLEDGE.ifcreated = 'false';
/* api */
    // local //
function Get() {
    var d = {};
    d.id=KNOWLEDGE.id;
    d.category_id = KNOWLEDGE.category_id;
    d.title = $('#InputTitle').val();
    d.brief = $('#InputBrief').val();
    //
    d.a_content = $('#InputContent').val();
    d.parent = $('#InputParent').val();
    //d.refer = '';
    return d;
}
    // sql //
function Tip(tip) {
    loading_on('c tip ing');
    if (tip.data('id')==undefined) {
        $.ajax({
            type: 'GET',
            url: '/knowledge/add_tip/?knowledge_id='+KNOWLEDGE.id+'&content='+tip.val(),
            success: function(id){
                loading_on('has add tip'+id);
                tip.data('id',id);
            }
        });
    } else {
        $.ajax({
            type: 'GET',
            url: '/knowledge/change_tip/?tip_id='+tip.data('id')+'&content='+tip.val(),
            success: function(status){
                loading_on(status);
            }
        });
    }
}

function CC() {
    var d = Get();
    loading_on('CCing');
    $.ajax({
        type: 'POST',
        url: '/knowledge/change/',
        data: 'category_id='+d.category_id
              +'&title='+d.title
              +'&brief='+d.brief
              +'&a_content='+d.a_content
              +'&parent='+d.parent
              +'&id='+d.id,
        success: function(id){
            if (OTHER.submit_button == 'create') {
                afterCreate(id);
            } else {
                afterChange(id);
            }
        }
    });
}
function searchParent(inputArea,showArea) {
    if (inputArea.val()!='') {
        $.ajax({
            type: 'GET',
            url: '/knowledge/ajax_parent/?category='+KNOWLEDGE.category_id+'&title='+inputArea.val()+'&knowledge_id='+KNOWLEDGE.id,
            success: function(html){
                showArea.css({'display':'inline'}).html(html);
                $('.search_result').mouseover(function(){
                    inputArea.val($(this).html());
                });
            }
        });
    }
}
/* handler */
function afterCreate(id) {
    KNOWLEDGE.id = id;
    KNOWLEDGE.ifcreated = 'true';
    ////
    loading_on(id+' created');
    View_KnowledgeList();
    Content_Knowledge();
}
function afterChange(id) {
    loading_on(id);
    KNOWLEDGE.id = id;
    InfoArea_KnowledgeList(); //in base.js, in level, it's global function
    $('#Submit').html('Saved').unbind();
}
function toCertify() {
    $('#Submit').css({'text-decoration':'none'})
                .html('Certify~')
                .unbind()
                .click(function(){
                    certify_onblur();
                });
}
function toSave() {
    $('#Submit')
        .html('save?')
        .css({'text-decoration':'none'})
        .unbind()
        .click(function(){
            CC();
        });
    OTHER.submit_button = 'save';
}
function toCreate() {
    $('#Submit')
        .html('Create?')
        .css({'text-decoration':'none'})
        .unbind()
        .click(function(){
            CC();
        });
    OTHER.submit_button = 'create';
}
function toWait() {
    $('#Submit')
        .html('Wait..')
        .css({'text-decoration':'none','color':'#999'})
        .unbind();
}

/* certify */
function certify_onkeyup() {
    var d = Get();
    if (KNOWLEDGE.ifcreated == 'false')
    {
        if (d.title!='' && d.brief!='' && d.a_content!='') { toCertify();AREA.sb = 'create'; }
        else
        {
            $('#Submit')
                .html('create').css({'text-decoration':'line-through'})
                .unbind();
        };
    }
    else
    {
        if (d.title!='' && d.brief!='' && d.a_content!='') { toCertify();AREA.sb = 'save' }
        else
        {
            $('#Submit')
                .html('save').css({'text-decoration':'line-through'})
                .unbind();
        };
    }
}
function certify_onblur() {
    alert('cer');
    var d = Get();
    $.ajax({
        type: 'POST',
        url: '/knowledge/ajax_certify/',
        data: '&title='+d.title
              +'&brief='+d.brief
              +'&a_content='+d.a_content
              +'&parent='+d.parent,
        success: function(status){
            if (status=='True') {
                if (AREA.sb = 'create') {
                    toCreate();
                } else {
                    toSave();
                }
            } else {
                loading_on('mistake');
            }
        }
    });
    toWait();
}
function certifyParentBrother() {
    var t = $('#InputTitle').val();
    var b = $('#InputBrief').val();
    var c = $('#InputContent').val();
}
function certifyTip(tip) {
    Tip(tip);
    if (tip.val()!='') {
        tip.parent().height('30px');
    } else {
        tip.parent().remove();
    }
    $('#TipsAddButton').show();
}
/* ui */
    ////
function extendUI(e) {
    var brief = $('#InputBrief_wrap');
    var p = $('#InputParent_wrap');
    var b = $('#InputBrother_wrap');
    switch(e) {
        case 'briefB':
            brief.removeClass().addClass('briefStandout');
            p.removeClass().addClass('parentLite');
            b.removeClass().addClass('brotherLite');
            break;
        case 'pB': 
            brief.removeClass().addClass('briefLite');
            p.removeClass().addClass('parentStandout');
            b.removeClass().addClass('brotherLite');
            break;
        case 'bB':
            brief.removeClass().addClass('briefLite');
            p.removeClass().addClass('parentLite');
            b.removeClass().addClass('brotherStandout');
            break;
        case 'N':
            brief.removeClass().addClass('briefLite');
            p.removeClass().addClass('parentLite');
            b.removeClass().addClass('brotherLite');
            break;
    }
}
    // click-dilation //
$('#InputTitle').bind({
    blur: function(){
    },
});
$('#InputBrief').bind({
    focus: function(){
        extendUI('briefB');
    },
    blur: function(){
        extendUI('N');
    },
});
$('#InputParent').bind({
    focus: function(){
        extendUI('pB');
    },
    keyup: function(){
        var inputArea = $(this);
        var showArea = $(this).parent().children().eq(1);
        searchParent(inputArea,showArea);
    },
    blur: function(){
        $(this).parent().children().eq(1).css({'display':'none'});
        extendUI('N');
    },
});
    // tip //
$('#TipsAddButton').click(function(){
    var clear = $(this).parent().find('.clearfix');
    var tip = $('#tip_model').clone().attr({'id':''}).css({'display':'inline'});
    clear.before(tip);
});
$('.InputTip').live({
    focus: function() {
        $(this).parent().height('100px');
        $('#TipsAddButton').hide();
    },
    blur: function() {
        var tip = $(this);
        certifyTip(tip);
    }
});
    ////
