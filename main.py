from pydub import AudioSegment

# global params
music1 = AudioSegment.from_mp3('botanist_boogie.mp3')
sound1 = AudioSegment.from_mp3('anna.mp3')
sound2 = AudioSegment.from_mp3('ben.mp3')
silence = AudioSegment.silent()


def create_intro(voice_clip, music_clip=None, intro_duration=6000, outro_duration=2000):
    intro_clip = AudioSegment.empty()

    if music_clip:
        voice_duration = voice_clip.duration_seconds * 1000

        # adapt music to voice duration
        music_duration = intro_duration + outro_duration + voice_duration
        music_clip = music_clip[:music_duration]

        # decrease volume to -10dB
        music_clip = music_clip.apply_gain(-10)

        # decrease volume smoothly to -15dB
        fade_duration = 2000
        start = intro_duration - fade_duration
        music_clip = music_clip.fade(to_gain=-15, start=start, duration=fade_duration)

        # apply fade out
        music_clip = music_clip.fade_out(outro_duration)

        # overlay voice on music, starting at second defined by intro_duration
        intro_clip = music_clip.overlay(voice_clip, position=intro_duration)
    else:
        # just add voice to the intro
        intro_clip += voice_clip

    # add 1s of silence
    intro_clip += AudioSegment.silent()

    return intro_clip


intro = create_intro(
    voice_clip=sound1, music_clip=music1, intro_duration=6000, outro_duration=2000
)

# adding sound2
podcast = intro + sound2

# save changes
file_name = 'podcast.mp3'
podcast.export(file_name)

print(f'{file_name} created successfully')
