# CP1404 Practical Reflection

Write short but thoughtful answers to each of the following.  
Replace each `...` with your meaningful answer.

## Estimates

Regarding the **estimates** that you did for practical tasks...

### How was your estimate accuracy usually?

My estimate accuracy was generally mixed, with some estimates being quite close to the actual time required, 
while others were less accurate, particularly for tasks that I initially found more complex or unclear. 
I sometimes underestimated the difficulty of debugging or overestimated my ability to multitask efficiently.

### How did your estimate accuracy improve or change during the course of the subject?

Over the course of the subject, I became better at breaking down tasks into smaller, more manageable components. 
This helped me estimate more realistically. I learned to factor in the time for debugging, research, and testing,
which improved the accuracy of my time estimates. 
I also started refining my process of assessing how much effort a task would require based on previous similar tasks.

### What did you learn from doing these estimates?

From doing these estimates, I learned the importance of planning and time management. 
Initially, I tended to underestimate tasks, which led to stress.
However, as I reflected on my previous mistakes, I developed a better understanding of how to allocate time for different aspects of the work,
including unexpected challenges. 
I also learned to be more flexible and adjust my estimates as I progressed.
## Code Reviews

### What have you learned from being reviewed by other people?

Being reviewed by others taught me how important it is to keep my code clean, understandable, and well-documented.
I also learned to welcome constructive feedback and realize that code reviews are opportunities for growth. 
I became more aware of best practices, such as adhering to naming conventions, 
ensuring code is modular, and writing clear, readable comments.

### What have you learned from doing code reviews of other people?

Reviewing others’ code improved my attention to detail and helped me identify potential issues in my own work. 
I became better at identifying patterns in code quality and offering suggestions to improve efficiency, readability, and maintainability. 
I also learned to communicate more clearly in my feedback, providing both praise and actionable suggestions.


Provide proper Markdown links (not bare URLs) to two (2) PRs that show you doing good code reviews for any of the past
pracs.  
For each one, write a short explanation of what was good about your review.

### Good Code Review 1

https://github.com/ZhihaoTang615/cp1404practical/pull/7/commits/3e3391b80c5f102990ee2613ff6a95bfa7c2d22f

### Explanation

In this code review, I provided feedback on the overall structure of the program, specifically focusing on the Band class and the interactions between the classes Band, Musician, and Guitar.
I suggested breaking down the logic within the play() function to ensure it adheres to the Single Responsibility Principle (SRP) by delegating the responsibility of playing an instrument to the Musician class. I also pointed out that adding comments for the classes and methods could improve readability and help future developers understand the code flow better. Additionally, I recommended checking if the Musician class had an existing method to handle instrument addition in a more efficient way. Lastly, I suggested improving error handling by verifying that musicians actually have instruments before attempting to "play." 
This feedback helped in making the code more maintainable, modular, and understandable.

### Good Code Review 2

https://github.com/ZhihaoTang615/cp1404practical/pull/6/commits/3e3391b80c5f102990ee2613ff6a95bfa7c2d22f

### Explanation

In this code review, the implementation of the Band class was well-structured and followed object-oriented principles effectively. 
The Band class demonstrated a clear responsibility for managing a list of musicians, adhering to the single responsibility principle. 
Its __str__ method efficiently provided a human-readable string representation of the band and its members, which improves code readability and debugging.
The use of encapsulation was also on point, as the class managed its internal data and interacted with external code through well-defined methods, such as add and play. 
The design of the class is scalable, making it easy to add new features, such as additional methods for the band. However, a potential improvement would be to handle cases where musicians may not have any instruments,
as the current implementation could result in errors when calling the play() method. Overall, the code follows good practices by separating concerns, 
with each class focusing on its own functionality,
and the review effectively highlighted areas for improvement while also recognizing the well-executed aspects of the design.

## Practicals

### Regarding the **practical tasks** overall, what would you change if you were in charge of the subject?

If I were in charge of the subject, I would consider incorporating more group work or pair programming to simulate real-world collaboration. 
It would also be helpful to provide more guidance on best practices, particularly on structuring projects and writing maintainable code.
More time for debugging and refining solutions could also be built into the schedule, as it’s often where students struggle the most.

### What did you do really well for practicals in this subject?

In this subject, I excelled at organizing my work and staying on top of deadlines.
I consistently produced well-structured, readable code and followed through with thorough testing. I also made a point of reviewing and reflecting on my work after each practical, 
which helped me identify areas for improvement. 
My proactive approach to seeking help when needed and asking clarifying questions was another strength that helped me perform well in this course.