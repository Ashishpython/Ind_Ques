Q1) You are the organiser of a conference and need to schedule presentations. You have received requests from N presenters stored in the csv file along with other details as

 

Presenter Name
	

No. of Hours for Presentation
	

Cost benefit for presenter

P1
	

2
	

$100

P2
	

4
	

$200

P3
	

2
	

$50

..
		

Pn
	

1
	

$400

 

·         The first column is the presenter name

·         Second column indicates number of hours presenter will take for the presentation (assume it to be an integer)

·         Last one indicates the associated cost (Fees that presenter will charge).

 

You are given that your conference will last for 8 hrs (but can be any number) with exactly 3 slots (with no breaks and back to back presentation), schedule the presentations for these two independent cases

 

1.    Maximize the number of presenters - Select the case that fits in maximum number of presenters in the given time schedule. If multiple cases satisfy this scenario, select the ones with minimum cost.

 

2.    Minimize the cost - Select the case which results in minimum cost for the organizer. If multiple cases satisfy this scenario, then select the ones with maximum number of presenters.

 

The output should be the names of selected presenters. and total cost e.g.

Presenter1, Presenter5, Presenter11 , $150

 

If multiple cases satisfy the required scenario (e.g having same minimum cost for maximum number of presenters), list all the cases as:

Presenter1, Presenter5, Presenter11 , $150

Presenter21, Presenter15, Presenter2, $150

Presenter12, Presenter4, Presenter11, $150

In case all the 3 slots can’t be filled in, output should be “Not enough presenters”
