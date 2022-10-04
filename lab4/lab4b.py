from re import I


def interpret(LogicalExpression, Interpretation): 

    if len(Interpretation) == 0:
            return 'true'
    if LogicalExpression == 'true':
        return LogicalExpression
    if LogicalExpression == 'false':
        return LogicalExpression
        
    if isinstance(LogicalExpression, str):
        if LogicalExpression in Interpretation:
            return Interpretation[LogicalExpression]
        return LogicalExpression 
    
    

    if len(LogicalExpression) == 0:
        return "invalid input"

    if len(LogicalExpression) == 1:
            if LogicalExpression[0] in Interpretation:
                return Interpretation[LogicalExpression[0]] # for example will return Cat_asleep...
            if  LogicalExpression == 'true':
                return 'true'
            if LogicalExpression ==  'false':
                return 'false'
    interpret(LogicalExpression[0], Interpretation) # checks if first one is true or not 
    if len(LogicalExpression) == 2:
        if isinstance(LogicalExpression[0], str):
            if LogicalExpression[0] in Interpretation:
                return Interpretation[LogicalExpression[0]] 
            if  LogicalExpression == ['NOT', 'true']:
                return 'false'
            if LogicalExpression ==  ['NOT', 'false']:
                return 'true'
        return interpret([LogicalExpression[0]] + [interpret(LogicalExpression[1], Interpretation)], Interpretation)


    if len(LogicalExpression) == 3: 
        if [interpret(LogicalExpression[0], Interpretation), LogicalExpression[1], interpret(LogicalExpression[2], Interpretation)] == ["true" "OR" "true"]:
            return "true"
        if [interpret(LogicalExpression[0],Interpretation), LogicalExpression[1], interpret(LogicalExpression[2],Interpretation)] == ["true", "OR", "true"]:
            return "true"
        if [interpret(LogicalExpression[0],Interpretation), LogicalExpression[1], interpret(LogicalExpression[2],Interpretation)] == ["true", "OR", "false"]:
            return "true"
        if [interpret(LogicalExpression[0],Interpretation) ,LogicalExpression[1], interpret(LogicalExpression[2],Interpretation)] == ["false", "OR", "true"]:
            return "true"
        if [interpret(LogicalExpression[0],Interpretation) ,LogicalExpression[1], interpret(LogicalExpression[2],Interpretation)] == ["false", "OR", "false"]:
            return "false"
        if [interpret(LogicalExpression[0],Interpretation) ,LogicalExpression[1], interpret(LogicalExpression[2],Interpretation)] == ["true", "AND", "true"]:
            return "true"
        if [interpret(LogicalExpression[0],Interpretation) ,LogicalExpression[1], interpret(LogicalExpression[2],Interpretation)] == ["true", "AND", "false"]:
            return "false"
        if [interpret(LogicalExpression[0],Interpretation) ,LogicalExpression[1], interpret(LogicalExpression[2],Interpretation)] == ["false", "AND", "true"]:
            return "false"
        if [interpret(LogicalExpression[0],Interpretation) ,LogicalExpression[1], interpret(LogicalExpression[2],Interpretation)] == ["false", "AND", "false"]: 
            return 'false'       


       


 

