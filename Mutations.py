def mutate_string(string, position, character):
    t=str(string[0:position])+str(character)+str(string[position+1:])
    return t

