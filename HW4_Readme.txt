Dataset Used:

Used the same books data from the 
class example for sake of simplicity.

MapRed Command:

(Did this with bash in a folder with the scripts and books.)

 cat books/*.txt | python3 mapper.py | sort | python3 reducer.py
