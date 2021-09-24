# EC601_P2_TwitterAPI
As a social media application, Twitter has about 1.45 million users, including companies, restaurants, people, and so on. Twitter provides a platform for users to do a lot of things, such as sending tweets, searching tweets, and following other people's twitter. All of these functions rely on API so that deelopers can collect those data and deal with it. There are some examples to show how API works for different function. 

## Send and Delete
Here is a file called sendTweet.py to show the basic process the API do when a user sends a tweet. When a user sends a tweet, the API will grab the user's consumer key, consumer seceret key, access token key, and access token secret key. After getting those info, API can access the user's account and update the status of this account. And Twitter also let users upload medias, and the process is easy. However, sending a media is complicated for Twitter API. First, it will get the media's information, like url and size. Second, it will request to post the media by sending data to post. Finally, the API will use the same url and let users to send words with the media. 
In deleteTweet.py file, it shows a basic process to delete tweets. In order to delete a tweet or multiple tweets, API also needs to access user's account, which would grab four keys we mentioned before. The API will have a list to collect tweets that needs to be deleted. After collecting those tweets, it will send those tweet ids into delet function. 

## Search - by timeline, by content
In order to search tweets by timeline, we need to have a start time and a end time using datetime library. After getting the period, we will search tweets that fit this condition and grab them into a list. Finally, print the list to users. File searchTimeline.py gives an example how to search tweets by timeline.
For searching tweets by content, users can choose if they want to search both tweets and retweets or only tweets. To ignore retweets, using a filter retweet to filter them out. And users also can search for more than one keywords to get more accurate tweets, such as boston and restaurants. API will also create a list to contain tweets that fit the information, and users can see who send those tweets and their location, which is convenient to get some information about a specific thing.

## Follow, Unfollow, Like, Block


## Tweet Counts - recent or full-archive
