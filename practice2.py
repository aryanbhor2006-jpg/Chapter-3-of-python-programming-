Letter = """Dear <|NAME|>,
         You are selected for the position of <|POSITION|> in our company. 
         We offer you a salary of <|SALARY|> per month"""

print (Letter.replace("<|NAME|>","Aryan").replace("<|POSITION|>","Python Developer").replace("<|SALARY|>","50000"))
