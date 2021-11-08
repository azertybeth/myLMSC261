Ok rachel said to write down the fact that I'm getting an error
that everyone else is getting.

"^
36 warnings and 1 error generated.
error: command '/usr/bin/gcc' failed with exit code 1
Elizabeths-MacBook-Pro:pyo elizabethautorino$
"

^ is how the error reads.


src/engine/ad_coreaudio.c:449:23: warning: comparison of integers of different signs: 'int' and 'UInt32' (aka 'unsigned int') [-Wsign-compare]
        for (i = 0; i < inputStreamDescription.mChannelsPerFrame; ++i)
                    ~ ^ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
src/engine/ad_coreaudio.c:470:19: warning: comparison of integers of different signs: 'int' and 'UInt32' (aka 'unsigned int') [-Wsign-compare]
    for (i = 0; i < outputStreamDescription.mChannelsPerFrame; ++i)
                ~ ^ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



these are the parts that are highlighted.

I have absolutely no idea what's going on.

Professor suggested using port audio instead of core audio, due to the fact that it
seems to be an issue correlating bewteen macOS version and audio drivers.
After attempting to install core audio, terminal returned that I already
have an installation on my computer.

Using portaudio as a term to replace coreaudio in the original command verbatim otherwise
returns an error saying portaudio is not recognized.


After googling the warning message, I'm able to gather that UInt means unsigned integer.
I now realize that the error message said that already.

UInt32 makes me think that the error has something to do with the deprecation
of 32bit compatibility in newer versions of macOS.

I tried googling in plain english the error I'm getting:

"pyo int comparison error", no relevant results. There seem to be many other
popular errors that are simply not what I'm getting.

Checking the Github's known issues page didn't yield any results either.
