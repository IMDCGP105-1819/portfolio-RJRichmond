Song = '''
Shadows fall over my heart
I black out the moon
I wait for you to come around
You got me dancing in the dark dancing in the dark
I've closed my eyes
But I won't sleep tonight

Baby you should come with me
I'll take you to the dark side
Me and you you and me
Do bad things in the night time
Baby you should come with me
And we can kill the lights
Hit the lights let it blackout blackout
Hit the lights let it blackout blackout woo!

Black bird black moon black sky black light
Black everything black
Black heart black keys black diamonds
Blackout black everything black
Black everything everything
All black everything everything
All black everything everything
All black everything everything black

In a nocturnal state of mind
Children of the night
But it's the only way of life
This black hole's pulling me inside
Of this black heart this black soul
Underneath this black black sky

Baby you should come with me
I'll take you to the dark side
Me and you, you and me
Do bad things in the night time
Baby you should come with me
And we can kill the lights
Hit the lights let it blackout blackout
Hit the lights let it blackout blackout woo!

Black bird black moon black sky black light
Black everything black
Black heart black keys black diamonds
Blackout black everything black
Black everything everything
All black everything everything
All black everything everything
All black everything everything black

Baby you should come with me
Me and you, you and me
Baby you should come with me
And we can kill the lights
Hit the lights let it blackout blackout
Hit the lights let it blackout blackout woo!

Black bird black moon, black sky black light
Black everything black
Black heart black keys black diamonds
Blackout black everything black
Black everything everything
All black everything everything
All black everything everything
All black everything everything black
'''

def Word_count(str):
    Counting = dict()
    SingleWords = str.split()
    for word in SingleWords:
        if word in Counting:
            Counting[word] += 1
        else:
            Counting[word] = 1
    max_value = max(Counting.values())
    max_key =  [key for (key,value) in Counting.items() if value == max_value]
    MoreThenNumber = int(input("Input a number of times a word should atleast appear! "))
    More_key =  [key for (key,value) in Counting.items() if value >= MoreThenNumber]
    print("The highest number of times a word appears is",max_value,"and it is", max_key)
    print("Words which appear more then",MoreThenNumber,"are",More_key)
    return Counting

Word_count(Song.lower())
