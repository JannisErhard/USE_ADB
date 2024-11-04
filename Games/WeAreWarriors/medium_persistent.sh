for i in `seq 1 10000`
  do sleep 0.2
	  adb shell input tap 648 2086
	  sleep 0.2
	  adb shell input tap 548 1656
	  echo $i
  done
