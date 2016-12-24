kill $(ps aux | grep '[P]ython' | awk '{print $2}')
kill $(ps aux | grep '[p]ython' | awk '{print $2}')
kill $(ps aux | grep '[j]imapp' | awk '{print $2}')

