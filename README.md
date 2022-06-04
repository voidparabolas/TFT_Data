# TFT_Data

Simple python scripts for pulling down TFT games and parsing the information.

----You need to update the API key in the file pull_data_tft.py

How to use:
1) Update your API key in pull_data_tft.py
2) run python3 pull_data_tft.py
3) This will pull match history from players in the ranked_tft_turbo. Matches will be populated in matches.txt
4) After pulling the matches, it will parse each match for the augments used, units, and placement. This will be written to matches.txt


5) You can further parse the match data by running parse by running python3 parse_data.py

To Do: 
Fix so I don't calculate the top4% multiple times
Add in items
