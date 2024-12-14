if [ $(shuf -i 0-1 -n 1 --random-source /dev/urandom) = 0 ]; then
  ffmpeg -i "concat:$1|$2" $3 2> /dev/null
  echo 'no--swap' > $3-ans.txt
else
  ffmpeg -i "concat:$2|$1" $3 2> /dev/null
  echo 'yes-swap' > $3-ans.txt
fi
