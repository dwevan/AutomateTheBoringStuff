def spm():
    global eggs
    eggs = 'spammalot'  # this is global


def bcn():
    eggs = 'bacon'  #this is local


def ham():
    print(eggs)  # this is the global


eggs = 42  # this is global again but will get overwritten
spm()
print(eggs)
