def heartRate(beats, duration):
	bpm = (60*beats)/duration
	ave = bpm/beats
	print(bpm-ave, bpm, bpm + ave)

N = int(input())
for i in range(N):
	b, p = input().split()
	heartRate(int(b), float(p))