# Project: Time Management
#### Video Demo:  <https://youtu.be/TAfA0xDBBRs>
#### Description: This web-based application project is used to analyze the time we spend on specific areas weekly, in order to find a better way to manage our valuable time.

This web-based application was designed because we often need to know how much time we spend each week on various aspects of our lives, such as the time spent on our own personal improvement, on necessities such as commuting, and on developing our hobbies. This is especially important when you need to complete a big project or have an important goal in the short term. This project is designed based on this idea.

This web-based application has three nav bar menus at the top of the web page, which is descriped below.
#### Home page menu
The first menu is Home. It can navigate us to the orginal home page. We can then add new events or drop events here.
We need to choose the type of activity that we want to add, the time when it starts and when it ends. The day select option is to choose the date when it happens.
In order to facilitate the user can delete the unintentionally wrong time, also added drop button at the bottom of the page, in addition to the add button.
In order to reduce the possibility of users entering invalid data or partially missing data records, it sets all input options on this page to required; if users leave this option blank, they will not be able to submit.

#### Activity details
The second navigation bar menu is Events. It redirects the user to acticity.html, where a table showing the details of each event that the user has added to the schedule database on the home page is displayed. On this page, a database table is displayed. This table has 5 columns, which are shown below:
- Event
- Start Time
- End Time
- Day
- Duration
It is almost the same as we manually inputs, except the duration colunm, this indicates the time of the events lasting. On this page, the user's input history is displayed to facilitate a more specific understanding of all the events that have occurred and recorded during the week, serving as a memo and double check.


#### Total Time overview
The third nav bar menu is Analyse. It redirects user to analyse.html, where shows a table of the time of each specific area and its total time, as well a pie chart.

##### Summary Table
This is a summary table which summarizes the total time spent on the same event during the week. This gives the user an overview of the time spent for each event. Aggregate tables are used to aggregate each specific time into its respective field, thus facilitating users to understand their time allocation from a statistical point of view.

##### Pie Chart
This is a pie chart and it gives user a direct view of the time spending on each area.
In this pie chart, it analyzes the percentage of all activities for the week, expressed as a percentage, and displayed in the graph. The purpose is to give the user a more visual and convenient view of the week's time spent, so that they can analyze some of the time allocations that did not meet expectations and those that exceeded them.
