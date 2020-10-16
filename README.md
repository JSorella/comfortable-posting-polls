# Comfortably Posting Polls Data Processor  

This project pretends to count in a "fairly" way the polls results made in "[Pink Floyd Comfortably Posting](https://www.facebook.com/groups/ComfortablyPosting)" Facebook group.

This program computes real votes from users in the group and an algorithm (described below) chooses "the most disliked" 
tracks from the band in the most fairly way.

The results tracks were chosen to create the following Spotify playlist:
https://open.spotify.com/playlist/3IFI2OPM6uNYS4HWu4xVtr?si=oR8BMWVaRtOhvjHa9TmS9w

_____

# How decisions were taken

## Poll #1 results
The first poll was made only for fun.
My intention was to understand which Pink Floyd albums among the less-liked
were most liked in the group.
The most recommended albums are always The Dark Side of The Moon, Wish You Were Here, Animals, The Wall & Meddle.
I wanted to know how many people liked the other ones, so I made this poll.

With the results, I was able to understand that five albums had very few votes.
So I decided to find out what were the most hated/disliked ones in a next poll.


## Poll #2 results

In this poll, I have asked to vote two options, just because many people agrees that "The Endless River" is not 
a favourite at all, so I also wanted to know for their "second dislike" pick.

* The endless river -- 129 votes    -- 41% 
* A momentary lapse	--  75 votes    -- 23.88%
* The final cut	    --  42 votes    -- 13.37%
* Ummagumma	        --  38 votes    -- 12.1%
* More 		        --  30 votes    -- 9.55%

With this data, I started to think that a compilation with "The Worst of Pink Floyd" could be achieved.

I thought that a compilation with 41% of "The Endless River", 24% of "A Momentary Lapse of Reason", 
etc... would be a good idea.

But I wasn't sure about the results. 

## Poll #3 results

So I decided to make a poll with all these albums tracks.

This was the task: 
"Pick 3 tracks to be saved to humanity, the rest will be erased forever from history."

This poll gave me data to select only the most liked songs from there, but wasn't enough sometimes to select the worst.
Many songs doesn't had any vote or enough votes.
I have noticed that songs without votes are totally ignored tracks, so, should be part of "the worst of Pink Floyd".

## Poll #4 results

In a previous post, I asked people to choose their most disliked songs from the band.
All mentioned tracks were in included in this poll, and I gave the option to people to add more.

I have asked to vote up to 3 options.
For my surprise, many songs were added and most of them were top-voted.

## Decisions for the playlist making

I was sure I wasn't able to achieve this task totally by myself, so I decided to compute all this data in Python.

These were my final decisions:

* The compilation/playlist should have less than 80 minutes (like a CD).
* The compilation/playlist should have an amount of tracks according to Poll #2 results. If an album had 40% of negative votes, then the playlist should have up to 40% tracks from that album.
* For albums whose tracks in Poll #4 does not belongs to albums in Poll #2, should only have one pick in the playlist.
* Make a "weight ratio" formula for each track and order the playlist using that weight (most hated first, less hated last).

### Formulas

Next, I have designed more than one formula:

```
Main Formula:
track_score = album_score + (track_positive_votes_corr - track_negative_votes_corr) * tracks_correction_factor
```
Where:
```
track_positive_votes_corr = track_positive_votes x tracks_positive_votes_correction_factor
track_negative_votes_corr = track_negative_votes x tracks_negative_votes_correction_factor
```

##### What are the "correction factors"?
Polls 3 & 4 had different total votes. The poll 4 had less votes than poll 3.
So it wasn't fair to count votes from polls 3 & 4 with the same weight.
So, this correction factor is "1" by default for each one, but, then the `tracks_negative_votes_correction_factor` 
is updated with the next formula:

```
tracks_negative_votes_correction_factor = total_votes_from_poll_3 / total_votes_from_poll_4
```

This should fix the weight between the votes from each poll.
For last, the `tracks_correction_factor` is the same concept applied to total votes between the sum of polls 1 & 2 
(albums votes) and the sum of polls 3 & 4 (track votes).
So, there is also a `albums_correction_factor` that will be used next.

##### Album score
Then, we have several formulas to compute the `album_score` value:

```
1) album_songs_weight_ratio = 1 / album_tracks_quantity
2) album_raw_score = album["positive_votes"] * album_positive_votes_correction_factor 
 - album["negative_votes"] * album_negativee_votes_correction_factor
3) album_score = album_raw_score * album_songs_weight_ratio * albums_correction_factor
```

For formula 1, the main idea is that a person dislikes an album for how many songs are not liked in there.
So, for ex., if an album has 4 songs, each song is 25% responsible to make that album good or bad (liked or disliked).

You could say... what's about if one of the song is 30 minutes long and other 2 minutes long?
I thought about that but this was pretty hard to compute.
It would be necessary to enter each track long and do extra efforts I thought this wouldn't change enough the final 
result (at least for this kind of playlist).

Formula 2 computes the album raw score. This is pretty much the same as I have explained for tracks.

Formula 3 multiplies results at formulas 1, 2 & the album correction factor explained above.

## Estimations & Corrections

There was problems with the data.
In poll #4, there are tracks belonging to albums not chosen in previous polls.
So, for "Meddle" and "The Wall" I have estimated the positive votes for them.

### Last Decisions

For making more attractive the playlist, I have corrected the order for `A New Machine` to make the following 
common-sense listen-able order:

* A New Machine - part 1
* The Grand Vizer's Garden Party - part 2
* A New Machine - part 2
 
 Also, there were a lack of votes for `The Endless River` album.
 So, the scores for each track in the album were pretty the same.
 I have decided then to choose the tracks by their "side".
 This is why the side were is "Louder than Words" is chosen in its entirety at first place 
 (this song was the most disliked in the album).
 The "side 2" had very low rating except for "Anisina", so I have chosen the full side except that track.
 
 
 ## Conclusions
 
 I have tried my best to do this a fair playlist.
 
 "The Worst of Pink Floyd" is the result of many people votes in a listenable way.
 
 I hate to include `What do you want from me`,  `Several Species` and `Another Brick in the Wall pt.2` here, I love that tracks, but this is what people 
 have chose.
 
 I hope you enjoy "The Worst of Pink Floyd", or dislike it as many others done!
