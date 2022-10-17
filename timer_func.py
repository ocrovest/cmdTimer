import time
import random
from datetime import date
import os


hlpmn = """
ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴄᴍᴅᴛɪᴍᴇʀ

» ʏᴏᴜ ᴀʀᴇ ᴘʀᴇsᴇɴᴛᴇᴅ ᴡɪᴛʜ 4 ᴏᴘᴛɪᴏɴs, sᴏʟᴠᴇ, ᴄᴏᴍᴍᴀɴᴅs, ʜᴇʟᴘ, ᴀɴᴅ ᴇxɪᴛ.
» sᴏʟᴠᴇ = ɢɪᴠᴇs sᴄʀᴀᴍʙʟᴇ, ʟᴇᴛs ʏᴏᴜ ɪɴsᴘᴇᴄᴛ, ᴀɴᴅ ᴛɪᴍᴇs ʏᴏᴜ sᴏʟᴠᴇs.
» ᴄᴏᴍᴍᴀɴᴅs = ʟᴇᴛs ʏᴏᴜ sᴡɪᴛᴄʜ ᴘᴜᴢᴢʟᴇs ᴛᴏ sʜᴏᴡ sᴘᴇᴄɪғɪᴄ sᴄʀᴀᴍʙʟᴇs ᴀɴᴅ sᴡɪᴛᴄʜ ɪɴsᴘᴇᴄᴛɪᴏɴ ᴛɪᴍᴇ.
» ʜᴇʟᴘ = ᴛʜɪs.
» ᴇxɪᴛ = ǫᴜɪᴛs ᴄᴍᴅᴛɪᴍᴇʀ

ɴᴏᴛᴇ:ʏᴏᴜ ᴀʀᴇ sʜᴏᴡɴ ᴡʜᴀᴛ ᴛᴏ ᴅᴏ ᴡʜᴇɴ ʏᴏᴜ sᴇʟᴇᴄᴛ ᴡᴏʀᴋ ɪɴ ᴍᴀɪɴ ᴍᴇɴᴜ

ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ɢᴏ ʙᴀᴄᴋ.
"""

def helpmenu():
	print(hlpmn)

def sleep(x):
	time.sleep(x)

def cls():
	os.system("clear")

class stopwatch:
	def time_processing(sec):
		mins = sec // 60
		sec = sec % 60
		mins = mins % 60
		return "ᴛɪᴍᴇ ᴛᴀᴋᴇɴ:\nᴍɪɴᴜᴛᴇs » {0}\nsᴇᴄᴏɴᴅs » {1}".format(int(mins),sec)
	def stopwatch():
		s = time.time()
		input()
		e = time.time()
		return e - s

def err(e):
	print(f"☠︎︎ » ᴡʜᴏᴏᴘs! ᴛʜᴇʀᴇ ɪs ᴀ ᴘʀᴏʙʟᴇᴍ ɪɴsɪᴅᴇ ᴛʜᴇ ᴘʀᴏɢʀᴀᴍ! {e} ʜᴀs ᴏᴄᴄᴜʀᴇᴅ" )

class scramble:
	puzzles = {"2x2":["R","L","U","D","F","B","R'","L'","U'","D'","F'","B'","R2","L2","U2","D2","F2","B2"],
	"3x3":["R","L","U","D","F","B","R'","L'","U'","D'","F'","B'","R2","L2","U2","D2","F2","B2"],
	"Pyraminx":["R","L","U","B","R'","L'","U'","B'","r","r'","l","l'","u","u'","b","b'"]}
	def scramble(puzzle,len):
		s = ""
		for x in range(len):
			s = s + random.choice(scramble.puzzles[puzzle]) + " "
		return s