sancGameScript(timeScale) {
		if WinActive("BloonsTD6") {
			
			Sleep(timeScale * 100)	;clear hot key lag
			
			Send("{vk51}")		; Dart monkey
			Sleep(timeScale * 100)
			MouseMove(750,263)	;inital dart placement
			Sleep(timeScale * 100)
			Click("750,263")
			Sleep(timeScale * 100)
			
			Send("{vk20}")		; Start game
			Sleep(timeScale * 100)
			Send("{vk20}")		; Increase Speed
			Sleep(timeScale * 100)
			
			Sleep(timeScale * 11500)
			
			Send("{vk55}")	;ben
			Sleep(timeScale * 100)
			MouseMove(1321,552)
			Sleep(timeScale * 100)
			Click("1321,552")
			Sleep(timeScale * 32400)
			
			Send("{vk4A}")	;spike
			Sleep(timeScale * 100)
			MouseMove(981,256)
			Sleep(timeScale * 100)
			Click("981,256")
			Sleep(timeScale * 100)
			
			Click("981,256")	;click spike
			Sleep(timeScale * 14700)
			
			Send("{vkBC}")	;spike 100
			Sleep(timeScale * 2100)
			
			Send("{sc035}")	;spike 101
			Sleep(timeScale * 8400)
			
			Send("{sc035}")	;spike 102
			Sleep(timeScale * 100)
			
			Send("^{vk09}")	;change target to smart
			Sleep(timeScale * 11500)
			
			Send("{vk5A}")	;sniper
			Sleep(timeScale * 100)
			MouseMove(911,960)
			Sleep(timeScale * 100)
			Click("911,960")
			Sleep(timeScale * 100)
			
			Click("911,960")	;click sniper
			Sleep(timeScale * 6000)
			
			Send("{vkBC}")	;sniper 100
			Sleep(timeScale * 18600)
			
			Click("960,540")	;click middle to clear menu
			Sleep(timeScale * 100)
			
			Send("{vk41}")	;wizard1
			Sleep(timeScale * 100)
			MouseMove(218,141)
			Sleep(timeScale * 100)
			Click("218,141")
			Sleep(timeScale * 100)
			
			Click("218,141")	;click wizard1
			Sleep(timeScale * 7800)
			
			Send("{vkBE}")	;wizard1 010
			Sleep(timeScale * 5800)
			
			Send("{vkBE}")	;wizard1 020
			Sleep(timeScale * 11800)
			
			Send("{vk41}")	;wizard2
			Sleep(timeScale * 100)
			MouseMove(1400,305)
			Sleep(timeScale * 100)
			Click("1400,305")
			Sleep(timeScale * 100)
			
			Click("1400,305")	;click wizard2
			Sleep(timeScale * 4400)
			
			Send("{vkBE}")	;wizard2 010
			Sleep(timeScale * 12000)
			
			Send("{vkBE}")	;wizard2 020
			Sleep(timeScale * 178500)	;wait for victory
		}
}