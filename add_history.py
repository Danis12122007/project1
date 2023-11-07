def add_history(object, input1, select1, input2, select2):
    with open('история.txt', 'a') as history:
        history.write(f'{object}: {input1} {select1} = {input2} {select2}\n')


def space():
    with open('история.txt', 'a') as history:
        if history.readlines():
            history.write(' \n')