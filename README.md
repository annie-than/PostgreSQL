
1. Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.

Sparkify team has a lot of data on songs and user activities from their new music streaming app. However, it is not easy for them to get the specific kinds of data that they want. That's why they want to create a Postges database with tables designed to optimize queries on song play analysis. The analytics team is particularly interested in understanding what songs users are listening to.

2. State and justify your database schema design and ETL pipeline.

Using the song and log datasets, we'll create a star schema optimized for queries on song play analysis. This includes the following tables.
- Fact Table: 
    songplays 
- Dimension Tables:
    users 
    songs 
    artists 
    time 
    
ETL pipeline: This process will walk all .json files and extract, transform and loading specific datas to fact and dimemsion tables.


3. Provide example queries and results for song play analysis.

%sql SELECT * FROM songplays LIMIT 5;
songplay_id	start_time	user_id	level	song_id	artist_id	session_id	location	user_agen
1	1542069637796	66	free	None	None	514	Harrisburg-Carlisle, PA	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"
3	1542071549796	51	free	None	None	510	Houston-The Woodlands-Sugar Land, TX	"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36"
4	1542079142796	9	free	None	None	379	Eureka-Arcata-Fortuna, CA	Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
5	1542081112796	49	free	None	None	506	San Francisco-Oakland-Hayward, CA	Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0
8	1542085206796	94	free	None	None	492	Ogden-Clearfield, UT	Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0

