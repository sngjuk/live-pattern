import random
from pydub import AudioSegment
from pydub.playback import play
# pip install pydub
# brew install ffmpeg

nl = ['RESET_voc.flac', 'RESET_inst.flac', 'RESET_live.mp3']

sl = []
for n in nl:
	sl.append(AudioSegment.from_file(n, format=n.split('.')[1]))

pl = [
		 '0:00:000',
		 '0:10:867',
		 '0:21:215',
		 '1:03:567',
		 '1:25:543',
		 '2:28:876',
		 '2:50:204',
		 '3:33:213',
		 '3:43:564',
		 '4:05:556',
		 '4:17:974'
		]
#ml = [1,2,1,0,1,1,2,0,0,0,1]

def mils(t):
	second = 1000
	minute = second * 60
	r = [int(x) for x in t.split(':')]
	return r[0]*minute + r[1]*second + r[2]


def cut(song, st, ed):
	s = mils(st)
	e = mils(ed)
	return song[s:e]


while True:
	rl = AudioSegment.empty()
	for i in range(len(pl) - 1):
			rl += cut(sl[random.randint(0, len(nl) - 1)], pl[i], pl[i+1])
			#rl += cut(sl[ml[i]], pl[i], pl[i+1])
	play(rl)
