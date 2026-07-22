def table_check(table:dict[str:int,str:int,str:dict], roll:int) ->dict[str:dict]:
    for min, max, result in table:
        if min <= roll <= max:
            return result