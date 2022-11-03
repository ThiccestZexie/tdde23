def interpret(logical_expression, interpretation): 
    
    if logical_expression == 'true':
        return logical_expression
    if logical_expression == 'false':
        return logical_expression
    if isinstance(logical_expression, str):
        if logical_expression in interpretation:
            return interpretation[logical_expression]
        return logical_expression

    if len(logical_expression) == 2:
        if isinstance(logical_expression[0], str):
            if  logical_expression == ['NOT', 'true']:
                return 'false'
            if logical_expression ==  ['NOT', 'false']:
                return 'true'
        return interpret([logical_expression[0]] + [interpret(logical_expression[1], interpretation)], interpretation)

    if len(logical_expression) == 3:
                    if [interpret(logical_expression[0], interpretation), logical_expression[1], interpret(logical_expression[2], interpretation)] == ["true" "OR" "true"]:
                        return "true"
                    if [interpret(logical_expression[0],interpretation), logical_expression[1], interpret(logical_expression[2],interpretation)] == ["true", "OR", "true"]:
                        return "true"
                    if [interpret(logical_expression[0],interpretation), logical_expression[1], interpret(logical_expression[2],interpretation)] == ["true", "OR", "false"]:
                        return "true"
                    if [interpret(logical_expression[0],interpretation) ,logical_expression[1], interpret(logical_expression[2],interpretation)] == ["false", "OR", "true"]:
                        return "true"
                    if [interpret(logical_expression[0],interpretation) ,logical_expression[1], interpret(logical_expression[2],interpretation)] == ["false", "OR", "false"]:
                        return "false"
                    if [interpret(logical_expression[0],interpretation) ,logical_expression[1], interpret(logical_expression[2],interpretation)] == ["true", "AND", "true"]:
                        return "true"
                    if [interpret(logical_expression[0],interpretation) ,logical_expression[1], interpret(logical_expression[2],interpretation)] == ["true", "AND", "false"]:
                        return "false"
                    if [interpret(logical_expression[0],interpretation) ,logical_expression[1], interpret(logical_expression[2],interpretation)] == ["false", "AND", "true"]:
                        return "false"
                    if [interpret(logical_expression[0],interpretation) ,logical_expression[1], interpret(logical_expression[2],interpretation)] == ["false", "AND", "false"]: 
                        return 'false'


def test():
    print(interpret(["door_open", "AND", "cat_gone"], {"door_open" : "false", "cat_gone" : "true", "cat_asleep" : "true"} )) # 'false'

    print(interpret(["cat_asleep", "OR", ["NOT", "cat_gone"]],{"door_open" : "false", "cat_gone" : "true", "cat_asleep" : "true"})) #true

    print(interpret(["true", "OR", "true"], {})) #'true'

    print(interpret("cat_gone", {"door_open": "false", "cat_gone": "true"})) #true

    print(interpret(["NOT", ["NOT", ["NOT", ["cat_asleep", "OR", ["NOT", "cat_asleep"]]]]],{"cat_asleep": "false"})) #false

    print(interpret(["NOT", "AND", "true"], {"NOT":"true"})) #true

    print(interpret(["NOT", "AND"], {"AND": "false"})) #true

    print(interpret(["NOT", "NOT"], {"NOT": "false"})) #true


test()

