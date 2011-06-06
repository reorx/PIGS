from my_PIGS.default.models import *

def create_basic(d):
    print d.a_content
    content0 = ContentPart(
        content=d.a_content
    )
    content0.save()
    print 'c save'
    ##
    knowledge = Knowledge(
        category=Category.objects.get(id=int(d.category_id)),
        title=d.title,
        brief=d.brief,
    )
    knowledge.save()
    print 'k save'
    ##
    knowledge.contents.add(content0)
    print 'add it'
    if d.parent!='':
        print 'h par'
        p = Knowledge.objects.filter(title=d.parent)
        print p.get().id
        knowledge.parent.add(p.get())
        print 'added'
    return knowledge.id

def change(d):
    print 'in change'
    knowledge = Knowledge.objects.get(id=int(d.id))
    print 'get k'
    # change # # ( no refer yet )
    knowledge.title=d.title
    knowledge.brief=d.brief
    knowledge.content=d.content
    ##
    knowledge.parent.clear()
    if d.parent!='':
        p = Knowledge.objects.filter(title=d.parent)
        knowledge.parent.add(p.get())
    knowledge.save()
    return knowledge.id

def delete(k_id):
    k = Knowledge.objects.get(id=int(k_id))
    if k.itsChildren.all():
        status = ''
    else:
        status = k.title
        k.delete()
    return status

def add_parent(d):
    knowledge = create_basic(d,1)
    # brother & parent #
    if d.brother!='':
        print 'hs bro'
        brother = Knowledge.objects.get(id=int(d.brother))
        print brother.id
        knowledge.brothers.add(brother)
        print 'brother added'
        if brother.parent.all():
            knowledge.parent.add(brother.parent.all().get())
        else: print 'no parent'
        print 'ok'
    else:
        print 'basic created'
        parent = Knowledge.objects.get(id=int(d.parent))
        print 'get parent'
        knowledge.parent.add(parent)
        print 'par saved'
    # tips #
    if d.tips!='':
        print 'hs tip'
        tips_ids = (d.tips).split(',') # type: []
        for tip_id in tips_ids:
            tip = Tip.objects.get(id=tip_id)
    knowledge.save()
    print 'well'

def add_content(k_id,c):
    contentx = ContentPart(
        content = c
    )
    contentx.save()
    print 'saved'
    k = Knowledge.objects.get(id=int(k_id))
    print 'get'
    k.contents.add(contentx)
    print 'added'

def add_tip(k_id,c):
    #first create
    tip = Tip(content=c)
    tip.save()
    #then add to proper Knowledge
    k = Knowledge.objects.get(id=int(k_id))
    k.tips.add(tip)
    return tip.id

def change_tip(t_id,c):
    tip = Tip.objects.get(id=int(t_id))
    tip.content = c
    tip.save()

def remove_tip(t_id):
    tip = Tip.objects.get(id=int(t_id))
    k = tip.inKnowledge.all().get()
    k.tips.remove(tip)
    tip.delete()
