# Calculator
### A QUICK 24 HOUR Project
Not much to say here, i worked on this project over the period of 24 hours. And then again, it was with a major part of it not touching it. It is a simple tkinter GUI calculator app. I went with ttk widgets for this one just to try out that syntax. I might copy the file and refactor it into tkinter classic to see the differences. I initially thought of creating two or three text entries as the display and data input frame. But i went againsts that idea after running into some complications. Mainly how to control the flow between one button input, and in which window it goes. 

So having worked with tkinter's text widget, i decided to use that one which allows me to use .insert() as a method and i can just put it in as a variable. 

Another issue i was having was taking the string from multiple tkinter insert methods and running math operations on it. I tried taking the different insert methods and calling them separately in variables. But those variables were string types. 

### HOW DID I SOLVE IT?
Mainly, i did it after looking up things such as REGEX which im not that familiar with and the syntax code i copied only gave me a list of strings with the math operators as string. I wanted to do type conversion but it turns out, that when i tried the REPL and check the type for +, -, * and other operators i got syntax errors. Don't remember why. I tried to call this wonky code "sum(var, var_1)" but it gave me a syntax error. 

i read about the Eval function but also how dangerous it was, and while i did not intent to give users the ability to type their own text. I decided to avoid it. Eventually as i was reading about the eval method. I read to treat math with strings like normal python math operations. So i had this inspirations...

#### Part of the evaluation function 

    '''def ins_equals():
        var_op = display_txt.get("2.0")
        var_1 = display_txt.get("1.0", "1.9")
        var_3= display_txt.get("3.0", "3.99")
        if var_op == "+":
            solve_sum = (int(var_1) + int(var_3))
            display_txt.delete("1.0", END)
            display_txt.insert("1.0", solve_sum)...'''
##### Basically i took the operator symbol based as string and used display_txt.get("2.0") and put it in a variable. 
At that point i took that variable used an if/elif/else control flow statements and called the numerical strings into a variable with display_txt.get() casting it to an int() and just run the respective operations. 

### REFACTORING TIME!!!!!! 
After further study, and a random article popping up in my news feed about Python functions. I came across an old subject that i had forgotten when i started this project LAMBDAS. 

With the use of these anonymous functions i was actually able to refactor the program. Following The Zen of Python advise that "Beautiful is better than Ugly" and "Simple is better than complex". 

Talking about the Zen, i went for this project with my noobie arsenal following the advise that now is better than never. 


#### Anyway! These are some of my opinions 




