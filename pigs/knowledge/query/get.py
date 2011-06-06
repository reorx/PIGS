from my_PIGS.default.models import *

def certify(d):
    print 'in certify'
    certify = True
    ##
    if Knowledge.objects.filter(title=d.title): # unallow title to be the same
        certify = False
    if d.parent != '':
        try: Knowledge.objects.get(title=str(d.parent))
        except: certify = False
    return certify


def knowledge(id):
    return Knowledge.objects.get(id=int(id))

def knowledge_all():
    return Knowledge.objects.all()

def knowledge_full(k_id):
    k = knowledge(k_id)
    # get content
    k.contents_reset = []
    cs = k.contents.all()
    if not cs:
        k.contents_reset = False
    else:
        for c in cs:
            # pretreatment for ContentPart
            ns = c.notes.all()
            c.notes_reset = []
            if not ns:
                c.notes_reset = False
            else:
                for n in ns:
                    c.notes_reset.append(n)
            ##
            k.contents_reset.append(c)
    # get refer
    if not k.refer:
        k.refer_reset = 'no reference'
    else:
        class r: pass
        r.name = k.refer_resource
        r.brief = refer_brief(r.name)
        r.url = refer_url(r.name,r.id)
        k.refer = r
    # done
    return k

def knowledge_info(k_id):
    k = knowledge(k_id)
    c = k.contents.all()
    if c:
        k.contents_list = []
        i = 0
        for cc in c:
            k.contents_list.append('#content '+str(i))
            i += 1
    return k


    # get refer

def knowledge_category_tree(c_id):
    def iteTree(p,m,i):
        for k in p:
            m += (
                '<div class="knowledge_wrap" level="'+
                str(i)+'"><a id="x" class="knowledge" level="'+
                str(i)+'" href="#knowledge" onclick="Content_Knowledge('+
                str(k.id)+')">'+
                k.title+'</a><div class="k_ToggleButton">+</div><a class="k_MenuButton" kID="'+
                str(k.id)+'"><img src="/static/img/knowledge_menu.png" /></a></div>'
            )
            if k.itsChildren.all():
                m = iteTree(k.itsChildren.all(),m,i+1)
            else:
                pass
        return m
    ####
    print '1'
    c = Category.objects.get(id=c_id)
    print '2'
    roots = Knowledge.objects.filter(category=c,parent=None)
    M = '<div>'
    M = iteTree(roots,M,0)
    M += '</div>'
    print 'end def'
    return M

def category_all():
    return Category.objects.all()

def category(id):
    return Category.objects.get(id=id)

def knowledge_brother_all(parent_id):
    parent = Knowledge.objects.get(id=parent_id)
    return parent.itsChildren

## ajax ##
def knowledge_title_search(c_id,t):
    c = category(c_id)
    return Knowledge.objects.filter(category=c).filter(title__startswith=t)

def knowledge_title_search_nochild(c_id,t,k_id):
    def iteTree(p,m):
        for k in p:
            m.append(k)
            if k.itsChildren.all():
                m = iteTree(k.itsChildren.all(),m)
            else:
                pass
        return m
    c = category(c_id)
    k = knowledge(k_id)
    full = Knowledge.objects.filter(category=c).filter(title__startswith=t)
    exclude,final = [],[]
    if k.itsChildren.all():
        exclude = iteTree(k.itsChildren.all(),exclude)
        for f in full:
            for e in exclude:
                if f.id != e.id:
                    r = f
                else:
                    r = ''
                    break
            if r !='':
                if r.id != k.id:
                    final.append(r)
    else:
        for f in full:
                if f.id != k.id:
                    final.append(f)
    return final

def get_parent_title(k_id):
    k = Knowledge.objects.get(id=int(k_id))
    if k.parent.all():
        title = k.parent.all().get().title
    else:
        title = ''
    return title

def get_self_title(k_id):
    return Knowledge.objects.get(id=int(k_id)).title

### use for blog(APP) ###
def blog_all():
    blogs_init = Knowledge.objects.all()#.filter() #order_by & NOT certain
    blogs_final = []
    for b in blogs_init:
        b.content = ''
        for c in b.contents.all():
            b.content += c.content
        blogs_final.append(b)
    return blogs_final
